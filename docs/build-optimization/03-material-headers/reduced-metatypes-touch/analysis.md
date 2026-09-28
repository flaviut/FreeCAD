# Clang build profile

* Recorded Ninja log timestamp span: 103.5 s (133–103589 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 152; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 614.2 | 0.0 | 614.2 |
| Frontend | 382.5 | 0.0 | 382.5 |
| Backend | 226.5 | 0.0 | 226.5 |
| Source | 238.2 | 0.0 | 238.2 |
| InstantiateFunction | 155.2 | 0.0 | 155.2 |
| InstantiateClass | 133.3 | 0.0 | 133.3 |
| Optimizer | 142.4 | 0.0 | 142.4 |
| CodeGenPasses | 83.8 | 0.0 | 83.8 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 21.8 | 21.6 | 10.1 | 11.5 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 14.1 | 14.0 | 7.9 | 6.0 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 12.6 | 12.5 | 6.9 | 5.6 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 11.0 | 10.9 | 4.4 | 6.5 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o |
| 9.9 | 9.9 | 4.7 | 5.1 | 2.7 | src/Gui/CMakeFiles/FreeCADGui.dir/Application.cpp.o |
| 9.5 | 9.5 | 4.6 | 4.8 | 2.6 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgPrimitives.cpp.o |
| 9.2 | 9.1 | 3.5 | 5.6 | 1.7 | src/Gui/CMakeFiles/FreeCADGui.dir/Dialogs/DlgExpressionInput.cpp.o |
| 8.8 | 8.7 | 6.1 | 2.5 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.6 | 8.5 | 5.2 | 3.3 | 3.9 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/AppPartGui.cpp.o |
| 8.4 | 8.3 | 5.6 | 2.7 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 8.3 | 8.2 | 4.1 | 4.1 | 2.7 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/Command.cpp.o |
| 8.0 | 7.9 | 4.4 | 3.4 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 7.9 | 7.8 | 3.8 | 4.0 | 2.1 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgFilletEdges.cpp.o |
| 7.8 | 7.7 | 5.4 | 2.3 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 7.7 | 7.6 | 3.9 | 3.7 | 2.5 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgExtrusion.cpp.o |
| 7.6 | 7.6 | 3.6 | 4.0 | 1.7 | src/Gui/CMakeFiles/FreeCADGui.dir/Widgets.cpp.o |
| 7.6 | 7.5 | 3.8 | 3.6 | 2.5 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/SectionCutting.cpp.o |
| 7.6 | 7.5 | 4.4 | 3.1 | 3.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 7.4 | 7.3 | 5.6 | 1.6 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 7.3 | 7.2 | 3.8 | 3.3 | 2.6 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgRevolution.cpp.o |
| 7.1 | 7.1 | 3.2 | 3.8 | 2.0 | src/Gui/CMakeFiles/FreeCADGui.dir/PreferencePages/DlgSettingsGeneral.cpp.o |
| 7.1 | 7.0 | 3.0 | 3.9 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyEditor.cpp.o |
| 7.0 | 6.9 | 3.2 | 3.6 | 2.1 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/CommandSimple.cpp.o |
| 6.7 | 6.7 | 2.9 | 3.7 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/Dialogs/DlgAddProperty.cpp.o |
| 6.7 | 6.6 | 3.3 | 3.2 | 2.2 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/CrossSections.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| src/Gui | 223.4 | 62 |
| Mod/Part | 164.3 | 37 |
| Mod/Sketcher | 129.1 | 17 |
| Mod/Material | 97.4 | 36 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 48.7 | src/App/DocumentObject.h |
| 37.8 | src/Gui/MetaTypes.h |
| 31.4 | src/App/Document.h |
| 23.4 | src/Gui/PrefWidgets.h |
| 22.8 | src/App/Application.h |
| 21.2 | src/Gui/QuantitySpinBox.h |
| 20.1 | src/App/PropertyStandard.h |
| 17.5 | src/App/PropertyLinks.h |
| 17.1 | src/Mod/Sketcher/App/SketchObject.h |
| 16.8 | src/Gui/Application.h |
| 16.0 | src/App/PropertyExpressionEngine.h |
| 13.9 | src/Mod/Part/App/PartFeature.h |
| 12.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 12.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 12.1 | src/Gui/propertyeditor/PropertyItem.h |
| 11.1 | src/Gui/Selection/Selection.h |
| 9.2 | src/Mod/Sketcher/App/Sketch.h |
| 9.0 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 8.7 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 8.4 | src/App/PropertyGeo.h |
| 8.1 | src/Gui/StyleParameters/ParameterManager.h |
| 7.9 | src/Mod/Part/App/PropertyTopoShape.h |
| 7.7 | src/Mod/Part/App/Attacher.h |
| 7.6 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 7.5 | src/App/ExportInfo.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 12.2 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 12.1 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 11.1 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 11.1 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 9.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 9.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 7.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 7.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 6.5 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 6.5 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 5.7 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 4.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 4.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 4.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 3.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 3.2 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 2.9 | QList<App::SubObjectT>::push_front |
| 2.9 | QList<App::SubObjectT>::prepend |
| 2.9 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 2.9 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 2.8 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 2.6 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 2.6 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 2.5 | QArrayDataPointer<App::SubObjectT>::relocate |
| 2.3 | std::vector<Base::Vector2d>::operator= |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 48.7 | src/App/DocumentObject.h |
| 37.8 | src/Gui/MetaTypes.h |
| 31.4 | src/App/Document.h |
| 23.4 | src/Gui/PrefWidgets.h |
| 22.8 | src/App/Application.h |
| 21.2 | src/Gui/QuantitySpinBox.h |
| 20.1 | src/App/PropertyStandard.h |
| 17.5 | src/App/PropertyLinks.h |
| 17.1 | src/Mod/Sketcher/App/SketchObject.h |
| 16.8 | src/Gui/Application.h |
| 16.0 | src/App/PropertyExpressionEngine.h |
| 13.9 | src/Mod/Part/App/PartFeature.h |
| 12.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 12.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 12.1 | src/Gui/propertyeditor/PropertyItem.h |
| 11.1 | src/Gui/Selection/Selection.h |
| 9.2 | src/Mod/Sketcher/App/Sketch.h |
| 9.0 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 8.7 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 8.4 | src/App/PropertyGeo.h |
| 8.1 | src/Gui/StyleParameters/ParameterManager.h |
| 7.9 | src/Mod/Part/App/PropertyTopoShape.h |
| 7.7 | src/Mod/Part/App/Attacher.h |
| 7.6 | src/3rdParty/PyCXX/CXX/Objects.hxx |
| 7.5 | src/App/ExportInfo.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 12.2 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 12.1 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 11.1 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 11.1 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 9.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 9.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 7.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 7.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 6.5 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 6.5 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 5.7 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 4.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 4.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 4.3 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 3.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 3.2 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 2.9 | QList<App::SubObjectT>::push_front |
| 2.9 | QList<App::SubObjectT>::prepend |
| 2.9 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 2.9 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 2.8 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 2.6 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 2.6 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 2.5 | QArrayDataPointer<App::SubObjectT>::relocate |
| 2.3 | std::vector<Base::Vector2d>::operator= |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 21.8 s; compiler 21.6 s; frontend 10.1 s; backend 11.5 s.

Top included files:

* 1.24 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/App/Datums.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.70 s — src/App/GeoFeature.h
* 0.69 s — src/App/DocumentObject.h
* 0.65 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.58 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h
* 0.57 s — src/Mod/Part/App/DatumFeature.h
* 0.57 s — src/Mod/Part/App/AttachExtension.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.17 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.17 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerCircle, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<3, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 14.1 s; compiler 14.0 s; frontend 7.9 s; backend 6.0 s.

Top included files:

* 1.76 s — src/Mod/Sketcher/App/SketchObject.h
* 0.87 s — src/Mod/Sketcher/App/Sketch.h
* 0.83 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.73 s — src/Gui/CommandT.h
* 0.68 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.62 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.58 s — src/App/Document.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h
* 0.50 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.47 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.20 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 12.6 s; compiler 12.5 s; frontend 6.9 s; backend 5.6 s.

Top included files:

* 1.58 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.88 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.68 s — src/Gui/CommandT.h
* 0.56 s — src/App/Document.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.54 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.50 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.50 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.47 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o

Ninja 11.0 s; compiler 10.9 s; frontend 4.4 s; backend 6.5 s.

Top included files:

* 0.98 s — src/Gui/propertyeditor/PropertyItem.h
* 0.37 s — src/Gui/MetaTypes.h
* 0.32 s — build/clang-profile/src/Gui/FreeCADGui_autogen/include/moc_PropertyItem.cpp
* 0.26 s — src/App/DocumentObject.h
* 0.23 s — src/App/PropertyStandard.h
* 0.21 s — src/Base/UnitsApi.h
* 0.20 s — src/Gui/Command.h
* 0.19 s — src/Gui/Application.h
* 0.15 s — src/App/Document.h
* 0.13 s — src/Base/UnitsSchemasData.h

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

## src/Gui/CMakeFiles/FreeCADGui.dir/Application.cpp.o

Ninja 9.9 s; compiler 9.9 s; frontend 4.7 s; backend 5.1 s.

Top included files:

* 0.71 s — src/App/Document.h
* 0.37 s — build/clang-profile/src/Gui/LinkViewPy.h
* 0.37 s — src/Gui/ViewProviderLink.h
* 0.19 s — src/Gui/Application.h
* 0.18 s — src/Base/UnitsApi.h
* 0.17 s — src/App/ExportInfo.h
* 0.17 s — src/App/DocumentObject.h
* 0.16 s — src/Gui/ViewProviderVarSet.h
* 0.14 s — src/Gui/Dialogs/DlgAddProperty.h
* 0.14 s — src/App/Link.h

Top template instantiations:

* 0.11 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.05 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
