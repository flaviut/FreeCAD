# Clang build profile

* Recorded Ninja log timestamp span: 38.8 s (134–38937 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 97; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 217.5 | 7.9 | 225.4 |
| Frontend | 102.9 | 6.3 | 109.1 |
| Backend | 110.9 | 0.0 | 110.9 |
| Source | 59.8 | 5.8 | 65.6 |
| InstantiateFunction | 39.6 | 1.0 | 40.6 |
| InstantiateClass | 36.0 | 1.2 | 37.2 |
| Optimizer | 70.9 | 0.0 | 70.9 |
| CodeGenPasses | 39.8 | 0.0 | 39.8 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 9.9 | 9.8 | 3.1 | 6.6 | 1.5 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/AppTechDrawPy.cpp.o |
| 9.2 | 9.1 | 2.7 | 6.4 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawUtil.cpp.o |
| 7.6 | 7.6 | 2.7 | 4.9 | 1.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewPart.cpp.o |
| 6.3 | 6.3 | 2.0 | 4.2 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewDimension.cpp.o |
| 5.7 | 5.6 | 2.2 | 3.4 | 0.9 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewSpreadsheet.cpp.o |
| 5.6 | 5.6 | 1.9 | 3.7 | 1.2 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawDimHelper.cpp.o |
| 5.4 | 5.3 | 2.0 | 3.3 | 1.3 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawPage.cpp.o |
| 5.3 | 5.3 | 1.8 | 3.5 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DimensionAutoCorrect.cpp.o |
| 5.3 | 5.2 | 1.9 | 3.3 | 1.3 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/LandmarkDimension.cpp.o |
| 5.2 | 5.1 | 1.7 | 3.4 | 1.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DimensionFormatter.cpp.o |
| 5.2 | 5.1 | 1.8 | 3.2 | 1.2 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewDetail.cpp.o |
| 5.0 | 4.9 | 1.8 | 3.1 | 1.2 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/AppTechDraw.cpp.o |
| 4.9 | 4.9 | 1.7 | 3.1 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewDimExtent.cpp.o |
| 4.8 | 4.7 | 1.6 | 3.0 | 1.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/GeometryMatcher.cpp.o |
| 4.7 | 4.6 | 1.6 | 3.0 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewDimensionPyImp.cpp.o |
| 4.6 | 4.5 | 1.6 | 2.9 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewDimExtentPyImp.cpp.o |
| 4.2 | 4.1 | 1.9 | 2.2 | 1.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawComplexSection.cpp.o |
| 4.2 | 4.1 | 1.9 | 2.2 | 0.9 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Geometry.cpp.o |
| 3.8 | 3.7 | 1.9 | 1.8 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewSection.cpp.o |
| 3.8 | 3.7 | 1.6 | 2.0 | 0.7 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/EdgeWalker.cpp.o |
| 3.6 | 3.6 | 1.9 | 1.6 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawBrokenView.cpp.o |
| 3.5 | 3.4 | 1.6 | 1.7 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawProjectSplit.cpp.o |
| 3.3 | 3.2 | 1.7 | 1.5 | 1.1 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawGeomHatch.cpp.o |
| 3.3 | 3.2 | 1.6 | 1.5 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/CenterLine.cpp.o |
| 3.2 | 3.1 | 1.7 | 1.4 | 1.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawProjGroup.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 8.0 | 7.9 | 6.3 | 0.0 | 5.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 217.5 | 97 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 19.6 | src/Mod/Part/App/PartFeature.h |
| 17.7 | src/Mod/TechDraw/App/DrawUtil.h |
| 13.5 | src/Mod/Part/App/TopoShape.h |
| 13.2 | src/Mod/TechDraw/App/Geometry.h |
| 11.7 | src/App/ComplexGeoData.h |
| 11.2 | src/Mod/Part/App/PropertyTopoShape.h |
| 9.9 | src/Base/Writer.h |
| 8.2 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 8.1 | src/Mod/TechDraw/App/DrawViewPart.h |
| 7.7 | src/Mod/Material/App/PropertyMaterial.h |
| 7.6 | src/Mod/TechDraw/App/CosmeticExtension.h |
| 7.3 | src/App/Application.h |
| 6.5 | src/Mod/Material/App/Materials.h |
| 5.4 | src/App/MappedName.h |
| 5.3 | src/App/ElementMap.h |
| 4.9 | src/Base/UniqueNameManager.h |
| 4.8 | src/Base/Reader.h |
| 4.2 | src/Base/UnlimitedUnsigned.h |
| 3.5 | src/3rdParty/zipios++/zipoutputstream.h |
| 3.2 | src/Base/UnitsApi.h |
| 3.0 | src/Base/Console.h |
| 2.9 | src/App/Document.h |
| 2.8 | src/3rdParty/zipios++/zipoutputstreambuf.h |
| 2.8 | src/Mod/TechDraw/App/Cosmetic.h |
| 2.7 | src/Mod/TechDraw/App/DrawBrokenView.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 2.3 | std::vector<int>::rbegin |
| 1.8 | std::unique_ptr<std::basic_istream<char>> |
| 1.6 | boost::basic_regex<char>::assign |
| 1.4 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 1.4 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 1.4 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 1.3 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 1.2 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 1.2 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 1.2 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 1.2 | std::map<QString, Materials::ModelProperty>::operator[] |
| 1.1 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 1.1 | std::set<Base::ILogger *> |
| 1.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 1.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 1.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 1.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.9 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.9 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.9 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.9 | std::reverse_iterator<__gnu_cxx::__normal_iterator<const int *, std::vector<int>>> |
| 0.9 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_drop_node |
| 0.9 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_destroy_node |
| 0.9 | QList<QString>::append |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 5.8 | build/clang-profile/src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx |
| 5.8 | src/Mod/TechDraw/App/PreCompiled.h |
| 1.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/QApplication |
| 1.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtWidgets/qapplication.h |
| 1.0 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/boyer_myrvold_planar_test.hpp |
| 0.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/planar_detail/boyer_myrvold_impl.hpp |
| 0.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.7 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/sstream |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/is_kuratowski_subgraph.hpp |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.3 | src/App/DocumentObject.h |
| 0.2 | src/boost_regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/isomorphism.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/named_function_params.hpp |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.1 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 0.0 | NCollection_IndexedDataMap<opencascade::handle<Transfer_Finder>, opencascade::handle<Transfer_Binder>, Transfer_FindHasher> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4695:35), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4695:35)> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 19.6 | src/Mod/Part/App/PartFeature.h |
| 17.7 | src/Mod/TechDraw/App/DrawUtil.h |
| 13.5 | src/Mod/Part/App/TopoShape.h |
| 13.2 | src/Mod/TechDraw/App/Geometry.h |
| 11.7 | src/App/ComplexGeoData.h |
| 11.2 | src/Mod/Part/App/PropertyTopoShape.h |
| 9.9 | src/Base/Writer.h |
| 8.2 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 8.1 | src/Mod/TechDraw/App/DrawViewPart.h |
| 7.7 | src/Mod/Material/App/PropertyMaterial.h |
| 7.6 | src/Mod/TechDraw/App/CosmeticExtension.h |
| 7.3 | src/App/Application.h |
| 6.5 | src/Mod/Material/App/Materials.h |
| 5.8 | build/clang-profile/src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/cmake_pch.hxx |
| 5.8 | src/Mod/TechDraw/App/PreCompiled.h |
| 5.4 | src/App/MappedName.h |
| 5.3 | src/App/ElementMap.h |
| 4.9 | src/Base/UniqueNameManager.h |
| 4.8 | src/Base/Reader.h |
| 4.2 | src/Base/UnlimitedUnsigned.h |
| 3.5 | src/3rdParty/zipios++/zipoutputstream.h |
| 3.2 | src/Base/UnitsApi.h |
| 3.0 | src/Base/Console.h |
| 2.9 | src/App/Document.h |
| 2.8 | src/3rdParty/zipios++/zipoutputstreambuf.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 2.3 | std::vector<int>::rbegin |
| 1.8 | std::unique_ptr<std::basic_istream<char>> |
| 1.6 | boost::basic_regex<char>::assign |
| 1.4 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 1.4 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 1.4 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 1.3 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 1.2 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 1.2 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 1.2 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 1.2 | std::map<QString, Materials::ModelProperty>::operator[] |
| 1.1 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 1.1 | std::set<Base::ILogger *> |
| 1.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 1.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 1.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 1.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 1.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.9 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.9 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.9 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.9 | std::reverse_iterator<__gnu_cxx::__normal_iterator<const int *, std::vector<int>>> |
| 0.9 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_drop_node |
| 0.9 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_destroy_node |
| 0.9 | QList<QString>::append |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/AppTechDrawPy.cpp.o

Ninja 9.9 s; compiler 9.8 s; frontend 3.1 s; backend 6.6 s.

Top included files:

* 0.88 s — src/Mod/Import/App/dxf/ImpExpDxf.h
* 0.29 s — src/Mod/Part/App/TopoShape.h
* 0.25 s — src/App/ComplexGeoData.h
* 0.20 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.20 s — src/Mod/Part/App/PartFeature.h
* 0.19 s — src/App/Link.h
* 0.19 s — src/Base/UnitsApi.h
* 0.16 s — src/Mod/Material/App/PropertyMaterial.h
* 0.14 s — src/Mod/TechDraw/App/DrawDimHelper.h
* 0.14 s — src/Mod/TechDraw/App/DimensionReferences.h

Top template instantiations:

* 0.49 s — boost::basic_regex<char>::assign
* 0.31 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.25 s — boost::basic_regex<char>::basic_regex
* 0.25 s — boost::basic_regex<char>::do_assign
* 0.24 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.21 s — boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>>
* 0.21 s — boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>>
* 0.16 s — boost::regex_iterator<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>::regex_iterator
* 0.15 s — boost::regex_iterator_implementation<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, char, boost::regex_traits<char>>::init
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawUtil.cpp.o

Ninja 9.2 s; compiler 9.1 s; frontend 2.7 s; backend 6.4 s.

Top included files:

* 0.53 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.52 s — src/Mod/Part/App/PartFeature.h
* 0.32 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.28 s — src/Mod/Part/App/TopoShape.h
* 0.25 s — src/App/ComplexGeoData.h
* 0.22 s — src/Base/UnitsApi.h
* 0.18 s — src/Mod/Material/App/PropertyMaterial.h
* 0.18 s — src/Mod/TechDraw/App/GeometryObject.h
* 0.14 s — src/Base/UnitsSchemasData.h
* 0.14 s — src/Mod/TechDraw/App/Geometry.h

Top template instantiations:

* 0.57 s — boost::basic_regex<char>::assign
* 0.32 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.28 s — boost::basic_regex<char>::basic_regex
* 0.28 s — boost::basic_regex<char>::do_assign
* 0.28 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.15 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.14 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.13 s — boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>>
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewPart.cpp.o

Ninja 7.6 s; compiler 7.6 s; frontend 2.7 s; backend 4.9 s.

Top included files:

* 0.43 s — src/Mod/TechDraw/App/DrawProjectSplit.h
* 0.43 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.42 s — src/Mod/Part/App/PartFeature.h
* 0.29 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.25 s — src/Mod/Part/App/TopoShape.h
* 0.24 s — src/Mod/TechDraw/App/Cosmetic.h
* 0.24 s — src/Mod/TechDraw/App/Geometry.h
* 0.21 s — src/App/ComplexGeoData.h
* 0.21 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.20 s — src/Base/UnitsApi.h

Top template instantiations:

* 0.04 s — std::vector<int>::rbegin
* 0.03 s — std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>>
* 0.02 s — boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>>
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::unique_ptr<std::basic_istream<char>>
* 0.02 s — boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>
* 0.02 s — std::vector<std::shared_ptr<TechDraw::Vertex>>::insert<__gnu_cxx::__normal_iterator<std::shared_ptr<TechDraw::Vertex> *, std::vector<std::shared_ptr<TechDraw::Vertex>>>, void>
* 0.02 s — Base::ConsoleSingleton::message<std::basic_string<char> &, unsigned long>
* 0.02 s — std::vector<std::shared_ptr<TechDraw::Vertex>>::_M_range_insert<__gnu_cxx::__normal_iterator<std::shared_ptr<TechDraw::Vertex> *, std::vector<std::shared_ptr<TechDraw::Vertex>>>>
* 0.02 s — std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewDimension.cpp.o

Ninja 6.3 s; compiler 6.3 s; frontend 2.0 s; backend 4.2 s.

Top included files:

* 0.41 s — build/clang-profile/src/Mod/TechDraw/App/DrawViewDimensionPy.h
* 0.40 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.21 s — src/App/Application.h
* 0.19 s — src/Base/UnitsApi.h
* 0.19 s — src/Mod/Part/App/TopoShape.h
* 0.18 s — src/Mod/TechDraw/App/DimensionReferences.h
* 0.18 s — src/Mod/TechDraw/App/Geometry.h
* 0.18 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.17 s — src/Mod/Part/App/PartFeature.h
* 0.15 s — src/App/ComplexGeoData.h

Top template instantiations:

* 0.03 s — std::vector<int>::rbegin
* 0.02 s — std::unique_ptr<Base::Exception>
* 0.02 s — std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>>
* 0.02 s — std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>>
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void>
* 0.02 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>>
* 0.02 s — qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>>
* 0.02 s — qRegisterNormalizedMetaType<Materials::MaterialValue>
* 0.02 s — qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue>

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/DrawViewSpreadsheet.cpp.o

Ninja 5.7 s; compiler 5.6 s; frontend 2.2 s; backend 3.4 s.

Top included files:

* 0.55 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.51 s — src/Mod/Part/App/PartFeature.h
* 0.33 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.29 s — src/Mod/Part/App/TopoShape.h
* 0.26 s — src/App/ComplexGeoData.h
* 0.19 s — src/Mod/TechDraw/App/Preferences.h
* 0.19 s — src/Mod/TechDraw/App/DrawBrokenView.h
* 0.19 s — src/Mod/TechDraw/App/DrawViewPart.h
* 0.17 s — src/Mod/TechDraw/App/CosmeticExtension.h
* 0.17 s — src/Mod/Material/App/PropertyMaterial.h

Top template instantiations:

* 0.54 s — boost::basic_regex<char>::assign
* 0.31 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.27 s — boost::basic_regex<char>::basic_regex
* 0.27 s — boost::basic_regex<char>::do_assign
* 0.26 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.16 s — boost::regex_search<std::char_traits<char>, std::allocator<char>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.14 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.13 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.13 s — boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>>
* 0.13 s — boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find
