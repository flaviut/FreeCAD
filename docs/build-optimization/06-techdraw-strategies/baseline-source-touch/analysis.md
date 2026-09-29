# Clang build profile

* Recorded Ninja log timestamp span: 5.0 s (131–5129 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 3.0 | 0.0 | 3.0 |
| Frontend | 1.8 | 0.0 | 1.8 |
| Backend | 1.2 | 0.0 | 1.2 |
| Source | 1.2 | 0.0 | 1.2 |
| InstantiateFunction | 0.7 | 0.0 | 0.7 |
| InstantiateClass | 0.7 | 0.0 | 0.7 |
| Optimizer | 0.8 | 0.0 | 0.8 |
| CodeGenPasses | 0.4 | 0.0 | 0.4 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 3.1 | 3.0 | 1.8 | 1.2 | 1.2 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/HatchLine.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 3.0 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 0.9 | src/Mod/TechDraw/App/DrawUtil.h |
| 0.8 | src/Mod/Part/App/PartFeature.h |
| 0.5 | src/App/FeaturePython.h |
| 0.4 | src/App/GeoFeature.h |
| 0.3 | src/App/DocumentObject.h |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.2 | src/Mod/TechDraw/App/HatchLine.h |
| 0.2 | src/Mod/Part/App/TopoShape.h |
| 0.2 | src/Mod/TechDraw/App/Geometry.h |
| 0.2 | src/App/ComplexGeoData.h |
| 0.1 | src/App/PropertyExpressionEngine.h |
| 0.1 | src/Base/Writer.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | src/Mod/Material/App/PropertyMaterial.h |
| 0.1 | src/Mod/Material/App/Materials.h |
| 0.1 | src/App/ElementMap.h |
| 0.1 | src/App/PropertyPythonObject.h |
| 0.1 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 0.1 | src/App/Application.h |
| 0.1 | src/App/MappedName.h |
| 0.1 | src/Base/UniqueNameManager.h |
| 0.1 | src/App/PropertyStandard.h |
| 0.1 | src/Base/UnlimitedUnsigned.h |
| 0.1 | src/3rdParty/PyCXX/CXX/WrapPython.h |
| 0.1 | /nix/store/h3l4z7p6wny3phbckwwhy1i2g52pdnj4-python3-3.13.15/include/python3.13/Python.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | Base::ConsoleSingleton::message<std::basic_string<char> &> |
| 0.0 | std::vector<int>::rbegin |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Message, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char> &> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.0 | std::format<std::basic_string<char> &> |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | std::unique_ptr<App::PropertyExpressionEngine::Private> |
| 0.0 | QList<QString>::append |
| 0.0 | QList<QString>::emplaceBack<const QString &> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 0.9 | src/Mod/TechDraw/App/DrawUtil.h |
| 0.8 | src/Mod/Part/App/PartFeature.h |
| 0.5 | src/App/FeaturePython.h |
| 0.4 | src/App/GeoFeature.h |
| 0.3 | src/App/DocumentObject.h |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.2 | src/Mod/TechDraw/App/HatchLine.h |
| 0.2 | src/Mod/Part/App/TopoShape.h |
| 0.2 | src/Mod/TechDraw/App/Geometry.h |
| 0.2 | src/App/ComplexGeoData.h |
| 0.1 | src/App/PropertyExpressionEngine.h |
| 0.1 | src/Base/Writer.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | src/Mod/Material/App/PropertyMaterial.h |
| 0.1 | src/Mod/Material/App/Materials.h |
| 0.1 | src/App/ElementMap.h |
| 0.1 | src/App/PropertyPythonObject.h |
| 0.1 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 0.1 | src/App/Application.h |
| 0.1 | src/App/MappedName.h |
| 0.1 | src/Base/UniqueNameManager.h |
| 0.1 | src/App/PropertyStandard.h |
| 0.1 | src/Base/UnlimitedUnsigned.h |
| 0.1 | src/3rdParty/PyCXX/CXX/WrapPython.h |
| 0.1 | /nix/store/h3l4z7p6wny3phbckwwhy1i2g52pdnj4-python3-3.13.15/include/python3.13/Python.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | Base::ConsoleSingleton::message<std::basic_string<char> &> |
| 0.0 | std::vector<int>::rbegin |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Message, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char> &> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.0 | std::format<std::basic_string<char> &> |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | std::unique_ptr<App::PropertyExpressionEngine::Private> |
| 0.0 | QList<QString>::append |
| 0.0 | QList<QString>::emplaceBack<const QString &> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/HatchLine.cpp.o

Ninja 3.1 s; compiler 3.0 s; frontend 1.8 s; backend 1.2 s.

Top included files:

* 0.86 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.83 s — src/Mod/Part/App/PartFeature.h
* 0.45 s — src/App/FeaturePython.h
* 0.35 s — src/App/GeoFeature.h
* 0.35 s — src/App/DocumentObject.h
* 0.26 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.25 s — src/Mod/TechDraw/App/HatchLine.h
* 0.23 s — src/Mod/Part/App/TopoShape.h
* 0.21 s — src/Mod/TechDraw/App/Geometry.h
* 0.20 s — src/App/ComplexGeoData.h

Top template instantiations:

* 0.03 s — Base::ConsoleSingleton::message<std::basic_string<char> &>
* 0.03 s — std::vector<int>::rbegin
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::unique_ptr<std::basic_istream<char>>
* 0.02 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>>
* 0.02 s — std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>>
* 0.02 s — std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
