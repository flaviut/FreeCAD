# Clang build profile

* Recorded Ninja log timestamp span: 38.2 s (138–38344 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 32; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 256.5 | 0.0 | 256.5 |
| Frontend | 176.8 | 0.0 | 176.8 |
| Backend | 78.1 | 0.0 | 78.1 |
| Source | 128.0 | 0.0 | 128.0 |
| InstantiateFunction | 61.3 | 0.0 | 61.3 |
| InstantiateClass | 56.1 | 0.0 | 56.1 |
| Optimizer | 48.8 | 0.0 | 48.8 |
| CodeGenPasses | 29.3 | 0.0 | 29.3 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 23.6 | 23.5 | 10.5 | 12.9 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 14.6 | 14.5 | 8.0 | 6.4 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 13.2 | 13.1 | 7.0 | 6.0 | 4.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 12.0 | 11.9 | 7.7 | 4.1 | 4.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 10.1 | 10.0 | 6.0 | 4.0 | 4.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 9.7 | 9.6 | 5.0 | 4.5 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 9.6 | 9.5 | 6.6 | 2.8 | 4.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 9.1 | 9.0 | 6.5 | 2.4 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 9.0 | 8.9 | 6.2 | 2.7 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.6 | 8.5 | 5.2 | 3.3 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 8.6 | 8.5 | 4.9 | 3.6 | 3.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 8.0 | 7.9 | 4.5 | 3.4 | 3.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 7.9 | 7.8 | 5.8 | 2.0 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 7.7 | 7.6 | 5.9 | 1.7 | 4.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 7.7 | 7.6 | 4.4 | 3.2 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 7.4 | 7.4 | 5.8 | 1.5 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |
| 7.4 | 7.3 | 5.8 | 1.5 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 7.3 | 7.2 | 5.3 | 1.8 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 7.1 | 7.0 | 5.4 | 1.5 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 7.0 | 6.9 | 4.8 | 2.0 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeCoinManager.cpp.o |
| 6.7 | 6.7 | 5.0 | 1.7 | 3.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |
| 6.6 | 6.5 | 5.1 | 1.3 | 3.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeGeometryCoinConverter.cpp.o |
| 6.2 | 6.2 | 5.0 | 1.1 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandlerDragAutoConstraint.cpp.o |
| 6.2 | 6.1 | 5.0 | 1.1 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SnapManager.cpp.o |
| 6.2 | 6.1 | 5.5 | 0.5 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 256.5 | 32 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 46.3 | src/Mod/Sketcher/App/SketchObject.h |
| 31.9 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 22.5 | src/Mod/Sketcher/App/Sketch.h |
| 21.2 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.3 | src/Mod/Part/App/PartFeature.h |
| 15.5 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 14.1 | src/Mod/Part/Gui/ViewProvider.h |
| 14.0 | src/Mod/Part/Gui/ViewProviderExt.h |
| 13.0 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 12.7 | src/Mod/Part/App/AttachExtension.h |
| 12.6 | src/Mod/Part/App/Attacher.h |
| 12.2 | src/Mod/Part/App/Part2DObject.h |
| 12.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 12.0 | src/App/DocumentObject.h |
| 10.5 | src/App/Document.h |
| 10.2 | src/Gui/CommandT.h |
| 9.7 | src/Mod/Part/App/Geometry.h |
| 8.6 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.1 | src/Mod/Material/App/PropertyMaterial.h |
| 7.7 | src/Mod/Part/App/TopoShape.h |
| 7.4 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 6.9 | src/App/Application.h |
| 6.7 | src/Mod/Material/App/Materials.h |
| 6.5 | src/Mod/Part/Gui/SoFCShapeObject.h |
| 6.4 | src/Mod/Sketcher/Gui/EditModeCoinManagerParameters.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.5 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.2 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.2 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 2.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 2.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.0 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.0 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 1.9 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 1.9 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.6 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.2 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 1.0 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.8 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.8 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.8 | QList<App::SubObjectT>::push_front |
| 0.8 | QList<App::SubObjectT>::prepend |
| 0.8 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.8 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.8 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.8 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 46.3 | src/Mod/Sketcher/App/SketchObject.h |
| 31.9 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 22.5 | src/Mod/Sketcher/App/Sketch.h |
| 21.2 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.3 | src/Mod/Part/App/PartFeature.h |
| 15.5 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 14.1 | src/Mod/Part/Gui/ViewProvider.h |
| 14.0 | src/Mod/Part/Gui/ViewProviderExt.h |
| 13.0 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 12.7 | src/Mod/Part/App/AttachExtension.h |
| 12.6 | src/Mod/Part/App/Attacher.h |
| 12.2 | src/Mod/Part/App/Part2DObject.h |
| 12.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 12.0 | src/App/DocumentObject.h |
| 10.5 | src/App/Document.h |
| 10.2 | src/Gui/CommandT.h |
| 9.7 | src/Mod/Part/App/Geometry.h |
| 8.6 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.1 | src/Mod/Material/App/PropertyMaterial.h |
| 7.7 | src/Mod/Part/App/TopoShape.h |
| 7.4 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 6.9 | src/App/Application.h |
| 6.7 | src/Mod/Material/App/Materials.h |
| 6.5 | src/Mod/Part/Gui/SoFCShapeObject.h |
| 6.4 | src/Mod/Sketcher/Gui/EditModeCoinManagerParameters.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.5 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.5 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.2 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.2 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 2.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 2.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.0 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.0 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 1.9 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 1.9 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.6 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.3 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.2 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 1.0 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 0.8 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.8 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.8 | QList<App::SubObjectT>::push_front |
| 0.8 | QList<App::SubObjectT>::prepend |
| 0.8 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.8 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.8 | std::sort<QList<App::StringIDRef>::iterator> |
| 0.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |
| 0.8 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 23.6 s; compiler 23.5 s; frontend 10.5 s; backend 12.9 s.

Top included files:

* 1.25 s — src/Mod/Sketcher/App/SketchObject.h
* 0.93 s — src/Mod/Sketcher/App/Sketch.h
* 0.91 s — src/App/Datums.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.73 s — src/App/GeoFeature.h
* 0.73 s — src/App/DocumentObject.h
* 0.66 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.55 s — src/Mod/Part/App/DatumFeature.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.54 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h

Top template instantiations:

* 0.23 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.21 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.14 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerCircle, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<3, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 14.6 s; compiler 14.5 s; frontend 8.0 s; backend 6.4 s.

Top included files:

* 1.87 s — src/Mod/Sketcher/App/SketchObject.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.73 s — src/Gui/CommandT.h
* 0.64 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.60 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.58 s — src/App/Document.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.49 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.49 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 13.2 s; compiler 13.1 s; frontend 7.0 s; backend 6.0 s.

Top included files:

* 1.63 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.88 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.72 s — src/Gui/CommandT.h
* 0.60 s — src/App/Document.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.51 s — src/Mod/Part/App/Part2DObject.h
* 0.51 s — src/Mod/Part/App/AttachExtension.h
* 0.50 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 12.0 s; compiler 11.9 s; frontend 7.7 s; backend 4.1 s.

Top included files:

* 1.67 s — src/Mod/Sketcher/App/SketchObject.h
* 0.98 s — src/Mod/Sketcher/App/Sketch.h
* 0.94 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.78 s — src/Gui/CommandT.h
* 0.63 s — src/App/Document.h
* 0.55 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.55 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 0.53 s — src/Mod/Part/App/Part2DObject.h
* 0.53 s — src/Mod/Part/App/AttachExtension.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.12 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.12 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.07 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.05 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 10.1 s; compiler 10.0 s; frontend 6.0 s; backend 4.0 s.

Top included files:

* 1.61 s — src/Mod/Sketcher/App/SketchObject.h
* 0.99 s — src/Gui/CommandT.h
* 0.91 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.64 s — src/App/Transactions.h
* 0.64 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.62 s — src/App/Document.h
* 0.54 s — src/Mod/Part/App/Part2DObject.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.52 s — src/Mod/Part/App/Attacher.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, int, int &>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
