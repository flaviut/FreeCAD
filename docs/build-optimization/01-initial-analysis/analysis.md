# Clang build profile

* Build wall time from Ninja log: 1672.3 s
* Translation units with traces: 3857
* Sum of traced compiler time: 12298.6 s
* Release build, Clang 21.1.8, `BUILD_ENABLE_TIME_TRACE=ON`, ccache off, 8 compile jobs.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.

## Top 25 translation units by Ninja elapsed time

| Ninja s | Trace s | Frontend s | Backend s | Source s | Function instantiation s | Output |
|---:|---:|---:|---:|---:|---:|---|
| 81.1 | 80.9 | 10.3 | 70.6 | 0.2 | 0.1 | src/3rdParty/pivy/interfaces/CMakeFiles/pivy_coin.dir/coinPYTHON_wrap.cxx.o |
| 27.1 | 27.0 | 14.5 | 12.3 | 7.6 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 18.9 | 18.7 | 9.0 | 9.6 | 5.4 | 2.7 | src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o |
| 18.4 | 18.3 | 12.3 | 5.9 | 7.1 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 17.9 | 17.8 | 13.4 | 4.4 | 7.8 | 3.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 17.8 | 17.6 | 12.1 | 5.4 | 8.5 | 3.2 | src/Mod/CAM/App/CMakeFiles/Path.dir/Area.cpp.o |
| 17.5 | 17.3 | 11.8 | 5.5 | 6.4 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 16.4 | 16.3 | 8.2 | 8.0 | 3.0 | 3.6 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/planegcs/GCS.cpp.o |
| 15.7 | 15.6 | 11.5 | 4.1 | 8.1 | 2.8 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 15.6 | 15.4 | 11.9 | 3.5 | 8.4 | 2.7 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/SketchObject.cpp.o |
| 15.3 | 15.1 | 9.7 | 5.4 | 4.5 | 2.3 | src/Gui/CMakeFiles/FreeCADGui.dir/MainWindow.cpp.o |
| 14.8 | 14.7 | 11.9 | 2.7 | 6.6 | 3.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 14.7 | 14.6 | 7.7 | 6.9 | 1.8 | 4.5 | src/Mod/MeshPart/App/CMakeFiles/flatmesh.dir/MeshFlatteningLscmRelax.cpp.o |
| 14.7 | 14.6 | 8.0 | 6.6 | 2.8 | 2.4 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o |
| 14.6 | 14.4 | 7.9 | 6.5 | 4.4 | 2.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/AppTechDrawPy.cpp.o |
| 14.4 | 14.3 | 8.9 | 5.3 | 4.2 | 2.5 | src/Gui/CMakeFiles/FreeCADGui.dir/Application.cpp.o |
| 14.4 | 14.3 | 7.2 | 7.0 | 4.8 | 2.0 | src/App/CMakeFiles/FreeCADApp.dir/Application.cpp.o |
| 14.4 | 14.2 | 9.6 | 4.6 | 5.1 | 2.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 14.2 | 14.1 | 10.2 | 3.9 | 6.0 | 2.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 14.2 | 14.1 | 11.6 | 2.4 | 6.4 | 2.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 13.8 | 13.7 | 9.8 | 3.8 | 5.6 | 2.4 | src/Mod/Measure/Gui/CMakeFiles/MeasureGui.dir/TaskMassProperties.cpp.o |
| 13.8 | 13.7 | 10.9 | 2.7 | 6.0 | 2.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 13.6 | 13.5 | 8.5 | 5.0 | 4.5 | 2.4 | src/Mod/Fem/Gui/CMakeFiles/FemGui.dir/TaskPostBoxes.cpp.o |
| 13.5 | 13.4 | 10.7 | 2.7 | 5.6 | 2.6 | src/Mod/PartDesign/Gui/CMakeFiles/PartDesignGui.dir/Command.cpp.o |
| 13.4 | 13.3 | 9.4 | 3.9 | 4.7 | 2.4 | src/Mod/PartDesign/Gui/CMakeFiles/PartDesignGui.dir/TaskExtrudeParameters.cpp.o |

## Compiler phase totals

| Phase | Sum of TU seconds |
|---|---:|
| ExecuteCompiler | 12298.6 |
| Frontend | 10405.3 |
| Backend | 1842.4 |
| Source | 5574.3 |
| InstantiateFunction | 2626.2 |
| InstantiateClass | 2424.8 |
| Optimizer | 1148.9 |
| CodeGenPasses | 685.7 |

## Largest source areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| src/Gui | 1865.6 | 387 |
| src/3rdParty | 1515.2 | 1546 |
| Mod/TechDraw | 1479.4 | 246 |
| Mod/Part | 1376.1 | 294 |
| Mod/PartDesign | 853.6 | 121 |
| tests | 821.3 | 213 |
| Mod/Sketcher | 688.9 | 88 |
| Mod/Fem | 672.1 | 143 |
| src/App | 389.4 | 104 |
| Mod/Mesh | 350.6 | 91 |
| Mod/Material | 341.0 | 62 |
| Mod/CAM | 321.8 | 83 |
| Mod/Robot | 261.2 | 102 |
| src/Base | 208.7 | 113 |
| Mod/Measure | 185.6 | 35 |
| Mod/Spreadsheet | 167.7 | 34 |
| Mod/Surface | 136.8 | 27 |
| Mod/Import | 125.5 | 28 |
| Mod/Assembly | 113.5 | 28 |
| Mod/MeshPart | 103.3 | 21 |

## Included files with greatest cumulative trace time

These are inclusive header parsing times summed across translation units; nested includes may overlap.

| Inclusive s | Header |
|---:|---|
| 822.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 697.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 582.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qwidget.h |
| 567.8 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 557.8 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 545.7 | src/App/DocumentObject.h |
| 518.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/memory |
| 507.6 | src/Mod/Part/App/PartFeature.h |
| 493.9 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 449.1 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 434.1 | src/App/Application.h |
| 417.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 414.9 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/string |
| 412.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ostream.h |
| 409.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 396.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 391.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 368.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/iostream |
| 357.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ios_base.h |
| 354.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qaction.h |
| 351.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication |
| 351.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h |
| 333.4 | src/Mod/Material/App/Materials.h |
| 332.5 | src/Mod/Material/App/PropertyMaterial.h |
| 328.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |

## Template instantiations with greatest cumulative trace time

These are inclusive event times summed across translation units.

| Inclusive s | Template |
|---:|---|
| 295.7 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 295.3 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 269.8 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 269.4 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 76.5 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 76.2 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 68.0 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 64.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 64.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 60.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 59.7 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 57.5 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 57.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 55.0 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 55.0 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 54.3 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 53.3 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 52.8 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 52.4 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 52.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 50.5 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 50.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 49.4 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 47.8 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 47.4 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |

## src/3rdParty/pivy/interfaces/CMakeFiles/pivy_coin.dir/coinPYTHON_wrap.cxx.o

Ninja 81.1 s; compiler 80.9 s; frontend 10.3 s; backend 70.6 s.

Top included files:

* 0.58 s — src/3rdParty/pivy/interfaces/coin_header_includes.h
* 0.28 s — /nix/store/h3l4z7p6wny3phbckwwhy1i2g52pdnj4-python3-3.13.15/include/python3.13/Python.h
* 0.19 s — src/3rdParty/coin/include/Inventor/actions/SoActions.h
* 0.17 s — src/3rdParty/coin/include/Inventor/actions/SoCallbackAction.h
* 0.17 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/math.h
* 0.17 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath
* 0.16 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/stdexcept
* 0.15 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/string
* 0.14 s — src/3rdParty/coin/include/Inventor/nodes/SoLightModel.h
* 0.14 s — src/3rdParty/coin/include/Inventor/elements/SoLazyElement.h

Top template instantiations:

* 0.01 s — std::basic_string<wchar_t>::_M_construct<const char *>
* 0.01 s — std::basic_string<wchar_t>::_S_copy_chars<const char *>
* 0.00 s — std::basic_string<char8_t>
* 0.00 s — std::basic_string<char32_t>
* 0.00 s — std::operator+<char, std::char_traits<char>, std::allocator<char>>
* 0.00 s — std::basic_string<wchar_t>
* 0.00 s — std::basic_string<char8_t>::_M_construct<const char8_t *>
* 0.00 s — std::basic_string<char>
* 0.00 s — std::basic_string<char16_t>
* 0.00 s — std::basic_string<char16_t>::_M_construct<const char16_t *>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 27.1 s; compiler 27.0 s; frontend 14.5 s; backend 12.3 s.

Top included files:

* 2.09 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication
* 2.09 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h
* 1.97 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.46 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 1.37 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.37 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 1.13 s — src/Mod/Sketcher/App/SketchObject.h
* 0.86 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.86 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.85 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h

Top template instantiations:

* 0.18 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.17 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.17 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.16 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.16 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.16 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.14 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.14 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.12 s — std::vformat_to<std::__format::_Sink_iter<char>>

## src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o

Ninja 18.9 s; compiler 18.7 s; frontend 9.0 s; backend 9.6 s.

Top included files:

* 0.73 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.73 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.54 s — build/clang-profile/src/App/DocumentPy.h
* 0.51 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/bimap.hpp
* 0.51 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/bimap/bimap.hpp
* 0.50 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/strong_components.hpp
* 0.50 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/bimap/detail/bimap_core.hpp
* 0.47 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp
* 0.45 s — src/App/private/DocumentP.h
* 0.45 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h

Top template instantiations:

* 0.36 s — boost::basic_regex<char>::assign
* 0.20 s — boost::regex_search<const char *, std::allocator<boost::sub_match<const char *>>, char, boost::regex_traits<char>>
* 0.19 s — boost::bimaps::bimap<Base::Reference<App::StringHasher>, int>
* 0.18 s — boost::basic_regex<char>::set_expression
* 0.18 s — boost::basic_regex<char>::do_assign
* 0.18 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.11 s — std::vformat_to<std::__format::_Sink_iter<wchar_t>>
* 0.11 s — std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>
* 0.11 s — std::vformat_to<std::__format::_Sink_iter<char>>
* 0.11 s — std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 18.4 s; compiler 18.3 s; frontend 12.3 s; backend 5.9 s.

Top included files:

* 2.10 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication
* 2.10 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h
* 2.04 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.93 s — src/Mod/Sketcher/App/SketchObject.h
* 1.48 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 1.39 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.38 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.87 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.87 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.86 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h

Top template instantiations:

* 0.18 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.17 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.14 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.14 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.14 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.14 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.11 s — std::vformat_to<std::__format::_Sink_iter<wchar_t>>
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.11 s — std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>
* 0.11 s — std::vformat_to<std::__format::_Sink_iter<char>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 17.9 s; compiler 17.8 s; frontend 13.4 s; backend 4.4 s.

Top included files:

* 1.92 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication
* 1.92 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h
* 1.57 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 1.50 s — src/Mod/Sketcher/App/SketchObject.h
* 1.43 s — src/Mod/Sketcher/Gui/EditTextDialog.h
* 1.43 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.43 s — src/Mod/Sketcher/Gui/PreCompiled.h
* 1.37 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 1.18 s — src/Gui/QtAll.h
* 1.06 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h

Top template instantiations:

* 0.11 s — std::vformat_to<std::__format::_Sink_iter<wchar_t>>
* 0.11 s — std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>
* 0.11 s — std::vformat_to<std::__format::_Sink_iter<char>>
* 0.11 s — std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
