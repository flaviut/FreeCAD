{
  description = "FreeCAD builds and development environments";

  inputs = {
    self.submodules = true;
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    devour-flake = {
      url = "github:srid/devour-flake";
      flake = false;
    };
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      devour-flake,
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
      nixDevour = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        pkgs.writeShellApplication {
          name = "nix-devour-flake";
          runtimeInputs = [
            pkgs.git
            pkgs.nix
          ];
          text = ''
            repo_root="$(git rev-parse --show-toplevel)"
            exec nix build "${devour-flake}#default" \
              --override-input flake "$repo_root" \
              --override-input nixpkgs "${nixpkgs}" \
              --no-write-lock-file --no-link --print-out-paths \
              "$@"
          '';
        }
      );
      defaultOcct = "occt-8_0";
      occtVersions = {
        occt-7_9 = {
          version = "7.9.3";
          rev = "V7_9_3";
          hash = "sha256-Zp4m+f1wrzynoCrzIwvYELUXsY/NQIBY+HFk5UteufI=";
        };
        occt-8_0 = {
          version = "8.0.1";
          rev = "V8_0_1";
          hash = "sha256-QgSfrWc6qxbiHBapyGa9+ixRi/dOXqMox8U2f+tCH8o=";
        };
        occt-8_1 = {
          version = "8.1.0-dev1";
          rev = "53706f78a8640c4407bdcc6752df13a270b159f2";
          hash = "sha256-PDmgfBH3yuWMm+kPQ1RQ/0n7H8yvga6PVff4lLGHPLI=";
        };
      };
      mkEnvironment =
        system: name: occt:
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
          cacheCompiler = pkgs.writeShellScript "cache-compile" (
            pkgs.lib.replaceStrings
              [ "@ccache@" "@zstd@" ]
              [ "${pkgs.ccache}/bin/ccache" "${pkgs.zstd}/bin/zstd" ]
              (builtins.readFile ./contrib/nix/cache-compile.sh)
          );
          withCache =
            package:
            if !pkgs.stdenv.isLinux then
              package
            else
              package.overrideAttrs (old: {
                outputs = (old.outputs or [ "out" ]) ++ [ "buildLog" ];
                meta = (old.meta or { }) // {
                  outputsToInstall = (old.meta.outputsToInstall or [ "out" ]) ++ [ "buildLog" ];
                };
                nativeBuildInputs = (old.nativeBuildInputs or [ ]) ++ [ pkgs.ccache ];
                preConfigure = (old.preConfigure or "") + ''
                  source ${./contrib/nix/cache-log.sh}
                '';
                cmakeFlags = (old.cmakeFlags or [ ]) ++ [
                  (pkgs.lib.cmakeFeature "CMAKE_C_COMPILER_LAUNCHER" "${cacheCompiler}")
                  (pkgs.lib.cmakeFeature "CMAKE_CXX_COMPILER_LAUNCHER" "${cacheCompiler}")
                ];
                env = (old.env or { }) // {
                  CCACHE_DIR = "/var/cache/ccache";
                  CCACHE_REMOTE_STORAGE = "file:/var/cache/ccache-shared";
                  CCACHE_UMASK = "007";
                  LANG = "C.UTF-8";
                };
              });
          occtBase = pkgs.opencascade-occt.overrideAttrs (
            attrs: old: {
              inherit (occt) version;
              cmakeBuildType = "RelWithDebInfo";
              src = pkgs.fetchFromGitHub {
                owner = "Open-Cascade-SAS";
                repo = "OCCT";
                inherit (occt) rev hash;
              };
              buildInputs =
                old.buildInputs
                ++ pkgs.lib.optionals (pkgs.lib.versionAtLeast attrs.version "8") [
                  pkgs.expat
                ];
            }
          );
          occtPackage = withCache occtBase;
          freecadBase = pkgs.freecad.override { opencascade-occt = occtPackage; };
          freecadInputs = {
            inherit (freecadBase) nativeBuildInputs;
            buildInputs =
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
              ) freecadBase.buildInputs
              ++ [ pkgs.python3Packages.lark ];
          };
          freecad = freecadBase.overrideAttrs (old: {
            version =
              let
                version = builtins.fromJSON (builtins.readFile ./version.json);
              in
              pkgs.lib.concatMapStringsSep "." toString [
                version.version_major
                version.version_minor
                version.version_patch
              ];
            src = self;
            meta = old.meta // {
              platforms = supportedSystems;
            };
            cmakeBuildDir = buildDir;
            preConfigure = (old.preConfigure or "") + ''
              cmakeDir="$PWD"
            '';
            cmakeBuildType = "RelWithDebInfo";
            inherit (freecadInputs) nativeBuildInputs;
            buildInputs = freecadInputs.buildInputs ++ [
              pkgs.gtest
              pkgs.netgen
            ];
            cmakeFlags = old.cmakeFlags ++ [
              (pkgs.lib.cmakeBool "FREECAD_VERSION_INCLUDE_GIT" false)
              (pkgs.lib.cmakeFeature "OpenCASCADE_DIR" "${occtPackage}/lib/cmake/opencascade")
            ];
            qtWrapperArgs = pkgs.lib.optionals pkgs.stdenv.isLinux old.qtWrapperArgs ++ [
              "--prefix PYTHONPATH : ${freecadPythonPath}"
            ];
          });
          buildDir = "build/relWithDebInfo/${name}";
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
              [
                "@cmake@"
                "@ninja@"
                "@python@"
                "@recorder@"
                "@jobs@"
              ]
              [
                "${pkgs.cmake}/bin/cmake"
                "${pkgs.ninja}/bin/ninja"
                "${pkgs.python3}/bin/python3"
                "${./tools/profile/record-build.py}"
                (if pkgs.stdenv.isLinux then "44" else "")
              ]
              (builtins.readFile ./contrib/cmake/cmake.sh)
          );
          selectBuild = ''
            build_dir="''${FREECAD_BUILD_DIR:-$PWD/${buildDir}}"
            if [[ -n ''${FREECAD_OCCT_SOURCE:-} ]]; then
              occt_source="$(realpath -e -- "$FREECAD_OCCT_SOURCE")" || exit 2
              if [[ ! -f "$occt_source/CMakeLists.txt" || ! -d "$occt_source/adm/cmake" ]]; then
                printf 'Not an OCCT source directory: %s\n' "$occt_source" >&2
                exit 2
              fi

              # Keep each checkout and toolchain out of the normal build tree.
              key="$(printf '%s\n' "$occt_source" '${pkgs.stdenv.cc}' | sha256sum)"
              local_dir="$(realpath -m -- "$build_dir")-local-occt/''${key%% *}"
              build_dir="$local_dir/freecad"
              occt_stage="$local_dir/stage"
            fi
          '';
          fc-build = pkgs.writeShellScriptBin "fc-build" ''
            set -e
            ${selectBuild}
            ${pkgs.lib.optionalString pkgs.stdenv.isLinux ''
              syncToolchain() {
                if ! NIX_SSHOPTS="''${NIX_SSHOPTS:+$NIX_SSHOPTS }-o BatchMode=yes -o ConnectTimeout=3" \
                  nix copy --no-check-sigs --to ssh-ng://flaviu@192.168.86.244 "$NIX_CC" $buildInputs $nativeBuildInputs "$@"; then
                  printf 'fc-build: toolchain sync failed; continuing build\n' >&2
                fi
              }
            ''}

            occt_flags=()
            if [[ -n ''${FREECAD_OCCT_SOURCE:-} ]]; then
              occt_build="$local_dir/occt"
              occt_config="$occt_build/.fc-build"
              if [[ ! -f "$occt_build/CMakeCache.txt" || ! -f "$occt_config" || "$(<"$occt_config")" != "$0" ]]; then
                ${fc-cmake}/bin/cmake -S "$occt_source" -B "$occt_build" -G Ninja \
                  ${pkgs.lib.escapeShellArgs occtBase.cmakeFlags} \
                  -DCMAKE_BUILD_TYPE=Release \
                  -DCMAKE_INSTALL_PREFIX="$occt_stage" \
                  -DCMAKE_INSTALL_MESSAGE=NEVER \
                  -DCMAKE_INSTALL_RPATH='${if pkgs.stdenv.isDarwin then "@loader_path" else "$ORIGIN"}' \
                  -DINSTALL_DIR_CMAKE=lib/cmake/opencascade \
                  -D3RDPARTY_RAPIDJSON_DIR=${pkgs.rapidjson} \
                  -DBUILD_MODULE_Draw=OFF -DUSE_TK=OFF
                printf '%s\n' "$0" > "$occt_config"
              fi
              ${pkgs.lib.optionalString pkgs.stdenv.isLinux ''
                syncToolchain ${pkgs.rapidjson}
              ''}
              ${fc-cmake}/bin/cmake --build "$occt_build" --target install

              # The packaged Netgen links against a different OCCT.
              occt_flags=(
                "-DOpenCASCADE_DIR=$occt_stage/lib/cmake/opencascade"
                -DCMAKE_REQUIRE_FIND_PACKAGE_OpenCASCADE=ON
                -DBUILD_FEM_NETGEN=OFF
              )
            fi

            config_file="$build_dir/.fc-build"
            if [[ ! -f "$build_dir/CMakeCache.txt" || ! -f "$config_file" || "$(<"$config_file")" != "$0" ]]; then
              source_dir=$PWD
              if [[ -f "$build_dir/CMakeCache.txt" ]]; then
                while IFS= read -r entry; do
                  case "$entry" in
                    CMAKE_HOME_DIRECTORY:INTERNAL=*) source_dir=''${entry#*=}; break ;;
                  esac
                done < "$build_dir/CMakeCache.txt"
              fi

              ${fc-cmake}/bin/cmake \
                -S "$source_dir" \
                -B "$build_dir" \
                -DCMAKE_BUILD_TYPE="${freecad.cmakeBuildType}" \
                ${pkgs.lib.escapeShellArgs freecad.cmakeFlags} \
                "''${occt_flags[@]}" \
                -G "''${CMAKE_GENERATOR:-Ninja}"
              printf '%s\n' "$0" > "$config_file"
            fi

            ${pkgs.lib.optionalString pkgs.stdenv.isLinux ''
              if [[ -z ''${FREECAD_OCCT_SOURCE:-} ]]; then
                syncToolchain
              fi
            ''}
            exec ${fc-cmake}/bin/cmake --build "$build_dir" "$@"
          '';
          qtPluginPath = pkgs.lib.makeSearchPath "lib/qt-6/plugins" (
            [
              pkgs.qt6.qtbase
              pkgs.qt6.qtimageformats
              pkgs.qt6.qtsvg
            ]
            ++ pkgs.lib.optionals pkgs.stdenv.isLinux [ pkgs.qt6.qtwayland ]
          );
          fc-run = pkgs.writeShellScriptBin "fc-run" ''
            set -e
            ${selectBuild}
            export QT_STYLE_OVERRIDE="''${FREECAD_QT_STYLE_OVERRIDE:-Fusion}"
            exec "$build_dir/bin/FreeCAD" \
              --python-path "${freecadPythonPath}" \
              "$@"
          '';
          fc-macro = pkgs.writeShellApplication {
            name = "fc-macro";
            runtimeInputs = [
              pkgs.coreutils
              pkgs.xvfb-run
            ];
            text =
              pkgs.lib.replaceStrings
                [ "@build@" "@run@" "@runner@" "@python@" ]
                [
                  "${fc-build}/bin/fc-build"
                  "${fc-run}/bin/fc-run"
                  "${./contrib/nix/macro-test.py}"
                  "${pkgs.python3}/bin/python3"
                ]
                (builtins.readFile ./contrib/nix/macro-test.sh);
          };
          fc-test = pkgs.writeShellScriptBin "fc-test" ''
            set -e
            ${selectBuild}
            export VIRTUAL_ENV="${freecadPythonEnv}"
            exec ${pkgs.cmake}/bin/ctest \
              --test-dir "$build_dir" \
              --output-on-failure "$@"
          '';
          devTools =
            (with pkgs; [
              coreutils
              fc-build
              fc-cmake
              fcFormat.${system}
              nixDevour.${system}
              fc-run
              fc-test
              imagemagick
            ])
            ++ pkgs.lib.optionals pkgs.stdenv.isLinux [
              pkgs.xvfb-run
              fc-macro
            ];
          devShellHook = ''
            # Keep shell tools out of compiler dependency flags.
            export PATH="${pkgs.lib.makeBinPath devTools}:$PATH"
            export QT_PLUGIN_PATH="${qtPluginPath}''${QT_PLUGIN_PATH:+:$QT_PLUGIN_PATH}"
            export CMAKE_GENERATOR="''${CMAKE_GENERATOR:-Ninja}"
            export FREECAD_BUILD_JOBS="''${FREECAD_BUILD_JOBS:-${if pkgs.stdenv.isDarwin then "" else "44"}}"
            export COIN_GL_NO_CURRENT_CONTEXT_CHECK=1

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
        in
        {
          package = withCache freecad;
          occt = occtPackage;
          shell = freecad.overrideAttrs { shellHook = devShellHook; };
        };
      environments = forAllSystems (system: nixpkgs.lib.mapAttrs (mkEnvironment system) occtVersions);
    in
    {
      formatter = fcFormat;
      apps = forAllSystems (system: {
        nix-devour-flake = {
          type = "app";
          program = "${nixDevour.${system}}/bin/nix-devour-flake";
        };
      });
      packages = nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" ] (
        system:
        let
          variants = environments.${system};
        in
        builtins.mapAttrs (_: env: env.occt) variants
        // nixpkgs.lib.mapAttrs' (
          name: env: nixpkgs.lib.nameValuePair "freecad-${name}" env.package
        ) variants
        // {
          default = variants.${defaultOcct}.package;
          freecad = variants.${defaultOcct}.package;
        }
      );
      devShells = forAllSystems (
        system:
        let
          variants = builtins.mapAttrs (_: env: env.shell) environments.${system};
        in
        variants // { default = variants.${defaultOcct}; }
      );
      checks = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
          python = pkgs.python3.withPackages (ps: [
            ps.packaging
            ps.pyyaml
          ]);
        in
        {
          occt-default =
            pkgs.runCommand "occt-default"
              {
                nativeBuildInputs = [ python ];
                occtVersion = environments.${system}.${defaultOcct}.occt.version;
              }
              ''
                python - <<'PY'
                import os
                import tomllib

                import yaml
                from packaging.specifiers import SpecifierSet

                version = os.environ["occtVersion"]
                with open("${./pixi.toml}", "rb") as source:
                    requirement = tomllib.load(source)["dependencies"]["occt"]

                assert version in SpecifierSet(requirement), (
                    f"Default OCCT {version} does not satisfy pixi.toml: {requirement}"
                )

                with open("${./pixi.lock}") as source:
                    lock = yaml.safe_load(source)

                versions = set()
                for package in lock["packages"]:
                    filename = package.get("conda", "").rsplit("/", 1)[-1]
                    if not filename.startswith("occt-"):
                        continue

                    versions.add(filename.split("-")[1])

                assert versions == {version}, (
                    f"Default OCCT {version} differs from pixi.lock: {sorted(versions)}"
                )
                PY
                touch "$out"
              '';
        }
      );
    };
}
