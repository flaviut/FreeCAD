# Clang build profile

* Recorded Ninja log timestamp span: 252.7 s (145–252883 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 515; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 1774.8 | 0.0 | 1774.8 |
| Frontend | 1199.5 | 0.0 | 1199.5 |
| Backend | 558.0 | 0.0 | 558.0 |
| Source | 810.8 | 0.0 | 810.8 |
| InstantiateFunction | 426.5 | 0.0 | 426.5 |
| InstantiateClass | 401.2 | 0.0 | 401.2 |
| Optimizer | 353.1 | 0.0 | 353.1 |
| CodeGenPasses | 203.8 | 0.0 | 203.8 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 22.4 | 22.2 | 10.1 | 12.0 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 15.3 | 15.2 | 5.7 | 9.4 | 2.3 | src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o |
| 13.9 | 13.8 | 7.9 | 5.8 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 12.5 | 12.4 | 6.8 | 5.6 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 12.2 | 12.1 | 8.4 | 3.6 | 6.1 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 11.9 | 11.8 | 7.5 | 4.1 | 4.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 11.1 | 11.0 | 4.5 | 6.4 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o |
| 10.4 | 10.3 | 3.7 | 6.5 | 1.9 | src/App/CMakeFiles/FreeCADApp.dir/Application.cpp.o |
| 10.3 | 10.2 | 4.9 | 5.2 | 3.1 | src/Gui/CMakeFiles/FreeCADGui.dir/MainWindow.cpp.o |
| 10.0 | 9.9 | 4.7 | 5.2 | 2.6 | src/Gui/CMakeFiles/FreeCADGui.dir/Application.cpp.o |
| 9.8 | 9.7 | 5.8 | 3.8 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 9.7 | 9.6 | 4.5 | 5.0 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/Tree.cpp.o |
| 9.4 | 9.3 | 4.8 | 4.5 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 9.4 | 9.3 | 3.6 | 5.6 | 1.8 | src/Gui/CMakeFiles/FreeCADGui.dir/Dialogs/DlgExpressionInput.cpp.o |
| 9.3 | 9.2 | 4.5 | 4.6 | 2.6 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgPrimitives.cpp.o |
| 9.3 | 9.2 | 3.5 | 5.6 | 1.9 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 8.8 | 8.8 | 3.3 | 5.4 | 1.7 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.8 | 8.7 | 6.0 | 2.6 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 8.7 | 8.6 | 4.2 | 4.3 | 2.3 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/PythonConverter.cpp.o |
| 8.6 | 8.5 | 3.2 | 5.3 | 1.2 | src/App/CMakeFiles/FreeCADApp.dir/PropertyLinks.cpp.o |
| 8.6 | 8.5 | 5.9 | 2.5 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.5 | 8.4 | 5.2 | 3.2 | 4.0 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/AppPartGui.cpp.o |
| 8.5 | 8.4 | 4.2 | 4.1 | 2.9 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/Command.cpp.o |
| 8.5 | 8.4 | 6.0 | 2.3 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 8.5 | 8.4 | 4.5 | 3.9 | 2.6 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/SketchObjectExternal.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 662.6 | 200 |
| src/Gui | 533.6 | 191 |
| Mod/Sketcher | 332.7 | 52 |
| Mod/Material | 140.3 | 45 |
| src/App | 105.6 | 27 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 137.4 | src/Mod/Part/App/PartFeature.h |
| 117.3 | src/App/DocumentObject.h |
| 107.4 | src/App/Application.h |
| 96.6 | src/Mod/Material/App/Materials.h |
| 92.3 | src/App/Document.h |
| 88.4 | src/Mod/Material/App/PropertyMaterial.h |
| 82.8 | src/App/ComplexGeoData.h |
| 58.9 | src/Mod/Sketcher/App/SketchObject.h |
| 57.6 | src/App/MappedName.h |
| 52.3 | src/App/PropertyStandard.h |
| 50.7 | src/Gui/Application.h |
| 49.9 | src/Mod/Part/Gui/ViewProviderExt.h |
| 49.6 | src/Mod/Part/App/AttachExtension.h |
| 49.4 | src/App/PropertyLinks.h |
| 49.4 | src/Mod/Part/App/Attacher.h |
| 48.5 | src/Mod/Part/App/TopoShape.h |
| 47.7 | src/Gui/MetaTypes.h |
| 46.8 | src/Mod/Material/App/MaterialValue.h |
| 43.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 42.3 | src/Mod/Part/Gui/ViewProvider.h |
| 41.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.5 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 39.3 | src/App/PropertyExpressionEngine.h |
| 38.8 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 38.0 | src/Mod/Part/App/PropertyTopoShape.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 24.1 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 24.1 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 22.4 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 22.4 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 18.1 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 18.1 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 14.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 14.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 13.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 13.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 11.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 8.7 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 8.7 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 8.6 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 8.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 7.8 | std::unique_ptr<Base::Exception> |
| 7.7 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 7.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 6.9 | std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>> |
| 6.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 6.9 | std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>> |
| 6.6 | std::vector<Base::Vector2d>::operator= |
| 6.5 | std::unique_ptr<App::DynamicProperty::Impl> |
| 6.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 5.9 | QList<App::SubObjectT>::push_front |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 137.4 | src/Mod/Part/App/PartFeature.h |
| 117.3 | src/App/DocumentObject.h |
| 107.4 | src/App/Application.h |
| 96.6 | src/Mod/Material/App/Materials.h |
| 92.3 | src/App/Document.h |
| 88.4 | src/Mod/Material/App/PropertyMaterial.h |
| 82.8 | src/App/ComplexGeoData.h |
| 58.9 | src/Mod/Sketcher/App/SketchObject.h |
| 57.6 | src/App/MappedName.h |
| 52.3 | src/App/PropertyStandard.h |
| 50.7 | src/Gui/Application.h |
| 49.9 | src/Mod/Part/Gui/ViewProviderExt.h |
| 49.6 | src/Mod/Part/App/AttachExtension.h |
| 49.4 | src/App/PropertyLinks.h |
| 49.4 | src/Mod/Part/App/Attacher.h |
| 48.5 | src/Mod/Part/App/TopoShape.h |
| 47.7 | src/Gui/MetaTypes.h |
| 46.8 | src/Mod/Material/App/MaterialValue.h |
| 43.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 42.3 | src/Mod/Part/Gui/ViewProvider.h |
| 41.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.5 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 39.3 | src/App/PropertyExpressionEngine.h |
| 38.8 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 38.0 | src/Mod/Part/App/PropertyTopoShape.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 24.1 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 24.1 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 22.4 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 22.4 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 18.1 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 18.1 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 14.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 14.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 13.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 13.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 11.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 8.7 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 8.7 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 8.6 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 8.5 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 7.8 | std::unique_ptr<Base::Exception> |
| 7.7 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 7.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 6.9 | std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>> |
| 6.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 6.9 | std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>> |
| 6.6 | std::vector<Base::Vector2d>::operator= |
| 6.5 | std::unique_ptr<App::DynamicProperty::Impl> |
| 6.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 5.9 | QList<App::SubObjectT>::push_front |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 22.4 s; compiler 22.2 s; frontend 10.1 s; backend 12.0 s.

Top included files:

* 1.21 s — src/Mod/Sketcher/App/SketchObject.h
* 0.89 s — src/Mod/Sketcher/App/Sketch.h
* 0.89 s — src/App/Datums.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.72 s — src/App/GeoFeature.h
* 0.72 s — src/App/DocumentObject.h
* 0.66 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.54 s — src/Mod/Part/App/DatumFeature.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.52 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.13 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerCircle, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<3, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o

Ninja 15.3 s; compiler 15.2 s; frontend 5.7 s; backend 9.4 s.

Top included files:

* 0.58 s — build/clang-profile/src/App/DocumentPy.h
* 0.41 s — src/App/Document.h
* 0.38 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/strong_components.hpp
* 0.33 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp
* 0.32 s — src/App/private/DocumentP.h
* 0.18 s — src/Base/UnitsApi.h
* 0.17 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/named_function_params.hpp
* 0.16 s — src/App/ExportInfo.h
* 0.16 s — src/App/DocumentObject.h
* 0.15 s — src/App/Application.h

Top template instantiations:

* 0.55 s — boost::basic_regex<char>::assign
* 0.27 s — boost::basic_regex<char>::set_expression
* 0.27 s — boost::basic_regex<char>::do_assign
* 0.27 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.24 s — boost::regex_search<const char *, std::allocator<boost::sub_match<const char *>>, char, boost::regex_traits<char>>
* 0.18 s — boost::bimaps::bimap<Base::Reference<App::StringHasher>, int>
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.13 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data
* 0.13 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 13.9 s; compiler 13.8 s; frontend 7.9 s; backend 5.8 s.

Top included files:

* 1.86 s — src/Mod/Sketcher/App/SketchObject.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.64 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.60 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.60 s — src/App/Document.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.49 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h
* 0.49 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 12.5 s; compiler 12.4 s; frontend 6.8 s; backend 5.6 s.

Top included files:

* 1.61 s — src/Mod/Sketcher/App/SketchObject.h
* 0.89 s — src/Mod/Sketcher/App/Sketch.h
* 0.85 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.69 s — src/Gui/CommandT.h
* 0.57 s — src/App/Document.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.55 s — src/Mod/Part/App/Part2DObject.h
* 0.54 s — src/Mod/Part/App/AttachExtension.h
* 0.53 s — src/Mod/Part/App/Attacher.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

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
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 12.2 s; compiler 12.1 s; frontend 8.4 s; backend 3.6 s.

Top included files:

* 3.82 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.82 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.81 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.78 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.75 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.18 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.18 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.17 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.11 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.21 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.21 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.20 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.20 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.20 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.20 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.20 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.20 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.20 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.18 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
