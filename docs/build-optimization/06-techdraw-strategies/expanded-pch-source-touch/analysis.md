# Clang build profile

* Recorded Ninja log timestamp span: 4.4 s (130–4502 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 2.5 | 0.0 | 2.5 |
| Frontend | 1.3 | 0.0 | 1.3 |
| Backend | 1.1 | 0.0 | 1.1 |
| Source | 0.8 | 0.0 | 0.8 |
| InstantiateFunction | 0.6 | 0.0 | 0.6 |
| InstantiateClass | 0.5 | 0.0 | 0.5 |
| Optimizer | 0.8 | 0.0 | 0.8 |
| CodeGenPasses | 0.4 | 0.0 | 0.4 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 2.6 | 2.5 | 1.3 | 1.1 | 0.8 | src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/HatchLine.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/TechDraw | 2.5 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 0.5 | src/Mod/TechDraw/App/DrawUtil.h |
| 0.4 | src/Mod/Part/App/PartFeature.h |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.3 | src/Mod/TechDraw/App/HatchLine.h |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | src/Mod/TechDraw/App/Geometry.h |
| 0.1 | src/Base/Writer.h |
| 0.1 | src/App/ElementMap.h |
| 0.1 | src/Mod/Material/App/PropertyMaterial.h |
| 0.1 | src/Mod/Material/App/Materials.h |
| 0.1 | src/App/Application.h |
| 0.1 | src/App/MappedName.h |
| 0.1 | src/Base/UniqueNameManager.h |
| 0.1 | src/Base/UnlimitedUnsigned.h |
| 0.1 | src/Base/Reader.h |
| 0.0 | src/3rdParty/zipios++/zipoutputstream.h |
| 0.0 | src/Base/Stream.h |
| 0.0 | src/3rdParty/zipios++/zipoutputstreambuf.h |
| 0.0 | src/Mod/Material/App/MaterialValue.h |
| 0.0 | src/Base/Console.h |
| 0.0 | src/3rdParty/zipios++/fcoll.h |
| 0.0 | src/App/StringHasher.h |
| 0.0 | src/App/ProcessArguments.h |
| 0.0 | src/Base/Converter.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.1 | Base::ConsoleSingleton::message<std::basic_string<char> &> |
| 0.0 | std::vector<int>::rbegin |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Message, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char> &> |
| 0.0 | std::format<std::basic_string<char> &> |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | Base::ConsoleSingleton::warning<std::basic_string<char> &, const char *> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | QList<QString>::append |
| 0.0 | QList<QString>::emplaceBack<const QString &> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 0.5 | src/Mod/TechDraw/App/DrawUtil.h |
| 0.4 | src/Mod/Part/App/PartFeature.h |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.3 | src/Mod/TechDraw/App/HatchLine.h |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | src/Mod/TechDraw/App/Geometry.h |
| 0.1 | src/Base/Writer.h |
| 0.1 | src/App/ElementMap.h |
| 0.1 | src/Mod/Material/App/PropertyMaterial.h |
| 0.1 | src/Mod/Material/App/Materials.h |
| 0.1 | src/App/Application.h |
| 0.1 | src/App/MappedName.h |
| 0.1 | src/Base/UniqueNameManager.h |
| 0.1 | src/Base/UnlimitedUnsigned.h |
| 0.1 | src/Base/Reader.h |
| 0.0 | src/3rdParty/zipios++/zipoutputstream.h |
| 0.0 | src/Base/Stream.h |
| 0.0 | src/3rdParty/zipios++/zipoutputstreambuf.h |
| 0.0 | src/Mod/Material/App/MaterialValue.h |
| 0.0 | src/Base/Console.h |
| 0.0 | src/3rdParty/zipios++/fcoll.h |
| 0.0 | src/App/StringHasher.h |
| 0.0 | src/App/ProcessArguments.h |
| 0.0 | src/Base/Converter.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | Base::ConsoleSingleton::message<std::basic_string<char> &> |
| 0.0 | std::vector<int>::rbegin |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Message, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char> &> |
| 0.0 | std::format<std::basic_string<char> &> |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | std::map<std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::clear |
| 0.0 | std::_Rb_tree<std::basic_string<char>, std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>, std::_Select1st<std::pair<const std::basic_string<char>, std::vector<Base::UniqueNameManager::PiecewiseSparseIntegerSet<Base::UnlimitedUnsigned>>>>, std::less<void>>::_M_erase |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | Base::ConsoleSingleton::warning<std::basic_string<char> &, const char *> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | QList<QString>::append |
| 0.0 | QList<QString>::emplaceBack<const QString &> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir/HatchLine.cpp.o

Ninja 2.6 s; compiler 2.5 s; frontend 1.3 s; backend 1.1 s.

Top included files:

* 0.46 s — src/Mod/TechDraw/App/DrawUtil.h
* 0.42 s — src/Mod/Part/App/PartFeature.h
* 0.30 s — src/Mod/Part/App/PropertyTopoShape.h
* 0.26 s — src/Mod/Part/App/TopoShape.h
* 0.25 s — src/Mod/TechDraw/App/HatchLine.h
* 0.22 s — src/App/ComplexGeoData.h
* 0.21 s — src/Mod/TechDraw/App/Geometry.h
* 0.14 s — src/Base/Writer.h
* 0.12 s — src/App/ElementMap.h
* 0.11 s — src/Mod/Material/App/PropertyMaterial.h

Top template instantiations:

* 0.05 s — Base::ConsoleSingleton::message<std::basic_string<char> &>
* 0.03 s — std::vector<int>::rbegin
* 0.02 s — Base::ConsoleSingleton::send<Base::LogStyle::Message, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char> &>
* 0.02 s — std::format<std::basic_string<char> &>
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::unique_ptr<std::basic_istream<char>>
* 0.02 s — std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>>
* 0.02 s — std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — std::sort<QList<App::StringIDRef>::iterator>
