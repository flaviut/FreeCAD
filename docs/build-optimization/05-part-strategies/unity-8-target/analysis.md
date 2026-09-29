# Clang build profile

* Recorded Ninja log timestamp span: 36.6 s (123–36719 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 37; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 178.9 | 4.2 | 183.0 |
| Frontend | 103.3 | 3.4 | 106.6 |
| Backend | 74.3 | 0.0 | 74.3 |
| Source | 36.4 | 0.0 | 36.4 |
| InstantiateFunction | 26.5 | 0.6 | 27.1 |
| InstantiateClass | 29.0 | 0.5 | 29.5 |
| Optimizer | 43.6 | 0.0 | 43.6 |
| CodeGenPasses | 30.5 | 0.0 | 30.5 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 11.8 | 11.7 | 8.1 | 3.5 | 6.0 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 11.6 | 11.5 | 5.6 | 5.9 | 3.4 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_21_cxx.cxx.o |
| 9.2 | 9.1 | 3.5 | 5.6 | 1.8 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 8.9 | 8.8 | 4.3 | 4.5 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_22_cxx.cxx.o |
| 8.8 | 8.7 | 3.2 | 5.5 | 1.6 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.4 | 8.3 | 4.3 | 4.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_19_cxx.cxx.o |
| 7.1 | 7.0 | 4.1 | 2.9 | 2.7 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 6.2 | 6.2 | 3.6 | 2.5 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_4_cxx.cxx.o |
| 5.9 | 5.8 | 3.4 | 2.4 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPartPy.cpp.o |
| 5.4 | 5.3 | 3.4 | 1.9 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_2_cxx.cxx.o |
| 5.4 | 5.3 | 3.3 | 2.0 | 2.5 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyTopoShape.cpp.o |
| 5.4 | 5.3 | 3.4 | 1.9 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_6_cxx.cxx.o |
| 5.4 | 5.3 | 2.5 | 2.8 | 1.6 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapePyImp.cpp.o |
| 5.2 | 5.1 | 3.3 | 1.7 | 2.6 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_5_cxx.cxx.o |
| 5.0 | 4.9 | 3.1 | 1.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_11_cxx.cxx.o |
| 5.0 | 4.9 | 3.1 | 1.8 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_1_cxx.cxx.o |
| 4.8 | 4.7 | 2.3 | 2.4 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_12_cxx.cxx.o |
| 4.6 | 4.6 | 3.1 | 1.4 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_0_cxx.cxx.o |
| 4.6 | 4.5 | 3.5 | 1.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_3_cxx.cxx.o |
| 4.2 | 4.2 | 2.2 | 2.0 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_20_cxx.cxx.o |
| 4.1 | 4.0 | 1.9 | 2.1 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_9_cxx.cxx.o |
| 4.1 | 4.0 | 2.9 | 1.1 | 2.4 | src/Mod/Part/App/CMakeFiles/Part.dir/ImportStep.cpp.o |
| 3.6 | 3.5 | 2.0 | 1.5 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_23_cxx.cxx.o |
| 3.3 | 3.3 | 1.9 | 1.3 | 1.5 | src/Mod/Part/App/CMakeFiles/Part.dir/FaceMakerBuildFace.cpp.o |
| 3.3 | 3.2 | 2.8 | 0.4 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartFuse.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 4.2 | 4.2 | 3.4 | 0.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 178.9 | 37 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 19.6 | src/Mod/Part/App/PartFeature.h |
| 18.9 | src/App/ComplexGeoData.h |
| 12.6 | src/Mod/Material/App/PropertyMaterial.h |
| 12.5 | src/Mod/Part/App/TopoShape.h |
| 12.3 | src/Mod/Material/App/Materials.h |
| 12.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 11.8 | src/App/MappedName.h |
| 10.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 9.4 | src/App/Application.h |
| 9.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 7.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 7.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 7.1 | src/Mod/Part/App/FaceMaker.h |
| 6.8 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 6.5 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 6.3 | src/App/ElementMap.h |
| 6.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 6.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 5.7 | src/Mod/Material/App/MaterialValue.h |
| 5.2 | src/Mod/Part/App/AttachExtension.h |
| 5.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 5.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 5.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 4.9 | src/App/Document.h |
| 4.8 | src/Mod/Part/App/Attacher.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.6 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.6 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.6 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.5 | boost::basic_regex<char>::assign |
| 0.5 | std::vector<Base::Vector2d>::operator= |
| 0.5 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.5 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.4 | std::unique_ptr<Data::MappedNameRef> |
| 0.4 | std::unique_ptr<QTextStreamPrivate> |
| 0.4 | std::unique_ptr<App::StringHasher::HashMap> |
| 0.4 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.4 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.4 | std::unique_ptr<std::thread::_State> |
| 0.4 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.4 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.4 | std::__uniq_ptr_data<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.4 | std::unique_ptr<Base::Exception> |
| 0.4 | std::__uniq_ptr_impl<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.4 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.4 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.4 | std::__uniq_ptr_data<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 0.3 | std::__uniq_ptr_impl<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 0.3 | std::__uniq_ptr_data<std::thread::_State, std::default_delete<std::thread::_State>> |
| 0.3 | std::__uniq_ptr_impl<std::thread::_State, std::default_delete<std::thread::_State>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 3.0 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 3.0 | src/Mod/Part/App/PreCompiled.h |
| 1.1 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_generators.hpp |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/nil_generator.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/algorithm/string/predicate.hpp |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/BRepMesh_IncrementalMesh.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_Context.hxx |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_clock.hpp |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_ModelBuilder.hxx |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Model.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Types.hxx |
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
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
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
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |
| 0.0 | std::__format::_Buf_sink<wchar_t> |
| 0.0 | std::__format::_Sink<wchar_t> |
| 0.0 | std::chrono::hh_mm_ss<std::chrono::duration<long>>::hh_mm_ss |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 19.6 | src/Mod/Part/App/PartFeature.h |
| 18.9 | src/App/ComplexGeoData.h |
| 12.6 | src/Mod/Material/App/PropertyMaterial.h |
| 12.5 | src/Mod/Part/App/TopoShape.h |
| 12.3 | src/Mod/Material/App/Materials.h |
| 12.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 11.8 | src/App/MappedName.h |
| 10.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 9.4 | src/App/Application.h |
| 9.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 7.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 7.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 7.1 | src/Mod/Part/App/FaceMaker.h |
| 6.8 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 6.5 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 6.3 | src/App/ElementMap.h |
| 6.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 6.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 5.7 | src/Mod/Material/App/MaterialValue.h |
| 5.2 | src/Mod/Part/App/AttachExtension.h |
| 5.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 5.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 5.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 4.9 | src/App/Document.h |
| 4.8 | src/Mod/Part/App/Attacher.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.6 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.6 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.6 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.5 | boost::basic_regex<char>::assign |
| 0.5 | std::vector<Base::Vector2d>::operator= |
| 0.5 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.5 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.4 | std::unique_ptr<Data::MappedNameRef> |
| 0.4 | std::unique_ptr<QTextStreamPrivate> |
| 0.4 | std::unique_ptr<App::StringHasher::HashMap> |
| 0.4 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.4 | std::__introsort_loop<QList<App::StringIDRef>::iterator, long long, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.4 | std::unique_ptr<std::thread::_State> |
| 0.4 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.4 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.4 | std::__uniq_ptr_data<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.4 | std::unique_ptr<Base::Exception> |
| 0.4 | std::__uniq_ptr_impl<Data::MappedNameRef, std::default_delete<Data::MappedNameRef>> |
| 0.4 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.4 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.4 | std::__uniq_ptr_data<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 0.3 | std::__uniq_ptr_impl<App::StringHasher::HashMap, std::default_delete<App::StringHasher::HashMap>> |
| 0.3 | std::__uniq_ptr_data<std::thread::_State, std::default_delete<std::thread::_State>> |
| 0.3 | std::__uniq_ptr_impl<std::thread::_State, std::default_delete<std::thread::_State>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 11.8 s; compiler 11.7 s; frontend 8.1 s; backend 3.5 s.

Top included files:

* 3.86 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.86 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.80 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.76 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.73 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.22 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.22 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.22 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.20 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.18 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.18 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.18 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.17 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.15 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>

## src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_21_cxx.cxx.o

Ninja 11.6 s; compiler 11.5 s; frontend 5.6 s; backend 5.9 s.

Top included files:

* 3.03 s — src/Mod/Part/App/Geometry.cpp
* 1.10 s — src/Mod/Part/App/Services.cpp
* 0.63 s — src/App/Application.h
* 0.43 s — src/Mod/Part/App/TopoShape.h
* 0.40 s — src/App/ComplexGeoData.h
* 0.38 s — src/App/Link.h
* 0.37 s — src/Mod/Part/App/Geometry2d.cpp
* 0.36 s — src/App/MappedName.h
* 0.33 s — src/Mod/Part/App/PartFeature.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h

Top template instantiations:

* 0.03 s — Base::ConsoleSingleton::warning<const char *&>
* 0.03 s — std::vector<int>::rbegin
* 0.02 s — std::make_unique<Part::Geom2dTrimmedCurve, opencascade::handle<Geom2d_TrimmedCurve>>
* 0.02 s — std::unique_ptr<Part::GeomCurve>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::__uniq_ptr_data<Part::GeomCurve, std::default_delete<Part::GeomCurve>>
* 0.02 s — std::__uniq_ptr_impl<Part::GeomCurve, std::default_delete<Part::GeomCurve>>
* 0.02 s — std::unique_ptr<Part::Geom2dTrimmedCurve>
* 0.02 s — std::make_unique<Part::GeomPoint, Base::Vector3<double>>
* 0.02 s — boost::stacktrace::basic_stacktrace<>::basic_stacktrace

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o

Ninja 9.2 s; compiler 9.1 s; frontend 3.5 s; backend 5.6 s.

Top included files:

* 0.97 s — src/Mod/Part/App/BRepMesh.h
* 0.97 s — src/App/ComplexGeoData.h
* 0.75 s — src/App/MappedName.h
* 0.35 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.35 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.30 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h
* 0.27 s — src/Mod/Part/App/FaceMakerBullseye.h
* 0.26 s — src/Mod/Part/App/FaceMaker.h
* 0.25 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication

Top template instantiations:

* 0.52 s — boost::basic_regex<char>::assign
* 0.26 s — boost::basic_regex<char>::basic_regex
* 0.26 s — boost::basic_regex<char>::do_assign
* 0.26 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.12 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.12 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.12 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data
* 0.12 s — boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper
* 0.12 s — boost::regex_traits<char>::regex_traits

## src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_22_cxx.cxx.o

Ninja 8.9 s; compiler 8.8 s; frontend 4.3 s; backend 4.5 s.

Top included files:

* 2.57 s — src/Mod/Part/App/MeasureClient.cpp
* 2.30 s — src/Mod/Part/App/DatumFeature.h
* 2.30 s — src/Mod/Part/App/AttachExtension.h
* 1.70 s — src/Mod/Part/App/Attacher.h
* 1.49 s — src/Mod/Part/App/PartFeature.h
* 1.08 s — src/Mod/Material/App/PropertyMaterial.h
* 1.03 s — src/Mod/Material/App/Materials.h
* 0.54 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet
* 0.54 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h
* 0.53 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h

Top template instantiations:

* 0.07 s — QList<App::StringIDRef>::append
* 0.04 s — QList<App::StringIDRef>::operator+=
* 0.03 s — QtPrivate::QCommonArrayOps<App::StringIDRef>::growAppend
* 0.03 s — Base::ConsoleSingleton::log<const char *, const char *>
* 0.03 s — QArrayDataPointer<App::StringIDRef>::detachAndGrow
* 0.03 s — QArrayDataPointer<App::StringIDRef>::tryReadjustFreeSpace
* 0.03 s — QArrayDataPointer<App::StringIDRef>::relocate
* 0.03 s — QtPrivate::q_relocate_overlap_n<App::StringIDRef, long long>
* 0.02 s — std::make_reverse_iterator<App::StringIDRef *>
* 0.02 s — std::reverse_iterator<App::StringIDRef *>

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o

Ninja 8.8 s; compiler 8.7 s; frontend 3.2 s; backend 5.5 s.

Top included files:

* 1.18 s — src/Mod/Part/App/CrossSection.h
* 1.18 s — src/Mod/Part/App/TopoShape.h
* 1.15 s — src/App/ComplexGeoData.h
* 0.87 s — src/App/MappedName.h
* 0.34 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash
* 0.34 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h
* 0.25 s — src/App/ElementMap.h
* 0.24 s — src/Mod/Part/App/FaceMaker.h

Top template instantiations:

* 0.04 s — QList<App::StringIDRef>::append
* 0.03 s — std::unique_ptr<OSD_Parallel::IteratorInterface>
* 0.02 s — std::make_unique<Part::ProgressIndicator>
* 0.02 s — std::unique_ptr<Part::ProgressIndicator>
* 0.02 s — std::__uniq_ptr_data<OSD_Parallel::IteratorInterface, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.02 s — std::__uniq_ptr_impl<OSD_Parallel::IteratorInterface, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.02 s — std::__uniq_ptr_data<Part::ProgressIndicator, std::default_delete<Part::ProgressIndicator>>
* 0.02 s — std::__uniq_ptr_impl<Part::ProgressIndicator, std::default_delete<Part::ProgressIndicator>>
* 0.02 s — std::map<Data::IndexedName, std::map<Part::NameKey, Part::NameInfo>>::operator[]
* 0.02 s — QList<App::StringIDRef>::operator+=
