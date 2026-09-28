# Clang build profile

* Recorded Ninja log timestamp span: 48.1 s (138–48258 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 52; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 280.4 | 6.9 | 287.3 |
| Frontend | 197.8 | 5.8 | 203.6 |
| Backend | 80.6 | 0.0 | 80.6 |
| Source | 139.4 | 0.0 | 139.4 |
| InstantiateFunction | 67.0 | 1.0 | 67.9 |
| InstantiateClass | 61.4 | 1.2 | 62.6 |
| Optimizer | 50.1 | 0.0 | 50.1 |
| CodeGenPasses | 30.3 | 0.0 | 30.3 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 22.5 | 22.4 | 10.1 | 12.2 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 13.8 | 13.7 | 7.9 | 5.8 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 12.3 | 12.2 | 6.7 | 5.4 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 12.1 | 12.0 | 7.6 | 4.3 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 9.7 | 9.6 | 5.7 | 3.8 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 9.4 | 9.3 | 4.7 | 4.5 | 3.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 8.9 | 8.8 | 6.1 | 2.6 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 8.8 | 8.7 | 6.0 | 2.6 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 8.6 | 8.5 | 5.1 | 3.3 | 3.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 8.4 | 8.3 | 6.0 | 2.3 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 8.1 | 8.0 | 4.5 | 3.5 | 3.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 7.8 | 7.7 | 5.6 | 2.0 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 7.6 | 7.5 | 5.8 | 1.7 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 7.5 | 7.4 | 4.3 | 3.1 | 3.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 7.0 | 6.9 | 5.2 | 1.7 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 7.0 | 6.9 | 4.1 | 2.8 | 3.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 7.0 | 6.9 | 5.3 | 1.5 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 6.9 | 6.8 | 5.3 | 1.4 | 4.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |
| 6.7 | 6.7 | 5.2 | 1.4 | 4.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 6.7 | 6.6 | 4.6 | 2.0 | 2.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeCoinManager.cpp.o |
| 6.5 | 6.4 | 4.7 | 1.6 | 3.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |
| 6.4 | 6.3 | 5.0 | 1.3 | 3.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeGeometryCoinConverter.cpp.o |
| 6.0 | 5.9 | 4.8 | 1.1 | 3.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandlerDragAutoConstraint.cpp.o |
| 5.9 | 5.8 | 5.3 | 0.5 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |
| 5.8 | 5.7 | 2.5 | 3.1 | 1.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/PropertyConstraintListItem.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 7.0 | 6.9 | 5.8 | 0.0 | 0.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 280.4 | 52 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 46.8 | src/Mod/Sketcher/App/SketchObject.h |
| 30.8 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 22.5 | src/Mod/Sketcher/App/Sketch.h |
| 21.2 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.2 | src/Mod/Part/App/PartFeature.h |
| 15.3 | src/App/DocumentObject.h |
| 14.8 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 13.4 | src/Mod/Part/Gui/ViewProvider.h |
| 13.4 | src/Mod/Part/Gui/ViewProviderExt.h |
| 13.0 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 12.9 | src/Mod/Part/App/AttachExtension.h |
| 12.8 | src/Mod/Part/App/Attacher.h |
| 12.4 | src/Mod/Part/App/Part2DObject.h |
| 12.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 11.4 | src/Mod/Part/App/Geometry.h |
| 10.0 | src/App/Document.h |
| 9.7 | src/Gui/CommandT.h |
| 8.5 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.1 | src/Mod/Material/App/PropertyMaterial.h |
| 8.0 | src/App/Application.h |
| 7.7 | src/Mod/Part/App/TopoShape.h |
| 7.2 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 6.7 | src/Mod/Material/App/Materials.h |
| 6.6 | src/Gui/Application.h |
| 6.5 | src/App/PropertyStandard.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.9 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.6 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.6 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 3.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 3.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 2.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 2.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.8 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.5 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.4 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 1.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.9 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.9 | QList<App::SubObjectT>::push_front |
| 0.9 | QList<App::SubObjectT>::prepend |
| 0.9 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.9 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.9 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 0.8 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 0.8 | qRegisterNormalizedMetaType<Base::Vector3<float>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 5.2 | build/clang-profile/src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx |
| 5.2 | src/Mod/Sketcher/Gui/PreCompiled.h |
| 2.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 1.0 | src/Gui/QtAll.h |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstractanimation.h |
| 0.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 0.4 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/QAbstractTextDocumentLayout |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qabstracttextdocumentlayout.h |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/math/special_functions/fpclassify.hpp |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qtextlayout.h |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/math/special_functions/math_fwd.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/math/tools/complex.hpp |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/complex |
| 0.2 | src/Gui/InventorAll.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/sstream |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstractitemmodel.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/q20chrono.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.1 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::formatter<wchar_t, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::__formatter_int<wchar_t>::format<unsigned int, std::__format::_Sink_iter<wchar_t>> |
| 0.0 | qvariant_cast<Qt::CheckState> |
| 0.0 | std::unique_ptr<QJsonDocumentPrivate> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | QExplicitlySharedDataPointer<QPageLayoutPrivate> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 46.8 | src/Mod/Sketcher/App/SketchObject.h |
| 30.8 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 22.5 | src/Mod/Sketcher/App/Sketch.h |
| 21.2 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.2 | src/Mod/Part/App/PartFeature.h |
| 15.3 | src/App/DocumentObject.h |
| 14.8 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 13.4 | src/Mod/Part/Gui/ViewProvider.h |
| 13.4 | src/Mod/Part/Gui/ViewProviderExt.h |
| 13.0 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 12.9 | src/Mod/Part/App/AttachExtension.h |
| 12.8 | src/Mod/Part/App/Attacher.h |
| 12.4 | src/Mod/Part/App/Part2DObject.h |
| 12.1 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 11.4 | src/Mod/Part/App/Geometry.h |
| 10.0 | src/App/Document.h |
| 9.7 | src/Gui/CommandT.h |
| 8.5 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.1 | src/Mod/Material/App/PropertyMaterial.h |
| 8.0 | src/App/Application.h |
| 7.7 | src/Mod/Part/App/TopoShape.h |
| 7.2 | src/Mod/Sketcher/Gui/EditModeCoinManager.h |
| 6.7 | src/Mod/Material/App/Materials.h |
| 6.6 | src/Gui/Application.h |
| 6.5 | src/App/PropertyStandard.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.9 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.6 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.6 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 3.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 3.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 2.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 2.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.8 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.5 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.4 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 1.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.9 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.9 | QList<App::SubObjectT>::push_front |
| 0.9 | QList<App::SubObjectT>::prepend |
| 0.9 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.9 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.9 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 0.8 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 0.8 | qRegisterNormalizedMetaType<Base::Vector3<float>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 22.5 s; compiler 22.4 s; frontend 10.1 s; backend 12.2 s.

Top included files:

* 1.23 s — src/Mod/Sketcher/App/SketchObject.h
* 0.92 s — src/Mod/Sketcher/App/Sketch.h
* 0.88 s — src/App/Datums.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.71 s — src/App/GeoFeature.h
* 0.70 s — src/App/DocumentObject.h
* 0.67 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.54 s — src/Mod/Part/App/DatumFeature.h
* 0.53 s — src/Mod/Part/App/AttachExtension.h
* 0.53 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.22 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.21 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.18 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.17 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.13 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRectangle, SketcherGui::StateMachines::FiveSeekEnd, 3, SketcherGui::OnViewParameters<6, 6, 8, 8>, SketcherGui::WidgetParameters<0, 0, 0, 0>, SketcherGui::WidgetCheckboxes<2, 2, 2, 2>, SketcherGui::WidgetComboboxes<1, 1, 1, 1>, SketcherGui::WidgetLineEdits<0, 0, 0, 0>, SketcherGui::ConstructionMethods::RectangleConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 13.8 s; compiler 13.7 s; frontend 7.9 s; backend 5.8 s.

Top included files:

* 1.85 s — src/Mod/Sketcher/App/SketchObject.h
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.77 s — src/Gui/CommandT.h
* 0.63 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.61 s — src/App/Document.h
* 0.60 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.48 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core
* 0.48 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h

Top template instantiations:

* 0.20 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.16 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 12.3 s; compiler 12.2 s; frontend 6.7 s; backend 5.4 s.

Top included files:

* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 0.89 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.68 s — src/Gui/CommandT.h
* 0.57 s — src/App/Document.h
* 0.56 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.50 s — src/Mod/Part/App/Part2DObject.h
* 0.50 s — src/Mod/Part/App/AttachExtension.h
* 0.50 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 12.1 s; compiler 12.0 s; frontend 7.6 s; backend 4.3 s.

Top included files:

* 1.63 s — src/Mod/Sketcher/App/SketchObject.h
* 0.94 s — src/Mod/Sketcher/App/Sketch.h
* 0.90 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.76 s — src/Gui/CommandT.h
* 0.62 s — src/App/Document.h
* 0.55 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.53 s — src/Mod/Part/App/Part2DObject.h
* 0.52 s — src/Mod/Part/App/AttachExtension.h
* 0.51 s — src/Mod/Part/App/Attacher.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — boost::basic_format<char>::basic_format

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 9.7 s; compiler 9.6 s; frontend 5.7 s; backend 3.8 s.

Top included files:

* 1.52 s — src/Mod/Sketcher/App/SketchObject.h
* 0.89 s — src/Gui/CommandT.h
* 0.87 s — src/Mod/Sketcher/App/Sketch.h
* 0.84 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.64 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 0.60 s — src/App/Transactions.h
* 0.56 s — src/App/Document.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR
* 0.50 s — src/Mod/Part/App/Part2DObject.h
* 0.49 s — src/Mod/Part/App/AttachExtension.h

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — Gui::cmdAppObjectArgs<int &, int, int &>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
