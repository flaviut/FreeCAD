# Clang build profile

* Recorded Ninja log timestamp span: 42.5 s (124–42590 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 61; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 219.8 | 4.1 | 223.9 |
| Frontend | 140.2 | 3.3 | 143.5 |
| Backend | 77.7 | 0.0 | 77.7 |
| Source | 39.0 | 0.0 | 39.0 |
| InstantiateFunction | 35.3 | 0.6 | 35.9 |
| InstantiateClass | 39.4 | 0.5 | 39.9 |
| Optimizer | 46.1 | 0.0 | 46.1 |
| CodeGenPasses | 31.5 | 0.0 | 31.5 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 12.0 | 11.8 | 8.3 | 3.5 | 6.1 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 9.4 | 9.3 | 4.1 | 5.2 | 3.4 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_42_cxx.cxx.o |
| 9.2 | 9.1 | 3.5 | 5.6 | 1.8 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 8.9 | 8.8 | 3.3 | 5.5 | 1.7 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.1 | 8.0 | 4.2 | 3.7 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_39_cxx.cxx.o |
| 7.1 | 7.0 | 4.0 | 2.9 | 2.7 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 6.8 | 6.7 | 3.7 | 2.9 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_44_cxx.cxx.o |
| 5.8 | 5.7 | 3.3 | 2.3 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPartPy.cpp.o |
| 5.4 | 5.4 | 3.2 | 2.1 | 2.4 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyTopoShape.cpp.o |
| 5.3 | 5.3 | 2.3 | 2.9 | 1.5 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapePyImp.cpp.o |
| 5.2 | 5.1 | 3.3 | 1.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_8_cxx.cxx.o |
| 4.9 | 4.8 | 3.2 | 1.6 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_12_cxx.cxx.o |
| 4.9 | 4.8 | 2.4 | 2.4 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_45_cxx.cxx.o |
| 4.8 | 4.7 | 3.2 | 1.5 | 2.6 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_11_cxx.cxx.o |
| 4.6 | 4.5 | 3.0 | 1.5 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_4_cxx.cxx.o |
| 4.6 | 4.5 | 2.9 | 1.5 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_23_cxx.cxx.o |
| 4.3 | 4.2 | 3.0 | 1.3 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_22_cxx.cxx.o |
| 4.3 | 4.2 | 3.3 | 0.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_6_cxx.cxx.o |
| 4.1 | 4.0 | 3.2 | 0.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_43_cxx.cxx.o |
| 4.0 | 4.0 | 2.8 | 1.1 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_1_cxx.cxx.o |
| 4.0 | 3.9 | 2.8 | 1.1 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/ImportStep.cpp.o |
| 3.9 | 3.9 | 2.8 | 1.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_2_cxx.cxx.o |
| 3.8 | 3.8 | 2.2 | 1.6 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_24_cxx.cxx.o |
| 3.7 | 3.6 | 1.8 | 1.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_40_cxx.cxx.o |
| 3.7 | 3.6 | 2.8 | 0.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_3_cxx.cxx.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 4.2 | 4.1 | 3.3 | 0.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 219.8 | 61 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 28.4 | src/App/ComplexGeoData.h |
| 28.4 | src/Mod/Part/App/PartFeature.h |
| 18.0 | src/Mod/Part/App/TopoShape.h |
| 17.9 | src/App/MappedName.h |
| 17.7 | src/Mod/Material/App/PropertyMaterial.h |
| 17.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 17.0 | src/Mod/Material/App/Materials.h |
| 14.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 12.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 12.9 | src/App/Application.h |
| 11.6 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 11.1 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 10.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 10.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 9.5 | src/App/ElementMap.h |
| 9.2 | src/Mod/Part/App/AttachExtension.h |
| 9.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 8.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 8.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.3 | src/Mod/Part/App/Attacher.h |
| 8.1 | src/Mod/Material/App/MaterialValue.h |
| 7.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 7.4 | src/Mod/Part/App/FaceMaker.h |
| 7.2 | src/Base/Exception.h |
| 7.1 | src/App/DocumentObject.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 1.0 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.9 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.9 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.8 | std::vector<Base::Vector2d>::operator= |
| 0.8 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.8 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.7 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.6 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.6 | std::unique_ptr<Data::MappedNameRef> |
| 0.6 | std::unique_ptr<QTextStreamPrivate> |
| 0.6 | std::unique_ptr<App::StringHasher::HashMap> |
| 0.6 | std::unique_ptr<std::thread::_State> |
| 0.6 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.5 | std::__uniq_ptr_data<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.5 | std::unique_ptr<Base::Exception> |
| 0.5 | std::__uniq_ptr_impl<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.5 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.5 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.5 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.5 | boost::basic_regex<char>::assign |
| 0.5 | std::__uniq_ptr_data<std::thread::_State, std::default_delete<std::thread::_State>> |
| 0.5 | std::__uniq_ptr_impl<std::thread::_State, std::default_delete<std::thread::_State>> |
| 0.5 | std::__uniq_ptr_data<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 0.5 | std::__uniq_ptr_impl<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 3.0 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 3.0 | src/Mod/Part/App/PreCompiled.h |
| 1.1 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_generators.hpp |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/nil_generator.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/algorithm/string/predicate.hpp |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/BRepMesh_IncrementalMesh.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_Context.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_ModelBuilder.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Model.hxx |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_clock.hpp |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Types.hxx |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bits/ios_base.h |
| 0.1 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/range/as_literal.hpp |
| 0.1 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/range/iterator_range.hpp |

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
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::chrono::hh_mm_ss<std::chrono::duration<long>>::hh_mm_ss |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |
| 0.0 | std::__format::_Buf_sink<wchar_t> |
| 0.0 | std::__format::_Sink<wchar_t> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 28.4 | src/App/ComplexGeoData.h |
| 28.4 | src/Mod/Part/App/PartFeature.h |
| 18.0 | src/Mod/Part/App/TopoShape.h |
| 17.9 | src/App/MappedName.h |
| 17.7 | src/Mod/Material/App/PropertyMaterial.h |
| 17.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 17.0 | src/Mod/Material/App/Materials.h |
| 14.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 12.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 12.9 | src/App/Application.h |
| 11.6 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 11.1 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 10.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 10.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 9.5 | src/App/ElementMap.h |
| 9.2 | src/Mod/Part/App/AttachExtension.h |
| 9.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 8.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 8.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.3 | src/Mod/Part/App/Attacher.h |
| 8.1 | src/Mod/Material/App/MaterialValue.h |
| 7.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 7.4 | src/Mod/Part/App/FaceMaker.h |
| 7.2 | src/Base/Exception.h |
| 7.1 | src/App/DocumentObject.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 1.0 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.9 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.9 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.8 | std::vector<Base::Vector2d>::operator= |
| 0.8 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.8 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.7 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.6 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.6 | std::unique_ptr<Data::MappedNameRef> |
| 0.6 | std::unique_ptr<QTextStreamPrivate> |
| 0.6 | std::unique_ptr<App::StringHasher::HashMap> |
| 0.6 | std::unique_ptr<std::thread::_State> |
| 0.6 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.5 | std::__uniq_ptr_data<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.5 | std::unique_ptr<Base::Exception> |
| 0.5 | std::__uniq_ptr_impl<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.5 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.5 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.5 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.5 | boost::basic_regex<char>::assign |
| 0.5 | std::__uniq_ptr_data<std::thread::_State, std::default_delete<std::thread::_State>> |
| 0.5 | std::__uniq_ptr_impl<std::thread::_State, std::default_delete<std::thread::_State>> |
| 0.5 | std::__uniq_ptr_data<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 0.5 | std::__uniq_ptr_impl<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 12.0 s; compiler 11.8 s; frontend 8.3 s; backend 3.5 s.

Top included files:

* 3.93 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.93 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.79 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.76 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.73 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.28 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.28 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.28 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.26 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.20 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

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

## src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_42_cxx.cxx.o

Ninja 9.4 s; compiler 9.3 s; frontend 4.1 s; backend 5.2 s.

Top included files:

* 3.01 s — src/Mod/Part/App/Geometry.cpp
* 0.65 s — src/App/Application.h
* 0.44 s — src/Mod/Part/App/TopoShape.h
* 0.41 s — src/App/ComplexGeoData.h
* 0.37 s — src/App/MappedName.h
* 0.36 s — src/Mod/Part/App/Geometry2d.cpp
* 0.31 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h

Top template instantiations:

* 0.03 s — Base::ConsoleSingleton::warning<const char *&>
* 0.03 s — std::vector<int>::rbegin
* 0.02 s — std::unique_ptr<Part::GeomCurve>
* 0.02 s — std::make_unique<Part::Geom2dTrimmedCurve, opencascade::handle<Geom2d_TrimmedCurve>>
* 0.02 s — std::__uniq_ptr_data<Part::GeomCurve, std::default_delete<Part::GeomCurve>>
* 0.02 s — std::__uniq_ptr_impl<Part::GeomCurve, std::default_delete<Part::GeomCurve>>
* 0.02 s — std::make_unique<Part::GeomPoint, Base::Vector3<double>>
* 0.02 s — std::unique_ptr<Part::Geom2dTrimmedCurve>
* 0.02 s — Base::ConsoleSingleton::error<std::basic_string<char> &>
* 0.02 s — std::__uniq_ptr_data<Part::Geom2dTrimmedCurve, std::default_delete<Part::Geom2dTrimmedCurve>>

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o

Ninja 9.2 s; compiler 9.1 s; frontend 3.5 s; backend 5.6 s.

Top included files:

* 0.97 s — src/Mod/Part/App/BRepMesh.h
* 0.97 s — src/App/ComplexGeoData.h
* 0.74 s — src/App/MappedName.h
* 0.35 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.35 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h
* 0.28 s — src/Mod/Part/App/FaceMakerBullseye.h
* 0.26 s — src/Mod/Part/App/FaceMaker.h
* 0.25 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication

Top template instantiations:

* 0.53 s — boost::basic_regex<char>::assign
* 0.26 s — boost::basic_regex<char>::basic_regex
* 0.26 s — boost::basic_regex<char>::do_assign
* 0.26 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.12 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.12 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.12 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data
* 0.12 s — boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper
* 0.12 s — boost::regex_traits<char>::regex_traits

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o

Ninja 8.9 s; compiler 8.8 s; frontend 3.3 s; backend 5.5 s.

Top included files:

* 1.21 s — src/Mod/Part/App/CrossSection.h
* 1.21 s — src/Mod/Part/App/TopoShape.h
* 1.18 s — src/App/ComplexGeoData.h
* 0.88 s — src/App/MappedName.h
* 0.34 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.34 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h
* 0.26 s — src/App/ElementMap.h
* 0.26 s — src/Mod/Part/App/FaceMaker.h

Top template instantiations:

* 0.04 s — QList<App::StringIDRef>::append
* 0.03 s — std::make_unique<Part::ProgressIndicator>
* 0.03 s — std::unique_ptr<OSD_Parallel::IteratorInterface>
* 0.02 s — std::unique_ptr<Part::ProgressIndicator>
* 0.02 s — std::__uniq_ptr_data<Part::ProgressIndicator, std::default_delete<Part::ProgressIndicator>>
* 0.02 s — std::__uniq_ptr_impl<Part::ProgressIndicator, std::default_delete<Part::ProgressIndicator>>
* 0.02 s — std::map<Data::IndexedName, std::map<Part::NameKey, Part::NameInfo>>::operator[]
* 0.02 s — QList<App::StringIDRef>::operator+=
* 0.02 s — Base::ConsoleSingleton::developerWarning<std::basic_string<char>>
* 0.02 s — QtPrivate::QCommonArrayOps<App::StringIDRef>::growAppend

## src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_39_cxx.cxx.o

Ninja 8.1 s; compiler 8.0 s; frontend 4.2 s; backend 3.7 s.

Top included files:

* 2.79 s — src/Mod/Part/App/Attacher.cpp
* 0.66 s — src/App/Application.h
* 0.59 s — src/Mod/Part/App/Attacher.h
* 0.58 s — src/App/Document.h
* 0.54 s — src/App/Datums.h
* 0.54 s — src/Mod/Part/App/PartFeature.h
* 0.51 s — src/Mod/Part/App/AppPart.cpp
* 0.50 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.50 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.33 s — src/Mod/Material/App/PropertyMaterial.h

Top template instantiations:

* 0.05 s — Base::ConsoleSingleton::warning<const char *>
* 0.03 s — Base::registerServiceImplementation<App::SubObjectPlacementProvider>
* 0.03 s — Base::ServiceProvider::registerImplementation<App::SubObjectPlacementProvider>
* 0.02 s — std::map<std::basic_string<char>, std::deque<Base::ServiceProvider::ServiceDescriptor>>::operator[]
* 0.02 s — Base::ConsoleSingleton::send<Base::LogStyle::Warning, Base::IntendedRecipient::All, Base::ContentType::Untranslated, const char *>
* 0.02 s — std::format<const char *>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::sort<QList<App::StringIDRef>::iterator>
* 0.02 s — std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter>
