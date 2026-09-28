# Clang build profile

* Recorded Ninja log timestamp span: 54.8 s (129–54940 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 52; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 319.1 | 5.7 | 324.9 |
| Frontend | 235.4 | 4.8 | 240.2 |
| Backend | 81.7 | 0.0 | 81.7 |
| Source | 176.3 | 0.0 | 176.3 |
| InstantiateFunction | 70.8 | 0.9 | 71.6 |
| InstantiateClass | 68.5 | 1.0 | 69.5 |
| Optimizer | 51.0 | 0.0 | 51.0 |
| CodeGenPasses | 30.6 | 0.0 | 30.6 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 24.2 | 24.1 | 11.7 | 12.3 | 6.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandCreateGeo.cpp.o |
| 15.2 | 15.1 | 9.3 | 5.8 | 6.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o |
| 13.9 | 13.8 | 8.1 | 5.7 | 5.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o |
| 13.2 | 13.1 | 8.7 | 4.3 | 5.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o |
| 11.3 | 11.2 | 7.2 | 4.0 | 5.8 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o |
| 10.8 | 10.6 | 6.0 | 4.6 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeConstraintCoinManager.cpp.o |
| 10.2 | 10.1 | 7.3 | 2.7 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherConstraints.cpp.o |
| 10.0 | 9.9 | 7.1 | 2.7 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Command.cpp.o |
| 9.5 | 9.5 | 6.2 | 3.2 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeInformationOverlayCoinConverter.cpp.o |
| 9.5 | 9.4 | 7.0 | 2.3 | 5.1 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherElements.cpp.o |
| 9.3 | 9.2 | 5.6 | 3.5 | 4.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SketcherToolDefaultWidget.cpp.o |
| 9.0 | 8.9 | 5.5 | 3.3 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/AppSketcherGui.cpp.o |
| 8.9 | 8.8 | 6.8 | 2.0 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandler.cpp.o |
| 8.5 | 8.4 | 6.5 | 1.9 | 5.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherBSpline.cpp.o |
| 8.4 | 8.3 | 6.6 | 1.6 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditDatumDialog.cpp.o |
| 8.3 | 8.2 | 5.4 | 2.8 | 4.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherTool.cpp.o |
| 8.2 | 8.1 | 6.6 | 1.5 | 5.4 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandAlterGeometry.cpp.o |
| 8.2 | 8.1 | 6.6 | 1.4 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherVirtualSpace.cpp.o |
| 8.0 | 7.9 | 6.4 | 1.5 | 5.3 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditTextDialog.cpp.o |
| 8.0 | 7.9 | 5.8 | 2.0 | 4.2 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeCoinManager.cpp.o |
| 7.3 | 7.2 | 6.0 | 1.1 | 4.9 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/DrawSketchHandlerDragAutoConstraint.cpp.o |
| 7.2 | 7.2 | 5.9 | 1.2 | 4.7 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/EditModeGeometryCoinConverter.cpp.o |
| 7.1 | 7.0 | 6.5 | 0.5 | 5.5 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherSolverAdvanced.cpp.o |
| 7.0 | 6.9 | 6.0 | 0.9 | 5.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/SnapManager.cpp.o |
| 6.7 | 6.6 | 4.9 | 1.7 | 3.6 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/TaskSketcherValidation.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 5.8 | 5.7 | 4.8 | 0.0 | 0.0 | src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Sketcher | 319.1 | 52 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 66.4 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 47.7 | src/Mod/Sketcher/App/SketchObject.h |
| 35.4 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 35.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 21.6 | src/Mod/Sketcher/App/Sketch.h |
| 20.3 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.1 | src/Mod/Part/App/PartFeature.h |
| 15.2 | src/App/DocumentObject.h |
| 14.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 14.8 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 14.7 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 14.7 | src/Mod/Part/App/Geometry.h |
| 13.4 | src/Mod/Part/Gui/ViewProvider.h |
| 13.3 | src/Mod/Part/Gui/ViewProviderExt.h |
| 12.8 | src/Mod/Part/App/AttachExtension.h |
| 12.7 | src/Mod/Part/App/Attacher.h |
| 12.4 | src/Mod/Part/App/Part2DObject.h |
| 12.3 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 11.5 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 10.0 | src/App/Document.h |
| 9.8 | src/Gui/CommandT.h |
| 8.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.1 | src/Mod/Material/App/PropertyMaterial.h |
| 7.6 | src/App/Application.h |
| 7.5 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.8 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.8 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 3.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 3.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 2.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 2.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.5 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.5 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
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
| 4.3 | build/clang-profile/src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/cmake_pch.hxx |
| 4.3 | src/Mod/Sketcher/Gui/PreCompiled.h |
| 2.9 | src/Gui/QtAll.h |
| 1.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QAbstractEventDispatcher |
| 1.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 0.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/QAbstractTextDocumentLayout |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qabstracttextdocumentlayout.h |
| 0.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtGui/qtextlayout.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QAbstractItemModel |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstractitemmodel.h |
| 0.2 | src/Gui/InventorAll.h |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/BRep_Tool.hxx |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/chrono |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/cmath |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qlist.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QDirIterator |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdiriterator.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdebug.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdir.h |
| 0.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 0.1 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/bitset |

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
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |
| 0.0 | std::__format::_Buf_sink<wchar_t> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::_Sink<wchar_t> |
| 0.0 | std::span<wchar_t> |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 66.4 | src/Mod/Sketcher/Gui/ViewProviderSketch.h |
| 47.7 | src/Mod/Sketcher/App/SketchObject.h |
| 35.4 | src/Mod/Part/Gui/ViewProviderPreviewExtension.h |
| 35.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore |
| 21.6 | src/Mod/Sketcher/App/Sketch.h |
| 20.3 | src/Mod/Sketcher/App/planegcs/GCS.h |
| 17.1 | src/Mod/Part/App/PartFeature.h |
| 15.2 | src/App/DocumentObject.h |
| 14.8 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h |
| 14.8 | /nix/store/5ivvhzl37ci5sfdmyxc62s0yq56gs0gf-clang-wrapper-21.1.8/resource-root/include/immintrin.h |
| 14.7 | src/Mod/Part/Gui/ViewProvider2DObject.h |
| 14.7 | src/Mod/Part/App/Geometry.h |
| 13.4 | src/Mod/Part/Gui/ViewProvider.h |
| 13.3 | src/Mod/Part/Gui/ViewProviderExt.h |
| 12.8 | src/Mod/Part/App/AttachExtension.h |
| 12.7 | src/Mod/Part/App/Attacher.h |
| 12.4 | src/Mod/Part/App/Part2DObject.h |
| 12.3 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR |
| 11.5 | /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/Core |
| 10.0 | src/App/Document.h |
| 9.8 | src/Gui/CommandT.h |
| 8.4 | src/Mod/Part/App/PropertyTopoShape.h |
| 8.1 | src/Mod/Material/App/PropertyMaterial.h |
| 7.6 | src/App/Application.h |
| 7.5 | src/Mod/Part/App/TopoShape.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.8 | qRegisterNormalizedMetaType<QList<Base::Vector3<double>>> |
| 3.8 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>> |
| 3.7 | qRegisterNormalizedMetaType<QList<App::SubObjectT>> |
| 3.7 | qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>> |
| 3.0 | qRegisterNormalizedMetaType<QList<Base::Quantity>> |
| 3.0 | qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>> |
| 2.3 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter |
| 2.3 | QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>> |
| 2.1 | QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter |
| 2.1 | QMetaType::registerConverter<QList<App::SubObjectT>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>> |
| 1.9 | QtPrivate::QSequentialIterableConvertFunctor<QList<App::SubObjectT>>::operator() |
| 1.5 | QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Quantity>>::registerConverter |
| 1.5 | QMetaType::registerConverter<QList<Base::Quantity>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Quantity>>> |
| 1.4 | QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>::operator() |
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

Ninja 24.2 s; compiler 24.1 s; frontend 11.7 s; backend 12.3 s.

Top included files:

* 1.79 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.22 s — src/Mod/Sketcher/App/SketchObject.h
* 1.13 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.13 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.89 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/App/Datums.h
* 0.83 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.68 s — src/App/GeoFeature.h
* 0.68 s — src/App/DocumentObject.h
* 0.54 s — src/Mod/Sketcher/Gui/DrawSketchHandlerArc.h

Top template instantiations:

* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:702:83)>
* 0.22 s — QObject::connect<void (EditableDatumLabel::*)(double), const (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:673:54) &>
* 0.21 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler
* 0.20 s — QObject::connect<void (EditableDatumLabel::*)(double), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:688:84)>
* 0.20 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::DrawSketchDefaultWidgetController
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:708:91)>
* 0.19 s — QObject::connect<void (EditableDatumLabel::*)(), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/DrawSketchController.h:695:80)>
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerArc, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>::initDefaultWidget
* 0.15 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerEllipse, SketcherGui::StateMachines::ThreeSeekEnd, 3, SketcherGui::OnViewParameters<5, 6>, SketcherGui::WidgetParameters<0, 0>, SketcherGui::WidgetCheckboxes<0, 0>, SketcherGui::WidgetComboboxes<1, 1>, SketcherGui::WidgetLineEdits<0, 0>, SketcherGui::ConstructionMethods::CircleEllipseConstructionMethod, true>>::DrawSketchControllableHandler

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandSketcherTools.cpp.o

Ninja 15.2 s; compiler 15.1 s; frontend 9.3 s; backend 5.8 s.

Top included files:

* 1.98 s — src/Mod/Sketcher/App/SketchObject.h
* 1.75 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.13 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.13 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.84 s — src/Mod/Sketcher/App/Sketch.h
* 0.80 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.76 s — src/Gui/CommandT.h
* 0.62 s — src/Mod/Sketcher/Gui/DrawSketchHandlerTranslate.h
* 0.61 s — src/App/Document.h
* 0.50 s — src/Mod/Sketcher/Gui/DrawSketchDefaultWidgetController.h

Top template instantiations:

* 0.19 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.19 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::doInitControls
* 0.15 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerTranslate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<6>, SketcherGui::WidgetParameters<2>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::initDefaultWidget
* 0.12 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.12 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerSymmetry, SketcherGui::StateMachines::OneSeekEnd, 0, SketcherGui::OnViewParameters<0>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchControllableHandler<SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>>::DrawSketchControllableHandler
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerRotate, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<4>, SketcherGui::WidgetParameters<1>, SketcherGui::WidgetCheckboxes<2>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController
* 0.11 s — SketcherGui::DrawSketchDefaultWidgetController<SketcherGui::DrawSketchHandlerScale, SketcherGui::StateMachines::ThreeSeekEnd, 0, SketcherGui::OnViewParameters<3>, SketcherGui::WidgetParameters<0>, SketcherGui::WidgetCheckboxes<1>, SketcherGui::WidgetComboboxes<0>, SketcherGui::WidgetLineEdits<0>>::DrawSketchDefaultWidgetController

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/CommandConstraints.cpp.o

Ninja 13.9 s; compiler 13.8 s; frontend 8.1 s; backend 5.7 s.

Top included files:

* 1.68 s — src/Mod/Sketcher/Gui/DrawSketchHandlerExternal.h
* 1.62 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.58 s — src/Mod/Sketcher/App/SketchObject.h
* 1.15 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.15 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.88 s — src/Mod/Sketcher/App/Sketch.h
* 0.85 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.69 s — src/Gui/CommandT.h
* 0.57 s — src/App/Document.h
* 0.51 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qsimd.h

Top template instantiations:

* 0.11 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.11 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.08 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.08 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.06 s — Gui::cmdAppObjectArgs<const char *const &, const char *const &, const char *, const char *>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/ViewProviderSketch.cpp.o

Ninja 13.2 s; compiler 13.1 s; frontend 8.7 s; backend 4.3 s.

Top included files:

* 1.68 s — src/Mod/Sketcher/Gui/TaskDlgEditSketch.h
* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 1.53 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.13 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.13 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.91 s — src/Mod/Sketcher/App/Sketch.h
* 0.87 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.75 s — src/Gui/CommandT.h
* 0.61 s — src/App/Document.h
* 0.51 s — /nix/store/pvyj99kvphskpksxs8773916hl2xbj72-eigen-3.4.1/include/eigen3/Eigen/QR

Top template instantiations:

* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Vector3<double>>>
* 0.10 s — qRegisterNormalizedMetaType<QList<Base::Quantity>>
* 0.10 s — qRegisterNormalizedMetaTypeImplementation<QList<Base::Quantity>>
* 0.09 s — qRegisterNormalizedMetaType<QList<App::SubObjectT>>
* 0.09 s — qRegisterNormalizedMetaTypeImplementation<QList<App::SubObjectT>>
* 0.07 s — QObject::connect<void (QWindow::*)(QScreen *), (lambda at /home/user/dev/FreeCAD/src/Mod/Sketcher/Gui/ViewProviderSketch.cpp:4685:84)>
* 0.06 s — QtPrivate::SequentialValueTypeIsMetaType<QList<Base::Vector3<double>>>::registerConverter
* 0.06 s — QMetaType::registerConverter<QList<Base::Vector3<double>>, QIterable<QMetaSequence>, QtPrivate::QSequentialIterableConvertFunctor<QList<Base::Vector3<double>>>>
* 0.05 s — QtPrivate::SequentialValueTypeIsMetaType<QList<App::SubObjectT>>::registerConverter

## src/Mod/Sketcher/Gui/CMakeFiles/SketcherGui.dir/Utils.cpp.o

Ninja 11.3 s; compiler 11.2 s; frontend 7.2 s; backend 4.0 s.

Top included files:

* 1.83 s — src/Mod/Sketcher/Gui/ViewProviderSketch.h
* 1.57 s — src/Mod/Sketcher/App/SketchObject.h
* 1.20 s — src/Mod/Part/Gui/ViewProviderPreviewExtension.h
* 1.20 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QtCore
* 0.94 s — src/Gui/CommandT.h
* 0.89 s — src/Mod/Sketcher/App/Sketch.h
* 0.85 s — src/Mod/Sketcher/App/planegcs/GCS.h
* 0.61 s — src/App/Transactions.h
* 0.60 s — src/App/Document.h
* 0.52 s — src/Mod/Part/App/Part2DObject.h

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
