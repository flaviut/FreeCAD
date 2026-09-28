# Clang build profile

* Recorded Ninja log timestamp span: 1142.7 s (124–1142852 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 3857; PCH jobs with traces: 45.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 7822.6 | 235.6 | 8058.2 |
| Frontend | 5860.5 | 193.3 | 6053.8 |
| Backend | 1896.1 | 0.0 | 1896.1 |
| Source | 3357.6 | 30.5 | 3388.2 |
| InstantiateFunction | 1756.5 | 34.0 | 1790.5 |
| InstantiateClass | 1610.8 | 37.0 | 1647.9 |
| Optimizer | 1188.4 | 0.0 | 1188.4 |
| CodeGenPasses | 700.5 | 0.0 | 700.5 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 85.1 | 84.9 | 10.9 | 74.0 | 0.2 | src/3rdParty/pivy/interfaces/CMakeFiles/pivy_coin.dir/coinPYTHON_wrap.cxx.o |
| 25.3 | 25.2 | 12.2 | 12.9 | 7.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 16.1 | 15.9 | 9.7 | 6.2 | 6.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 15.7 | 15.6 | 5.7 | 9.8 | 2.3 | src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o |
| 15.6 | 15.5 | 8.3 | 7.1 | 1.9 | src/Mod/MeshPart/App/CMakeFiles/flatmesh.dir/MeshFlatteningLscmRelax.cpp.o |
| 14.6 | 14.4 | 8.5 | 5.9 | 6.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 14.2 | 14.1 | 6.2 | 7.8 | 0.9 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/planegcs/GCS.cpp.o |
| 13.8 | 13.7 | 9.4 | 4.2 | 4.8 | src/Mod/MeshPart/App/CMakeFiles/flatmesh.dir/MeshFlatteningPy.cpp.o |
| 13.8 | 13.7 | 9.0 | 4.6 | 6.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 13.5 | 13.4 | 7.3 | 6.1 | 2.9 | src/Mod/CAM/libarea/CMakeFiles/area.dir/pyarea.cpp.o |
| 13.5 | 13.4 | 5.8 | 7.6 | 0.2 | src/3rdParty/salomesmesh/CMakeFiles/SMESH.dir/src/SMESH/SMESH_MeshEditor.cpp.o |
| 13.2 | 13.1 | 9.0 | 4.0 | 6.4 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 12.2 | 12.2 | 4.9 | 7.2 | 3.3 | tests/src/Gui/CMakeFiles/Gui_tests_run.dir/StyleParameters/ParserTest.cpp.o |
| 12.1 | 12.0 | 6.7 | 5.2 | 3.5 | src/Mod/CAM/App/CMakeFiles/Path.dir/Area.cpp.o |
| 11.8 | 11.7 | 6.2 | 5.4 | 3.9 | tests/src/Mod/Part/App/CMakeFiles/Part_tests_run.dir/TopoShapeExpansion.cpp.o |
| 11.5 | 11.4 | 7.4 | 3.9 | 6.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 11.3 | 11.3 | 4.7 | 6.5 | 1.7 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o |
| 11.3 | 11.2 | 5.5 | 5.6 | 3.4 | src/Gui/CMakeFiles/FreeCADGui.dir/MainWindow.cpp.o |
| 11.1 | 11.0 | 6.3 | 4.7 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 11.0 | 10.9 | 4.2 | 6.7 | 2.2 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/AppTechDrawPy.cpp.o |
| 11.0 | 10.9 | 3.8 | 7.1 | 2.1 | src/App/CMakeFiles/FreeCADApp.dir/Application.cpp.o |
| 10.6 | 10.5 | 6.6 | 3.9 | 1.4 | tests/src/Gui/CMakeFiles/QuantitySpinBox_Tests_run.dir/QuantitySpinBox.cpp.o |
| 10.6 | 10.5 | 7.6 | 2.8 | 5.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 10.6 | 10.4 | 7.6 | 2.8 | 5.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 10.5 | 10.4 | 5.3 | 5.1 | 3.3 | src/Mod/Fem/Gui/CMakeFiles/FemGui.dir/TaskPostBoxes.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 10.9 | 10.8 | 8.8 | 0.0 | 0.0 | src/Mod/Import/Gui/CMakeFiles/ImportGui.dir/cmake_pch.hxx.pch |
| 10.2 | 10.1 | 8.0 | 0.0 | 7.6 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/cmake_pch.hxx.pch |
| 8.8 | 8.7 | 7.1 | 0.0 | 0.0 | src/Mod/Measure/Gui/CMakeFiles/MeasureGui.dir/cmake_pch.hxx.pch |
| 8.5 | 8.4 | 6.9 | 0.0 | 0.0 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/cmake_pch.hxx.pch |
| 8.4 | 8.3 | 6.6 | 0.0 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx.pch |
| 8.1 | 8.0 | 6.3 | 0.0 | 0.0 | src/Mod/CAM/App/CMakeFiles/Path.dir/cmake_pch.hxx.pch |
| 7.8 | 7.7 | 6.5 | 0.0 | 0.0 | src/Mod/Fem/Gui/CMakeFiles/FemGui.dir/cmake_pch.hxx.pch |
| 7.7 | 7.6 | 6.2 | 0.0 | 0.0 | src/Gui/CMakeFiles/FreeCADGui.dir/cmake_pch.hxx.pch |
| 7.4 | 7.3 | 6.3 | 0.0 | 0.0 | src/Mod/Assembly/Gui/CMakeFiles/AssemblyGui.dir/cmake_pch.hxx.pch |
| 6.8 | 6.7 | 5.5 | 0.0 | 0.0 | src/Mod/PartDesign/Gui/CMakeFiles/PartDesignGui.dir/cmake_pch.hxx.pch |
| 6.6 | 6.5 | 5.3 | 0.0 | 0.0 | src/Mod/TechDraw/Gui/CMakeFiles/TechDrawGui.dir/cmake_pch.hxx.pch |
| 6.5 | 6.5 | 5.4 | 0.0 | 0.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx.pch |
| 6.4 | 6.4 | 5.3 | 0.0 | 0.0 | src/Mod/Mesh/Gui/CMakeFiles/MeshGui.dir/cmake_pch.hxx.pch |
| 6.4 | 6.3 | 5.0 | 0.0 | 4.4 | src/Mod/Material/App/CMakeFiles/Materials.dir/cmake_pch.hxx.pch |
| 6.4 | 6.3 | 5.1 | 0.0 | 0.0 | src/Mod/Fem/App/CMakeFiles/Fem.dir/cmake_pch.hxx.pch |
| 6.3 | 6.2 | 5.3 | 0.0 | 0.0 | src/Mod/MeshPart/Gui/CMakeFiles/MeshPartGui.dir/cmake_pch.hxx.pch |
| 6.3 | 6.2 | 5.1 | 0.0 | 0.0 | src/Mod/Material/Gui/CMakeFiles/MatGui.dir/cmake_pch.hxx.pch |
| 6.1 | 6.0 | 5.1 | 0.0 | 0.0 | src/Mod/CAM/Gui/CMakeFiles/PathGui.dir/cmake_pch.hxx.pch |
| 6.0 | 5.9 | 5.0 | 0.0 | 0.0 | src/Mod/Spreadsheet/Gui/CMakeFiles/SpreadsheetGui.dir/cmake_pch.hxx.pch |
| 5.6 | 5.5 | 4.2 | 0.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |
| 5.6 | 5.5 | 4.4 | 0.0 | 0.0 | src/App/CMakeFiles/FreeCADApp.dir/cmake_pch.hxx.pch |
| 5.4 | 5.3 | 4.6 | 0.0 | 0.0 | src/Mod/Spreadsheet/App/CMakeFiles/Spreadsheet.dir/cmake_pch.hxx.pch |
| 4.5 | 4.4 | 3.7 | 0.0 | 0.0 | src/Mod/Start/Gui/CMakeFiles/StartGui.dir/cmake_pch.hxx.pch |
| 4.5 | 4.4 | 3.5 | 0.0 | 3.2 | src/Mod/Mesh/App/CMakeFiles/Mesh.dir/cmake_pch.hxx.pch |
| 4.5 | 4.4 | 3.6 | 0.0 | 0.0 | src/Mod/Import/App/CMakeFiles/Import.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| src/3rdParty | 1544.2 | 1546 |
| tests | 848.9 | 213 |
| src/Gui | 845.3 | 387 |
| Mod/TechDraw | 777.5 | 246 |
| Mod/Part | 748.5 | 294 |
| Mod/PartDesign | 566.0 | 121 |
| Mod/Sketcher | 451.6 | 88 |
| Mod/Fem | 323.3 | 143 |
| Mod/CAM | 261.7 | 83 |
| Mod/Mesh | 200.4 | 91 |
| src/App | 198.1 | 104 |
| Mod/Material | 160.8 | 62 |
| Mod/Measure | 126.6 | 35 |
| Mod/Robot | 97.7 | 102 |
| Mod/Spreadsheet | 93.2 | 34 |
| src/Base | 93.2 | 113 |
| Mod/Surface | 87.3 | 27 |
| Mod/MeshPart | 79.2 | 21 |
| Mod/Import | 77.5 | 28 |
| Mod/Assembly | 76.0 | 28 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 471.6 | src/App/DocumentObject.h |
| 428.3 | src/Mod/Part/App/PartFeature.h |
| 326.5 | src/App/Application.h |
| 311.8 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/memory |
| 307.9 | src/App/Document.h |
| 273.8 | src/Mod/Material/App/PropertyMaterial.h |
| 271.9 | src/Mod/Material/App/Materials.h |
| 230.4 | src/App/ComplexGeoData.h |
| 219.8 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 215.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 204.1 | /nix/store/dvbl1537hhrzrycfv66cikzs0xcrk5px-gtest-1.17.0-dev/include/gtest/gtest.h |
| 198.9 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/unique_ptr.h |
| 195.8 | src/App/PropertyLinks.h |
| 194.7 | src/App/PropertyStandard.h |
| 194.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ostream.h |
| 169.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 163.7 | build/clang-profile/src/3rdParty/coin/include/Inventor/C/basic.h |
| 161.5 | src/App/PropertyExpressionEngine.h |
| 160.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/math.h |
| 159.8 | src/App/MappedName.h |
| 152.9 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/string |
| 150.1 | src/Mod/Part/App/TopoShape.h |
| 148.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 148.2 | src/3rdParty/coin/include/Inventor/SbByteBuffer.h |
| 148.0 | src/3rdParty/coin/include/Inventor/SbBasic.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 69.5 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 69.4 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 64.3 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 64.3 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 61.5 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 61.4 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 61.3 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 61.2 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 49.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 48.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 38.7 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 38.5 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 36.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 36.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 31.5 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 30.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 26.9 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 24.8 | std::vector<Base::Vector2d>::operator= |
| 23.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 23.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 23.2 | std::unique_ptr<App::DynamicProperty::Impl> |
| 23.1 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 23.1 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 19.1 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 19.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 36.7 | src/Gui/QtAll.h |
| 23.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 16.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 16.4 | src/Mod/Part/App/OpenCascadeAll.h |
| 14.9 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 14.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 12.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication |
| 12.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h |
| 12.1 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 11.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QAbstractEventDispatcher |
| 11.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 11.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |
| 10.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 10.0 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/sstream |
| 9.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 8.5 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp |
| 8.5 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp |
| 8.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 8.0 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/iostream |
| 8.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 7.8 | build/clang-profile/src/Mod/Import/Gui/CMakeFiles/ImportGui.dir/cmake_pch.hxx |
| 7.8 | src/Mod/Import/Gui/PreCompiled.h |
| 7.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdebug.h |
| 7.8 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ios_base.h |
| 7.6 | build/clang-profile/src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/cmake_pch.hxx |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 5.7 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 5.7 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 5.1 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 5.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 1.4 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 1.4 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 1.2 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 1.2 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 1.2 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 1.2 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 1.2 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 1.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 1.1 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 1.1 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 1.1 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 1.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 1.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 1.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.9 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.9 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.9 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.8 | std::formatter<bool, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.8 | std::__format::__formatter_int<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.8 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |
| 0.8 | std::__format::_Buf_sink<wchar_t> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 471.6 | src/App/DocumentObject.h |
| 428.3 | src/Mod/Part/App/PartFeature.h |
| 326.5 | src/App/Application.h |
| 316.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/memory |
| 307.9 | src/App/Document.h |
| 273.8 | src/Mod/Material/App/PropertyMaterial.h |
| 271.9 | src/Mod/Material/App/Materials.h |
| 230.4 | src/App/ComplexGeoData.h |
| 225.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 225.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 204.1 | /nix/store/dvbl1537hhrzrycfv66cikzs0xcrk5px-gtest-1.17.0-dev/include/gtest/gtest.h |
| 200.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/unique_ptr.h |
| 199.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ostream.h |
| 195.8 | src/App/PropertyLinks.h |
| 194.7 | src/App/PropertyStandard.h |
| 184.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 163.9 | build/clang-profile/src/3rdParty/coin/include/Inventor/C/basic.h |
| 163.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 161.5 | src/App/PropertyExpressionEngine.h |
| 160.8 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/math.h |
| 160.1 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/string |
| 159.8 | src/App/MappedName.h |
| 150.1 | src/Mod/Part/App/TopoShape.h |
| 148.6 | src/3rdParty/coin/include/Inventor/SbByteBuffer.h |
| 148.2 | src/3rdParty/coin/include/Inventor/SbBasic.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 75.3 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 75.2 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 66.4 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 66.3 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 64.3 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 64.3 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 61.5 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 61.4 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 49.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 48.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 38.7 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 38.5 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 36.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 36.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 31.5 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 30.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 26.9 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 24.8 | std::vector<Base::Vector2d>::operator= |
| 23.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 23.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 23.2 | std::unique_ptr<App::DynamicProperty::Impl> |
| 23.1 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 23.1 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 19.1 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 19.1 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/3rdParty/pivy/interfaces/CMakeFiles/pivy_coin.dir/coinPYTHON_wrap.cxx.o

Ninja 85.1 s; compiler 84.9 s; frontend 10.9 s; backend 74.0 s.

Top included files:

* 0.61 s — src/3rdParty/pivy/interfaces/coin_header_includes.h
* 0.29 s — /nix/store/h3l4z7p6wny3phbckwwhy1i2g52pdnj4-python3-3.13.15/include/python3.13/Python.h
* 0.20 s — src/3rdParty/coin/include/Inventor/actions/SoActions.h
* 0.19 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/math.h
* 0.19 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath
* 0.18 s — src/3rdParty/coin/include/Inventor/actions/SoCallbackAction.h
* 0.17 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/stdexcept
* 0.16 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/string
* 0.15 s — src/3rdParty/coin/include/Inventor/nodes/SoLightModel.h
* 0.15 s — src/3rdParty/coin/include/Inventor/elements/SoLazyElement.h

Top template instantiations:

* 0.01 s — std::basic_string<wchar_t>::_M_construct<const char *>
* 0.01 s — std::basic_string<wchar_t>::_S_copy_chars<const char *>
* 0.00 s — std::basic_string<char8_t>
* 0.00 s — std::operator+<char, std::char_traits<char>, std::allocator<char>>
* 0.00 s — std::basic_string<char32_t>
* 0.00 s — std::basic_string<wchar_t>
* 0.00 s — std::basic_string<char>
* 0.00 s — std::basic_string<char16_t>
* 0.00 s — std::basic_string<char8_t>::_M_construct<const char8_t *>
* 0.00 s — std::basic_string<char32_t>::_M_construct<const char32_t *>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 25.3 s; compiler 25.2 s; frontend 12.2 s; backend 12.9 s.

Top included files:

* 1.90 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.33 s — src/Mod/Sketcher/App/SketchObject.h
* 1.18 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.18 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.98 s — src/Mod/Sketcher/App/Sketch.h
* 0.92 s — src/App/Datums.h
* 0.92 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.74 s — src/App/GeoFeature.h
* 0.73 s — src/App/DocumentObject.h
* 0.62 s — src/Mod/Part/App/DatumFeature.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.15 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerEllipse, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 16.1 s; compiler 15.9 s; frontend 9.7 s; backend 6.2 s.

Top included files:

* 2.13 s — src/Mod/Sketcher/App/SketchObject.h
* 1.85 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.18 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.18 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.94 s — src/Mod/Sketcher/App/Sketch.h
* 0.91 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.79 s — src/Gui/CommandT.h
* 0.64 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.64 s — src/App/Document.h
* 0.56 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.13 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.13 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController

## src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o

Ninja 15.7 s; compiler 15.6 s; frontend 5.7 s; backend 9.8 s.

Top included files:

* 0.59 s — build/clang-profile/src/App/DocumentPy.h
* 0.42 s — src/App/Document.h
* 0.37 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/strong_components.hpp
* 0.33 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp
* 0.32 s — src/App/private/DocumentP.h
* 0.18 s — src/Base/UnitsApi.h
* 0.17 s — src/App/ExportInfo.h
* 0.17 s — src/App/DocumentObject.h
* 0.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/named_function_params.hpp
* 0.15 s — src/App/Application.h

Top template instantiations:

* 0.58 s — boost::basic_regex<char>::assign
* 0.29 s — boost::basic_regex<char>::set_expression
* 0.29 s — boost::basic_regex<char>::do_assign
* 0.28 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.25 s — boost::regex_search<const char *, std::allocator<boost::sub_match<const char *>>, char, boost::regex_traits<char>>
* 0.18 s — boost::bimaps::bimap<Base::Reference<App::StringHasher>, int>
* 0.14 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.14 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data
* 0.14 s — boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper
* 0.14 s — boost::regex_traits<char>::regex_traits

## src/Mod/MeshPart/App/CMakeFiles/flatmesh.dir/MeshFlatteningLscmRelax.cpp.o

Ninja 15.6 s; compiler 15.5 s; frontend 8.3 s; backend 7.1 s.

Top included files:

* 0.64 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/SparseCholesky
* 0.63 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/SparseCore
* 0.56 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.56 s — src/Mod/MeshPart/App/MeshFlatteningLscmRelax.h
* 0.54 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/iostream
* 0.53 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream
* 0.41 s — src/Mod/MeshPart/App/MeshFlattening.h
* 0.27 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ostream.h
* 0.26 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios
* 0.26 s — /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format

Top template instantiations:

* 1.69 s — Eigen::JacobiSVD<Eigen::Matrix<double, -1, -1>>::JacobiSVD
* 1.69 s — Eigen::JacobiSVD<Eigen::Matrix<double, -1, -1>>::compute
* 1.57 s — Eigen::internal::qr_preconditioner_impl<Eigen::Matrix<double, -1, -1>, 2, 0>::run
* 1.18 s — Eigen::Matrix<double, -1, -1>::operator=<Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>>
* 1.18 s — Eigen::PlainObjectBase<Eigen::Matrix<double, -1, -1>>::_set<Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>>
* 1.18 s — Eigen::internal::call_assignment<Eigen::Matrix<double, -1, -1>, Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>>
* 1.18 s — Eigen::internal::call_assignment<Eigen::Matrix<double, -1, -1>, Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>, Eigen::internal::assign_op<double, double>>
* 1.18 s — Eigen::Matrix<double, -1, -1>::Matrix<Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>>
* 1.18 s — Eigen::PlainObjectBase<Eigen::Matrix<double, -1, -1>>::_init1<Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>, Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>>
* 1.18 s — Eigen::PlainObjectBase<Eigen::Matrix<double, -1, -1>>::_set_noalias<Eigen::Product<Eigen::Matrix<double, -1, -1>, Eigen::Inverse<Eigen::Product<Eigen::Transpose<Eigen::Matrix<double, -1, -1>>, Eigen::Matrix<double, -1, -1>>>>>
