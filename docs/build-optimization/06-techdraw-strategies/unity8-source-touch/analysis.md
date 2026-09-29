# Clang build profile

* Recorded Ninja log timestamp span: 15.3 s (128–15394 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 13.2 | 0.0 | 13.2 |
| Frontend | 4.4 | 0.0 | 4.4 |
| Backend | 8.8 | 0.0 | 8.8 |
| Source | 0.4 | 0.0 | 0.4 |
| InstantiateFunction | 1.9 | 0.0 | 1.9 |
| InstantiateClass | 1.4 | 0.0 | 1.4 |
| Optimizer | 5.4 | 0.0 | 5.4 |
| CodeGenPasses | 3.3 | 0.0 | 3.3 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 13.3 | 13.2 | 4.4 | 8.8 | 0.4 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_0_cxx.cxx.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 13.2 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 1.6 | src/Mod/TechDraw/App/AppTechDraw.cpp |
| 0.6 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 0.6 | src/Mod/TechDraw/App/CenterLine.h |
| 0.4 | src/Mod/TechDraw/App/AppTechDrawPy.cpp |
| 0.4 | src/App/FeaturePython.h |
| 0.4 | src/App/GeoFeature.h |
| 0.4 | src/App/DocumentObject.h |
| 0.2 | src/Mod/Part/App/PropertyTopoShapeList.h |
| 0.2 | src/Mod/Part/App/TopoShape.h |
| 0.2 | src/Mod/Import/App/dxf/ImpExpDxf.h |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | src/Mod/TechDraw/App/EdgeWalker.cpp |
| 0.2 | src/Mod/TechDraw/App/DrawUtil.cpp |
| 0.2 | src/Base/UnitsApi.h |
| 0.2 | src/Mod/TechDraw/App/DrawUtil.h |
| 0.2 | src/Mod/TechDraw/App/Cosmetic.h |
| 0.2 | src/Mod/TechDraw/App/Geometry.h |
| 0.2 | src/App/PropertyExpressionEngine.h |
| 0.1 | src/Base/Interpreter.h |
| 0.1 | src/Mod/Part/App/PartFeature.h |
| 0.1 | src/App/Link.h |
| 0.1 | src/Mod/TechDraw/App/ShapeExtractor.cpp |
| 0.1 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 0.1 | src/Base/UnitsSchemasData.h |
| 0.1 | src/App/PropertyLinks.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.5 | boost::basic_regex<char>::assign |
| 0.2 | boost::basic_regex<char>::basic_regex |
| 0.2 | boost::basic_regex<char>::do_assign |
| 0.2 | boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>> |
| 0.2 | boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | boost::regex_iterator<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>::operator++ |
| 0.1 | boost::regex_iterator_implementation<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, char, boost::regex_traits<char>>::next |
| 0.1 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.1 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign |
| 0.1 | boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>> |
| 0.1 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find |
| 0.1 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp |
| 0.1 | boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse |
| 0.1 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation |
| 0.1 | boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data |
| 0.1 | boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper |
| 0.1 | boost::regex_traits<char>::regex_traits |
| 0.1 | boost::cpp_regex_traits<char>::cpp_regex_traits |
| 0.1 | boost::re_detail_600::create_cpp_regex_traits<char> |
| 0.1 | boost::object_cache<boost::re_detail_600::cpp_regex_traits_base<char>, boost::re_detail_600::cpp_regex_traits_implementation<char>>::get |
| 0.1 | boost::object_cache<boost::re_detail_600::cpp_regex_traits_base<char>, boost::re_detail_600::cpp_regex_traits_implementation<char>>::do_get |
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor> |
| 0.1 | boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse_extended |
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor, boost::adj_list_edge_property_map<boost::bidirectional_tag, int, const int &, unsigned long, const boost::property<boost::edge_index_t, int>, boost::edge_index_t>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 1.6 | src/Mod/TechDraw/App/AppTechDraw.cpp |
| 0.6 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 0.6 | src/Mod/TechDraw/App/CenterLine.h |
| 0.4 | src/Mod/TechDraw/App/AppTechDrawPy.cpp |
| 0.4 | src/App/FeaturePython.h |
| 0.4 | src/App/GeoFeature.h |
| 0.4 | src/App/DocumentObject.h |
| 0.2 | src/Mod/Part/App/PropertyTopoShapeList.h |
| 0.2 | src/Mod/Part/App/TopoShape.h |
| 0.2 | src/Mod/Import/App/dxf/ImpExpDxf.h |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | src/Mod/TechDraw/App/EdgeWalker.cpp |
| 0.2 | src/Mod/TechDraw/App/DrawUtil.cpp |
| 0.2 | src/Base/UnitsApi.h |
| 0.2 | src/Mod/TechDraw/App/DrawUtil.h |
| 0.2 | src/Mod/TechDraw/App/Cosmetic.h |
| 0.2 | src/Mod/TechDraw/App/Geometry.h |
| 0.2 | src/App/PropertyExpressionEngine.h |
| 0.1 | src/Base/Interpreter.h |
| 0.1 | src/Mod/Part/App/PartFeature.h |
| 0.1 | src/App/Link.h |
| 0.1 | src/Mod/TechDraw/App/ShapeExtractor.cpp |
| 0.1 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 0.1 | src/Base/UnitsSchemasData.h |
| 0.1 | src/App/PropertyLinks.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.5 | boost::basic_regex<char>::assign |
| 0.2 | boost::basic_regex<char>::basic_regex |
| 0.2 | boost::basic_regex<char>::do_assign |
| 0.2 | boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>> |
| 0.2 | boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>> |
| 0.2 | boost::regex_iterator<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>::operator++ |
| 0.1 | boost::regex_iterator_implementation<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, char, boost::regex_traits<char>>::next |
| 0.1 | boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>> |
| 0.1 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign |
| 0.1 | boost::re_detail_600::factory_find<boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>> |
| 0.1 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find |
| 0.1 | boost::re_detail_600::perl_matcher<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, boost::regex_traits<char>>::find_imp |
| 0.1 | boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse |
| 0.1 | boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation |
| 0.1 | boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data |
| 0.1 | boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper |
| 0.1 | boost::regex_traits<char>::regex_traits |
| 0.1 | boost::cpp_regex_traits<char>::cpp_regex_traits |
| 0.1 | boost::re_detail_600::create_cpp_regex_traits<char> |
| 0.1 | boost::object_cache<boost::re_detail_600::cpp_regex_traits_base<char>, boost::re_detail_600::cpp_regex_traits_implementation<char>>::get |
| 0.1 | boost::object_cache<boost::re_detail_600::cpp_regex_traits_base<char>, boost::re_detail_600::cpp_regex_traits_implementation<char>>::do_get |
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor> |
| 0.1 | boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse_extended |
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor, boost::adj_list_edge_property_map<boost::bidirectional_tag, int, const int &, unsigned long, const boost::property<boost::edge_index_t, int>, boost::edge_index_t>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_0_cxx.cxx.o

Ninja 13.3 s; compiler 13.2 s; frontend 4.4 s; backend 8.8 s.

Top included files:

* 1.61 s — src/Mod/TechDraw/App/AppTechDraw.cpp
* 0.62 s — src/Mod/TechDraw/App/DrawViewDimension.h
* 0.59 s — src/Mod/TechDraw/App/CenterLine.h
* 0.42 s — src/Mod/TechDraw/App/AppTechDrawPy.cpp
* 0.42 s — src/App/FeaturePython.h
* 0.41 s — src/App/GeoFeature.h
* 0.40 s — src/App/DocumentObject.h
* 0.25 s — src/Mod/Part/App/PropertyTopoShapeList.h
* 0.24 s — src/Mod/Part/App/TopoShape.h
* 0.24 s — src/Mod/Import/App/dxf/ImpExpDxf.h

Top template instantiations:

* 0.45 s — boost::basic_regex<char>::assign
* 0.23 s — boost::basic_regex<char>::basic_regex
* 0.23 s — boost::basic_regex<char>::do_assign
* 0.22 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.22 s — boost::regex_replace<boost::regex_traits<char>, char, std::basic_string<char>>
* 0.21 s — boost::regex_replace<boost::re_detail_600::string_out_iterator<std::basic_string<char>>, __gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, boost::regex_traits<char>, char, std::basic_string<char>>
* 0.17 s — boost::regex_iterator<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>::operator++
* 0.14 s — boost::regex_iterator_implementation<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, char, boost::regex_traits<char>>::next
* 0.14 s — boost::regex_search<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<const char *, std::basic_string<char>>>>, char, boost::regex_traits<char>>
* 0.12 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
