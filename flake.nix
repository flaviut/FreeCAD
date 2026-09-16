{
  description = "FreeCAD Linux development environment";

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
          pkgs = import nixpkgs { inherit system; };
          freecadPythonDeps = builtins.filter (
            dependency:
            dependency ? pythonModule && dependency.pythonModule == pkgs.python3 && dependency != pkgs.python3
          ) pkgs.freecad.buildInputs;
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
          fc-build = pkgs.writeShellScriptBin "fc-build" ''
            build_dir="''${FREECAD_BUILD_DIR:-$PWD/build}"
            if [[ ! -f "$build_dir/CMakeCache.txt" ]]; then
              ${pkgs.cmake}/bin/cmake \
                -S "$PWD" \
                -B "$build_dir" \
                -DFREECAD_VCS_PROVENANCE=OFF \
                -G "''${CMAKE_GENERATOR:-Ninja}"
            fi
            exec ${pkgs.cmake}/bin/cmake --build "$build_dir" "$@"
          '';
          fc-run = pkgs.writeShellScriptBin "fc-run" ''
            export QT_STYLE_OVERRIDE="''${FREECAD_QT_STYLE_OVERRIDE:-Fusion}"
            export QT_PLUGIN_PATH="${pkgs.qt6.qtbase}/lib/qt-6/plugins:${pkgs.qt6.qtsvg}/lib/qt-6/plugins:${pkgs.qt6.qtwayland}/lib/qt-6/plugins''${QT_PLUGIN_PATH:+:$QT_PLUGIN_PATH}"
            exec "''${FREECAD_BUILD_DIR:-$PWD/build}/bin/FreeCAD" \
              --python-path "${freecadPythonPath}" \
              "$@"
          '';
          fc-test = pkgs.writeShellScriptBin "fc-test" ''
            export VIRTUAL_ENV="${freecadPythonEnv}"
            exec ${pkgs.cmake}/bin/ctest \
              --test-dir "''${FREECAD_BUILD_DIR:-$PWD/build}" \
              --output-on-failure "$@"
          '';
        in
        {
          default = pkgs.mkShell {
            # Keep the shell aligned with the FreeCAD package in nixpkgs. This
            # supplies the compiler, CMake/Qt tooling, OCCT, Coin, PySide,
            # Python modules, and the remaining linked libraries.
            inputsFrom = [ pkgs.freecad ];

            packages = with pkgs; [
              fc-build
              fcFormat.${system}
              fc-run
              fc-test
              ccache
              expat
              graphviz
              gtest
              imagemagick
              netgen
              nlohmann_json
              pcl
              proj
              xvfb-run
            ];

            shellHook = ''
              export CCACHE_DIR="''${CCACHE_DIR:-$PWD/.cache/ccache}"
              export CMAKE_GENERATOR="''${CMAKE_GENERATOR:-Ninja}"
              export COIN_GL_NO_CURRENT_CONTEXT_CHECK=1
            '';
          };
        }
      );
    };
}
