# Clang build profile

* Recorded Ninja log timestamp span: 68.0 s (127–68103 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 203; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 412.6 | 4.5 | 417.1 |
| Frontend | 313.7 | 3.6 | 317.4 |
| Backend | 93.2 | 0.0 | 93.2 |
| Source | 247.0 | 0.0 | 247.0 |
| InstantiateFunction | 76.0 | 0.6 | 76.6 |
| InstantiateClass | 86.2 | 0.6 | 86.7 |
| Optimizer | 57.3 | 0.0 | 57.3 |
| CodeGenPasses | 35.4 | 0.0 | 35.4 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 11.6 | 11.5 | 8.0 | 3.5 | 5.9 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 9.4 | 9.3 | 3.5 | 5.7 | 1.8 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 9.1 | 9.0 | 3.4 | 5.6 | 1.7 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.2 | 8.1 | 3.7 | 4.3 | 2.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o |
| 7.1 | 7.0 | 4.0 | 3.0 | 2.6 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 6.7 | 6.6 | 3.5 | 3.0 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/Attacher.cpp.o |
| 6.0 | 5.9 | 3.4 | 2.4 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPartPy.cpp.o |
| 5.5 | 5.5 | 2.4 | 3.0 | 1.6 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapePyImp.cpp.o |
| 5.5 | 5.4 | 3.4 | 2.0 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyTopoShape.cpp.o |
| 5.0 | 4.9 | 3.3 | 1.6 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/MeasureClient.cpp.o |
| 4.8 | 4.7 | 3.5 | 1.2 | 2.9 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPart.cpp.o |
| 4.5 | 4.5 | 3.1 | 1.3 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachExtension.cpp.o |
| 4.5 | 4.4 | 2.9 | 1.5 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachEnginePyImp.cpp.o |
| 4.5 | 4.4 | 3.2 | 1.2 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyGeometryList.cpp.o |
| 4.1 | 4.0 | 2.9 | 1.1 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/ImportStep.cpp.o |
| 4.0 | 3.9 | 2.8 | 1.1 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartImportIges.cpp.o |
| 4.0 | 3.9 | 2.8 | 1.1 | 2.2 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartImportStep.cpp.o |
| 3.9 | 3.8 | 2.8 | 1.0 | 2.4 | src/Mod/Part/App/CMakeFiles/Part.dir/FeatureScale.cpp.o |
| 3.9 | 3.8 | 2.7 | 1.0 | 2.2 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartImportBrep.cpp.o |
| 3.8 | 3.8 | 2.7 | 1.1 | 2.2 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeaturePyImp.cpp.o |
| 3.8 | 3.7 | 2.7 | 1.0 | 2.2 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartCurveNet.cpp.o |
| 3.8 | 3.7 | 2.8 | 0.9 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachExtensionPyImp.cpp.o |
| 3.6 | 3.5 | 3.0 | 0.5 | 2.4 | src/Mod/Part/App/CMakeFiles/Part.dir/LinearPatternExtension.cpp.o |
| 3.6 | 3.5 | 2.8 | 0.6 | 2.2 | src/Mod/Part/App/CMakeFiles/Part.dir/FeatureProjectOnSurface.cpp.o |
| 3.4 | 3.4 | 2.9 | 0.4 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/FeatureExtrusion.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 4.6 | 4.5 | 3.6 | 0.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 412.6 | 203 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 76.5 | src/Mod/Part/App/PartFeature.h |
| 69.4 | src/App/ComplexGeoData.h |
| 46.3 | src/Mod/Material/App/PropertyMaterial.h |
| 44.4 | src/Mod/Material/App/Materials.h |
| 43.5 | src/App/MappedName.h |
| 43.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 40.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.6 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 37.9 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 35.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 33.3 | src/Mod/Part/App/TopoShape.h |
| 29.2 | src/App/Application.h |
| 25.4 | src/Mod/Part/App/AttachExtension.h |
| 25.0 | src/App/ElementMap.h |
| 24.7 | src/Mod/Part/App/Attacher.h |
| 23.8 | src/Base/Exception.h |
| 22.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 21.8 | src/Base/FileInfo.h |
| 21.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/filesystem |
| 21.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 21.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 20.6 | src/Mod/Part/App/PropertyTopoShape.h |
| 20.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 19.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 19.6 | src/App/DocumentObject.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.3 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.6 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.6 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.5 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 2.3 | std::vector<Base::Vector2d>::operator= |
| 2.2 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 2.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 2.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.5 | std::tuple<std::filesystem::path::_List::_Impl *, std::filesystem::path::_List::_Impl_deleter> |
| 1.4 | std::unique_ptr<Data::MappedNameRef> |
| 1.4 | std::unique_ptr<std::thread::_State> |
| 1.4 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 1.4 | std::unique_ptr<QTextStreamPrivate> |
| 1.4 | std::unique_ptr<App::StringHasher::HashMap> |
| 1.3 | std::unique_ptr<Base::Exception> |
| 1.3 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 1.3 | std::__uniq_ptr_data<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 1.3 | std::__uniq_ptr_impl<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 1.2 | std::__uniq_ptr_data<std::thread::_State, std::default_delete<std::thread::_State>> |
| 1.2 | std::__uniq_ptr_impl<std::thread::_State, std::default_delete<std::thread::_State>> |
| 1.2 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 1.2 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 1.2 | std::__uniq_ptr_data<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 1.2 | std::__uniq_ptr_impl<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 3.2 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 3.2 | src/Mod/Part/App/PreCompiled.h |
| 1.2 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_generators.hpp |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/BRepMesh_IncrementalMesh.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_Context.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_ModelBuilder.hxx |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/nil_generator.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid.hpp |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Model.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Types.hxx |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/queue |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/stl_queue.h |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/algorithm/string/predicate.hpp |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ranges |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_clock.hpp |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.1 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::formatter<bool, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::__formatter_int<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_int<wchar_t>::format<unsigned char, std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 76.5 | src/Mod/Part/App/PartFeature.h |
| 69.4 | src/App/ComplexGeoData.h |
| 46.3 | src/Mod/Material/App/PropertyMaterial.h |
| 44.4 | src/Mod/Material/App/Materials.h |
| 43.5 | src/App/MappedName.h |
| 43.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 40.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.6 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 37.9 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 35.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 33.3 | src/Mod/Part/App/TopoShape.h |
| 29.2 | src/App/Application.h |
| 25.4 | src/Mod/Part/App/AttachExtension.h |
| 25.0 | src/App/ElementMap.h |
| 24.7 | src/Mod/Part/App/Attacher.h |
| 23.8 | src/Base/Exception.h |
| 22.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 21.8 | src/Base/FileInfo.h |
| 21.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/filesystem |
| 21.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 21.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 20.6 | src/Mod/Part/App/PropertyTopoShape.h |
| 20.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 19.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 19.6 | src/App/DocumentObject.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.3 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.6 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.6 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 2.5 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 2.3 | std::vector<Base::Vector2d>::operator= |
| 2.2 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 2.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 2.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.5 | std::tuple<std::filesystem::path::_List::_Impl *, std::filesystem::path::_List::_Impl_deleter> |
| 1.4 | std::unique_ptr<Data::MappedNameRef> |
| 1.4 | std::unique_ptr<std::thread::_State> |
| 1.4 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 1.4 | std::unique_ptr<QTextStreamPrivate> |
| 1.4 | std::unique_ptr<App::StringHasher::HashMap> |
| 1.3 | std::unique_ptr<Base::Exception> |
| 1.3 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 1.3 | std::__uniq_ptr_data<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 1.3 | std::__uniq_ptr_impl<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 1.2 | std::__uniq_ptr_data<std::thread::_State, std::default_delete<std::thread::_State>> |
| 1.2 | std::__uniq_ptr_impl<std::thread::_State, std::default_delete<std::thread::_State>> |
| 1.2 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 1.2 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 1.2 | std::__uniq_ptr_data<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 1.2 | std::__uniq_ptr_impl<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 11.6 s; compiler 11.5 s; frontend 8.0 s; backend 3.5 s.

Top included files:

* 3.79 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.79 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.84 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.81 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.78 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.14 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.14 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.14 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.13 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.08 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.18 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.18 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.17 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.17 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.15 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o

Ninja 9.4 s; compiler 9.3 s; frontend 3.5 s; backend 5.7 s.

Top included files:

* 0.98 s — src/Mod/Part/App/BRepMesh.h
* 0.98 s — src/App/ComplexGeoData.h
* 0.76 s — src/App/MappedName.h
* 0.36 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.36 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h
* 0.28 s — src/Mod/Part/App/FaceMakerBullseye.h
* 0.27 s — src/Mod/Part/App/FaceMaker.h
* 0.26 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication

Top template instantiations:

* 0.49 s — boost::basic_regex<char>::assign
* 0.24 s — boost::basic_regex<char>::basic_regex
* 0.24 s — boost::basic_regex<char>::do_assign
* 0.24 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.12 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.12 s — boost::regex_match<char, std::allocator<boost::sub_match<const char *>>, boost::regex_traits<char>>
* 0.12 s — boost::regex_match<const char *, std::allocator<boost::sub_match<const char *>>, char, boost::regex_traits<char>>
* 0.12 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.11 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.11 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o

Ninja 9.1 s; compiler 9.0 s; frontend 3.4 s; backend 5.6 s.

Top included files:

* 1.20 s — src/Mod/Part/App/CrossSection.h
* 1.20 s — src/Mod/Part/App/TopoShape.h
* 1.17 s — src/App/ComplexGeoData.h
* 0.88 s — src/App/MappedName.h
* 0.35 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.35 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h
* 0.26 s — src/App/ElementMap.h
* 0.26 s — src/Mod/Part/App/FaceMaker.h

Top template instantiations:

* 0.04 s — QList<App::StringIDRef>::append
* 0.03 s — std::unique_ptr<OSD_Parallel::IteratorInterface>
* 0.03 s — std::make_unique<Part::ProgressIndicator>
* 0.03 s — Base::ConsoleSingleton::developerWarning<std::basic_string<char>>
* 0.03 s — Base::ConsoleSingleton::send<Base::LogStyle::Warning, Base::IntendedRecipient::Developer, Base::ContentType::Untranslatable, std::basic_string<char>>
* 0.03 s — std::format<std::basic_string<char>>
* 0.03 s — std::unique_ptr<Part::ProgressIndicator>
* 0.03 s — std::__uniq_ptr_data<Part::ProgressIndicator, std::default_delete<Part::ProgressIndicator>>
* 0.03 s — std::__uniq_ptr_impl<Part::ProgressIndicator, std::default_delete<Part::ProgressIndicator>>
* 0.02 s — std::map<Data::IndexedName, std::map<Part::NameKey, Part::NameInfo>>::operator[]

## src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o

Ninja 8.2 s; compiler 8.1 s; frontend 3.7 s; backend 4.3 s.

Top included files:

* 0.67 s — src/App/Application.h
* 0.44 s — src/Mod/Part/App/TopoShape.h
* 0.41 s — src/App/ComplexGeoData.h
* 0.37 s — src/App/MappedName.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.26 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h
* 0.23 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.21 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/mutex.hpp

Top template instantiations:

* 0.04 s — Base::ConsoleSingleton::warning<const char *&>
* 0.03 s — std::vector<int>::rbegin
* 0.02 s — std::unique_ptr<Part::GeomCurve>
* 0.02 s — std::make_unique<Part::GeomPoint, Base::Vector3<double>>
* 0.02 s — std::__uniq_ptr_data<Part::GeomCurve, std::default_delete<Part::GeomCurve>>
* 0.02 s — std::__uniq_ptr_impl<Part::GeomCurve, std::default_delete<Part::GeomCurve>>
* 0.02 s — Base::ConsoleSingleton::error<std::basic_string<char> &>
* 0.02 s — std::make_unique<Part::GeomEllipse, opencascade::handle<Geom_Ellipse> &>
* 0.02 s — Base::ConsoleSingleton::send<Base::LogStyle::Warning, Base::IntendedRecipient::All, Base::ContentType::Untranslated, const char *&>
* 0.02 s — std::sort<QList<App::StringIDRef>::iterator>

## src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o

Ninja 7.1 s; compiler 7.0 s; frontend 4.0 s; backend 3.0 s.

Top included files:

* 0.66 s — src/App/Application.h
* 0.59 s — src/App/Document.h
* 0.56 s — src/App/Datums.h
* 0.53 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.53 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.36 s — src/Mod/Material/App/MaterialManager.h
* 0.32 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.29 s — src/Mod/Material/App/Materials.h

Top template instantiations:

* 0.03 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.03 s — std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>
* 0.03 s — std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>>
* 0.03 s — QList<Data::MappedElement>::append
* 0.03 s — QList<Data::MappedElement>::push_back
* 0.02 s — QList<Data::MappedElement>::emplaceBack<Data::MappedElement>
* 0.02 s — QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement>
* 0.02 s — boost::algorithm::starts_with<std::basic_string<char>, const char *>
* 0.02 s — boost::algorithm::starts_with<std::basic_string<char>, const char *, boost::algorithm::is_equal>
* 0.02 s — QArrayDataPointer<Data::MappedElement>::detachAndGrow
