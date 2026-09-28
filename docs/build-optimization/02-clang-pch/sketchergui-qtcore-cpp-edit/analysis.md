# Clang build profile

* Recorded Ninja log timestamp span: 11.6 s (127–11699 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 7; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 52.3 | 0.0 | 52.3 |
| Frontend | 36.8 | 0.0 | 36.8 |
| Backend | 15.1 | 0.0 | 15.1 |
| Source | 27.4 | 0.0 | 27.4 |
| InstantiateFunction | 11.9 | 0.0 | 11.9 |
| InstantiateClass | 11.1 | 0.0 | 11.1 |
| Optimizer | 9.6 | 0.0 | 9.6 |
| CodeGenPasses | 5.5 | 0.0 | 5.5 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 9.5 | 9.4 | 5.8 | 3.6 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 8.7 | 8.6 | 6.0 | 2.5 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 8.2 | 8.2 | 5.9 | 2.2 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 7.8 | 7.7 | 4.4 | 3.3 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 6.7 | 6.6 | 5.1 | 1.5 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 6.4 | 6.3 | 4.6 | 1.6 | 3.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |
| 5.7 | 5.6 | 5.1 | 0.4 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 52.3 | 7 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 11.5 | src/Mod/Sketcher/App/SketchObject.h |
| 5.3 | src/Mod/Sketcher/App/Sketch.h |
| 5.1 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 5.0 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 3.7 | src/App/Document.h |
| 3.5 | src/Mod/Part/App/PartFeature.h |
| 3.4 | src/Mod/Part/App/Part2DObject.h |
| 3.3 | src/Mod/Part/App/AttachExtension.h |
| 3.2 | src/Mod/Part/App/Attacher.h |
| 3.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 2.9 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 2.5 | src/Gui/CommandT.h |
| 2.2 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 2.0 | src/Mod/Part/Gui/ViewProvider.h |
| 2.0 | src/Mod/Part/Gui/ViewProviderExt.h |
| 2.0 | src/Mod/Part/App/Geometry.h |
| 1.9 | src/Mod/Part/App/PropertyTopoShape.h |
| 1.8 | src/App/DocumentObject.h |
| 1.6 | src/Mod/Part/App/TopoShape.h |
| 1.6 | src/Gui/Application.h |
| 1.5 | src/Mod/Material/App/PropertyMaterial.h |
| 1.5 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 1.5 | src/App/Application.h |
| 1.2 | src/Mod/Part/Gui/SoFCShapeObject.h |
| 1.2 | src/Mod/Material/App/Materials.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 0.7 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 0.5 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 0.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 0.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 0.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 0.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.2 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 0.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 0.2 | boost::basic_format<char>::basic_format |
| 0.2 | boost::basic_format<char>::parse |
| 0.2 | QList<App::SubObjectT>::push_front |
| 0.2 | QList<App::SubObjectT>::prepend |
| 0.2 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.2 | Gui::StyleParameters::Diagnostics::report<const char *, std::basic_string<char>> |
| 0.2 | std::sort<QList<App::StringIDRef>::iterator> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 11.5 | src/Mod/Sketcher/App/SketchObject.h |
| 5.3 | src/Mod/Sketcher/App/Sketch.h |
| 5.1 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 5.0 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 3.7 | src/App/Document.h |
| 3.5 | src/Mod/Part/App/PartFeature.h |
| 3.4 | src/Mod/Part/App/Part2DObject.h |
| 3.3 | src/Mod/Part/App/AttachExtension.h |
| 3.2 | src/Mod/Part/App/Attacher.h |
| 3.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 2.9 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 2.5 | src/Gui/CommandT.h |
| 2.2 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 2.0 | src/Mod/Part/Gui/ViewProvider.h |
| 2.0 | src/Mod/Part/Gui/ViewProviderExt.h |
| 2.0 | src/Mod/Part/App/Geometry.h |
| 1.9 | src/Mod/Part/App/PropertyTopoShape.h |
| 1.8 | src/App/DocumentObject.h |
| 1.6 | src/Mod/Part/App/TopoShape.h |
| 1.6 | src/Gui/Application.h |
| 1.5 | src/Mod/Material/App/PropertyMaterial.h |
| 1.5 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 1.5 | src/App/Application.h |
| 1.2 | src/Mod/Part/Gui/SoFCShapeObject.h |
| 1.2 | src/Mod/Material/App/Materials.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 0.7 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 0.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 0.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 0.5 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 0.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 0.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 0.4 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 0.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 0.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 0.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 0.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.2 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 0.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 0.2 | boost::basic_format<char>::basic_format |
| 0.2 | boost::basic_format<char>::parse |
| 0.2 | QList<App::SubObjectT>::push_front |
| 0.2 | QList<App::SubObjectT>::prepend |
| 0.2 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.2 | Gui::StyleParameters::Diagnostics::report<const char *, std::basic_string<char>> |
| 0.2 | std::sort<QList<App::StringIDRef>::iterator> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 9.5 s; compiler 9.4 s; frontend 5.8 s; backend 3.6 s.

Top included files:

* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 0.93 s — src/Gui/CommandT.h
* 0.91 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.63 s — src/App/Transactions.h
* 0.63 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.58 s — src/App/Document.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.51 s — src/Mod/Part/App/Part2DObject.h
* 0.51 s — src/Mod/Part/App/AttachExtension.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, int, int &>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o

Ninja 8.7 s; compiler 8.6 s; frontend 6.0 s; backend 2.5 s.

Top included files:

* 1.93 s — src/Mod/Sketcher/App/SketchObject.h
* 0.91 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.68 s — src/App/Document.h
* 0.66 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.55 s — src/Mod/Part/App/Part2DObject.h
* 0.55 s — src/Mod/Part/App/AttachExtension.h
* 0.53 s — src/Mod/Part/App/Attacher.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.51 s — src/Mod/Part/App/PartFeature.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o

Ninja 8.2 s; compiler 8.2 s; frontend 5.9 s; backend 2.2 s.

Top included files:

* 1.59 s — src/Mod/Sketcher/App/SketchObject.h
* 0.90 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.67 s — src/App/Document.h
* 0.67 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.54 s — src/Mod/Part/App/Part2DObject.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.52 s — src/Mod/Part/App/Attacher.h
* 0.50 s — src/Mod/Part/App/PartFeature.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.05 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o

Ninja 7.8 s; compiler 7.7 s; frontend 4.4 s; backend 3.3 s.

Top included files:

* 1.56 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.06 s — build/clang-profile/src/Mod/Sketcher/Gui/SketcherGui_autogen/include/ui_SketcherToolDefaultWidget.h
* 0.96 s — src/Gui/PrefWidgets.h
* 0.83 s — src/Mod/Part/Gui/ViewProvider2DObject.h
* 0.79 s — src/Mod/Part/Gui/ViewProvider.h
* 0.79 s — src/Mod/Part/Gui/ViewProviderExt.h
* 0.56 s — src/Gui/QuantitySpinBox.h
* 0.56 s — src/Gui/MetaTypes.h
* 0.45 s — src/App/DocumentObject.h
* 0.45 s — src/Mod/Part/App/PartFeature.h

Top template instantiations:

* 0.11 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.07 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o

Ninja 6.7 s; compiler 6.6 s; frontend 5.1 s; backend 1.5 s.

Top included files:

* 1.94 s — src/Mod/Sketcher/App/SketchObject.h
* 1.27 s — src/Gui/CommandT.h
* 0.89 s — src/App/Document.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.85 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.72 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.59 s — src/Mod/Part/App/Part2DObject.h
* 0.59 s — src/Mod/Part/App/AttachExtension.h
* 0.57 s — src/Mod/Part/App/Attacher.h
* 0.52 s — src/Mod/Part/App/PartFeature.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — Gui::cmdAppObjectArgs<int &, const char *, const char *, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
