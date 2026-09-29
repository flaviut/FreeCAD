# Clang build profile

* Recorded Ninja log timestamp span: 2.2 s (139–2376 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 1; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 0.5 | 0.0 | 0.5 |
| Frontend | 0.3 | 0.0 | 0.3 |
| Backend | 0.1 | 0.0 | 0.1 |
| Source | 0.2 | 0.0 | 0.2 |
| InstantiateFunction | 0.1 | 0.0 | 0.1 |
| InstantiateClass | 0.1 | 0.0 | 0.1 |
| Optimizer | 0.1 | 0.0 | 0.1 |
| CodeGenPasses | 0.0 | 0.0 | 0.0 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 0.5 | 0.5 | 0.3 | 0.1 | 0.2 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartBox.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 0.5 | 1 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 0.2 | src/Mod/Part/App/FeaturePartBox.h |
| 0.2 | src/Mod/Part/App/PrimitiveFeature.h |
| 0.1 | src/Mod/Part/App/AttachExtension.h |
| 0.1 | src/Mod/Part/App/Attacher.h |
| 0.1 | src/App/DocumentObserver.h |
| 0.0 | src/App/ExtensionPython.h |
| 0.0 | src/Base/Interpreter.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx |
| 0.0 | src/Mod/Part/App/PrismExtension.h |
| 0.0 | src/App/PropertyUnits.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionOldType.hxx |
| 0.0 | src/App/DocumentObjectExtension.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionModule.hxx |
| 0.0 | src/App/Extension.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionType.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/PythonType.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionTypeBase.hxx |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.0 | std::unique_ptr<App::DocumentWeakPtrT::Private> |
| 0.0 | std::__uniq_ptr_data<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::__uniq_ptr_impl<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.0 | std::vector<PyMethodDef> |
| 0.0 | std::_Vector_base<PyMethodDef, std::allocator<PyMethodDef>> |
| 0.0 | std::tuple<App::DocumentWeakPtrT::Private *, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::allocator<PyMethodDef> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.0 | std::__new_allocator<PyMethodDef> |
| 0.0 | std::unique_ptr<App::DocumentObjectWeakPtrT::Private> |
| 0.0 | std::unique_ptr<Attacher::AttachEngine> |
| 0.0 | std::vector<Attacher::eRefType>::push_back |
| 0.0 | std::__uniq_ptr_data<Attacher::AttachEngine, std::default_delete<Attacher::AttachEngine>> |
| 0.0 | std::__uniq_ptr_impl<Attacher::AttachEngine, std::default_delete<Attacher::AttachEngine>> |
| 0.0 | std::__uniq_ptr_data<App::DocumentObjectWeakPtrT::Private, std::default_delete<App::DocumentObjectWeakPtrT::Private>> |
| 0.0 | std::__uniq_ptr_impl<App::DocumentObjectWeakPtrT::Private, std::default_delete<App::DocumentObjectWeakPtrT::Private>> |
| 0.0 | std::vector<Attacher::eRefType>::_M_realloc_append<const Attacher::eRefType &> |
| 0.0 | std::is_move_constructible<std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::set<Attacher::eRefType> |
| 0.0 | std::vector<Attacher::eRefType>::~vector |
| 0.0 | std::_Destroy<Attacher::eRefType *, Attacher::eRefType> |
| 0.0 | std::_Destroy<Attacher::eRefType *> |
| 0.0 | std::tuple<Attacher::AttachEngine *, std::default_delete<Attacher::AttachEngine>> |
| 0.0 | std::_Rb_tree<Attacher::eRefType, Attacher::eRefType, std::_Identity<Attacher::eRefType>, std::less<Attacher::eRefType>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 0.2 | src/Mod/Part/App/FeaturePartBox.h |
| 0.2 | src/Mod/Part/App/PrimitiveFeature.h |
| 0.1 | src/Mod/Part/App/AttachExtension.h |
| 0.1 | src/Mod/Part/App/Attacher.h |
| 0.1 | src/App/DocumentObserver.h |
| 0.0 | src/App/ExtensionPython.h |
| 0.0 | src/Base/Interpreter.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx |
| 0.0 | src/Mod/Part/App/PrismExtension.h |
| 0.0 | src/App/PropertyUnits.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionOldType.hxx |
| 0.0 | src/App/DocumentObjectExtension.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionModule.hxx |
| 0.0 | src/App/Extension.h |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionType.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/PythonType.hxx |
| 0.0 | src/3rdParty/PyCXX/CXX/Python3/ExtensionTypeBase.hxx |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.0 | std::unique_ptr<App::DocumentWeakPtrT::Private> |
| 0.0 | std::__uniq_ptr_data<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::__uniq_ptr_impl<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 0.0 | std::vector<PyMethodDef> |
| 0.0 | std::_Vector_base<PyMethodDef, std::allocator<PyMethodDef>> |
| 0.0 | std::tuple<App::DocumentWeakPtrT::Private *, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::allocator<PyMethodDef> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 0.0 | std::__new_allocator<PyMethodDef> |
| 0.0 | std::unique_ptr<App::DocumentObjectWeakPtrT::Private> |
| 0.0 | std::unique_ptr<Attacher::AttachEngine> |
| 0.0 | std::vector<Attacher::eRefType>::push_back |
| 0.0 | std::__uniq_ptr_data<Attacher::AttachEngine, std::default_delete<Attacher::AttachEngine>> |
| 0.0 | std::__uniq_ptr_impl<Attacher::AttachEngine, std::default_delete<Attacher::AttachEngine>> |
| 0.0 | std::__uniq_ptr_data<App::DocumentObjectWeakPtrT::Private, std::default_delete<App::DocumentObjectWeakPtrT::Private>> |
| 0.0 | std::__uniq_ptr_impl<App::DocumentObjectWeakPtrT::Private, std::default_delete<App::DocumentObjectWeakPtrT::Private>> |
| 0.0 | std::vector<Attacher::eRefType>::_M_realloc_append<const Attacher::eRefType &> |
| 0.0 | std::is_move_constructible<std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.0 | std::set<Attacher::eRefType> |
| 0.0 | std::vector<Attacher::eRefType>::~vector |
| 0.0 | std::_Destroy<Attacher::eRefType *, Attacher::eRefType> |
| 0.0 | std::_Destroy<Attacher::eRefType *> |
| 0.0 | std::tuple<Attacher::AttachEngine *, std::default_delete<Attacher::AttachEngine>> |
| 0.0 | std::_Rb_tree<Attacher::eRefType, Attacher::eRefType, std::_Identity<Attacher::eRefType>, std::less<Attacher::eRefType>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartBox.cpp.o

Ninja 0.5 s; compiler 0.5 s; frontend 0.3 s; backend 0.1 s.

Top included files:

* 0.19 s — src/Mod/Part/App/FeaturePartBox.h
* 0.18 s — src/Mod/Part/App/PrimitiveFeature.h
* 0.15 s — src/Mod/Part/App/AttachExtension.h
* 0.09 s — src/Mod/Part/App/Attacher.h
* 0.05 s — src/App/DocumentObserver.h
* 0.04 s — src/App/ExtensionPython.h
* 0.04 s — src/Base/Interpreter.h
* 0.03 s — src/3rdParty/PyCXX/CXX/Extensions.hxx
* 0.03 s — src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx
* 0.01 s — src/Mod/Part/App/PrismExtension.h

Top template instantiations:

* 0.03 s — std::unique_ptr<App::DocumentWeakPtrT::Private>
* 0.02 s — std::__uniq_ptr_data<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>>
* 0.02 s — std::__uniq_ptr_impl<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>>
* 0.02 s — std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve
* 0.02 s — std::vector<PyMethodDef>
* 0.01 s — std::_Vector_base<PyMethodDef, std::allocator<PyMethodDef>>
* 0.01 s — std::tuple<App::DocumentWeakPtrT::Private *, std::default_delete<App::DocumentWeakPtrT::Private>>
* 0.01 s — std::allocator<PyMethodDef>
* 0.01 s — std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve
* 0.01 s — std::__new_allocator<PyMethodDef>
