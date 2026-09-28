# Clang build profile

* Recorded Ninja log timestamp span: 141.7 s (131–141828 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 287; PCH jobs with traces: 3.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 834.0 | 14.7 | 848.8 |
| Frontend | 618.1 | 12.1 | 630.2 |
| Backend | 207.1 | 0.0 | 207.1 |
| Source | 448.2 | 2.4 | 450.6 |
| InstantiateFunction | 193.2 | 2.1 | 195.3 |
| InstantiateClass | 181.5 | 2.3 | 183.8 |
| Optimizer | 127.6 | 0.0 | 127.6 |
| CodeGenPasses | 78.9 | 0.0 | 78.9 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 23.4 | 23.3 | 10.7 | 12.5 | 5.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 14.5 | 14.4 | 8.1 | 6.2 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 13.1 | 13.0 | 7.1 | 5.8 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 12.3 | 12.2 | 8.6 | 3.5 | 6.3 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 11.8 | 11.7 | 7.5 | 4.2 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 9.9 | 9.8 | 5.8 | 3.9 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 9.7 | 9.6 | 5.0 | 4.6 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 9.4 | 9.3 | 6.5 | 2.8 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 9.4 | 9.3 | 3.5 | 5.8 | 1.8 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 9.2 | 9.1 | 6.3 | 2.8 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 9.1 | 9.0 | 3.2 | 5.7 | 1.7 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.9 | 8.8 | 6.3 | 2.4 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 8.4 | 8.3 | 5.1 | 3.2 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 8.3 | 8.2 | 4.7 | 3.4 | 3.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 8.0 | 7.9 | 4.5 | 3.3 | 3.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 7.9 | 7.8 | 3.7 | 4.1 | 2.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o |
| 7.7 | 7.6 | 4.7 | 2.9 | 3.0 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 7.6 | 7.5 | 4.4 | 3.1 | 3.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 7.5 | 7.4 | 5.5 | 1.9 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 7.5 | 7.4 | 5.7 | 1.6 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 7.4 | 7.3 | 3.2 | 4.1 | 2.1 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapePyImp.cpp.o |
| 7.4 | 7.3 | 5.3 | 2.0 | 3.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 7.3 | 7.2 | 5.5 | 1.6 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |
| 7.1 | 6.9 | 5.4 | 1.4 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 7.0 | 6.9 | 5.3 | 1.5 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 7.3 | 7.2 | 6.0 | 0.0 | 0.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx.pch |
| 4.4 | 4.3 | 3.5 | 0.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |
| 3.3 | 3.2 | 2.7 | 0.0 | 2.4 | src/Mod/Material/App/CMakeFiles/Materials.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 467.4 | 203 |
| Mod/Sketcher | 287.8 | 52 |
| Mod/Material | 78.8 | 32 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 102.4 | src/Mod/Part/App/PartFeature.h |
| 75.7 | src/App/ComplexGeoData.h |
| 72.1 | src/Mod/Material/App/Materials.h |
| 69.3 | src/Mod/Material/App/PropertyMaterial.h |
| 53.2 | src/App/MappedName.h |
| 49.6 | src/App/DocumentObject.h |
| 47.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 47.8 | src/Mod/Sketcher/App/SketchObject.h |
| 47.6 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 45.6 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 45.6 | src/App/Application.h |
| 45.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 41.7 | src/Mod/Part/App/AttachExtension.h |
| 41.5 | src/Mod/Part/App/Attacher.h |
| 40.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 36.9 | src/Mod/Material/App/MaterialValue.h |
| 35.2 | src/Mod/Part/App/TopoShape.h |
| 31.9 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 28.7 | src/Base/Exception.h |
| 25.1 | src/Gui/MetaTypes.h |
| 24.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 23.9 | src/Base/FileInfo.h |
| 23.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/filesystem |
| 23.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 23.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 10.5 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 10.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 10.4 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 10.4 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 8.5 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 8.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 6.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 6.2 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 6.2 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 6.2 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 5.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 4.2 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 4.2 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 3.7 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 3.7 | std::vector<Base::Vector2d>::operator= |
| 3.7 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 3.6 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 3.3 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 3.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 3.1 | std::sort<QList<App::StringIDRef>::iterator> |
| 3.1 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 3.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 2.8 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.8 | QList<App::SubObjectT>::push_front |
| 2.8 | QList<App::SubObjectT>::prepend |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 5.5 | build/clang-profile/src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx |
| 5.5 | src/Mod/Sketcher/Gui/PreCompiled.h |
| 3.1 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 3.1 | src/Mod/Part/App/PreCompiled.h |
| 2.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 2.4 | build/clang-profile/src/Mod/Material/App/CMakeFiles/Materials.dir/cmake_pch.hxx |
| 2.4 | src/Mod/Material/App/PreCompiled.h |
| 1.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdir.h |
| 1.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdiriterator.h |
| 1.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QDirIterator |
| 1.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 1.1 | src/Mod/Part/App/OpenCascadeAll.h |
| 1.1 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 1.1 | src/Gui/QtAll.h |
| 1.0 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdirlisting.h |
| 0.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstractanimation.h |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qfiledevice.h |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.6 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qiodevice.h |
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
| 0.1 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.1 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.1 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.1 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
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
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 102.4 | src/Mod/Part/App/PartFeature.h |
| 75.7 | src/App/ComplexGeoData.h |
| 72.1 | src/Mod/Material/App/Materials.h |
| 69.3 | src/Mod/Material/App/PropertyMaterial.h |
| 53.2 | src/App/MappedName.h |
| 49.6 | src/App/DocumentObject.h |
| 48.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 47.8 | src/Mod/Sketcher/App/SketchObject.h |
| 47.6 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 45.6 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 45.6 | src/App/Application.h |
| 45.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 41.7 | src/Mod/Part/App/AttachExtension.h |
| 41.5 | src/Mod/Part/App/Attacher.h |
| 40.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 36.9 | src/Mod/Material/App/MaterialValue.h |
| 35.2 | src/Mod/Part/App/TopoShape.h |
| 31.9 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 28.7 | src/Base/Exception.h |
| 25.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 25.1 | src/Gui/MetaTypes.h |
| 23.9 | src/Base/FileInfo.h |
| 23.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/filesystem |
| 23.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 23.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 10.5 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 10.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 10.4 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 10.4 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 8.5 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 8.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 6.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 6.2 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 6.2 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 6.2 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 5.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 4.2 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 4.2 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 3.7 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 3.7 | std::vector<Base::Vector2d>::operator= |
| 3.7 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 3.6 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 3.3 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 3.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 3.1 | std::sort<QList<App::StringIDRef>::iterator> |
| 3.1 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 3.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 2.8 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.8 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.8 | QList<App::SubObjectT>::push_front |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 23.4 s; compiler 23.3 s; frontend 10.7 s; backend 12.5 s.

Top included files:

* 1.27 s — src/Mod/Sketcher/App/SketchObject.h
* 0.95 s — src/Mod/Sketcher/App/Sketch.h
* 0.90 s — src/App/Datums.h
* 0.89 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.74 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.73 s — src/App/GeoFeature.h
* 0.72 s — src/App/DocumentObject.h
* 0.55 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h
* 0.55 s — src/Mod/Part/App/DatumFeature.h
* 0.54 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.25 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.24 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.23 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.21 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.14 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerBSpline, SketcherGui::StateMachines::TwoSeekEnd, 2, SketcherGui::OnViewParameters<4, 4>, SketcherGui::WidgetParameters<1, 1>, SketcherGui::WidgetCheckboxes<1, 1>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::BSplineConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 14.5 s; compiler 14.4 s; frontend 8.1 s; backend 6.2 s.

Top included files:

* 1.97 s — src/Mod/Sketcher/App/SketchObject.h
* 0.93 s — src/Mod/Sketcher/App/Sketch.h
* 0.89 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.79 s — src/Gui/CommandT.h
* 0.70 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.63 s — src/App/Document.h
* 0.59 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.55 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.51 s — src/Mod/Part/App/Part2DObject.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.20 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.19 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 13.1 s; compiler 13.0 s; frontend 7.1 s; backend 5.8 s.

Top included files:

* 1.68 s — src/Mod/Sketcher/App/SketchObject.h
* 0.96 s — src/Mod/Sketcher/App/Sketch.h
* 0.92 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.73 s — src/Gui/CommandT.h
* 0.60 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.60 s — src/App/Document.h
* 0.55 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.54 s — src/Mod/Part/App/Part2DObject.h
* 0.53 s — src/Mod/Part/App/AttachExtension.h
* 0.53 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 12.3 s; compiler 12.2 s; frontend 8.6 s; backend 3.5 s.

Top included files:

* 4.06 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 4.06 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 2.09 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 2.05 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 2.02 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.27 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_int.hpp
* 1.14 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.13 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.13 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.12 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp

Top template instantiations:

* 0.20 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.20 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.19 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.19 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.19 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.19 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.19 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.19 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.19 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.17 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 11.8 s; compiler 11.7 s; frontend 7.5 s; backend 4.2 s.

Top included files:

* 1.64 s — src/Mod/Sketcher/App/SketchObject.h
* 0.96 s — src/Mod/Sketcher/App/Sketch.h
* 0.92 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.62 s — src/App/Document.h
* 0.54 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.53 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 0.52 s — src/Mod/Part/App/Part2DObject.h
* 0.52 s — src/Mod/Part/App/AttachExtension.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
