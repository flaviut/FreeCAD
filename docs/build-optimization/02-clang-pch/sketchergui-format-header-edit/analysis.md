# Clang build profile

* Recorded Ninja log timestamp span: 44.4 s (132–44528 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 32; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 286.7 | 0.0 | 286.7 |
| Frontend | 209.0 | 0.0 | 209.0 |
| Backend | 76.1 | 0.0 | 76.1 |
| Source | 161.0 | 0.0 | 161.0 |
| InstantiateFunction | 63.2 | 0.0 | 63.2 |
| InstantiateClass | 61.5 | 0.0 | 61.5 |
| Optimizer | 47.2 | 0.0 | 47.2 |
| CodeGenPasses | 28.8 | 0.0 | 28.8 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 24.4 | 24.3 | 11.7 | 12.5 | 6.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 15.4 | 15.3 | 9.4 | 5.8 | 6.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 14.1 | 14.0 | 8.4 | 5.5 | 5.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 13.0 | 12.9 | 8.6 | 4.2 | 5.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 11.1 | 11.0 | 7.0 | 4.0 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 10.6 | 10.5 | 6.1 | 4.3 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 10.4 | 10.3 | 7.5 | 2.7 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 10.2 | 10.1 | 7.3 | 2.7 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 9.8 | 9.7 | 6.4 | 3.3 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 9.7 | 9.6 | 7.2 | 2.4 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 9.4 | 9.3 | 5.7 | 3.6 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 9.0 | 8.9 | 5.5 | 3.3 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 8.8 | 8.7 | 6.7 | 1.9 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 8.7 | 8.6 | 6.5 | 2.0 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 8.7 | 8.6 | 5.4 | 3.2 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 8.5 | 8.4 | 6.8 | 1.6 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 8.1 | 8.0 | 6.5 | 1.4 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 8.1 | 8.0 | 6.5 | 1.4 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |
| 8.0 | 7.9 | 6.4 | 1.5 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 7.9 | 7.8 | 5.9 | 1.9 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeCoinManager.cpp.o |
| 7.7 | 7.6 | 6.3 | 1.3 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeGeometryCoinConverter.cpp.o |
| 7.5 | 7.4 | 6.1 | 1.2 | 5.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandlerDragAutoConstraint.cpp.o |
| 7.2 | 7.1 | 6.6 | 0.5 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |
| 7.1 | 7.0 | 5.9 | 1.0 | 4.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SnapManager.cpp.o |
| 6.7 | 6.6 | 4.8 | 1.7 | 3.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 286.7 | 32 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 67.3 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 45.5 | src/Mod/Sketcher/App/SketchObject.h |
| 35.8 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 35.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 21.1 | src/Mod/Sketcher/App/Sketch.h |
| 19.8 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 16.6 | src/Mod/Part/App/PartFeature.h |
| 14.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 14.9 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 14.9 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 13.5 | src/Mod/Part/Gui/ViewProvider.h |
| 13.4 | src/Mod/Part/Gui/ViewProviderExt.h |
| 12.1 | src/Mod/Part/App/AttachExtension.h |
| 12.1 | src/Mod/Part/App/Attacher.h |
| 12.0 | src/Mod/Part/App/Geometry.h |
| 11.9 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 11.7 | src/Mod/Part/App/Part2DObject.h |
| 11.3 | src/App/DocumentObject.h |
| 11.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 10.0 | src/App/Document.h |
| 9.7 | src/Gui/CommandT.h |
| 8.1 | src/Mod/Part/App/PropertyTopoShape.h |
| 7.9 | src/Mod/Material/App/PropertyMaterial.h |
| 7.3 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 7.3 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.2 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.2 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.1 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.1 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 2.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 2.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 1.9 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 1.9 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 1.8 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 1.8 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.6 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.2 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.2 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 1.0 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.8 | QList<App::SubObjectT>::push_front |
| 0.8 | QList<App::SubObjectT>::prepend |
| 0.8 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.8 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.8 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.8 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.7 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 0.7 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 67.3 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 45.5 | src/Mod/Sketcher/App/SketchObject.h |
| 35.8 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 35.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 21.1 | src/Mod/Sketcher/App/Sketch.h |
| 19.8 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 16.6 | src/Mod/Part/App/PartFeature.h |
| 14.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 14.9 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 14.9 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 13.5 | src/Mod/Part/Gui/ViewProvider.h |
| 13.4 | src/Mod/Part/Gui/ViewProviderExt.h |
| 12.1 | src/Mod/Part/App/AttachExtension.h |
| 12.1 | src/Mod/Part/App/Attacher.h |
| 12.0 | src/Mod/Part/App/Geometry.h |
| 11.9 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 11.7 | src/Mod/Part/App/Part2DObject.h |
| 11.3 | src/App/DocumentObject.h |
| 11.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 10.0 | src/App/Document.h |
| 9.7 | src/Gui/CommandT.h |
| 8.1 | src/Mod/Part/App/PropertyTopoShape.h |
| 7.9 | src/Mod/Material/App/PropertyMaterial.h |
| 7.3 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 7.3 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.2 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.2 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.1 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.1 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 2.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 2.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 1.9 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 1.9 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 1.8 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 1.8 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.6 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.2 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.2 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 1.0 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.8 | QList<App::SubObjectT>::push_front |
| 0.8 | QList<App::SubObjectT>::prepend |
| 0.8 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.8 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.8 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.8 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.7 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 0.7 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 24.4 s; compiler 24.3 s; frontend 11.7 s; backend 12.5 s.

Top included files:

* 1.81 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.25 s — src/Mod/Sketcher/App/SketchObject.h
* 1.12 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.12 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.93 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.85 s — src/App/Datums.h
* 0.68 s — src/App/GeoFeature.h
* 0.67 s — src/App/DocumentObject.h
* 0.54 s — src/Mod/Part/App/DatumFeature.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.14 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerEllipse, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 15.4 s; compiler 15.3 s; frontend 9.4 s; backend 5.8 s.

Top included files:

* 1.95 s — src/Mod/Sketcher/App/SketchObject.h
* 1.81 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.13 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.13 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.85 s — src/Mod/Sketcher/App/Sketch.h
* 0.81 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.61 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.60 s — src/App/Document.h
* 0.49 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h

Top template instantiations:

* 0.20 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.13 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.12 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 14.1 s; compiler 14.0 s; frontend 8.4 s; backend 5.5 s.

Top included files:

* 1.74 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 1.68 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.65 s — src/Mod/Sketcher/App/SketchObject.h
* 1.15 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.15 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.95 s — src/Mod/Sketcher/App/Sketch.h
* 0.90 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.70 s — src/Gui/CommandT.h
* 0.58 s — src/App/Document.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.11 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 13.0 s; compiler 12.9 s; frontend 8.6 s; backend 4.2 s.

Top included files:

* 1.66 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 1.51 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.12 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.12 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.90 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.62 s — src/App/Document.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.07 s — QObject::connect<void (QWindow::*)(QScreen *), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/ViewProviderSketch.cpp:4685:84)>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 11.1 s; compiler 11.0 s; frontend 7.0 s; backend 4.0 s.

Top included files:

* 1.71 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.59 s — src/Mod/Sketcher/App/SketchObject.h
* 1.10 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.10 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.88 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.86 s — src/Gui/CommandT.h
* 0.56 s — src/App/Transactions.h
* 0.55 s — src/App/Document.h
* 0.51 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — Gui::cmdAppObjectArgs<int &, int, int &>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
