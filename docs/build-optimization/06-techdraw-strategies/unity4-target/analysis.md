# Clang build profile

* Recorded Ninja log timestamp span: 33.3 s (147–33447 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 28; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 143.1 | 7.4 | 150.4 |
| Frontend | 65.6 | 5.9 | 71.6 |
| Backend | 76.1 | 0.0 | 76.1 |
| Source | 19.3 | 0.0 | 19.3 |
| InstantiateFunction | 23.6 | 0.9 | 24.5 |
| InstantiateClass | 23.0 | 1.0 | 24.0 |
| Optimizer | 47.8 | 0.0 | 47.8 |
| CodeGenPasses | 28.2 | 0.0 | 28.2 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 12.5 | 12.4 | 4.7 | 7.7 | 3.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_6_cxx.cxx.o |
| 11.6 | 11.5 | 4.1 | 7.3 | 0.5 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_0_cxx.cxx.o |
| 8.9 | 8.8 | 3.4 | 5.3 | 0.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_10_cxx.cxx.o |
| 8.8 | 8.7 | 3.5 | 5.2 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_1_cxx.cxx.o |
| 8.7 | 8.6 | 3.5 | 5.0 | 1.9 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_8_cxx.cxx.o |
| 8.7 | 8.6 | 3.4 | 5.1 | 1.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_5_cxx.cxx.o |
| 7.7 | 7.6 | 3.2 | 4.3 | 0.7 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_14_cxx.cxx.o |
| 7.3 | 7.2 | 2.6 | 4.6 | 1.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_12_cxx.cxx.o |
| 7.3 | 7.2 | 3.0 | 4.2 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_9_cxx.cxx.o |
| 6.8 | 6.7 | 2.4 | 4.2 | 1.6 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_16_cxx.cxx.o |
| 5.9 | 5.8 | 2.3 | 3.5 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_18_cxx.cxx.o |
| 5.1 | 5.0 | 2.4 | 2.5 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_15_cxx.cxx.o |
| 4.8 | 4.7 | 2.9 | 1.8 | 1.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_7_cxx.cxx.o |
| 4.7 | 4.6 | 2.5 | 2.0 | 1.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_11_cxx.cxx.o |
| 4.6 | 4.5 | 2.5 | 2.0 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_4_cxx.cxx.o |
| 4.5 | 4.4 | 2.4 | 1.9 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_2_cxx.cxx.o |
| 3.8 | 3.7 | 2.1 | 1.5 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_17_cxx.cxx.o |
| 3.6 | 3.5 | 2.0 | 1.5 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_21_cxx.cxx.o |
| 3.3 | 3.2 | 1.6 | 1.6 | 0.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_3_cxx.cxx.o |
| 2.4 | 2.3 | 1.3 | 1.0 | 0.9 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyGeomFormatList.cpp.o |
| 2.4 | 2.3 | 1.2 | 1.0 | 0.9 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyCosmeticEdgeList.cpp.o |
| 2.3 | 2.3 | 1.2 | 1.0 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyCosmeticVertexList.cpp.o |
| 2.3 | 2.3 | 1.2 | 1.0 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/PropertyCenterLineList.cpp.o |
| 2.2 | 2.1 | 1.7 | 0.4 | 1.3 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_13_cxx.cxx.o |
| 1.5 | 1.4 | 1.2 | 0.2 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_19_cxx.cxx.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 7.5 | 7.4 | 5.9 | 0.0 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 143.1 | 28 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 11.2 | src/App/DocumentObject.h |
| 8.5 | src/Mod/Part/App/PartFeature.h |
| 8.0 | src/Mod/TechDraw/App/DrawUtil.h |
| 7.3 | src/App/FeaturePython.h |
| 5.4 | src/App/GeoFeature.h |
| 5.3 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 5.0 | src/Mod/Part/App/TopoShape.h |
| 4.4 | src/App/PropertyExpressionEngine.h |
| 4.4 | src/Mod/TechDraw/App/DrawViewPart.h |
| 4.3 | src/App/ComplexGeoData.h |
| 4.3 | src/Mod/TechDraw/App/Geometry.h |
| 4.0 | src/App/Document.h |
| 4.0 | src/App/PropertyLinks.h |
| 3.8 | src/Mod/Part/App/PropertyTopoShape.h |
| 3.7 | src/Base/Writer.h |
| 3.1 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 2.9 | src/Mod/TechDraw/App/DrawBrokenView.h |
| 2.8 | src/Mod/TechDraw/App/DrawViewPart.cpp |
| 2.7 | src/Mod/Material/App/PropertyMaterial.h |
| 2.7 | src/App/Application.h |
| 2.6 | src/Mod/TechDraw/App/CenterLine.h |
| 2.5 | src/Mod/TechDraw/App/Cosmetic.h |
| 2.4 | src/Mod/TechDraw/App/CosmeticExtension.h |
| 2.4 | src/Mod/Material/App/Materials.h |
| 2.3 | src/Mod/TechDraw/App/Preferences.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 1.1 | boost::basic_regex<char>::assign |
| 0.9 | std::vector<int>::rbegin |
| 0.7 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.5 | boost::basic_regex<char>::basic_regex |
| 0.5 | boost::basic_regex<char>::do_assign |
| 0.5 | boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>> |
| 0.5 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.5 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.5 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.5 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.5 | std::vector<Base::Vector2d>::operator= |
| 0.5 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.5 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.5 | std::unique_ptr<std::basic_istream<char>> |
| 0.4 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_M_emplace_hint_unique<const std::piecewise_construct_t &, std::tuple<App::DocumentObject *const &>, std::tuple<>> |
| 0.4 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.4 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.4 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.4 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.4 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.4 | std::reverse_iterator<__gnu_cxx::__normal_iterator<const int *, std::vector<int>>> |
| 0.4 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.4 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.4 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_drop_node |
| 0.4 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 5.5 | build/clang-profile/src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx |
| 5.5 | src/Mod/TechDraw/App/PreCompiled.h |
| 1.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication |
| 1.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h |
| 1.0 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/boyer_myrvold_planar_test.hpp |
| 0.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/planar_detail/boyer_myrvold_impl.hpp |
| 0.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.7 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/sstream |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/is_kuratowski_subgraph.hpp |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | src/boost_regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/isomorphism.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/named_function_params.hpp |
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
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | NCollection_IndexedDataMap<opencascade::handle<Transfer_Finder>, opencascade::handle<Transfer_Binder>, Transfer_FindHasher> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::formatter<bool, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 11.2 | src/App/DocumentObject.h |
| 8.5 | src/Mod/Part/App/PartFeature.h |
| 8.0 | src/Mod/TechDraw/App/DrawUtil.h |
| 7.3 | src/App/FeaturePython.h |
| 5.5 | build/clang-profile/src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx |
| 5.5 | src/Mod/TechDraw/App/PreCompiled.h |
| 5.4 | src/App/GeoFeature.h |
| 5.3 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 5.0 | src/Mod/Part/App/TopoShape.h |
| 4.4 | src/App/PropertyExpressionEngine.h |
| 4.4 | src/Mod/TechDraw/App/DrawViewPart.h |
| 4.3 | src/App/ComplexGeoData.h |
| 4.3 | src/Mod/TechDraw/App/Geometry.h |
| 4.0 | src/App/Document.h |
| 4.0 | src/App/PropertyLinks.h |
| 3.8 | src/Mod/Part/App/PropertyTopoShape.h |
| 3.7 | src/Base/Writer.h |
| 3.1 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 2.9 | src/Mod/TechDraw/App/DrawBrokenView.h |
| 2.8 | src/Mod/TechDraw/App/DrawViewPart.cpp |
| 2.7 | src/Mod/Material/App/PropertyMaterial.h |
| 2.7 | src/App/Application.h |
| 2.6 | src/Mod/TechDraw/App/CenterLine.h |
| 2.5 | src/Mod/TechDraw/App/Cosmetic.h |
| 2.4 | src/Mod/TechDraw/App/CosmeticExtension.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 1.1 | boost::basic_regex<char>::assign |
| 0.9 | std::vector<int>::rbegin |
| 0.7 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.5 | boost::basic_regex<char>::basic_regex |
| 0.5 | boost::basic_regex<char>::do_assign |
| 0.5 | boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>> |
| 0.5 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.5 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.5 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.5 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.5 | std::vector<Base::Vector2d>::operator= |
| 0.5 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.5 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.5 | std::unique_ptr<std::basic_istream<char>> |
| 0.4 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_M_emplace_hint_unique<const std::piecewise_construct_t &, std::tuple<App::DocumentObject *const &>, std::tuple<>> |
| 0.4 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.4 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.4 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.4 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.4 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.4 | std::reverse_iterator<__gnu_cxx::__normal_iterator<const int *, std::vector<int>>> |
| 0.4 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.4 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.4 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_drop_node |
| 0.4 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_6_cxx.cxx.o

Ninja 12.5 s; compiler 12.4 s; frontend 4.7 s; backend 7.7 s.

Top included files:

* 2.78 s — src/Mod/TechDraw/App/DrawViewPart.cpp
* 0.83 s — src/App/Document.h
* 0.47 s — src/Mod/TechDraw/App/DrawProjectSplit.h
* 0.47 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.46 s — src/Mod/Part/App/PartFeature.h
* 0.31 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.27 s — src/Mod/Part/App/TopoShape.h
* 0.26 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.26 s — src/Mod/TechDraw/App/Cosmetic.h
* 0.25 s — src/Base/UnitsApi.h

Top template instantiations:

* 0.52 s — boost::basic_regex<char>::assign
* 0.31 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.26 s — boost::basic_regex<char>::basic_regex
* 0.26 s — boost::basic_regex<char>::do_assign
* 0.25 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.16 s — boost::regex_search<std::char_traits<char>, std::allocator<char>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.13 s — boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>>
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_0_cxx.cxx.o

Ninja 11.6 s; compiler 11.5 s; frontend 4.1 s; backend 7.3 s.

Top included files:

* 1.84 s — src/Mod/TechDraw/App/AppTechDraw.cpp
* 0.72 s — src/Mod/TechDraw/App/CenterLine.h
* 0.66 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.50 s — src/App/FeaturePython.h
* 0.49 s — src/App/GeoFeature.h
* 0.48 s — src/App/DocumentObject.h
* 0.47 s — src/Mod/TechDraw/App/AppTechDrawPy.cpp
* 0.27 s — src/Mod/Import/App/dxf/ImpExpDxf.h
* 0.26 s — src/Mod/Part/App/PropertyTopoShapeList.h
* 0.26 s — src/Mod/Part/App/TopoShape.h

Top template instantiations:

* 0.55 s — boost::basic_regex<char>::assign
* 0.28 s — boost::basic_regex<char>::basic_regex
* 0.28 s — boost::basic_regex<char>::do_assign
* 0.27 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.21 s — boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>>
* 0.21 s — boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>>
* 0.16 s — boost::regex_iterator<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>::operator++
* 0.15 s — boost::regex_iterator_implementation<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, char, boost::regex_traits<char>>::next
* 0.15 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.14 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_10_cxx.cxx.o

Ninja 8.9 s; compiler 8.8 s; frontend 3.4 s; backend 5.3 s.

Top included files:

* 1.96 s — src/Mod/TechDraw/App/DimensionFormatter.cpp
* 1.52 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.54 s — src/App/DocumentObject.h
* 0.46 s — src/Mod/Part/App/PropertyTopoShapeList.h
* 0.46 s — src/Mod/Part/App/TopoShape.h
* 0.43 s — src/Mod/TechDraw/App/DrawViewSection.cpp
* 0.42 s — src/App/ComplexGeoData.h
* 0.28 s — src/Base/UnitsApi.h
* 0.26 s — src/App/MappedName.h
* 0.25 s — src/Mod/TechDraw/App/DrawUtil.h

Top template instantiations:

* 0.03 s — std::vector<int>::rbegin
* 0.03 s — boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>>
* 0.03 s — std::unique_ptr<Base::UnitsSchema>
* 0.03 s — boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>
* 0.03 s — std::sort<QList<App::StringIDRef>::iterator>
* 0.03 s — std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter>
* 0.02 s — Base::ConsoleSingleton::message<const char *, std::basic_string<char> &>
* 0.02 s — std::vector<Base::Vector2d>::operator=
* 0.02 s — std::unordered_map<std::basic_string<char>, Part::TopoShape>
* 0.02 s — QtConcurrent::run<(lambda at /home/user/dev/FreeCAD/src/Mod/TechDraw/App/DrawViewSection.cpp:491:23)>

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_1_cxx.cxx.o

Ninja 8.8 s; compiler 8.7 s; frontend 3.5 s; backend 5.2 s.

Top included files:

* 1.88 s — src/Mod/TechDraw/App/ShapeExtractor.cpp
* 0.75 s — src/App/Document.h
* 0.50 s — src/Mod/Part/App/PartFeature.h
* 0.33 s — src/Mod/TechDraw/App/DrawDimHelper.cpp
* 0.30 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.26 s — src/Mod/Part/App/TopoShape.h
* 0.26 s — src/Mod/TechDraw/App/EdgeWalker.cpp
* 0.23 s — src/App/ComplexGeoData.h
* 0.21 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.20 s — src/Base/UnitsApi.h

Top template instantiations:

* 0.08 s — boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor>
* 0.08 s — boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor, boost::adj_list_edge_property_map<boost::bidirectional_tag, int, const int &, unsigned long, const boost::property<boost::edge_index_t, int>, boost::edge_index_t>>
* 0.06 s — boost::add_edge<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config, boost::bidirectional_graph_helper_with_property<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config>>
* 0.03 s — std::vector<int>::rbegin
* 0.03 s — Base::ConsoleSingleton::error<const char *>
* 0.02 s — boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::unique_ptr<App::DynamicProperty::Impl>
* 0.02 s — boost::add_edge<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config>
* 0.02 s — std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>>

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_8_cxx.cxx.o

Ninja 8.7 s; compiler 8.6 s; frontend 3.5 s; backend 5.0 s.

Top included files:

* 1.81 s — src/Mod/TechDraw/App/DrawSVGTemplate.cpp
* 0.67 s — src/App/Document.h
* 0.48 s — src/Mod/TechDraw/App/DrawViewDimension.cpp
* 0.42 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.39 s — src/Mod/Part/App/PartFeature.h
* 0.36 s — src/App/Application.h
* 0.26 s — src/Mod/TechDraw/App/DrawPage.h
* 0.25 s — src/Mod/TechDraw/App/DrawViewPart.h
* 0.23 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.22 s — src/Base/UnitsApi.h

Top template instantiations:

* 0.04 s — Base::ConsoleSingleton::error<const char *>
* 0.04 s — std::sort<__gnu_cxx::__normal_iterator<QString *, std::vector<QString>>, QCollator>
* 0.04 s — std::__sort<__gnu_cxx::__normal_iterator<QString *, std::vector<QString>>, __gnu_cxx::__ops::_Iter_comp_iter<QCollator>>
* 0.04 s — App::PropertyListsT<App::DocumentObject *, std::vector<App::DocumentObject *>, App::PropertyLinkListBase>::setValue
* 0.04 s — std::vector<int>::rbegin
* 0.02 s — std::unique_ptr<Base::Exception>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>>
* 0.02 s — qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>>
