# Clang build profile

* Recorded Ninja log timestamp span: 4.9 s (135–5039 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 2.9 | 0.0 | 2.9 |
| Frontend | 2.8 | 0.0 | 2.8 |
| Backend | 0.2 | 0.0 | 0.2 |
| Source | 2.4 | 0.0 | 2.4 |
| InstantiateFunction | 0.7 | 0.0 | 0.7 |
| InstantiateClass | 0.9 | 0.0 | 0.9 |
| Optimizer | 0.1 | 0.0 | 0.1 |
| CodeGenPasses | 0.1 | 0.0 | 0.1 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 3.0 | 2.9 | 2.8 | 0.2 | 2.4 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartBox.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 2.9 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 2.2 | src/Mod/Part/App/FeaturePartBox.h |
| 2.0 | src/Mod/Part/App/PrimitiveFeature.h |
| 1.9 | src/Mod/Part/App/AttachExtension.h |
| 1.7 | src/Mod/Part/App/Attacher.h |
| 1.4 | src/Mod/Part/App/PartFeature.h |
| 1.0 | src/Mod/Material/App/PropertyMaterial.h |
| 1.0 | src/Mod/Material/App/Materials.h |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.4 | src/Mod/Material/App/MaterialValue.h |
| 0.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.3 | src/App/ComplexGeoData.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | src/App/ElementMap.h |
| 0.2 | src/App/PropertyStandard.h |
| 0.2 | src/Base/Reader.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstringview.h |
| 0.2 | src/App/Application.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.0 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::unique_ptr<App::PropertyData::Impl> |
| 0.0 | std::unique_ptr<Base::Exception> |
| 0.0 | std::vector<char *> |
| 0.0 | std::unique_ptr<std::thread::_State> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.0 | std::unique_ptr<QTextStreamPrivate> |
| 0.0 | std::unique_ptr<App::PropertyExpressionEngine::Private> |
| 0.0 | std::unique_ptr<QtPrivate::QSlotObjectBase, QtPrivate::QSlotObjectBase::Deleter> |
| 0.0 | std::_Vector_base<char *, std::allocator<char *>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 2.2 | src/Mod/Part/App/FeaturePartBox.h |
| 2.0 | src/Mod/Part/App/PrimitiveFeature.h |
| 1.9 | src/Mod/Part/App/AttachExtension.h |
| 1.7 | src/Mod/Part/App/Attacher.h |
| 1.4 | src/Mod/Part/App/PartFeature.h |
| 1.0 | src/Mod/Material/App/PropertyMaterial.h |
| 1.0 | src/Mod/Material/App/Materials.h |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 0.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.4 | src/Mod/Material/App/MaterialValue.h |
| 0.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.3 | src/App/ComplexGeoData.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | src/App/ElementMap.h |
| 0.2 | src/App/PropertyStandard.h |
| 0.2 | src/Base/Reader.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstringview.h |
| 0.2 | src/App/Application.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.0 | std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::unique_ptr<App::PropertyData::Impl> |
| 0.0 | std::unique_ptr<Base::Exception> |
| 0.0 | std::vector<char *> |
| 0.0 | std::unique_ptr<std::thread::_State> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.0 | std::unique_ptr<QTextStreamPrivate> |
| 0.0 | std::unique_ptr<App::PropertyExpressionEngine::Private> |
| 0.0 | std::unique_ptr<QtPrivate::QSlotObjectBase, QtPrivate::QSlotObjectBase::Deleter> |
| 0.0 | std::_Vector_base<char *, std::allocator<char *>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartBox.cpp.o

Ninja 3.0 s; compiler 2.9 s; frontend 2.8 s; backend 0.2 s.

Top included files:

* 2.18 s — src/Mod/Part/App/FeaturePartBox.h
* 1.97 s — src/Mod/Part/App/PrimitiveFeature.h
* 1.93 s — src/Mod/Part/App/AttachExtension.h
* 1.65 s — src/Mod/Part/App/Attacher.h
* 1.45 s — src/Mod/Part/App/PartFeature.h
* 1.05 s — src/Mod/Material/App/PropertyMaterial.h
* 1.05 s — src/Mod/Material/App/Materials.h
* 0.56 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet
* 0.56 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h
* 0.56 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h

Top template instantiations:

* 0.02 s — std::unique_ptr<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — std::sort<QList<App::StringIDRef>::iterator>
* 0.02 s — std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter>
* 0.02 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>>
* 0.02 s — qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>>
* 0.02 s — std::__uniq_ptr_data<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter>
* 0.02 s — std::__uniq_ptr_impl<std::filesystem::path::_List::_Impl, std::filesystem::path::_List::_Impl_deleter>
* 0.01 s — std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve
