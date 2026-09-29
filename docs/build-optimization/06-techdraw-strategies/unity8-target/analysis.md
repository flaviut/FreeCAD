# Clang build profile

* Recorded Ninja log timestamp span: 30.2 s (137–30317 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 16; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 99.3 | 7.5 | 106.7 |
| Frontend | 40.6 | 5.9 | 46.5 |
| Backend | 58.0 | 0.0 | 58.0 |
| Source | 13.5 | 0.0 | 13.5 |
| InstantiateFunction | 15.1 | 0.9 | 15.9 |
| InstantiateClass | 13.6 | 1.0 | 14.6 |
| Optimizer | 36.0 | 0.0 | 36.0 |
| CodeGenPasses | 21.9 | 0.0 | 21.9 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 13.5 | 13.4 | 4.8 | 8.5 | 0.5 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_0_cxx.cxx.o |
| 12.6 | 12.6 | 4.4 | 8.0 | 2.7 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_3_cxx.cxx.o |
| 9.8 | 9.7 | 3.7 | 5.9 | 0.9 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_2_cxx.cxx.o |
| 8.6 | 8.5 | 3.0 | 5.5 | 0.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_5_cxx.cxx.o |
| 8.6 | 8.5 | 3.1 | 5.3 | 1.6 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_4_cxx.cxx.o |
| 8.3 | 8.2 | 3.4 | 4.7 | 0.7 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_7_cxx.cxx.o |
| 7.1 | 7.0 | 2.6 | 4.3 | 1.6 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_8_cxx.cxx.o |
| 6.8 | 6.8 | 2.7 | 4.0 | 2.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_6_cxx.cxx.o |
| 5.8 | 5.7 | 2.3 | 3.3 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_9_cxx.cxx.o |
| 5.1 | 5.0 | 2.4 | 2.6 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_1_cxx.cxx.o |
| 3.6 | 3.6 | 2.0 | 1.5 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_10_cxx.cxx.o |
| 2.3 | 2.3 | 1.2 | 1.0 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyGeomFormatList.cpp.o |
| 2.3 | 2.3 | 1.2 | 1.0 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyCosmeticVertexList.cpp.o |
| 2.3 | 2.2 | 1.2 | 1.0 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyCosmeticEdgeList.cpp.o |
| 2.3 | 2.2 | 1.2 | 1.0 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyCenterLineList.cpp.o |
| 1.4 | 1.3 | 1.2 | 0.1 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_11_cxx.cxx.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 7.6 | 7.5 | 5.9 | 0.0 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 99.3 | 16 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 6.3 | src/App/DocumentObject.h |
| 5.2 | src/Mod/Part/App/PartFeature.h |
| 5.1 | src/App/FeaturePython.h |
| 4.9 | src/Mod/TechDraw/App/DrawUtil.h |
| 4.0 | src/App/GeoFeature.h |
| 3.5 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 2.9 | src/Mod/Part/App/TopoShape.h |
| 2.5 | src/App/ComplexGeoData.h |
| 2.5 | src/App/PropertyExpressionEngine.h |
| 2.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 2.4 | src/Mod/TechDraw/App/DrawViewPart.cpp |
| 2.2 | src/Mod/TechDraw/App/Geometry.h |
| 2.2 | src/Base/Writer.h |
| 2.1 | src/App/PropertyLinks.h |
| 1.8 | src/Mod/TechDraw/App/CenterLine.h |
| 1.8 | src/Mod/TechDraw/App/AppTechDraw.cpp |
| 1.7 | src/Mod/TechDraw/App/DimensionFormatter.cpp |
| 1.6 | src/Base/UnitsApi.h |
| 1.6 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 1.6 | src/Mod/TechDraw/App/DrawProjectSplit.h |
| 1.6 | src/Mod/TechDraw/App/CosmeticExtension.cpp |
| 1.5 | src/Mod/TechDraw/App/DrawProjectSplit.cpp |
| 1.5 | src/Mod/TechDraw/App/DrawSVGTemplate.cpp |
| 1.5 | src/Mod/TechDraw/App/DrawViewMulti.cpp |
| 1.5 | src/Mod/Material/App/PropertyMaterial.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 1.0 | boost::basic_regex<char>::assign |
| 0.5 | std::vector<int>::rbegin |
| 0.5 | boost::basic_regex<char>::basic_regex |
| 0.5 | boost::basic_regex<char>::do_assign |
| 0.5 | boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>> |
| 0.5 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.3 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.3 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.3 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.3 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.3 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.3 | std::unique_ptr<std::basic_istream<char>> |
| 0.3 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign |
| 0.3 | std::vector<Base::Vector2d>::operator= |
| 0.3 | boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>> |
| 0.3 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find |
| 0.3 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp |
| 0.2 | boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse |
| 0.2 | boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.2 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.2 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation |
| 0.2 | boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 5.4 | build/clang-profile/src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx |
| 5.4 | src/Mod/TechDraw/App/PreCompiled.h |
| 1.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication |
| 1.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h |
| 1.0 | src/Mod/Part/App/OpenCascadeAll.h |
| 1.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/boyer_myrvold_planar_test.hpp |
| 1.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/planar_detail/boyer_myrvold_impl.hpp |
| 0.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.7 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.5 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/sstream |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/is_kuratowski_subgraph.hpp |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/named_function_params.hpp |
| 0.2 | src/boost_regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/isomorphism.hpp |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.1 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::view |
| 0.0 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | NCollection_IndexedDataMap<opencascade::handle<Transfer_Finder>, opencascade::handle<Transfer_Binder>, Transfer_FindHasher> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 6.3 | src/App/DocumentObject.h |
| 5.4 | build/clang-profile/src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx |
| 5.4 | src/Mod/TechDraw/App/PreCompiled.h |
| 5.2 | src/Mod/Part/App/PartFeature.h |
| 5.1 | src/App/FeaturePython.h |
| 4.9 | src/Mod/TechDraw/App/DrawUtil.h |
| 4.0 | src/App/GeoFeature.h |
| 3.5 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 2.9 | src/Mod/Part/App/TopoShape.h |
| 2.5 | src/App/ComplexGeoData.h |
| 2.5 | src/App/PropertyExpressionEngine.h |
| 2.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 2.4 | src/Mod/TechDraw/App/DrawViewPart.cpp |
| 2.2 | src/Mod/TechDraw/App/Geometry.h |
| 2.2 | src/Base/Writer.h |
| 2.1 | src/App/PropertyLinks.h |
| 1.8 | src/Mod/TechDraw/App/CenterLine.h |
| 1.8 | src/Mod/TechDraw/App/AppTechDraw.cpp |
| 1.7 | src/Mod/TechDraw/App/DimensionFormatter.cpp |
| 1.6 | src/Base/UnitsApi.h |
| 1.6 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 1.6 | src/Mod/TechDraw/App/DrawProjectSplit.h |
| 1.6 | src/Mod/TechDraw/App/CosmeticExtension.cpp |
| 1.5 | src/Mod/TechDraw/App/DrawProjectSplit.cpp |
| 1.5 | src/Mod/TechDraw/App/DrawSVGTemplate.cpp |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 1.0 | boost::basic_regex<char>::assign |
| 0.5 | std::vector<int>::rbegin |
| 0.5 | boost::basic_regex<char>::basic_regex |
| 0.5 | boost::basic_regex<char>::do_assign |
| 0.5 | boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>> |
| 0.5 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.3 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.3 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.3 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.3 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.3 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.3 | std::unique_ptr<std::basic_istream<char>> |
| 0.3 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign |
| 0.3 | std::vector<Base::Vector2d>::operator= |
| 0.3 | boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>> |
| 0.3 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find |
| 0.3 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp |
| 0.2 | boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse |
| 0.2 | boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.2 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.2 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation |
| 0.2 | boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_0_cxx.cxx.o

Ninja 13.5 s; compiler 13.4 s; frontend 4.8 s; backend 8.5 s.

Top included files:

* 1.77 s — src/Mod/TechDraw/App/AppTechDraw.cpp
* 0.66 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.66 s — src/Mod/TechDraw/App/CenterLine.h
* 0.46 s — src/App/FeaturePython.h
* 0.46 s — src/Mod/TechDraw/App/AppTechDrawPy.cpp
* 0.45 s — src/App/GeoFeature.h
* 0.45 s — src/App/DocumentObject.h
* 0.26 s — src/Mod/Import/App/dxf/ImpExpDxf.h
* 0.26 s — src/Mod/Part/App/PropertyTopoShapeList.h
* 0.26 s — src/Mod/Part/App/TopoShape.h

Top template instantiations:

* 0.52 s — boost::basic_regex<char>::assign
* 0.26 s — boost::basic_regex<char>::basic_regex
* 0.26 s — boost::basic_regex<char>::do_assign
* 0.25 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.24 s — boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>>
* 0.24 s — boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>>
* 0.19 s — boost::regex_iterator<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>::operator++
* 0.15 s — boost::regex_iterator_implementation<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, char, boost::regex_traits<char>>::next
* 0.15 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.14 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_3_cxx.cxx.o

Ninja 12.6 s; compiler 12.6 s; frontend 4.4 s; backend 8.0 s.

Top included files:

* 2.35 s — src/Mod/TechDraw/App/DrawViewPart.cpp
* 0.70 s — src/App/Document.h
* 0.41 s — src/Mod/TechDraw/App/DrawProjectSplit.h
* 0.41 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.40 s — src/Mod/Part/App/PartFeature.h
* 0.27 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.24 s — src/Mod/Part/App/TopoShape.h
* 0.22 s — src/Mod/TechDraw/App/DrawViewSpreadsheet.cpp
* 0.22 s — src/Mod/TechDraw/App/Cosmetic.h
* 0.20 s — src/Mod/TechDraw/App/Geometry.h

Top template instantiations:

* 0.49 s — boost::basic_regex<char>::assign
* 0.31 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.25 s — boost::basic_regex<char>::basic_regex
* 0.25 s — boost::basic_regex<char>::do_assign
* 0.24 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.16 s — boost::regex_search<std::char_traits<char>, std::allocator<char>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.13 s — boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>>
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_2_cxx.cxx.o

Ninja 9.8 s; compiler 9.7 s; frontend 3.7 s; backend 5.9 s.

Top included files:

* 1.15 s — src/Mod/TechDraw/App/XMLQuery.cpp
* 1.15 s — src/Mod/TechDraw/App/DrawUtil.h
* 1.10 s — src/Mod/Part/App/PartFeature.h
* 0.59 s — src/App/FeaturePython.h
* 0.47 s — src/App/GeoFeature.h
* 0.46 s — src/App/DocumentObject.h
* 0.46 s — src/Mod/TechDraw/App/DrawPage.cpp
* 0.37 s — src/Mod/TechDraw/App/LineGenerator.cpp
* 0.35 s — src/Mod/TechDraw/App/DrawComplexSection.cpp
* 0.30 s — src/Mod/Part/App/PropertyTopoShape.h

Top template instantiations:

* 0.04 s — Base::ConsoleSingleton::message<std::basic_string<char> &>
* 0.03 s — std::vector<int>::rbegin
* 0.03 s — std::unique_ptr<std::basic_ostream<char>>
* 0.02 s — std::__uniq_ptr_data<std::basic_ostream<char>, std::default_delete<std::basic_ostream<char>>>
* 0.02 s — std::__uniq_ptr_impl<std::basic_ostream<char>, std::default_delete<std::basic_ostream<char>>>
* 0.02 s — QList<double>::QList<__gnu_cxx::__normal_iterator<double *, std::vector<double>>, true>
* 0.02 s — std::unique_ptr<App::DynamicProperty::Impl>
* 0.02 s — Base::ConsoleSingleton::send<Base::LogStyle::Message, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char> &>
* 0.02 s — std::format<std::basic_string<char> &>
* 0.02 s — std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>>

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_5_cxx.cxx.o

Ninja 8.6 s; compiler 8.5 s; frontend 3.0 s; backend 5.5 s.

Top included files:

* 1.66 s — src/Mod/TechDraw/App/DimensionFormatter.cpp
* 1.26 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.42 s — src/App/DocumentObject.h
* 0.39 s — src/Mod/Part/App/PropertyTopoShapeList.h
* 0.39 s — src/Mod/Part/App/TopoShape.h
* 0.35 s — src/App/ComplexGeoData.h
* 0.31 s — src/Mod/TechDraw/App/DrawViewSection.cpp
* 0.27 s — src/Base/UnitsApi.h
* 0.23 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.22 s — src/App/MappedName.h

Top template instantiations:

* 0.03 s — std::vector<int>::rbegin
* 0.03 s — std::unique_ptr<Base::UnitsSchema>
* 0.02 s — boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>>
* 0.02 s — std::sort<QList<App::StringIDRef>::iterator>
* 0.02 s — std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter>
* 0.02 s — Base::ConsoleSingleton::message<const char *, std::basic_string<char> &>
* 0.02 s — std::__uniq_ptr_data<Base::UnitsSchema, std::default_delete<Base::UnitsSchema>>
* 0.02 s — std::__uniq_ptr_impl<Base::UnitsSchema, std::default_delete<Base::UnitsSchema>>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_4_cxx.cxx.o

Ninja 8.6 s; compiler 8.5 s; frontend 3.1 s; backend 5.3 s.

Top included files:

* 1.48 s — src/Mod/TechDraw/App/DrawSVGTemplate.cpp
* 0.54 s — src/App/Document.h
* 0.43 s — src/Mod/TechDraw/App/DrawViewDimension.cpp
* 0.36 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.33 s — src/Mod/Part/App/PartFeature.h
* 0.27 s — src/App/Application.h
* 0.22 s — src/Mod/TechDraw/App/DrawPage.h
* 0.22 s — src/Mod/TechDraw/App/DrawViewPart.h
* 0.20 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.19 s — src/Base/UnitsApi.h

Top template instantiations:

* 0.03 s — Base::ConsoleSingleton::error<const char *>
* 0.03 s — std::vector<int>::rbegin
* 0.03 s — std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void>
* 0.03 s — App::PropertyListsT<App::DocumentObject *, std::vector<App::DocumentObject *>, App::PropertyLinkListBase>::setValue
* 0.03 s — std::sort<__gnu_cxx::__normal_iterator<QString *, std::vector<QString>>, QCollator>
* 0.03 s — std::__sort<__gnu_cxx::__normal_iterator<QString *, std::vector<QString>>, __gnu_cxx::__ops::_Iter_comp_iter<QCollator>>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::unique_ptr<Base::Exception>
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>>
