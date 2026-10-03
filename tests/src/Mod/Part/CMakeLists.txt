# SPDX-License-Identifier: LGPL-2.1-or-later

add_subdirectory(App)

if(BUILD_GUI)
    add_executable(TaskPatternLifecycle_Tests_run Gui/TaskPatternLifecycle.cpp)
    set_target_properties(TaskPatternLifecycle_Tests_run PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/tests)
    target_link_libraries(TaskPatternLifecycle_Tests_run PRIVATE
        FreeCADApp FreeCADGui PartGui Part ${Python3_LIBRARIES} ${QtTest_LIBRARIES})
    add_test(NAME TaskPatternLifecycle_Tests_run COMMAND TaskPatternLifecycle_Tests_run)
    set_tests_properties(TaskPatternLifecycle_Tests_run PROPERTIES
        LABELS "Qt" ENVIRONMENT "QT_QPA_PLATFORM=offscreen" TIMEOUT 10)
    if(WIN32)
        set_target_properties(TaskPatternLifecycle_Tests_run PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
        set_tests_properties(TaskPatternLifecycle_Tests_run PROPERTIES
            ENVIRONMENT_MODIFICATION "${_test_env_mod}")
    endif()

    target_sources(Part_tests_run PRIVATE
        Gui/SoBrepEdgeSet.cpp
    )
    target_link_libraries(Part_tests_run PartGui)
endif()

target_link_libraries(Part_tests_run
    GTest::gtest_main
    ${Python3_LIBRARIES}
    Part
)
