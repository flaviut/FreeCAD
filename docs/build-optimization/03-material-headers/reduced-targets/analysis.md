# Clang build profile

* Recorded Ninja log timestamp span: 126.5 s (132–126666 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 287; PCH jobs with traces: 3.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 734.7 | 14.2 | 748.9 |
| Frontend | 532.9 | 11.8 | 544.7 |
| Backend | 193.9 | 0.0 | 193.9 |
| Source | 401.9 | 2.3 | 404.3 |
| InstantiateFunction | 148.4 | 2.1 | 150.4 |
| InstantiateClass | 155.0 | 2.2 | 157.2 |
| Optimizer | 119.8 | 0.0 | 119.8 |
| CodeGenPasses | 73.5 | 0.0 | 73.5 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 22.4 | 22.2 | 10.2 | 11.9 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 13.8 | 13.7 | 7.8 | 5.8 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 12.4 | 12.3 | 6.8 | 5.4 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 11.6 | 11.5 | 8.0 | 3.4 | 5.9 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 11.4 | 11.3 | 7.1 | 4.2 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 9.3 | 9.2 | 3.5 | 5.7 | 1.8 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 9.2 | 9.1 | 5.3 | 3.8 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 9.2 | 9.1 | 4.5 | 4.5 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 8.8 | 8.7 | 3.2 | 5.5 | 1.6 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.8 | 8.7 | 6.0 | 2.6 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.5 | 8.4 | 5.8 | 2.6 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 8.1 | 8.0 | 5.7 | 2.3 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 8.0 | 7.9 | 4.7 | 3.2 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 7.9 | 7.8 | 3.7 | 4.1 | 2.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o |
| 7.8 | 7.7 | 4.4 | 3.3 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 7.6 | 7.5 | 4.4 | 3.1 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 7.4 | 7.3 | 5.6 | 1.6 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 7.2 | 7.1 | 5.2 | 1.9 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 6.9 | 6.8 | 3.9 | 2.9 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 6.7 | 6.7 | 4.8 | 1.8 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 6.5 | 6.4 | 4.8 | 1.5 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 6.4 | 6.4 | 4.9 | 1.4 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 6.4 | 6.3 | 3.5 | 2.7 | 2.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 6.4 | 6.3 | 3.4 | 2.8 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/Attacher.cpp.o |
| 6.3 | 6.2 | 4.7 | 1.4 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 7.0 | 6.9 | 5.8 | 0.0 | 0.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx.pch |
| 4.2 | 4.2 | 3.4 | 0.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |
| 3.2 | 3.2 | 2.6 | 0.0 | 2.3 | src/Mod/Material/App/CMakeFiles/Materials.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 405.1 | 203 |
| Mod/Sketcher | 268.6 | 52 |
| Mod/Material | 61.0 | 32 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 90.4 | src/Mod/Part/App/PartFeature.h |
| 74.5 | src/App/ComplexGeoData.h |
| 51.4 | src/Mod/Material/App/PropertyMaterial.h |
| 49.3 | src/Mod/Material/App/Materials.h |
| 46.7 | src/App/MappedName.h |
| 45.4 | src/Mod/Sketcher/App/SketchObject.h |
| 42.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 41.4 | src/App/Application.h |
| 41.4 | src/Mod/Part/App/TopoShape.h |
| 40.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.9 | src/App/DocumentObject.h |
| 39.2 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 37.6 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 36.5 | src/Mod/Part/App/AttachExtension.h |
| 35.9 | src/Mod/Part/App/Attacher.h |
| 35.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 30.2 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 29.5 | src/Mod/Part/App/PropertyTopoShape.h |
| 26.3 | src/App/ElementMap.h |
| 25.8 | src/Base/Exception.h |
| 22.5 | src/Mod/Sketcher/App/Sketch.h |
| 22.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 21.3 | src/Base/FileInfo.h |
| 21.2 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 21.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.4 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 3.2 | std::vector<Base::Vector2d>::operator= |
| 3.2 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 3.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 2.8 | std::sort<QList<App::StringIDRef>::iterator> |
| 2.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 2.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 2.5 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.5 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.3 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 2.3 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 2.2 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 2.2 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 2.2 | std::map<QString, Materials::ModelProperty>::operator[] |
| 2.1 | std::unique_ptr<Base::Exception> |
| 2.1 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 1.9 | std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>> |
| 1.9 | std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>> |
| 1.9 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 1.9 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 1.9 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.8 | std::unique_ptr<Data::MappedNameRef> |
| 1.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 1.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 1.7 | std::unique_ptr<App::StringHasher::HashMap> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 5.2 | build/clang-profile/src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx |
| 5.2 | src/Mod/Sketcher/Gui/PreCompiled.h |
| 3.0 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 3.0 | src/Mod/Part/App/PreCompiled.h |
| 2.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 2.3 | build/clang-profile/src/Mod/Material/App/CMakeFiles/Materials.dir/cmake_pch.hxx |
| 2.3 | src/Mod/Material/App/PreCompiled.h |
| 1.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdir.h |
| 1.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdiriterator.h |
| 1.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QDirIterator |
| 1.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 1.1 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 1.1 | src/Mod/Part/App/OpenCascadeAll.h |
| 1.0 | src/Gui/QtAll.h |
| 0.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdirlisting.h |
| 0.9 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstractanimation.h |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qfiledevice.h |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qiodevice.h |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 0.3 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 0.3 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.3 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 0.3 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.1 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.1 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.1 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.1 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.1 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.1 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.1 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.1 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.1 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::formatter<wchar_t, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::formatter<bool, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_int<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::chrono::hh_mm_ss<std::chrono::duration<long>>::hh_mm_ss |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 90.4 | src/Mod/Part/App/PartFeature.h |
| 74.5 | src/App/ComplexGeoData.h |
| 51.4 | src/Mod/Material/App/PropertyMaterial.h |
| 49.3 | src/Mod/Material/App/Materials.h |
| 46.7 | src/App/MappedName.h |
| 45.4 | src/Mod/Sketcher/App/SketchObject.h |
| 43.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 41.4 | src/App/Application.h |
| 41.4 | src/Mod/Part/App/TopoShape.h |
| 40.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.9 | src/App/DocumentObject.h |
| 39.2 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 37.6 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 36.5 | src/Mod/Part/App/AttachExtension.h |
| 35.9 | src/Mod/Part/App/Attacher.h |
| 35.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 30.2 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 29.5 | src/Mod/Part/App/PropertyTopoShape.h |
| 26.3 | src/App/ElementMap.h |
| 25.8 | src/Base/Exception.h |
| 22.5 | src/Mod/Sketcher/App/Sketch.h |
| 22.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 21.3 | src/Base/FileInfo.h |
| 21.2 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 21.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.4 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 3.2 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 3.2 | std::vector<Base::Vector2d>::operator= |
| 3.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 2.8 | std::sort<QList<App::StringIDRef>::iterator> |
| 2.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 2.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 2.5 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.5 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.3 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 2.3 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 2.2 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 2.2 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 2.2 | std::map<QString, Materials::ModelProperty>::operator[] |
| 2.1 | std::unique_ptr<Base::Exception> |
| 2.1 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 1.9 | std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>> |
| 1.9 | std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>> |
| 1.9 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 1.9 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 1.9 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.8 | std::unique_ptr<Data::MappedNameRef> |
| 1.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 1.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 1.7 | std::unique_ptr<App::StringHasher::HashMap> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 22.4 s; compiler 22.2 s; frontend 10.2 s; backend 11.9 s.

Top included files:

* 1.23 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.84 s — src/App/Datums.h
* 0.68 s — src/App/GeoFeature.h
* 0.67 s — src/App/DocumentObject.h
* 0.67 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.58 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.50 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h

Top template instantiations:

* 0.23 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerCircle, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<3, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 13.8 s; compiler 13.7 s; frontend 7.8 s; backend 5.8 s.

Top included files:

* 1.77 s — src/Mod/Sketcher/App/SketchObject.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.85 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.72 s — src/Gui/CommandT.h
* 0.67 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.66 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.57 s — src/App/Document.h
* 0.54 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.48 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.20 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 12.4 s; compiler 12.3 s; frontend 6.8 s; backend 5.4 s.

Top included files:

* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.88 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.68 s — src/Gui/CommandT.h
* 0.57 s — src/App/Document.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.50 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.49 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.47 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.07 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.07 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.05 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 11.6 s; compiler 11.5 s; frontend 8.0 s; backend 3.4 s.

Top included files:

* 3.81 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.81 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.89 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.86 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.81 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.12 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.12 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.11 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_int.hpp

Top template instantiations:

* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.17 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.17 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.17 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.17 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.15 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 11.4 s; compiler 11.3 s; frontend 7.1 s; backend 4.2 s.

Top included files:

* 1.55 s — src/Mod/Sketcher/App/SketchObject.h
* 0.94 s — src/Mod/Sketcher/App/Sketch.h
* 0.90 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.61 s — src/App/Document.h
* 0.55 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 0.54 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.50 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.47 s — src/Mod/Part/App/Part2DObject.h
* 0.47 s — src/Mod/Part/App/AttachExtension.h

Top template instantiations:

* 0.05 s — Gui::cmdAppObjectArgs<>
* 0.05 s — QObject::connect<void (QWindow::*)(QScreen *), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/ViewProviderSketch.cpp:4685:84)>
* 0.04 s — boost::basic_format<char>::basic_format
* 0.04 s — boost::basic_format<char>::parse
* 0.03 s — std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator=
* 0.03 s — std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base
* 0.03 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.03 s — Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple>
* 0.03 s — QMap<QString, QString>
* 0.03 s — Gui::StyleParameters::Diagnostics::report<const char *, std::basic_string<char>>
