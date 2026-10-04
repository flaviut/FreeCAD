{
  description = "FreeCAD development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      nixpkgs,
      treefmt-nix,
      ...
    }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
      ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      treefmtEval = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        treefmt-nix.lib.evalModule pkgs ./treefmt.nix
      );
      fcFormat = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        pkgs.writeShellApplication {
          name = "fc-format";
          runtimeInputs = with pkgs; [
            coreutils
            git
            treefmtEval.${system}.config.build.wrapper
          ];
          text = ''
            repo_root="$(git rev-parse --show-toplevel)"
            cd "$repo_root"

            changed_files=()
            while IFS= read -r -d "" path; do
              changed_files+=("$path")
            done < <(
              {
                git diff --name-only --diff-filter=ACMR -z
                git diff --cached --name-only --diff-filter=ACMR -z
                git ls-files --others --exclude-standard -z
              } | sort -zu
            )

            if (( ''${#changed_files[@]} == 0 )); then
              exit 0
            fi

            exec treefmt --fail-on-change -- "''${changed_files[@]}"
          '';
        }
      );
    in
    {
      formatter = fcFormat;

      devShells = forAllSystems (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            overlays = [
              (final: prev: {
                # MED needs the HDF5 1.10 API, but must share VTK's HDF5 library.
                medfile = (prev.medfile.override { hdf5 = final.hdf5; }).overrideAttrs (old: {
                  env = (old.env or { }) // {
                    NIX_CFLAGS_COMPILE = (old.env.NIX_CFLAGS_COMPILE or "") + " -DH5_USE_110_API";
                  };
                });
              })
            ];
          };
          freecadOcct = pkgs.opencascade-occt.overrideAttrs (
            finalAttrs: old: {
              patches =
                (old.patches or [ ])
                ++ pkgs.lib.optional (
                  finalAttrs.version == "7.9.3"
                ) ./contrib/patches/occt-thread-local-error-handlers.patch;
            }
          );
          freecadInputs = {
            inherit (pkgs.freecad) nativeBuildInputs;
            buildInputs =
              map (dependency: if dependency == pkgs.opencascade-occt then freecadOcct else dependency) (
                builtins.filter (
                  dependency:
                  dependency != null
                  && !(
                    pkgs.stdenv.isDarwin
                    && builtins.elem (dependency.pname or "") [
                      "qtwayland"
                      "qtwebengine"
                      "libxmu"
                      "libspnav"
                      "ifcopenshell"
                    ]
                  )
                ) pkgs.freecad.buildInputs
              )
              ++ [ pkgs.python3Packages.lark ];
          };
          freecadPythonDeps = builtins.filter (
            dependency:
            dependency ? pythonModule && dependency.pythonModule == pkgs.python3 && dependency != pkgs.python3
          ) freecadInputs.buildInputs;
          freecadPythonEnv = pkgs.python3.withPackages (
            pythonPackages:
            freecadPythonDeps
            ++ (with pythonPackages; [
              defusedxml
              requests
              scour
            ])
          );
          freecadPythonPath = "${freecadPythonEnv}/${pkgs.python3.sitePackages}";
          fc-cmake = pkgs.writeShellScriptBin "cmake" (
            pkgs.lib.replaceStrings
              [ "@cmake@" "@ninja@" "@python@" "@nc@" "@recorder@" "@jobs@" ]
              [
                "${pkgs.cmake}/bin/cmake"
                "${pkgs.ninja}/bin/ninja"
                "${pkgs.python3}/bin/python3"
                "${pkgs.netcat}/bin/nc"
                "${./tools/profile/record-build.py}"
                (if pkgs.stdenv.isLinux then "44" else "")
              ]
              (builtins.readFile ./contrib/cmake/cmake.sh)
          );
          fc-build = pkgs.writeShellScriptBin "fc-build" ''
            set -e
            build_dir="''${FREECAD_BUILD_DIR:-$PWD/build/relWithDebInfo}"
            if [[ ! -f "$build_dir/CMakeCache.txt" ]]; then
              ${fc-cmake}/bin/cmake \
                --preset rel-with-deb-info \
                -S "$PWD" \
                -B "$build_dir" \
                -G "''${CMAKE_GENERATOR:-Ninja}"
            fi

            exec ${fc-cmake}/bin/cmake --build "$build_dir" "$@"
          '';
          qtPluginPath = pkgs.lib.makeSearchPath "lib/qt-6/plugins" (
            [
              pkgs.qt6.qtbase
              pkgs.qt6.qtsvg
            ]
            ++ pkgs.lib.optionals pkgs.stdenv.isLinux [ pkgs.qt6.qtwayland ]
          );
          fc-run = pkgs.writeShellScriptBin "fc-run" ''
            export QT_STYLE_OVERRIDE="''${FREECAD_QT_STYLE_OVERRIDE:-Fusion}"
            export QT_PLUGIN_PATH="${qtPluginPath}''${QT_PLUGIN_PATH:+:$QT_PLUGIN_PATH}"
            exec "''${FREECAD_BUILD_DIR:-$PWD/build/relWithDebInfo}/bin/FreeCAD" \
              --python-path "${freecadPythonPath}" \
              "$@"
          '';
          fc-test = pkgs.writeShellScriptBin "fc-test" ''
            export VIRTUAL_ENV="${freecadPythonEnv}"
            exec ${pkgs.cmake}/bin/ctest \
              --test-dir "''${FREECAD_BUILD_DIR:-$PWD/build/relWithDebInfo}" \
              --output-on-failure "$@"
          '';

        in
        {
          default = pkgs.mkShell {
            # Keep the shell aligned with the FreeCAD package in nixpkgs. This
            # supplies the compiler, CMake/Qt tooling, OCCT, Coin, PySide,
            # Python modules, and the remaining linked libraries.
            inputsFrom = [ freecadInputs ];

            packages =
              with pkgs;
              [
                coreutils
                fc-build
                fc-cmake
                fcFormat.${system}
                fc-run
                fc-test
                ccache
                distcc
                expat
                graphviz
                gtest
                imagemagick
                netgen
                nlohmann_json
                pcl
                proj
              ]
              ++ pkgs.lib.optionals pkgs.stdenv.isLinux [ pkgs.xvfb-run ];

            shellHook = ''
              export CCACHE_DIR="''${CCACHE_DIR:-$PWD/.cache/ccache}"
              export CMAKE_GENERATOR="''${CMAKE_GENERATOR:-Ninja}"
              export FREECAD_BUILD_JOBS="''${FREECAD_BUILD_JOBS:-${if pkgs.stdenv.isDarwin then "" else "44"}}"
              export FREECAD_USE_DISTCC="''${FREECAD_USE_DISTCC:-${if pkgs.stdenv.isLinux then "1" else "0"}}"
              export COIN_GL_NO_CURRENT_CONTEXT_CHECK=1
              export CC="$(readlink -f "$(command -v "$CC")")"
              export CXX="$(readlink -f "$(command -v "$CXX")")"

              ide_bin="$PWD/.cache/bin"
              mkdir -p "$ide_bin"
              for tool in ninja ctest cc c++ gcc g++ make pkg-config; do
                tool_path="$(command -v "$tool" || true)"
                if [[ -n "$tool_path" ]]; then
                  ln -sfnT "$(readlink -f "$tool_path")" "$ide_bin/$tool"
                fi
              done
              ln -sfnT "${fc-cmake}/bin/cmake" "$ide_bin/cmake"
              ln -sfnT "$(readlink -f "$(command -v "$CC")")" "$ide_bin/c"
            '';
          };
        }
      );
    };
}
