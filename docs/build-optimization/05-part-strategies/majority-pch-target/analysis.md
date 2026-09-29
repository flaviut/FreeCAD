# Clang build profile

* Recorded Ninja log timestamp span: 46.4 s (128–46498 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 203; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 243.7 | 5.3 | 249.0 |
| Frontend | 149.7 | 4.2 | 153.9 |
| Backend | 89.2 | 0.0 | 89.2 |
| Source | 93.0 | 3.8 | 96.8 |
| InstantiateFunction | 46.8 | 0.7 | 47.5 |
| InstantiateClass | 44.6 | 0.7 | 45.3 |
| Optimizer | 55.0 | 0.0 | 55.0 |
| CodeGenPasses | 33.9 | 0.0 | 33.9 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 10.6 | 10.5 | 7.0 | 3.4 | 4.9 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 7.9 | 7.9 | 2.3 | 5.5 | 0.7 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 7.5 | 7.4 | 2.1 | 5.3 | 0.5 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 6.7 | 6.6 | 2.4 | 4.1 | 0.9 | src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o |
| 5.8 | 5.8 | 2.9 | 2.8 | 1.5 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 5.2 | 5.2 | 2.3 | 2.8 | 1.3 | src/Mod/Part/App/CMakeFiles/Part.dir/Attacher.cpp.o |
| 4.7 | 4.6 | 2.2 | 2.4 | 1.4 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPartPy.cpp.o |
| 4.3 | 4.2 | 2.2 | 2.0 | 1.3 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyTopoShape.cpp.o |
| 4.1 | 4.1 | 1.2 | 2.8 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapePyImp.cpp.o |
| 3.7 | 3.6 | 2.0 | 1.6 | 1.3 | src/Mod/Part/App/CMakeFiles/Part.dir/MeasureClient.cpp.o |
| 3.6 | 3.6 | 2.4 | 1.1 | 1.9 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPart.cpp.o |
| 3.3 | 3.2 | 2.0 | 1.2 | 1.4 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyGeometryList.cpp.o |
| 3.3 | 3.2 | 1.9 | 1.3 | 1.3 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachExtension.cpp.o |
| 3.2 | 3.1 | 1.7 | 1.4 | 1.2 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachEnginePyImp.cpp.o |
| 3.2 | 3.1 | 0.8 | 2.3 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/modelRefine.cpp.o |
| 2.7 | 2.7 | 1.6 | 1.0 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/ImportStep.cpp.o |
| 2.6 | 2.6 | 1.6 | 0.9 | 1.2 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachExtensionPyImp.cpp.o |
| 2.6 | 2.6 | 1.6 | 1.0 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeaturePyImp.cpp.o |
| 2.6 | 2.6 | 1.5 | 1.0 | 1.2 | src/Mod/Part/App/CMakeFiles/Part.dir/FeatureScale.cpp.o |
| 2.5 | 2.4 | 1.5 | 0.9 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartImportStep.cpp.o |
| 2.5 | 2.4 | 1.5 | 0.9 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartImportBrep.cpp.o |
| 2.5 | 2.4 | 1.9 | 0.5 | 1.3 | src/Mod/Part/App/CMakeFiles/Part.dir/LinearPatternExtension.cpp.o |
| 2.5 | 2.4 | 1.5 | 0.9 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartCurveNet.cpp.o |
| 2.4 | 2.3 | 1.4 | 0.9 | 1.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FeaturePartImportIges.cpp.o |
| 2.2 | 2.1 | 1.7 | 0.4 | 1.3 | src/Mod/Part/App/CMakeFiles/Part.dir/FeatureExtrusion.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 5.4 | 5.3 | 4.2 | 0.0 | 3.8 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 243.7 | 203 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 37.1 | src/Mod/Part/App/PartFeature.h |
| 25.6 | src/Mod/Material/App/PropertyMaterial.h |
| 23.8 | src/Mod/Material/App/Materials.h |
| 19.9 | src/Mod/Material/App/MaterialValue.h |
| 18.0 | src/App/DocumentObject.h |
| 13.8 | src/Mod/Part/App/AttachExtension.h |
| 13.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 12.8 | src/Mod/Part/App/Attacher.h |
| 11.9 | src/App/GeoFeature.h |
| 9.6 | src/App/PropertyStandard.h |
| 9.1 | src/App/FeaturePython.h |
| 8.9 | src/App/PropertyLinks.h |
| 8.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 8.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QVariant |
| 8.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |
| 7.1 | src/Base/BoundBox.h |
| 6.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 6.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 6.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 6.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 6.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 6.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 6.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 6.3 | src/Base/Tools2D.h |
| 6.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdebug.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 3.7 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 3.3 | std::vector<Base::Vector2d>::operator= |
| 2.2 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 1.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 1.2 | std::unique_ptr<App::DynamicProperty::Impl> |
| 1.0 | std::vector<Base::Vector2d>::clear |
| 1.0 | std::vector<Base::Vector2d>::_M_erase_at_end |
| 1.0 | std::_Destroy<Base::Vector2d *, Base::Vector2d> |
| 1.0 | std::_Destroy<Base::Vector2d *> |
| 1.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 1.0 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 1.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.9 | QList<QString>::operator<< |
| 0.9 | QList<QString>::append |
| 0.9 | QList<QString>::emplaceBack<const QString &> |
| 0.9 | std::vector<PyMethodDef> |
| 0.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.8 | QtPrivate::QMovableArrayOps<QString>::emplace<const QString &> |
| 0.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.8 | std::unique_ptr<QtPrivate::QSlotObjectBase, QtPrivate::QSlotObjectBase::Deleter> |
| 0.8 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_M_emplace_hint_unique<const std::piecewise_construct_t &, std::tuple<App::DocumentObject *const &>, std::tuple<>> |
| 0.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 3.8 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 3.8 | src/Mod/Part/App/PreCompiled.h |
| 1.1 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.9 | src/App/ComplexGeoData.h |
| 0.7 | src/App/MappedName.h |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.4 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_generators.hpp |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QHash |
| 0.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/nil_generator.hpp |
| 0.2 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid.hpp |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/BRepMesh_IncrementalMesh.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_Context.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshTools_ModelBuilder.hxx |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Model.hxx |
| 0.2 | src/App/StringHasher.h |
| 0.2 | /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/IMeshData_Types.hxx |

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
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<wchar_t>, wchar_t>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::chrono::hh_mm_ss<std::chrono::duration<long>>::hh_mm_ss |
| 0.0 | std::formatter<bool, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_int<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Seq_sink<std::basic_string<wchar_t>> |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 37.1 | src/Mod/Part/App/PartFeature.h |
| 25.6 | src/Mod/Material/App/PropertyMaterial.h |
| 23.8 | src/Mod/Material/App/Materials.h |
| 19.9 | src/Mod/Material/App/MaterialValue.h |
| 18.0 | src/App/DocumentObject.h |
| 13.8 | src/Mod/Part/App/AttachExtension.h |
| 13.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h |
| 12.8 | src/Mod/Part/App/Attacher.h |
| 11.9 | src/App/GeoFeature.h |
| 9.6 | src/App/PropertyStandard.h |
| 9.1 | src/App/FeaturePython.h |
| 8.9 | src/App/PropertyLinks.h |
| 8.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QMetaType |
| 8.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QVariant |
| 8.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qvariant.h |
| 7.1 | src/Base/BoundBox.h |
| 6.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 6.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 6.7 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 6.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 6.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp |
| 6.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 6.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp |
| 6.3 | src/Base/Tools2D.h |
| 6.3 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdebug.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 3.7 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 3.3 | std::vector<Base::Vector2d>::operator= |
| 2.2 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 1.4 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |
| 1.2 | std::unique_ptr<App::DynamicProperty::Impl> |
| 1.0 | std::vector<Base::Vector2d>::clear |
| 1.0 | std::vector<Base::Vector2d>::_M_erase_at_end |
| 1.0 | std::_Destroy<Base::Vector2d *, Base::Vector2d> |
| 1.0 | std::_Destroy<Base::Vector2d *> |
| 1.0 | std::map<QString, Materials::ModelProperty>::operator[] |
| 1.0 | std::__uniq_ptr_data<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 1.0 | std::__uniq_ptr_impl<App::DynamicProperty::Impl, std::default_delete<App::DynamicProperty::Impl>> |
| 0.9 | QList<QString>::operator<< |
| 0.9 | QList<QString>::append |
| 0.9 | QList<QString>::emplaceBack<const QString &> |
| 0.9 | std::vector<PyMethodDef> |
| 0.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array2D>> |
| 0.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array2D>> |
| 0.8 | QtPrivate::QMovableArrayOps<QString>::emplace<const QString &> |
| 0.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>> |
| 0.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>> |
| 0.8 | std::unique_ptr<QtPrivate::QSlotObjectBase, QtPrivate::QSlotObjectBase::Deleter> |
| 0.8 | std::_Rb_tree<App::DocumentObject *, std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>, std::_Select1st<std::pair<App::DocumentObject *const, std::vector<std::basic_string<char>>>>, std::less<App::DocumentObject *>>::_M_emplace_hint_unique<const std::piecewise_construct_t &, std::tuple<App::DocumentObject *const &>, std::tuple<>> |
| 0.8 | qRegisterNormalizedMetaType<std::shared_ptr<Materials::Material>> |
| 0.8 | qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Material>> |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 10.6 s; compiler 10.5 s; frontend 7.0 s; backend 3.4 s.

Top included files:

* 3.73 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.73 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.80 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.77 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.74 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.15 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.14 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.17 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.17 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.17 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.17 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.16 s — boost::geometry::index::rtree<Part::WireJoiner::WireJoinerP::VertexInfo, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::PntGetter>::remove

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o

Ninja 7.9 s; compiler 7.9 s; frontend 2.3 s; backend 5.5 s.

Top included files:

* 0.30 s — src/Mod/Part/App/FaceMakerBullseye.h
* 0.28 s — src/Mod/Part/App/FaceMaker.h
* 0.27 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.27 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.27 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.26 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.26 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h
* 0.23 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h
* 0.18 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h
* 0.15 s — src/Base/Writer.h

Top template instantiations:

* 0.53 s — boost::basic_regex<char>::assign
* 0.27 s — boost::basic_regex<char>::basic_regex
* 0.27 s — boost::basic_regex<char>::do_assign
* 0.26 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.13 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.12 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.12 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data
* 0.12 s — boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper
* 0.12 s — boost::regex_traits<char>::regex_traits

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o

Ninja 7.5 s; compiler 7.4 s; frontend 2.1 s; backend 5.3 s.

Top included files:

* 0.30 s — src/Mod/Part/App/FaceMaker.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.27 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h
* 0.25 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h
* 0.19 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qmetatype.h
* 0.09 s — src/Mod/Part/App/TopoShapeMapper.h
* 0.06 s — src/Mod/Part/App/Geometry.h

Top template instantiations:

* 0.05 s — QList<App::StringIDRef>::append
* 0.03 s — std::unique_ptr<OSD_Parallel::IteratorInterface>
* 0.03 s — std::__uniq_ptr_data<OSD_Parallel::IteratorInterface, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.03 s — std::__uniq_ptr_impl<OSD_Parallel::IteratorInterface, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.02 s — QList<App::StringIDRef>::operator+=
* 0.02 s — QtPrivate::QCommonArrayOps<App::StringIDRef>::growAppend
* 0.02 s — Base::ConsoleSingleton::developerWarning<std::basic_string<char>>
* 0.02 s — Base::ConsoleSingleton::send<Base::LogStyle::Warning, Base::IntendedRecipient::Developer, Base::ContentType::Untranslatable, std::basic_string<char>>
* 0.02 s — std::format<std::basic_string<char>>
* 0.02 s — QArrayDataPointer<App::StringIDRef>::detachAndGrow

## src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o

Ninja 6.7 s; compiler 6.6 s; frontend 2.4 s; backend 4.1 s.

Top included files:

* 0.20 s — src/App/PropertyStandard.h
* 0.20 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/mutex.hpp
* 0.20 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/pthread/mutex.hpp
* 0.14 s — src/Base/Writer.h
* 0.14 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/lock_types.hpp
* 0.12 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/thread.hpp
* 0.12 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/thread_time.hpp
* 0.11 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset.hpp
* 0.11 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/dynamic_bitset/dynamic_bitset.hpp
* 0.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/date_time/posix_time/posix_time_types.hpp

Top template instantiations:

* 0.04 s — std::vector<int>::rbegin
* 0.04 s — Base::ConsoleSingleton::warning<const char *&>
* 0.03 s — std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>>
* 0.02 s — Base::ConsoleSingleton::error<std::basic_string<char> &>
* 0.02 s — std::unique_ptr<std::basic_istream<char>>
* 0.02 s — std::__uniq_ptr_data<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — std::__uniq_ptr_impl<std::basic_istream<char>, std::default_delete<std::basic_istream<char>>>
* 0.02 s — std::make_shared<Part::GeomBSplineCurve, opencascade::handle<Geom_BSplineCurve> &>
* 0.02 s — std::make_unique<Part::GeomPoint, Base::Vector3<double>>
* 0.02 s — std::shared_ptr<Part::GeomBSplineCurve>::shared_ptr<std::allocator<void>, opencascade::handle<Geom_BSplineCurve> &>

## src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o

Ninja 5.8 s; compiler 5.8 s; frontend 2.9 s; backend 2.8 s.

Top included files:

* 0.55 s — src/App/Document.h
* 0.32 s — src/Mod/Material/App/MaterialManager.h
* 0.31 s — src/App/Datums.h
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.29 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.28 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h
* 0.26 s — src/Mod/Material/App/Materials.h
* 0.25 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qobject.h

Top template instantiations:

* 0.03 s — std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[]
* 0.03 s — std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>
* 0.03 s — qRegisterNormalizedMetaType<std::shared_ptr<Materials::Array3D>>
* 0.03 s — qRegisterNormalizedMetaTypeImplementation<std::shared_ptr<Materials::Array3D>>
* 0.03 s — std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>>
* 0.03 s — QList<Data::MappedElement>::append
* 0.02 s — QList<Data::MappedElement>::push_back
* 0.02 s — QList<QString>::operator<<
* 0.02 s — QList<Data::MappedElement>::emplaceBack<Data::MappedElement>
* 0.02 s — QList<QString>::append
