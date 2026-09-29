# Clang build profile

* Recorded Ninja log timestamp span: 5.7 s (128–5823 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 4.0 | 0.0 | 4.0 |
| Frontend | 2.8 | 0.0 | 2.8 |
| Backend | 1.2 | 0.0 | 1.2 |
| Source | 0.0 | 0.0 | 0.0 |
| InstantiateFunction | 0.7 | 0.0 | 0.7 |
| InstantiateClass | 0.9 | 0.0 | 0.9 |
| Optimizer | 0.8 | 0.0 | 0.8 |
| CodeGenPasses | 0.4 | 0.0 | 0.4 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 4.1 | 4.0 | 2.8 | 1.2 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_0_cxx.cxx.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 4.0 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 2.1 | src/Mod/Part/App/FeaturePartBoolean.cpp |
| 1.5 | src/Mod/Part/App/FeaturePartBoolean.h |
| 1.3 | src/Mod/Part/App/PartFeature.h |
| 0.7 | src/Mod/Material/App/PropertyMaterial.h |
| 0.7 | src/Mod/Material/App/Materials.h |
| 0.6 | src/App/Application.h |
| 0.4 | src/App/FeaturePython.h |
| 0.4 | src/Mod/Material/App/MaterialValue.h |
| 0.3 | src/App/GeoFeature.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h |
| 0.3 | src/App/DocumentObject.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstringview.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.2 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 0.1 | src/Mod/Part/App/TopoShape.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QVariant |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | App::PropertyListsT<App::DocumentObject *, std::vector<App::DocumentObject *>, App::PropertyLinkListBase>::setValue |
| 0.0 | Base::ConsoleSingleton::log<const char *> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::unique_ptr<QTextStreamPrivate> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, const char *> |
| 0.0 | std::format<const char *> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | std::vector<App::DocumentObject *>::resize |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.0 | std::vector<App::DocumentObject *>::_M_fill_insert |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | std::map<QString, std::shared_ptr<Materials::MaterialProperty>> |
| 0.0 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_M_emplace_hint_unique<const std::piecewise_construct_t &, std::tuple<App::DocumentObject *const &>, std::tuple<>> |
| 0.0 | std::_Rb_tree<QString, std::pair<const QString, std::shared_ptr<Materials::MaterialProperty>>, std::_Select1st<std::pair<const QString, std::shared_ptr<Materials::MaterialProperty>>>, std::less<QString>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | std::unique_ptr<std::vector<App::PropertyXLinkContainer::RestoreInfo>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 2.1 | src/Mod/Part/App/FeaturePartBoolean.cpp |
| 1.5 | src/Mod/Part/App/FeaturePartBoolean.h |
| 1.3 | src/Mod/Part/App/PartFeature.h |
| 0.7 | src/Mod/Material/App/PropertyMaterial.h |
| 0.7 | src/Mod/Material/App/Materials.h |
| 0.6 | src/App/Application.h |
| 0.4 | src/App/FeaturePython.h |
| 0.4 | src/Mod/Material/App/MaterialValue.h |
| 0.3 | src/App/GeoFeature.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h |
| 0.3 | src/App/DocumentObject.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstringview.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.2 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 0.1 | src/Mod/Part/App/TopoShape.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QVariant |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | App::PropertyListsT<App::DocumentObject *, std::vector<App::DocumentObject *>, App::PropertyLinkListBase>::setValue |
| 0.0 | Base::ConsoleSingleton::log<const char *> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::unique_ptr<QTextStreamPrivate> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, const char *> |
| 0.0 | std::format<const char *> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | std::vector<App::DocumentObject *>::resize |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_data<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_impl<QTextStreamPrivate, std::default_delete<QTextStreamPrivate>> |
| 0.0 | std::vector<App::DocumentObject *>::_M_fill_insert |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | std::map<QString, std::shared_ptr<Materials::MaterialProperty>> |
| 0.0 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_M_emplace_hint_unique<const std::piecewise_construct_t &, std::tuple<App::DocumentObject *const &>, std::tuple<>> |
| 0.0 | std::_Rb_tree<QString, std::pair<const QString, std::shared_ptr<Materials::MaterialProperty>>, std::_Select1st<std::pair<const QString, std::shared_ptr<Materials::MaterialProperty>>>, std::less<QString>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | std::unique_ptr<std::vector<App::PropertyXLinkContainer::RestoreInfo>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/Unity/unity_0_cxx.cxx.o

Ninja 4.1 s; compiler 4.0 s; frontend 2.8 s; backend 1.2 s.

Top included files:

* 2.13 s — src/Mod/Part/App/FeaturePartBoolean.cpp
* 1.45 s — src/Mod/Part/App/FeaturePartBoolean.h
* 1.31 s — src/Mod/Part/App/PartFeature.h
* 0.74 s — src/Mod/Material/App/PropertyMaterial.h
* 0.70 s — src/Mod/Material/App/Materials.h
* 0.61 s — src/App/Application.h
* 0.39 s — src/App/FeaturePython.h
* 0.36 s — src/Mod/Material/App/MaterialValue.h
* 0.29 s — src/App/GeoFeature.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h

Top template instantiations:

* 0.03 s — App::PropertyListsT<App::DocumentObject *, std::vector<App::DocumentObject *>, App::PropertyLinkListBase>::setValue
* 0.03 s — Base::ConsoleSingleton::log<const char *>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::unique_ptr<QTextStreamPrivate>
* 0.02 s — std::sort<QList<App::StringIDRef>::iterator>
* 0.02 s — std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter>
* 0.02 s — Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, const char *>
* 0.01 s — std::format<const char *>
* 0.01 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>>
