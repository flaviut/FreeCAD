# Clang build profile

* Recorded Ninja log timestamp span: 51.0 s (135–51164 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 52; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 324.0 | 5.8 | 329.9 |
| Frontend | 238.5 | 4.9 | 243.4 |
| Backend | 83.5 | 0.0 | 83.5 |
| Source | 178.9 | 0.0 | 178.9 |
| InstantiateFunction | 71.5 | 0.9 | 72.4 |
| InstantiateClass | 69.2 | 1.0 | 70.3 |
| Optimizer | 52.0 | 0.0 | 52.0 |
| CodeGenPasses | 31.3 | 0.0 | 31.3 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 24.4 | 24.3 | 11.5 | 12.6 | 6.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 15.7 | 15.6 | 9.3 | 6.2 | 6.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 13.6 | 13.5 | 7.9 | 5.6 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 13.3 | 13.2 | 8.8 | 4.4 | 5.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 11.2 | 11.2 | 7.2 | 3.9 | 5.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 10.9 | 10.8 | 6.2 | 4.6 | 4.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 10.5 | 10.4 | 7.6 | 2.7 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 10.1 | 10.1 | 7.3 | 2.7 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 9.9 | 9.8 | 7.4 | 2.3 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 9.7 | 9.6 | 6.2 | 3.3 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 9.3 | 9.2 | 5.9 | 3.3 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 9.2 | 9.1 | 5.6 | 3.4 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 8.9 | 8.8 | 6.7 | 2.0 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 8.8 | 8.7 | 5.6 | 3.1 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 8.6 | 8.5 | 6.7 | 1.7 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 8.5 | 8.4 | 6.5 | 1.9 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 8.4 | 8.3 | 6.7 | 1.5 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 8.3 | 8.2 | 6.6 | 1.5 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |
| 8.0 | 7.9 | 5.9 | 2.0 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeCoinManager.cpp.o |
| 8.0 | 7.9 | 6.3 | 1.5 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 7.6 | 7.5 | 6.2 | 1.3 | 4.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeGeometryCoinConverter.cpp.o |
| 7.3 | 7.2 | 6.6 | 0.5 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |
| 7.2 | 7.1 | 6.1 | 1.0 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SnapManager.cpp.o |
| 7.2 | 7.1 | 5.9 | 1.1 | 4.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandlerDragAutoConstraint.cpp.o |
| 6.7 | 6.6 | 4.9 | 1.7 | 3.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 5.9 | 5.8 | 4.9 | 0.0 | 0.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 324.0 | 52 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 67.7 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 48.5 | src/Mod/Sketcher/App/SketchObject.h |
| 35.9 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 35.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 22.2 | src/Mod/Sketcher/App/Sketch.h |
| 20.9 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.4 | src/Mod/Part/App/PartFeature.h |
| 15.4 | src/App/DocumentObject.h |
| 15.1 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 15.0 | src/Mod/Part/App/Geometry.h |
| 14.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 14.9 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 13.7 | src/Mod/Part/Gui/ViewProvider.h |
| 13.6 | src/Mod/Part/Gui/ViewProviderExt.h |
| 12.9 | src/Mod/Part/App/AttachExtension.h |
| 12.8 | src/Mod/Part/App/Attacher.h |
| 12.7 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 12.4 | src/Mod/Part/App/Part2DObject.h |
| 11.8 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 10.0 | src/App/Document.h |
| 9.7 | src/Gui/CommandT.h |
| 8.5 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.2 | src/Mod/Material/App/PropertyMaterial.h |
| 7.8 | src/App/Application.h |
| 7.7 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.9 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 3.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 3.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 2.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 2.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.4 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 0.9 | QList<App::SubObjectT>::push_front |
| 0.9 | QList<App::SubObjectT>::prepend |
| 0.9 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.9 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.9 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.9 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.9 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 0.8 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 0.8 | std::sort<QList<App::StringIDRef>::iterator> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 4.4 | build/clang-profile/src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx |
| 4.4 | src/Mod/Sketcher/Gui/PreCompiled.h |
| 2.9 | src/Gui/QtAll.h |
| 1.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QAbstractEventDispatcher |
| 1.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 1.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/math/special_functions/fpclassify.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/math/special_functions/math_fwd.hpp |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/QAbstractTextDocumentLayout |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qabstracttextdocumentlayout.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qtextlayout.h |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/math/tools/complex.hpp |
| 0.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/complex |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/sstream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QAbstractItemModel |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstractitemmodel.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.2 | src/Gui/InventorAll.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qlist.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |

## Template instantiations in PCH jobs

| Inclusive s | Template |
|---:|---|
| 0.1 | std::vformat_to<std::__format::_Sink_iter<char>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<char>, char, std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.1 | std::vformat_to<std::__format::_Sink_iter<wchar_t>> |
| 0.1 | std::__format::__do_vformat_to<std::__format::_Sink_iter<wchar_t>, wchar_t, std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::formatter<bool>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_int<char>::format<unsigned char, std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |
| 0.0 | std::chrono::hh_mm_ss<std::chrono::duration<long>>::hh_mm_ss |
| 0.0 | std::__format::_Buf_sink<wchar_t> |
| 0.0 | std::formatter<bool, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 67.7 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 48.5 | src/Mod/Sketcher/App/SketchObject.h |
| 35.9 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 35.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 22.2 | src/Mod/Sketcher/App/Sketch.h |
| 20.9 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.4 | src/Mod/Part/App/PartFeature.h |
| 15.4 | src/App/DocumentObject.h |
| 15.1 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 15.0 | src/Mod/Part/App/Geometry.h |
| 14.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 14.9 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 13.7 | src/Mod/Part/Gui/ViewProvider.h |
| 13.6 | src/Mod/Part/Gui/ViewProviderExt.h |
| 12.9 | src/Mod/Part/App/AttachExtension.h |
| 12.8 | src/Mod/Part/App/Attacher.h |
| 12.7 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 12.4 | src/Mod/Part/App/Part2DObject.h |
| 11.8 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 10.0 | src/App/Document.h |
| 9.7 | src/Gui/CommandT.h |
| 8.5 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.2 | src/Mod/Material/App/PropertyMaterial.h |
| 7.8 | src/App/Application.h |
| 7.7 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.9 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.9 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 3.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 3.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 2.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 2.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.4 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
| 1.4 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.2 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>::operator() |
| 1.1 | std::__detail::__variant::_Copy_assign_base<false, bool, long, unsigned long, double, std::basic_string<char>>::operator= |
| 0.9 | QList<App::SubObjectT>::push_front |
| 0.9 | QList<App::SubObjectT>::prepend |
| 0.9 | QList<App::SubObjectT>::emplaceFront<const App::SubObjectT &> |
| 0.9 | QtPrivate::QGenericArrayOps<App::SubObjectT>::emplace<const App::SubObjectT &> |
| 0.9 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 0.9 | std::__detail::__variant::_Copy_ctor_base<false, Gui::StyleParameters::Numeric, Base::Color, std::basic_string<char>, Gui::StyleParameters::Tuple>::_Copy_ctor_base |
| 0.9 | QArrayDataPointer<App::SubObjectT>::detachAndGrow |
| 0.8 | QArrayDataPointer<App::SubObjectT>::tryReadjustFreeSpace |
| 0.8 | std::sort<QList<App::StringIDRef>::iterator> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o

Ninja 24.4 s; compiler 24.3 s; frontend 11.5 s; backend 12.6 s.

Top included files:

* 1.74 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.25 s — src/Mod/Sketcher/App/SketchObject.h
* 1.10 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.09 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.94 s — src/Mod/Sketcher/App/Sketch.h
* 0.89 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.84 s — src/App/Datums.h
* 0.67 s — src/App/GeoFeature.h
* 0.66 s — src/App/DocumentObject.h
* 0.54 s — src/Mod/Part/App/DatumFeature.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.15 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerEllipse, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerEllipse, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 15.7 s; compiler 15.6 s; frontend 9.3 s; backend 6.2 s.

Top included files:

* 1.99 s — src/Mod/Sketcher/App/SketchObject.h
* 1.70 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.08 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.08 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.87 s — src/Mod/Sketcher/App/Sketch.h
* 0.83 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.63 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.60 s — src/App/Document.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.20 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.19 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.13 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.13 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerOffset, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<1, 1>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<2, 2>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::OffsetConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 13.6 s; compiler 13.5 s; frontend 7.9 s; backend 5.6 s.

Top included files:

* 1.62 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 1.56 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.08 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.08 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.85 s — src/Mod/Sketcher/App/Sketch.h
* 0.81 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.66 s — src/Gui/CommandT.h
* 0.55 s — src/App/Document.h
* 0.53 s — src/Mod/Part/App/Part2DObject.h

Top template instantiations:

* 0.11 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.07 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 13.3 s; compiler 13.2 s; frontend 8.8 s; backend 4.4 s.

Top included files:

* 1.67 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 1.60 s — src/Mod/Sketcher/App/SketchObject.h
* 1.53 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.12 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.12 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.93 s — src/Mod/Sketcher/App/Sketch.h
* 0.89 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.73 s — src/Gui/CommandT.h
* 0.60 s — src/App/Document.h
* 0.53 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.08 s — QObject::connect<void (QWindow::*)(QScreen *), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/ViewProviderSketch.cpp:4685:84)>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 11.2 s; compiler 11.2 s; frontend 7.2 s; backend 3.9 s.

Top included files:

* 1.75 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.58 s — src/Mod/Sketcher/App/SketchObject.h
* 1.12 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.12 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.95 s — src/Gui/CommandT.h
* 0.90 s — src/Mod/Sketcher/App/Sketch.h
* 0.86 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.60 s — src/App/Document.h
* 0.60 s — src/App/Transactions.h
* 0.52 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

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
