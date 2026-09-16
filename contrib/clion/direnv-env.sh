_freecad_clion_env() {
  local shell_name script_path project_dir previous_dir exports

  if [ -n "${BASH_VERSION-}" ]; then
    shell_name=bash
    script_path=${BASH_SOURCE[0]}
  elif [ -n "${ZSH_VERSION-}" ]; then
    shell_name=zsh
    script_path=${(%):-%x}
  else
    printf 'FreeCAD CLion environment requires Bash or Zsh\n' >&2
    return 1
  fi

  project_dir="$(cd -- "$(dirname -- "$script_path")/../.." && pwd -P)" || return 1
  previous_dir=$PWD
  cd -- "$project_dir" || return 1
  if ! exports="$(direnv export "$shell_name")"; then
    cd -- "$previous_dir"
    return 1
  fi
  cd -- "$previous_dir" || return 1
  eval "$exports"
  case ":$PATH:" in
    *":$project_dir/.cache/bin:"*) ;;
    *) export PATH="$project_dir/.cache/bin:$PATH" ;;
  esac
}

if ! _freecad_clion_env; then
  unset -f _freecad_clion_env
  return 1
fi
unset -f _freecad_clion_env
