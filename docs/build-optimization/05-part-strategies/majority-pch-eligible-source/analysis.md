# Clang build profile

* Recorded Ninja log timestamp span: 3.3 s (133–3445 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 1.6 | 0.0 | 1.6 |
| Frontend | 1.4 | 0.0 | 1.4 |
| Backend | 0.1 | 0.0 | 0.1 |
| Source | 1.1 | 0.0 | 1.1 |
| InstantiateFunction | 0.4 | 0.0 | 0.4 |
| InstantiateClass | 0.5 | 0.0 | 0.5 |
| Optimizer | 0.1 | 0.0 | 0.1 |
| CodeGenPasses | 0.0 | 0.0 | 0.0 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 1.6 | 1.6 | 1.4 | 0.1 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartBox.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 1.6 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 1.0 | src/Mod/Part/App/FeaturePartBox.h |
| 0.9 | src/Mod/Part/App/PrimitiveFeature.h |
| 0.8 | src/Mod/Part/App/AttachExtension.h |
| 0.7 | src/Mod/Part/App/Attacher.h |
| 0.5 | src/Mod/Part/App/PartFeature.h |
| 0.5 | src/Mod/Material/App/PropertyMaterial.h |
| 0.5 | src/Mod/Material/App/Materials.h |
| 0.4 | src/Mod/Material/App/MaterialValue.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.2 | src/App/PropertyStandard.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QVariant |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |
| 0.1 | src/App/GeoFeature.h |
| 0.1 | src/App/DocumentObject.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdebug.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 0.1 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 0.1 | src/Base/Reader.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdatastream.h |
| 0.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/functional/hash/hash.hpp |
| 0.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/container_hash/hash.hpp |
| 0.0 | src/App/PropertyGeo.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobjectdefs.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | QList<QString>::append |
| 0.0 | QList<QString>::emplaceBack<const QString &> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | QtPrivate::QMovableArrayOps<QString>::emplace<const QString &> |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.0 | std::map<std::basic_string<char>, std::basic_string<char>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.0 | QArrayDataPointer<QString>::detachAndGrow |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::unique_ptr<Attacher::AttachEngine> |
| 0.0 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.0 | std::unique_ptr<App::DocumentWeakPtrT::Private> |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 1.0 | src/Mod/Part/App/FeaturePartBox.h |
| 0.9 | src/Mod/Part/App/PrimitiveFeature.h |
| 0.8 | src/Mod/Part/App/AttachExtension.h |
| 0.7 | src/Mod/Part/App/Attacher.h |
| 0.5 | src/Mod/Part/App/PartFeature.h |
| 0.5 | src/Mod/Material/App/PropertyMaterial.h |
| 0.5 | src/Mod/Material/App/Materials.h |
| 0.4 | src/Mod/Material/App/MaterialValue.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.2 | src/App/PropertyStandard.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QVariant |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |
| 0.1 | src/App/GeoFeature.h |
| 0.1 | src/App/DocumentObject.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdebug.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 0.1 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 0.1 | src/Base/Reader.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdatastream.h |
| 0.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/functional/hash/hash.hpp |
| 0.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/container_hash/hash.hpp |
| 0.0 | src/App/PropertyGeo.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobjectdefs.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | std::unique_ptr<std::basic_istream<char>> |
| 0.0 | std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>> |
| 0.0 | QList<QString>::operator<< |
| 0.0 | QList<QString>::append |
| 0.0 | QList<QString>::emplaceBack<const QString &> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | QtPrivate::QMovableArrayOps<QString>::emplace<const QString &> |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.0 | std::map<std::basic_string<char>, std::basic_string<char>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.0 | QArrayDataPointer<QString>::detachAndGrow |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |
| 0.0 | std::unique_ptr<Attacher::AttachEngine> |
| 0.0 | std::unique_ptr<App::DynamicProperty::Impl> |
| 0.0 | std::unique_ptr<App::DocumentWeakPtrT::Private> |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialValue> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialValue> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartBox.cpp.o

Ninja 1.6 s; compiler 1.6 s; frontend 1.4 s; backend 0.1 s.

Top included files:

* 1.02 s — src/Mod/Part/App/FeaturePartBox.h
* 0.86 s — src/Mod/Part/App/PrimitiveFeature.h
* 0.83 s — src/Mod/Part/App/AttachExtension.h
* 0.67 s — src/Mod/Part/App/Attacher.h
* 0.50 s — src/Mod/Part/App/PartFeature.h
* 0.45 s — src/Mod/Material/App/PropertyMaterial.h
* 0.45 s — src/Mod/Material/App/Materials.h
* 0.39 s — src/Mod/Material/App/MaterialValue.h
* 0.20 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType
* 0.20 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h

Top template instantiations:

* 0.03 s — std::unique_ptr<std::basic_istream<char>>
* 0.02 s — std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — QList<QString>::operator<<
* 0.02 s — QList<QString>::append
* 0.02 s — QList<QString>::emplaceBack<const QString &>
* 0.02 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — QtPrivate::QMovableArrayOps<QString>::emplace<const QString &>
* 0.02 s — std::map<QString, Materials::ModelProperty>::operator[]
* 0.02 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>>
