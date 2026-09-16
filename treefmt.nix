{ lib, ... }:

let
  formattedRoots = [
    ".github"
    "src/Base"
    "src/Gui"
    "src/Main"
    "src/Tools"
    "src/Mod/Assembly"
    "src/Mod/BIM"
    "src/Mod/CAM"
    "src/Mod/Cloud"
    "src/Mod/Draft"
    "src/Mod/Fem"
    "src/Mod/Help"
    "src/Mod/Import"
    "src/Mod/Inspection"
    "src/Mod/JtReader"
    "src/Mod/Measure"
    "src/Mod/MeshPart"
    "src/Mod/Mesh"
    "src/Mod/PartDesign"
    "src/Mod/Part"
    "src/Mod/Plot"
    "src/Mod/Points"
    "src/Mod/ReverseEngineering"
    "src/Mod/Robot"
    "src/Mod/Show"
    "src/Mod/Sketcher"
    "src/Mod/Spreadsheet"
    "src/Mod/Start"
    "src/Mod/Surface"
    "src/Mod/Test"
    "src/Mod/Tux"
    "src/Mod/Web"
    "tests/src"
  ];

  filesUnderRoots =
    patterns: lib.concatMap (root: map (pattern: "${root}/${pattern}") patterns) formattedRoots;

  commonExcludes = [
    "**/*vcproj*"
    "**/*vcxproj*"
    ".github/ISSUE_TEMPLATE/**"
    "src/App/ExpressionParser.tab.c"
    "src/App/ExpressionParser.tab.h"
    "src/App/ExpressionParser.y"
    "src/App/lex.ExpressionParser.c"
    "src/Doc/ThirdPartyLibraries.html.cmake"
    "src/Gui/3Dconnexion/navlib/**"
    "src/Gui/QSint/**"
    "src/Gui/Quarter/**"
    "src/Mod/Fem/femexamples/**"
    "src/Mod/Mesh/App/TestData/**"
    "src/Mod/Mesh/App/WildMagic4/**"
    "src/Mod/Robot/App/kdl_cp/**"
    "src/Mod/Robot/Lib/**"
    "**/*.ts"
    "**/*.brep"
  ];
in
{
  projectRootFile = "flake.nix";

  programs.black = {
    enable = true;
    includes = filesUnderRoots [ "**/*.py" ];
    excludes = commonExcludes ++ [ "src/Tools/typing/generated/**" ];
  };

  programs.clang-format = {
    enable = true;
    includes = filesUnderRoots [
      "**/*.c"
      "**/*.cc"
      "**/*.cpp"
      "**/*.h"
      "**/*.hh"
      "**/*.hpp"
      "**/*.glsl"
      "**/*.vert"
      "**/*.tesc"
      "**/*.tese"
      "**/*.geom"
      "**/*.frag"
      "**/*.comp"
    ];
    excludes = commonExcludes;
  };

  programs.nixfmt.enable = true;

  settings.formatter.black.options = [
    "--line-length"
    "100"
  ];
}
