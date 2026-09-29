# Clang build profile

* Recorded Ninja log timestamp span: 9.9 s (132–9996 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 8.0 | 0.0 | 8.0 |
| Frontend | 3.2 | 0.0 | 3.2 |
| Backend | 4.7 | 0.0 | 4.7 |
| Source | 0.0 | 0.0 | 0.0 |
| InstantiateFunction | 1.2 | 0.0 | 1.2 |
| InstantiateClass | 1.1 | 0.0 | 1.1 |
| Optimizer | 3.0 | 0.0 | 3.0 |
| CodeGenPasses | 1.7 | 0.0 | 1.7 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 8.1 | 8.0 | 3.2 | 4.7 | 0.0 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_1_cxx.cxx.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 8.0 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 1.7 | src/Mod/TechDraw/App/ShapeExtractor.cpp |
| 0.7 | src/App/Document.h |
| 0.5 | src/Mod/Part/App/PartFeature.h |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/TechDraw/App/DrawDimHelper.cpp |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.2 | src/Mod/TechDraw/App/EdgeWalker.cpp |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | src/Mod/Material/App/PropertyMaterial.h |
| 0.2 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 0.2 | src/Base/UnitsApi.h |
| 0.2 | src/App/ExportInfo.h |
| 0.2 | src/App/DocumentObject.h |
| 0.1 | src/App/Link.h |
| 0.1 | src/Mod/TechDraw/App/Preferences.h |
| 0.1 | src/Mod/TechDraw/App/DrawBrokenView.h |
| 0.1 | src/Mod/TechDraw/App/DrawViewPart.h |
| 0.1 | src/Mod/Material/App/Materials.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | src/Mod/TechDraw/App/CosmeticExtension.h |
| 0.1 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 0.1 | src/App/ElementMap.h |
| 0.1 | src/Mod/TechDraw/App/Geometry.h |
| 0.1 | src/Base/UnitsSchemasData.h |
| 0.1 | src/Mod/Part/App/PrimitiveFeature.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor> |
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor, boost::adj_list_edge_property_map<boost::bidirectional_tag, int, const int &, unsigned long, const boost::property<boost::edge_index_t, int>, boost::edge_index_t>> |
| 0.0 | boost::add_edge<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config, boost::bidirectional_graph_helper_with_property<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config>> |
| 0.0 | Base::ConsoleSingleton::error<const char *> |
| 0.0 | std::vector<int>::rbegin |
| 0.0 | boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>> |
| 0.0 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | boost::add_edge<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config> |
| 0.0 | boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>> |
| 0.0 | std::uninitialized_copy<std::move_iterator<double *>, double *> |
| 0.0 | std::sort<__gnu_cxx::__normal_iterator<TopoDS_Wire *, std::vector<TopoDS_Wire>>, bool (*)(const TopoDS_Wire &, const TopoDS_Wire &)> |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.0 | std::__sort<__gnu_cxx::__normal_iterator<TopoDS_Wire *, std::vector<TopoDS_Wire>>, __gnu_cxx::__ops::_Iter_comp_iter<bool (*)(const TopoDS_Wire &, const TopoDS_Wire &)>> |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::vector<TopoDS_Shape>::insert<__gnu_cxx::__normal_iterator<TopoDS_Shape *, std::vector<TopoDS_Shape>>, void> |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 1.7 | src/Mod/TechDraw/App/ShapeExtractor.cpp |
| 0.7 | src/App/Document.h |
| 0.5 | src/Mod/Part/App/PartFeature.h |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/TechDraw/App/DrawDimHelper.cpp |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.2 | src/Mod/TechDraw/App/EdgeWalker.cpp |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | src/Mod/Material/App/PropertyMaterial.h |
| 0.2 | src/Mod/TechDraw/App/DrawViewDimension.h |
| 0.2 | src/Base/UnitsApi.h |
| 0.2 | src/App/ExportInfo.h |
| 0.2 | src/App/DocumentObject.h |
| 0.1 | src/App/Link.h |
| 0.1 | src/Mod/TechDraw/App/Preferences.h |
| 0.1 | src/Mod/TechDraw/App/DrawBrokenView.h |
| 0.1 | src/Mod/TechDraw/App/DrawViewPart.h |
| 0.1 | src/Mod/Material/App/Materials.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | src/Mod/TechDraw/App/CosmeticExtension.h |
| 0.1 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 0.1 | src/App/ElementMap.h |
| 0.1 | src/Mod/TechDraw/App/Geometry.h |
| 0.1 | src/Base/UnitsSchemasData.h |
| 0.1 | src/Mod/Part/App/PrimitiveFeature.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor> |
| 0.1 | boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor, boost::adj_list_edge_property_map<boost::bidirectional_tag, int, const int &, unsigned long, const boost::property<boost::edge_index_t, int>, boost::edge_index_t>> |
| 0.0 | boost::add_edge<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config, boost::bidirectional_graph_helper_with_property<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config>> |
| 0.0 | Base::ConsoleSingleton::error<const char *> |
| 0.0 | std::vector<int>::rbegin |
| 0.0 | boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>> |
| 0.0 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | boost::add_edge<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config> |
| 0.0 | boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>> |
| 0.0 | std::uninitialized_copy<std::move_iterator<double *>, double *> |
| 0.0 | std::sort<__gnu_cxx::__normal_iterator<TopoDS_Wire *, std::vector<TopoDS_Wire>>, bool (*)(const TopoDS_Wire &, const TopoDS_Wire &)> |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 0.0 | std::__sort<__gnu_cxx::__normal_iterator<TopoDS_Wire *, std::vector<TopoDS_Wire>>, __gnu_cxx::__ops::_Iter_comp_iter<bool (*)(const TopoDS_Wire &, const TopoDS_Wire &)>> |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::vector<TopoDS_Shape>::insert<__gnu_cxx::__normal_iterator<TopoDS_Shape *, std::vector<TopoDS_Shape>>, void> |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/Unity/unity_1_cxx.cxx.o

Ninja 8.1 s; compiler 8.0 s; frontend 3.2 s; backend 4.7 s.

Top included files:

* 1.74 s — src/Mod/TechDraw/App/ShapeExtractor.cpp
* 0.70 s — src/App/Document.h
* 0.50 s — src/Mod/Part/App/PartFeature.h
* 0.30 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.30 s — src/Mod/TechDraw/App/DrawDimHelper.cpp
* 0.26 s — src/Mod/Part/App/TopoShape.h
* 0.24 s — src/Mod/TechDraw/App/EdgeWalker.cpp
* 0.23 s — src/App/ComplexGeoData.h
* 0.19 s — src/Mod/Material/App/PropertyMaterial.h
* 0.19 s — src/Mod/TechDraw/App/DrawViewDimension.h

Top template instantiations:

* 0.07 s — boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor>
* 0.07 s — boost::planar_face_traversal<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, std::vector<boost::detail::edge_desc_impl<boost::bidirectional_tag, unsigned long>> *, TechDraw::edgeVisitor, boost::adj_list_edge_property_map<boost::bidirectional_tag, int, const int &, unsigned long, const boost::property<boost::edge_index_t, int>, boost::edge_index_t>>
* 0.05 s — boost::add_edge<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config, boost::bidirectional_graph_helper_with_property<boost::detail::adj_list_gen<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>, boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>, boost::no_property, boost::listS>::config>>
* 0.03 s — Base::ConsoleSingleton::error<const char *>
* 0.03 s — std::vector<int>::rbegin
* 0.02 s — boost::graph_traits<boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::property<boost::vertex_index_t, int>, boost::property<boost::edge_index_t, int>>>
* 0.02 s — std::unique_ptr<App::DynamicProperty::Impl>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>>
* 0.02 s — std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>>
