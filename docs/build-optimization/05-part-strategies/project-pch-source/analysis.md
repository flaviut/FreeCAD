# Clang build profile

* Recorded Ninja log timestamp span: 6.0 s (138–6110 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 4.2 | 0.0 | 4.2 |
| Frontend | 1.6 | 0.0 | 1.6 |
| Backend | 2.6 | 0.0 | 2.6 |
| Source | 0.5 | 0.0 | 0.5 |
| InstantiateFunction | 0.6 | 0.0 | 0.6 |
| InstantiateClass | 0.5 | 0.0 | 0.5 |
| Optimizer | 1.6 | 0.0 | 1.6 |
| CodeGenPasses | 0.9 | 0.0 | 0.9 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 4.3 | 4.2 | 1.6 | 2.6 | 0.5 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 4.2 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 0.1 | src/App/Link.h |
| 0.1 | src/App/Document.h |
| 0.1 | src/Mod/Material/App/MaterialManager.h |
| 0.1 | src/App/Datums.h |
| 0.1 | src/Mod/Material/App/MaterialLibrary.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.0 | src/Mod/Material/App/ModelLibrary.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.0 | src/App/MainThreadSignal.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qeventloop.h |
| 0.0 | src/Base/Interpreter.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdeadlinetimer.h |
| 0.0 | src/Base/Tools.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx |
| 0.0 | src/Mod/Part/App/Tools.h |
| 0.0 | src/Mod/Part/App/Geometry.h |
| 0.0 | src/Base/Stream.h |
| 0.0 | src/App/GroupExtension.h |
| 0.0 | src/Base/Converter.h |
| 0.0 | src/Mod/Material/App/MaterialFilter.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionOldType.hxx |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | QList<Data::MappedElement>::append |
| 0.0 | std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)> |
| 0.0 | QList<Data::MappedElement>::push_back |
| 0.0 | QList<Data::MappedElement>::emplaceBack<Data::MappedElement> |
| 0.0 | std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>> |
| 0.0 | QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::detachAndGrow |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialFilter> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialFilter> |
| 0.0 | std::unique_ptr<std::map<QString, std::shared_ptr<Materials::Model>>> |
| 0.0 | std::__uniq_ptr_data<std::map<QString, std::shared_ptr<Materials::Model>>, std::default_delete<std::map<QString, std::shared_ptr<Materials::Model>>>> |
| 0.0 | std::__uniq_ptr_impl<std::map<QString, std::shared_ptr<Materials::Model>>, std::default_delete<std::map<QString, std::shared_ptr<Materials::Model>>>> |
| 0.0 | std::unordered_map<const App::DocumentObject *, fastsignals::scoped_connection> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::tryReadjustFreeSpace |
| 0.0 | Base::ConsoleSingleton::log<std::basic_string<char>> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char>> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::relocate |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *> |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *, boost::algorithm::is_equal> |
| 0.0 | std::format<std::basic_string<char>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::ModelLibrary>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::ModelLibrary>> |
| 0.0 | std::map<int, std::vector<int>>::operator[] |
| 0.0 | QtPrivate::q_relocate_overlap_n<Data::MappedElement, long long> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::ModelLibraryLocal>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 0.1 | src/App/Link.h |
| 0.1 | src/App/Document.h |
| 0.1 | src/Mod/Material/App/MaterialManager.h |
| 0.1 | src/App/Datums.h |
| 0.1 | src/Mod/Material/App/MaterialLibrary.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.0 | src/Mod/Material/App/ModelLibrary.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.0 | src/App/MainThreadSignal.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qeventloop.h |
| 0.0 | src/Base/Interpreter.h |
| 0.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdeadlinetimer.h |
| 0.0 | src/Base/Tools.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx |
| 0.0 | src/Mod/Part/App/Tools.h |
| 0.0 | src/Mod/Part/App/Geometry.h |
| 0.0 | src/Base/Stream.h |
| 0.0 | src/App/GroupExtension.h |
| 0.0 | src/Base/Converter.h |
| 0.0 | src/Mod/Material/App/MaterialFilter.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionOldType.hxx |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | QList<Data::MappedElement>::append |
| 0.0 | std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)> |
| 0.0 | QList<Data::MappedElement>::push_back |
| 0.0 | QList<Data::MappedElement>::emplaceBack<Data::MappedElement> |
| 0.0 | std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>> |
| 0.0 | QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::detachAndGrow |
| 0.0 | qRegisterNormalizedMetaType<Materials::MaterialFilter> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<Materials::MaterialFilter> |
| 0.0 | std::unique_ptr<std::map<QString, std::shared_ptr<Materials::Model>>> |
| 0.0 | std::__uniq_ptr_data<std::map<QString, std::shared_ptr<Materials::Model>>, std::default_delete<std::map<QString, std::shared_ptr<Materials::Model>>>> |
| 0.0 | std::__uniq_ptr_impl<std::map<QString, std::shared_ptr<Materials::Model>>, std::default_delete<std::map<QString, std::shared_ptr<Materials::Model>>>> |
| 0.0 | std::unordered_map<const App::DocumentObject *, fastsignals::scoped_connection> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::tryReadjustFreeSpace |
| 0.0 | Base::ConsoleSingleton::log<std::basic_string<char>> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char>> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::relocate |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *> |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *, boost::algorithm::is_equal> |
| 0.0 | std::format<std::basic_string<char>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::ModelLibrary>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::ModelLibrary>> |
| 0.0 | std::map<int, std::vector<int>>::operator[] |
| 0.0 | QtPrivate::q_relocate_overlap_n<Data::MappedElement, long long> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::ModelLibraryLocal>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o

Ninja 4.3 s; compiler 4.2 s; frontend 1.6 s; backend 2.6 s.

Top included files:

* 0.15 s — src/App/Link.h
* 0.11 s — src/App/Document.h
* 0.08 s — src/Mod/Material/App/MaterialManager.h
* 0.08 s — src/App/Datums.h
* 0.07 s — src/Mod/Material/App/MaterialLibrary.h
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.05 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.05 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.05 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.04 s — src/Mod/Material/App/ModelLibrary.h

Top template instantiations:

* 0.03 s — QList<Data::MappedElement>::append
* 0.03 s — std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>
* 0.02 s — QList<Data::MappedElement>::push_back
* 0.02 s — QList<Data::MappedElement>::emplaceBack<Data::MappedElement>
* 0.02 s — std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>>
* 0.02 s — QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement>
* 0.02 s — QArrayDataPointer<Data::MappedElement>::detachAndGrow
* 0.02 s — qRegisterNormalizedMetaType<Materials::MaterialFilter>
* 0.02 s — qRegisterNormalizedMetaTypeImplementation<Materials::MaterialFilter>
* 0.02 s — std::unique_ptr<std::map<QString, std::shared_ptr<Materials::Model>>>
