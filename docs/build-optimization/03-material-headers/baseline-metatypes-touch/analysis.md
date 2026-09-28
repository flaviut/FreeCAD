# Clang build profile

* Recorded Ninja log timestamp span: 180.4 s (132–180566 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 293; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 1232.5 | 0.0 | 1232.5 |
| Frontend | 867.7 | 0.0 | 867.7 |
| Backend | 353.9 | 0.0 | 353.9 |
| Source | 579.5 | 0.0 | 579.5 |
| InstantiateFunction | 337.1 | 0.0 | 337.1 |
| InstantiateClass | 292.5 | 0.0 | 292.5 |
| Optimizer | 223.6 | 0.0 | 223.6 |
| CodeGenPasses | 129.5 | 0.0 | 129.5 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 23.3 | 23.1 | 10.8 | 12.2 | 5.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 14.7 | 14.6 | 8.2 | 6.3 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 13.4 | 13.3 | 7.2 | 6.0 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 12.2 | 12.1 | 8.5 | 3.5 | 6.1 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 12.0 | 11.9 | 7.6 | 4.2 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 11.1 | 11.0 | 4.5 | 6.5 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o |
| 10.2 | 10.1 | 6.2 | 3.9 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 10.2 | 10.1 | 4.6 | 5.4 | 2.6 | src/Gui/CMakeFiles/FreeCADGui.dir/Application.cpp.o |
| 9.9 | 9.8 | 4.8 | 5.0 | 2.8 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgPrimitives.cpp.o |
| 9.7 | 9.6 | 5.0 | 4.6 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 9.3 | 9.2 | 3.6 | 5.6 | 1.7 | src/Gui/CMakeFiles/FreeCADGui.dir/Dialogs/DlgExpressionInput.cpp.o |
| 9.3 | 9.2 | 6.4 | 2.7 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 9.2 | 9.1 | 6.3 | 2.8 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.9 | 8.8 | 5.2 | 3.5 | 2.8 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/SketchObject.cpp.o |
| 8.8 | 8.7 | 5.3 | 3.3 | 4.1 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/AppPartGui.cpp.o |
| 8.7 | 8.6 | 5.2 | 3.4 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 8.7 | 8.6 | 4.6 | 3.9 | 2.8 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/SketchObjectExternal.cpp.o |
| 8.7 | 8.6 | 6.1 | 2.4 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 8.6 | 8.5 | 4.2 | 4.2 | 2.4 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/PythonConverter.cpp.o |
| 8.3 | 8.2 | 4.3 | 3.9 | 2.8 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/Command.cpp.o |
| 8.2 | 8.1 | 3.9 | 4.2 | 2.2 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgFilletEdges.cpp.o |
| 8.1 | 8.0 | 4.5 | 3.4 | 3.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 8.1 | 8.0 | 3.5 | 4.4 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/Widgets.cpp.o |
| 8.0 | 7.9 | 4.1 | 3.8 | 2.6 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgExtrusion.cpp.o |
| 8.0 | 7.9 | 4.5 | 3.3 | 3.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 510.2 | 129 |
| Mod/Sketcher | 341.8 | 50 |
| src/Gui | 227.0 | 62 |
| Mod/Material | 153.6 | 52 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 138.7 | src/Mod/Part/App/PartFeature.h |
| 99.2 | src/App/DocumentObject.h |
| 97.0 | src/Mod/Material/App/Materials.h |
| 88.9 | src/Mod/Material/App/PropertyMaterial.h |
| 61.5 | src/Gui/MetaTypes.h |
| 61.1 | src/Mod/Sketcher/App/SketchObject.h |
| 56.0 | src/App/Document.h |
| 55.1 | src/App/Application.h |
| 51.4 | src/Mod/Part/App/AttachExtension.h |
| 51.2 | src/Mod/Part/App/Attacher.h |
| 51.1 | src/Mod/Part/Gui/ViewProviderExt.h |
| 50.1 | src/Mod/Material/App/MaterialValue.h |
| 45.3 | src/App/PropertyStandard.h |
| 43.4 | src/Mod/Part/Gui/ViewProvider.h |
| 40.2 | src/App/PropertyLinks.h |
| 34.5 | src/App/PropertyExpressionEngine.h |
| 33.9 | src/Mod/Part/App/PropertyTopoShape.h |
| 31.7 | src/Mod/Part/App/TopoShape.h |
| 31.5 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 30.1 | src/Mod/Sketcher/App/Sketch.h |
| 28.0 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 28.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 27.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 27.5 | src/Mod/Part/App/Part2DObject.h |
| 25.0 | src/App/ComplexGeoData.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 27.4 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 27.4 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 25.5 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 25.5 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 20.4 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 20.4 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 16.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 16.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 15.0 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 15.0 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 13.0 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 9.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 9.8 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 9.8 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 7.8 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 6.8 | QList<App::SubObjectT>::push_front |
| 6.7 | QList<App::SubObjectT>::prepend |
| 6.7 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 6.7 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 6.6 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 6.3 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 6.1 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 5.7 | QArrayDataPointer<App::SubObjectT>::relocate |
| 5.3 | qRegisterNormalizedMetaType<Base::Vector3<float>> |
| 5.2 | qRegisterNormalizedMetaTypeImplementation<Base::Vector3<float>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 138.7 | src/Mod/Part/App/PartFeature.h |
| 99.2 | src/App/DocumentObject.h |
| 97.0 | src/Mod/Material/App/Materials.h |
| 88.9 | src/Mod/Material/App/PropertyMaterial.h |
| 61.5 | src/Gui/MetaTypes.h |
| 61.1 | src/Mod/Sketcher/App/SketchObject.h |
| 56.0 | src/App/Document.h |
| 55.1 | src/App/Application.h |
| 51.4 | src/Mod/Part/App/AttachExtension.h |
| 51.2 | src/Mod/Part/App/Attacher.h |
| 51.1 | src/Mod/Part/Gui/ViewProviderExt.h |
| 50.1 | src/Mod/Material/App/MaterialValue.h |
| 45.3 | src/App/PropertyStandard.h |
| 43.4 | src/Mod/Part/Gui/ViewProvider.h |
| 40.2 | src/App/PropertyLinks.h |
| 34.5 | src/App/PropertyExpressionEngine.h |
| 33.9 | src/Mod/Part/App/PropertyTopoShape.h |
| 31.7 | src/Mod/Part/App/TopoShape.h |
| 31.5 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 30.1 | src/Mod/Sketcher/App/Sketch.h |
| 28.0 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 28.0 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 27.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 27.5 | src/Mod/Part/App/Part2DObject.h |
| 25.0 | src/App/ComplexGeoData.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 27.4 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 27.4 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 25.5 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 25.5 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 20.4 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 20.4 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 16.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 16.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 15.0 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 15.0 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 13.0 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 9.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 9.8 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 9.8 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 7.8 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 6.8 | QList<App::SubObjectT>::push_front |
| 6.7 | QList<App::SubObjectT>::prepend |
| 6.7 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 6.7 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 6.6 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 6.3 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 6.1 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 5.7 | QArrayDataPointer<App::SubObjectT>::relocate |
| 5.3 | qRegisterNormalizedMetaType<Base::Vector3<float>> |
| 5.2 | qRegisterNormalizedMetaTypeImplementation<Base::Vector3<float>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 23.3 s; compiler 23.1 s; frontend 10.8 s; backend 12.2 s.

Top included files:

* 1.33 s — src/Mod/Sketcher/App/SketchObject.h
* 0.99 s — src/Mod/Sketcher/App/Sketch.h
* 0.93 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.90 s — src/App/Datums.h
* 0.73 s — src/App/GeoFeature.h
* 0.72 s — src/App/DocumentObject.h
* 0.67 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.58 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.57 s — src/Mod/Part/App/DatumFeature.h
* 0.57 s — src/Mod/Part/App/AttachExtension.h

Top template instantiations:

* 0.25 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.22 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.14 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerPolyLine, SketcherGui::StateMachines::TwoSeekEnd, 2, SketcherGui::OnViewParameters<4, 5>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<1, 1>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::PolyLineConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 14.7 s; compiler 14.6 s; frontend 8.2 s; backend 6.3 s.

Top included files:

* 1.94 s — src/Mod/Sketcher/App/SketchObject.h
* 0.94 s — src/Mod/Sketcher/App/Sketch.h
* 0.91 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.78 s — src/Gui/CommandT.h
* 0.67 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.64 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.61 s — src/App/Document.h
* 0.58 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.54 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.51 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h

Top template instantiations:

* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 13.4 s; compiler 13.3 s; frontend 7.2 s; backend 6.0 s.

Top included files:

* 1.71 s — src/Mod/Sketcher/App/SketchObject.h
* 0.96 s — src/Mod/Sketcher/App/Sketch.h
* 0.92 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.72 s — src/Gui/CommandT.h
* 0.60 s — src/App/Document.h
* 0.58 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.56 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.56 s — src/Mod/Part/App/Part2DObject.h
* 0.56 s — src/Mod/Part/App/AttachExtension.h
* 0.54 s — src/Mod/Part/App/Attacher.h

Top template instantiations:

* 0.12 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.12 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.07 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 12.2 s; compiler 12.1 s; frontend 8.5 s; backend 3.5 s.

Top included files:

* 3.89 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.89 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.89 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.86 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.83 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.17 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.17 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.15 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.20 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.20 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.19 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.19 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.19 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.19 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.19 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.19 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.19 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.17 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 12.0 s; compiler 11.9 s; frontend 7.6 s; backend 4.2 s.

Top included files:

* 1.63 s — src/Mod/Sketcher/App/SketchObject.h
* 0.95 s — src/Mod/Sketcher/App/Sketch.h
* 0.91 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.77 s — src/Gui/CommandT.h
* 0.63 s — src/App/Document.h
* 0.54 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 0.54 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.52 s — src/Mod/Part/App/Part2DObject.h
* 0.51 s — src/Mod/Part/App/AttachExtension.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

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
