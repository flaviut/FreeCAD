# Clang build profile

* Recorded Ninja log timestamp span: 12.9 s (140–13002 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 7; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 60.9 | 0.0 | 60.9 |
| Frontend | 44.9 | 0.0 | 44.9 |
| Backend | 15.6 | 0.0 | 15.6 |
| Source | 35.1 | 0.0 | 35.1 |
| InstantiateFunction | 12.9 | 0.0 | 12.9 |
| InstantiateClass | 12.8 | 0.0 | 12.8 |
| Optimizer | 9.8 | 0.0 | 9.8 |
| CodeGenPasses | 5.7 | 0.0 | 5.7 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 10.8 | 10.7 | 7.0 | 3.6 | 5.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 10.1 | 10.0 | 7.3 | 2.6 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 9.6 | 9.5 | 7.2 | 2.3 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 9.3 | 9.2 | 5.7 | 3.4 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 8.2 | 8.1 | 6.5 | 1.6 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 7.1 | 7.0 | 6.5 | 0.5 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |
| 6.5 | 6.4 | 4.7 | 1.6 | 3.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 60.9 | 7 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 12.1 | src/Mod/Sketcher/App/SketchObject.h |
| 12.0 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 6.9 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 6.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 5.3 | src/Mod/Sketcher/App/Sketch.h |
| 5.1 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 3.7 | src/App/Document.h |
| 3.5 | src/Mod/Part/App/PartFeature.h |
| 3.4 | src/Mod/Part/App/Part2DObject.h |
| 3.4 | src/Mod/Part/App/AttachExtension.h |
| 3.3 | src/Mod/Part/App/Attacher.h |
| 3.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 2.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 2.9 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 2.9 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 2.8 | src/Mod/Part/App/Geometry.h |
| 2.5 | src/Gui/CommandT.h |
| 2.3 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 2.0 | src/Mod/Part/Gui/ViewProvider.h |
| 2.0 | src/Mod/Part/Gui/ViewProviderExt.h |
| 1.8 | src/Mod/Part/App/PropertyTopoShape.h |
| 1.8 | src/App/DocumentObject.h |
| 1.7 | src/Mod/Part/App/PropertyGeometryList.h |
| 1.6 | src/Gui/Application.h |
| 1.6 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.7 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 0.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 0.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 0.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 0.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 0.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.2 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 0.2 | boost::basic_format<char>::basic_format |
| 0.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 0.2 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.2 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.2 | QList<App::SubObjectT>::push_front |
| 0.2 | QList<App::SubObjectT>::prepend |
| 0.2 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.2 | boost::basic_format<char>::parse |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 12.1 | src/Mod/Sketcher/App/SketchObject.h |
| 12.0 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 6.9 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 6.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 5.3 | src/Mod/Sketcher/App/Sketch.h |
| 5.1 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 3.7 | src/App/Document.h |
| 3.5 | src/Mod/Part/App/PartFeature.h |
| 3.4 | src/Mod/Part/App/Part2DObject.h |
| 3.4 | src/Mod/Part/App/AttachExtension.h |
| 3.3 | src/Mod/Part/App/Attacher.h |
| 3.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 2.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 2.9 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 2.9 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 2.8 | src/Mod/Part/App/Geometry.h |
| 2.5 | src/Gui/CommandT.h |
| 2.3 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 2.0 | src/Mod/Part/Gui/ViewProvider.h |
| 2.0 | src/Mod/Part/Gui/ViewProviderExt.h |
| 1.8 | src/Mod/Part/App/PropertyTopoShape.h |
| 1.8 | src/App/DocumentObject.h |
| 1.7 | src/Mod/Part/App/PropertyGeometryList.h |
| 1.6 | src/Gui/Application.h |
| 1.6 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.7 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 0.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 0.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 0.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 0.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 0.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.2 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 0.2 | boost::basic_format<char>::basic_format |
| 0.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 0.2 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.2 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.2 | QList<App::SubObjectT>::push_front |
| 0.2 | QList<App::SubObjectT>::prepend |
| 0.2 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.2 | boost::basic_format<char>::parse |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 10.8 s; compiler 10.7 s; frontend 7.0 s; backend 3.6 s.

Top included files:

* 1.75 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.56 s — src/Mod/Sketcher/App/SketchObject.h
* 1.13 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.13 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.95 s — src/Gui/CommandT.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.60 s — src/App/Document.h
* 0.60 s — src/App/Transactions.h
* 0.51 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.07 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.07 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, int, int &>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.05 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o

Ninja 10.1 s; compiler 10.0 s; frontend 7.3 s; backend 2.6 s.

Top included files:

* 2.03 s — src/Mod/Sketcher/App/SketchObject.h
* 1.77 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.12 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.12 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.87 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.67 s — src/App/Document.h
* 0.55 s — src/Mod/Part/App/Part2DObject.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.53 s — src/Mod/Part/App/Attacher.h

Top template instantiations:

* 0.11 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o

Ninja 9.6 s; compiler 9.5 s; frontend 7.2 s; backend 2.3 s.

Top included files:

* 1.81 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.59 s — src/Mod/Sketcher/App/SketchObject.h
* 1.13 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.13 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.67 s — src/App/Document.h
* 0.54 s — src/Mod/Part/App/Part2DObject.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.52 s — src/Mod/Part/App/Attacher.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o

Ninja 9.3 s; compiler 9.2 s; frontend 5.7 s; backend 3.4 s.

Top included files:

* 2.88 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.17 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.17 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 1.06 s — build/clang-profile/src/Mod/Sketcher/Gui/SketcherGui_autogen/include/ui_SketcherToolDefaultWidget.h
* 0.97 s — src/Gui/PrefWidgets.h
* 0.85 s — src/Mod/Part/Gui/ViewProvider2DObject.h
* 0.81 s — src/Mod/Part/Gui/ViewProvider.h
* 0.81 s — src/Mod/Part/Gui/ViewProviderExt.h
* 0.58 s — src/Gui/QuantitySpinBox.h
* 0.58 s — src/Gui/MetaTypes.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o

Ninja 8.2 s; compiler 8.1 s; frontend 6.5 s; backend 1.6 s.

Top included files:

* 2.10 s — src/Mod/Sketcher/App/SketchObject.h
* 1.87 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.27 s — src/Gui/CommandT.h
* 1.14 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.14 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.90 s — src/App/Document.h
* 0.90 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.58 s — src/Mod/Part/App/Part2DObject.h
* 0.58 s — src/Mod/Part/App/AttachExtension.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, const char *, const char *, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
