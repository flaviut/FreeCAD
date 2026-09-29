# Clang build profile

* Recorded Ninja log timestamp span: 7.8 s (128–7966 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 6.2 | 0.0 | 6.2 |
| Frontend | 3.6 | 0.0 | 3.6 |
| Backend | 2.6 | 0.0 | 2.6 |
| Source | 2.3 | 0.0 | 2.3 |
| InstantiateFunction | 1.1 | 0.0 | 1.1 |
| InstantiateClass | 1.1 | 0.0 | 1.1 |
| Optimizer | 1.7 | 0.0 | 1.7 |
| CodeGenPasses | 0.9 | 0.0 | 0.9 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 6.2 | 6.2 | 3.6 | 2.6 | 2.3 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 6.2 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 0.6 | src/App/Application.h |
| 0.5 | src/App/Document.h |
| 0.5 | src/App/Datums.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.3 | src/Mod/Material/App/MaterialManager.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h |
| 0.3 | src/Mod/Material/App/Materials.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.2 | src/Mod/Part/App/PartFeature.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstringview.h |
| 0.2 | src/Mod/Material/App/MaterialValue.h |
| 0.2 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.1 | src/App/ExportInfo.h |
| 0.1 | src/App/DocumentObject.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | src/Mod/Part/App/TopoShape.h |
| 0.1 | src/App/Link.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)> |
| 0.0 | std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>> |
| 0.0 | QList<Data::MappedElement>::append |
| 0.0 | QList<Data::MappedElement>::push_back |
| 0.0 | QList<Data::MappedElement>::emplaceBack<Data::MappedElement> |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *> |
| 0.0 | QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement> |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *, boost::algorithm::is_equal> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::detachAndGrow |
| 0.0 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_S_key |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | Base::ConsoleSingleton::log<std::basic_string<char>> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char>> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::tryReadjustFreeSpace |
| 0.0 | QArrayDataPointer<Data::MappedElement>::relocate |
| 0.0 | std::format<std::basic_string<char>> |
| 0.0 | std::vector<std::pair<long, Data::MappedName>>::rbegin |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | std::reverse_iterator<__gnu_cxx::__normal_iterator<std::pair<long, Data::MappedName> *, std::vector<std::pair<long, Data::MappedName>>>> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 0.6 | src/App/Application.h |
| 0.5 | src/App/Document.h |
| 0.5 | src/App/Datums.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 0.3 | src/Mod/Material/App/MaterialManager.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h |
| 0.3 | src/Mod/Material/App/Materials.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.2 | src/Mod/Part/App/PartFeature.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstringview.h |
| 0.2 | src/Mod/Material/App/MaterialValue.h |
| 0.2 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbytearray.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.1 | src/App/ExportInfo.h |
| 0.1 | src/App/DocumentObject.h |
| 0.1 | src/App/PropertyLinks.h |
| 0.1 | src/Mod/Part/App/TopoShape.h |
| 0.1 | src/App/Link.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.0 | std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)> |
| 0.0 | std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>> |
| 0.0 | QList<Data::MappedElement>::append |
| 0.0 | QList<Data::MappedElement>::push_back |
| 0.0 | QList<Data::MappedElement>::emplaceBack<Data::MappedElement> |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *> |
| 0.0 | QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement> |
| 0.0 | boost::algorithm::starts_with<std::basic_string<char>, const char *, boost::algorithm::is_equal> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::detachAndGrow |
| 0.0 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_S_key |
| 0.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 0.0 | Base::ConsoleSingleton::log<std::basic_string<char>> |
| 0.0 | Base::ConsoleSingleton::send<Base::LogStyle::Log, Base::IntendedRecipient::All, Base::ContentType::Untranslated, std::basic_string<char>> |
| 0.0 | QArrayDataPointer<Data::MappedElement>::tryReadjustFreeSpace |
| 0.0 | QArrayDataPointer<Data::MappedElement>::relocate |
| 0.0 | std::format<std::basic_string<char>> |
| 0.0 | std::vector<std::pair<long, Data::MappedName>>::rbegin |
| 0.0 | std::vector<Base::Vector2d>::operator= |
| 0.0 | std::reverse_iterator<__gnu_cxx::__normal_iterator<std::pair<long, Data::MappedName> *, std::vector<std::pair<long, Data::MappedName>>>> |
| 0.0 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.0 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.0 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.0 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o

Ninja 6.2 s; compiler 6.2 s; frontend 3.6 s; backend 2.6 s.

Top included files:

* 0.60 s — src/App/Application.h
* 0.53 s — src/App/Document.h
* 0.48 s — src/App/Datums.h
* 0.45 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.45 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.32 s — src/Mod/Material/App/MaterialManager.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qtextstream.h
* 0.26 s — src/Mod/Material/App/Materials.h
* 0.25 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.25 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h

Top template instantiations:

* 0.03 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.02 s — std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>
* 0.02 s — std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>>
* 0.02 s — QList<Data::MappedElement>::append
* 0.02 s — QList<Data::MappedElement>::push_back
* 0.02 s — QList<Data::MappedElement>::emplaceBack<Data::MappedElement>
* 0.02 s — boost::algorithm::starts_with<std::basic_string<char>, const char *>
* 0.02 s — QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement>
* 0.02 s — boost::algorithm::starts_with<std::basic_string<char>, const char *, boost::algorithm::is_equal>
* 0.02 s — QArrayDataPointer<Data::MappedElement>::detachAndGrow
