# SPDX-License-Identifier: LGPL-2.1-or-later

add_subdirectory(App)

target_link_libraries(TechDraw_tests_run
    GTest::gtest_main
    ${Python3_LIBRARIES}
    TechDraw
)

if(BUILD_GUI)
    # Exercise the rendering curves without loading the GUI module, whose
    # static initialization requires an already running FreeCAD application.
    target_sources(TechDraw_tests_run PRIVATE
        ${CMAKE_SOURCE_DIR}/src/Mod/TechDraw/Gui/PathBuilder.cpp
    )
    target_compile_definitions(TechDraw_tests_run PRIVATE TECHDRAW_TEST_GUI TechDrawGuiExport=)
endif()
