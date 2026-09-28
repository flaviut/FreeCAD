# Clang build profile

* Recorded Ninja log timestamp span: 235.0 s (131–235089 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 500; PCH jobs with traces: 0.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 1648.2 | 0.0 | 1648.2 |
| Frontend | 1090.1 | 0.0 | 1090.1 |
| Backend | 541.9 | 0.0 | 541.9 |
| Source | 767.9 | 0.0 | 767.9 |
| InstantiateFunction | 353.6 | 0.0 | 353.6 |
| InstantiateClass | 365.0 | 0.0 | 365.0 |
| Optimizer | 342.6 | 0.0 | 342.6 |
| CodeGenPasses | 198.1 | 0.0 | 198.1 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 22.6 | 22.5 | 10.3 | 12.1 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 15.1 | 15.0 | 5.7 | 9.3 | 2.3 | src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o |
| 13.5 | 13.4 | 7.8 | 5.5 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 12.4 | 12.3 | 6.8 | 5.5 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 11.6 | 11.5 | 8.0 | 3.5 | 5.9 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 11.5 | 11.4 | 7.2 | 4.2 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 10.9 | 10.8 | 4.5 | 6.3 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/propertyeditor/PropertyItem.cpp.o |
| 10.2 | 10.1 | 4.9 | 5.1 | 3.1 | src/Gui/CMakeFiles/FreeCADGui.dir/MainWindow.cpp.o |
| 10.1 | 10.1 | 3.7 | 6.3 | 2.0 | src/App/CMakeFiles/FreeCADApp.dir/Application.cpp.o |
| 10.1 | 10.0 | 4.8 | 5.2 | 2.7 | src/Gui/CMakeFiles/FreeCADGui.dir/Application.cpp.o |
| 9.5 | 9.5 | 4.6 | 4.8 | 2.6 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/DlgPrimitives.cpp.o |
| 9.3 | 9.2 | 4.2 | 5.0 | 1.6 | src/Gui/CMakeFiles/FreeCADGui.dir/Tree.cpp.o |
| 9.3 | 9.2 | 3.5 | 5.6 | 1.8 | src/Gui/CMakeFiles/FreeCADGui.dir/Dialogs/DlgExpressionInput.cpp.o |
| 9.3 | 9.2 | 5.4 | 3.7 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 9.1 | 9.0 | 3.4 | 5.5 | 1.8 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 9.0 | 8.9 | 4.4 | 4.5 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 8.7 | 8.6 | 6.0 | 2.6 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.7 | 8.7 | 3.3 | 5.4 | 1.7 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 8.6 | 8.5 | 5.2 | 3.3 | 4.0 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/AppPartGui.cpp.o |
| 8.4 | 8.3 | 5.7 | 2.5 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 8.4 | 8.3 | 3.0 | 5.2 | 1.1 | src/App/CMakeFiles/FreeCADApp.dir/PropertyLinks.cpp.o |
| 8.2 | 8.1 | 3.5 | 4.6 | 1.8 | src/Gui/CMakeFiles/FreeCADGui.dir/CommandDoc.cpp.o |
| 8.2 | 8.1 | 4.0 | 4.0 | 2.7 | src/Mod/Part/Gui/CMakeFiles/PartGui.dir/Command.cpp.o |
| 8.2 | 8.1 | 3.8 | 4.2 | 2.3 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/PythonConverter.cpp.o |
| 8.1 | 8.0 | 4.1 | 3.8 | 2.7 | src/Mod/Sketcher/App/CMakeFiles/Sketcher.dir/SketchObjectExternal.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 613.8 | 200 |
| src/Gui | 526.8 | 191 |
| Mod/Sketcher | 315.7 | 52 |
| src/App | 105.3 | 27 |
| Mod/Material | 86.7 | 30 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 124.2 | src/Mod/Part/App/PartFeature.h |
| 103.9 | src/App/Application.h |
| 102.0 | src/App/DocumentObject.h |
| 94.8 | src/App/ComplexGeoData.h |
| 91.1 | src/App/Document.h |
| 64.0 | src/Mod/Material/App/PropertyMaterial.h |
| 60.7 | src/Mod/Part/App/TopoShape.h |
| 60.1 | src/Mod/Material/App/Materials.h |
| 57.3 | src/App/MappedName.h |
| 57.1 | src/Mod/Sketcher/App/SketchObject.h |
| 50.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 50.1 | src/Gui/Application.h |
| 47.1 | src/App/PropertyStandard.h |
| 46.9 | src/Mod/Part/App/AttachExtension.h |
| 46.6 | src/Mod/Part/Gui/ViewProviderExt.h |
| 46.4 | src/Mod/Part/App/Attacher.h |
| 44.7 | src/App/PropertyLinks.h |
| 41.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 40.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.7 | src/Mod/Part/Gui/ViewProvider.h |
| 39.3 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 38.6 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 35.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 35.4 | src/App/ElementMap.h |
| 33.8 | src/App/PropertyExpressionEngine.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 8.9 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 8.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 8.2 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 8.2 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 7.8 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 7.5 | std::unique_ptr<Base::Exception> |
| 7.4 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 7.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 6.7 | std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>> |
| 6.7 | std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>> |
| 6.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 6.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 6.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 6.1 | std::vector<Base::Vector2d>::operator= |
| 6.0 | std::unique_ptr<App::DynamicProperty::Impl> |
| 5.6 | Gui::StyleParameters::Diagnostics::report<const char *, std::basic_string<char>> |
| 5.5 | std::format<const char *, std::basic_string<char>> |
| 5.5 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 5.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 5.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 5.1 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 5.0 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 5.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 4.9 | std::sort<QList<App::StringIDRef>::iterator> |
| 4.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 124.2 | src/Mod/Part/App/PartFeature.h |
| 103.9 | src/App/Application.h |
| 102.0 | src/App/DocumentObject.h |
| 94.8 | src/App/ComplexGeoData.h |
| 91.1 | src/App/Document.h |
| 64.0 | src/Mod/Material/App/PropertyMaterial.h |
| 60.7 | src/Mod/Part/App/TopoShape.h |
| 60.1 | src/Mod/Material/App/Materials.h |
| 57.3 | src/App/MappedName.h |
| 57.1 | src/Mod/Sketcher/App/SketchObject.h |
| 50.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 50.1 | src/Gui/Application.h |
| 47.1 | src/App/PropertyStandard.h |
| 46.9 | src/Mod/Part/App/AttachExtension.h |
| 46.6 | src/Mod/Part/Gui/ViewProviderExt.h |
| 46.4 | src/Mod/Part/App/Attacher.h |
| 44.7 | src/App/PropertyLinks.h |
| 41.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 40.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 39.7 | src/Mod/Part/Gui/ViewProvider.h |
| 39.3 | build/clang-profile/src/Mod/Part/App/TopoShapePy.h |
| 38.6 | build/clang-profile/src/App/ComplexGeoDataPy.h |
| 35.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 35.4 | src/App/ElementMap.h |
| 33.8 | src/App/PropertyExpressionEngine.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 8.9 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 8.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 8.2 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 8.2 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 7.8 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 7.5 | std::unique_ptr<Base::Exception> |
| 7.4 | std::vector<std::basic_string<char>>::vector<__gnu_cxx::__normal_iterator<char *const *, std::vector<char *>>, void> |
| 7.2 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 6.7 | std::__uniq_ptr_data<Base::Exception, std::default_delete<Base::Exception>> |
| 6.7 | std::__uniq_ptr_impl<Base::Exception, std::default_delete<Base::Exception>> |
| 6.6 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 6.6 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 6.2 | Gui::StyleParameters::Value::get<Gui::StyleParameters::Tuple> |
| 6.1 | std::vector<Base::Vector2d>::operator= |
| 6.0 | std::unique_ptr<App::DynamicProperty::Impl> |
| 5.6 | Gui::StyleParameters::Diagnostics::report<const char *, std::basic_string<char>> |
| 5.5 | std::format<const char *, std::basic_string<char>> |
| 5.5 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 5.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 5.4 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 5.1 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 5.0 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 5.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 4.9 | std::sort<QList<App::StringIDRef>::iterator> |
| 4.8 | std::__sort<QList<App::StringIDRef>::iterator, __gnu_cxx::__ops::_Iter_less_iter> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 22.6 s; compiler 22.5 s; frontend 10.3 s; backend 12.1 s.

Top included files:

* 1.24 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.85 s — src/App/Datums.h
* 0.68 s — src/App/GeoFeature.h
* 0.67 s — src/App/DocumentObject.h
* 0.66 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.58 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.49 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.23 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.13 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerCircle, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<3, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/App/CMakeFiles/FreeCADApp.dir/Document.cpp.o

Ninja 15.1 s; compiler 15.0 s; frontend 5.7 s; backend 9.3 s.

Top included files:

* 0.59 s — build/clang-profile/src/App/DocumentPy.h
* 0.42 s — src/App/Document.h
* 0.36 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/strong_components.hpp
* 0.33 s — src/App/private/DocumentP.h
* 0.32 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/depth_first_search.hpp
* 0.18 s — src/Base/UnitsApi.h
* 0.17 s — src/App/ExportInfo.h
* 0.17 s — src/App/DocumentObject.h
* 0.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/graph/named_function_params.hpp
* 0.15 s — src/App/Application.h

Top template instantiations:

* 0.55 s — boost::basic_regex<char>::assign
* 0.27 s — boost::basic_regex<char>::set_expression
* 0.27 s — boost::basic_regex<char>::do_assign
* 0.27 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.23 s — boost::regex_search<const char *, std::allocator<boost::sub_match<const char *>>, char, boost::regex_traits<char>>
* 0.19 s — boost::bimaps::bimap<Base::Reference<App::StringHasher>, int>
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.13 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.13 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 13.5 s; compiler 13.4 s; frontend 7.8 s; backend 5.5 s.

Top included files:

* 1.77 s — src/Mod/Sketcher/App/SketchObject.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.64 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.63 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.60 s — src/App/Document.h
* 0.53 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.49 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core

Top template instantiations:

* 0.19 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.19 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 12.4 s; compiler 12.3 s; frontend 6.8 s; backend 5.5 s.

Top included files:

* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 0.93 s — src/Mod/Sketcher/App/Sketch.h
* 0.90 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.67 s — src/Gui/CommandT.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.56 s — src/App/Document.h
* 0.55 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.50 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.46 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 11.6 s; compiler 11.5 s; frontend 8.0 s; backend 3.5 s.

Top included files:

* 3.82 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.82 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.82 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.79 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.76 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.17 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.15 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.18 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.18 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.18 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.17 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.16 s — boost::detail::variant::visitation_impl_invoke<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
