# Clang build profile

* Recorded Ninja log timestamp span: 38.8 s (136–38922 ms). This span is not a complete build wall time if the log contains multiple builds.
* Ordinary translation units with traces: 203; PCH jobs with traces: 1.
* Missing traces: 0; invalid traces: 0.
* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.
* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.

## Compiler phase totals

| Phase | Ordinary TU s | PCH s | Combined s |
|---|---:|---:|---:|
| ExecuteCompiler | 178.2 | 6.7 | 184.9 |
| Frontend | 81.1 | 5.5 | 86.5 |
| Backend | 92.0 | 0.0 | 92.0 |
| Source | 28.4 | 4.9 | 33.3 |
| InstantiateFunction | 22.1 | 1.1 | 23.2 |
| InstantiateClass | 17.7 | 1.2 | 18.9 |
| Optimizer | 56.8 | 0.0 | 56.8 |
| CodeGenPasses | 34.9 | 0.0 | 34.9 |

## Translation units by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 9.9 | 9.8 | 6.1 | 3.7 | 4.2 | src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o |
| 7.9 | 7.8 | 2.2 | 5.6 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o |
| 7.7 | 7.6 | 2.0 | 5.5 | 0.3 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o |
| 6.9 | 6.8 | 2.6 | 4.2 | 0.7 | src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o |
| 4.8 | 4.7 | 1.9 | 2.8 | 0.6 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o |
| 4.5 | 4.5 | 1.3 | 3.2 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/Attacher.cpp.o |
| 4.0 | 3.9 | 1.0 | 2.9 | 0.2 | src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapePyImp.cpp.o |
| 3.8 | 3.7 | 1.1 | 2.6 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPartPy.cpp.o |
| 3.2 | 3.1 | 0.8 | 2.3 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/modelRefine.cpp.o |
| 3.1 | 3.1 | 1.1 | 2.0 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyTopoShape.cpp.o |
| 2.6 | 2.5 | 1.2 | 1.2 | 0.9 | src/Mod/Part/App/CMakeFiles/Part.dir/AppPart.cpp.o |
| 2.6 | 2.5 | 0.9 | 1.5 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/MeasureClient.cpp.o |
| 2.4 | 2.3 | 0.9 | 1.3 | 0.5 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachExtension.cpp.o |
| 2.1 | 2.0 | 0.8 | 1.2 | 0.4 | src/Mod/Part/App/CMakeFiles/Part.dir/PropertyGeometryList.cpp.o |
| 2.1 | 2.0 | 0.5 | 1.5 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/ExtrusionHelper.cpp.o |
| 2.0 | 1.9 | 0.9 | 1.0 | 0.3 | src/Mod/Part/App/CMakeFiles/Part.dir/Geometry2d.cpp.o |
| 2.0 | 1.9 | 0.5 | 1.3 | 0.2 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachEnginePyImp.cpp.o |
| 1.9 | 1.9 | 0.5 | 1.3 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FaceMakerBuildFace.cpp.o |
| 1.8 | 1.8 | 0.5 | 1.2 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FaceMakerUnified.cpp.o |
| 1.8 | 1.8 | 0.5 | 1.2 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/FT2FC.cpp.o |
| 1.8 | 1.7 | 0.5 | 1.2 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/ImportStep.cpp.o |
| 1.5 | 1.4 | 0.4 | 1.0 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/FeatureScale.cpp.o |
| 1.5 | 1.4 | 0.4 | 1.0 | 0.0 | src/Mod/Part/App/CMakeFiles/Part.dir/PartFeaturePyImp.cpp.o |
| 1.5 | 1.4 | 0.4 | 0.9 | 0.2 | src/Mod/Part/App/CMakeFiles/Part.dir/AttachExtensionPyImp.cpp.o |
| 1.4 | 1.4 | 0.5 | 0.9 | 0.1 | src/Mod/Part/App/CMakeFiles/Part.dir/BSplineCurvePyImp.cpp.o |

## Pch jobs by Ninja elapsed time

| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |
|---:|---:|---:|---:|---:|---|
| 6.8 | 6.7 | 5.5 | 0.0 | 4.9 | src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx.pch |

## Largest ordinary compilation areas

| Area | Compiler s | Translation units |
|---|---:|---:|
| Mod/Part | 178.2 | 203 |

## Included files in ordinary translation units

| Inclusive s | Source |
|---:|---|
| 3.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp |
| 3.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp |
| 3.6 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 3.6 | src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx |
| 2.6 | src/Base/GeometryPyCXX.h |
| 2.6 | src/App/Link.h |
| 2.4 | src/Mod/Part/App/Geometry.h |
| 2.4 | src/Mod/Part/App/AttachExtension.h |
| 2.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 2.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 2.0 | src/Mod/Part/App/Attacher.h |
| 2.0 | build/clang-profile/src/Mod/Part/App/GeometryPy.h |
| 2.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 1.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 1.8 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp |
| 1.8 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp |
| 1.8 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp |
| 1.7 | src/Base/Interpreter.h |
| 1.7 | src/Base/Writer.h |
| 1.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 1.6 | src/App/Document.h |
| 1.6 | src/Mod/Part/App/LinkArray.h |
| 1.5 | src/App/Datums.h |
| 1.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qeventloop.h |
| 1.4 | src/Mod/Part/App/FaceMaker.h |

## Template instantiations in ordinary translation units

| Inclusive s | Template |
|---:|---|
| 4.5 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 2.3 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 1.7 | std::vector<PyMethodDef> |
| 1.4 | std::_Vector_base<PyMethodDef, std::allocator<PyMethodDef>> |
| 1.0 | std::allocator<PyMethodDef> |
| 1.0 | std::__new_allocator<PyMethodDef> |
| 0.6 | std::unique_ptr<App::DocumentWeakPtrT::Private> |
| 0.6 | std::unordered_map<const App::DocumentObject *, fastsignals::scoped_connection> |
| 0.6 | boost::basic_regex<char>::assign |
| 0.5 | std::vector<std::shared_ptr<Part::GeometryExtension>> |
| 0.5 | std::__uniq_ptr_data<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.5 | std::__uniq_ptr_impl<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.5 | std::basic_string<char>::__resize_and_overwrite<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:3332:10)> |
| 0.5 | std::_Vector_base<std::shared_ptr<Part::GeometryExtension>, std::allocator<std::shared_ptr<Part::GeometryExtension>>> |
| 0.4 | std::basic_string<char>::resize_and_overwrite<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:3332:10) &> |
| 0.4 | opencascade::handle<Geom_CartesianPoint> |
| 0.3 | std::_Hashtable<const App::DocumentObject *, std::pair<const App::DocumentObject *const, fastsignals::scoped_connection>, std::allocator<std::pair<const App::DocumentObject *const, fastsignals::scoped_connection>>, std::__detail::_Select1st, std::equal_to<const App::DocumentObject *>, std::hash<const App::DocumentObject *>, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<false, false, true>> |
| 0.3 | std::vector<int>::rbegin |
| 0.3 | std::allocator<std::shared_ptr<Part::GeometryExtension>> |
| 0.3 | std::tuple<float, float, float> |
| 0.3 | Base::ConsoleSingleton::log<const char *> |
| 0.3 | std::__new_allocator<std::shared_ptr<Part::GeometryExtension>> |
| 0.3 | std::vector<Part::TopoShape>::push_back |
| 0.3 | boost::basic_regex<char>::basic_regex |
| 0.3 | boost::basic_regex<char>::do_assign |

## Included files in PCH jobs

| Inclusive s | Source |
|---:|---|
| 4.9 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 4.9 | src/Mod/Part/App/PreCompiled.h |
| 1.3 | src/Mod/Part/App/PartFeature.h |
| 1.1 | src/Mod/Part/App/OpenCascadeAll.h |
| 0.9 | src/Mod/Material/App/PropertyMaterial.h |
| 0.9 | src/Mod/Material/App/Materials.h |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/fstream |
| 0.5 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/istream |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QSet |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qset.h |
| 0.5 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhash.h |
| 0.4 | src/App/DocumentObject.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qhashfunctions.h |
| 0.4 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qstring.h |
| 0.4 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex.hpp |
| 0.3 | src/Mod/Material/App/MaterialValue.h |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/regex/v5/regex.hpp |
| 0.3 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/uuid/uuid_generators.hpp |
| 0.3 | src/Mod/Part/App/PropertyTopoShape.h |
| 0.3 | src/Mod/Part/App/TopoShape.h |
| 0.3 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ios |
| 0.2 | src/App/ComplexGeoData.h |
| 0.2 | /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/ostream |
| 0.2 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qchar.h |
| 0.2 | src/App/PropertyExpressionEngine.h |

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
| 0.0 | std::__format::__formatter_int<char>::_M_format_int<std::__format::_Sink_iter<char>> |
| 0.0 | std::map<QString, Materials::ModelProperty> |
| 0.0 | App::PropertyListsT<App::Material>::setValue |
| 0.0 | App::PropertyListsT<App::Material>::setValues |
| 0.0 | std::vector<App::Material>::operator= |
| 0.0 | std::_Rb_tree<QString, std::pair<const QString, Materials::ModelProperty>, std::_Select1st<std::pair<const QString, Materials::ModelProperty>>, std::less<QString>> |
| 0.0 | std::formatter<const wchar_t *, wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::__formatter_str<wchar_t>::format<std::__format::_Sink_iter<wchar_t>> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<char>, char>::_M_format_arg |
| 0.0 | std::__format::__visit_format_arg<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31), std::basic_format_context<std::__format::_Sink_iter<char>, char>> |
| 0.0 | std::basic_format_arg<std::basic_format_context<std::__format::_Sink_iter<char>, char>>::_M_visit<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:4593:31)> |
| 0.0 | std::__format::_Spec<wchar_t>::_M_parse_fill_and_align |
| 0.0 | std::__format::__write_padded<std::__format::_Sink_iter<char>, char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_parse<char> |
| 0.0 | std::__format::__formatter_int<wchar_t>::_M_do_parse |
| 0.0 | std::__format::_Formatting_scanner<std::__format::_Sink_iter<wchar_t>, wchar_t> |
| 0.0 | std::map<App::DocumentObject *, std::vector<std::basic_string<char>>>::operator[] |

## Included files in all traced jobs

| Inclusive s | Source |
|---:|---|
| 4.9 | build/clang-profile/src/Mod/Part/App/CMakeFiles/Part.dir/cmake_pch.hxx |
| 4.9 | src/Mod/Part/App/PreCompiled.h |
| 3.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp |
| 3.9 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp |
| 3.6 | src/3rdParty/PyCXX/CXX/Extensions.hxx |
| 3.6 | src/3rdParty/PyCXX/CXX/Python3/Extensions.hxx |
| 2.6 | src/Base/GeometryPyCXX.h |
| 2.6 | src/App/Link.h |
| 2.4 | src/Mod/Part/App/Geometry.h |
| 2.4 | src/Mod/Part/App/AttachExtension.h |
| 2.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication |
| 2.1 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h |
| 2.0 | src/Mod/Part/App/Attacher.h |
| 2.0 | build/clang-profile/src/Mod/Part/App/GeometryPy.h |
| 2.0 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h |
| 1.9 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h |
| 1.8 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp |
| 1.8 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp |
| 1.8 | /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp |
| 1.7 | src/Base/Interpreter.h |
| 1.7 | src/Base/Writer.h |
| 1.6 | /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h |
| 1.6 | src/App/Document.h |
| 1.6 | src/Mod/Part/App/LinkArray.h |
| 1.5 | src/App/Datums.h |

## Template instantiations in all traced jobs

| Inclusive s | Template |
|---:|---|
| 4.5 | std::__format::_Seq_sink<std::basic_string<char>>::_M_reserve |
| 2.3 | std::__format::_Seq_sink<std::basic_string<wchar_t>>::_M_reserve |
| 1.7 | std::vector<PyMethodDef> |
| 1.4 | std::_Vector_base<PyMethodDef, std::allocator<PyMethodDef>> |
| 1.0 | std::allocator<PyMethodDef> |
| 1.0 | std::__new_allocator<PyMethodDef> |
| 0.6 | std::unique_ptr<App::DocumentWeakPtrT::Private> |
| 0.6 | std::unordered_map<const App::DocumentObject *, fastsignals::scoped_connection> |
| 0.6 | boost::basic_regex<char>::assign |
| 0.5 | std::vector<std::shared_ptr<Part::GeometryExtension>> |
| 0.5 | std::__uniq_ptr_data<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.5 | std::__uniq_ptr_impl<App::DocumentWeakPtrT::Private, std::default_delete<App::DocumentWeakPtrT::Private>> |
| 0.5 | std::basic_string<char>::__resize_and_overwrite<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:3332:10)> |
| 0.5 | std::_Vector_base<std::shared_ptr<Part::GeometryExtension>, std::allocator<std::shared_ptr<Part::GeometryExtension>>> |
| 0.4 | std::basic_string<char>::resize_and_overwrite<(lambda at /nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0/include/c++/15.2.0/format:3332:10) &> |
| 0.4 | opencascade::handle<Geom_CartesianPoint> |
| 0.3 | std::_Hashtable<const App::DocumentObject *, std::pair<const App::DocumentObject *const, fastsignals::scoped_connection>, std::allocator<std::pair<const App::DocumentObject *const, fastsignals::scoped_connection>>, std::__detail::_Select1st, std::equal_to<const App::DocumentObject *>, std::hash<const App::DocumentObject *>, std::__detail::_Mod_range_hashing, std::__detail::_Default_ranged_hash, std::__detail::_Prime_rehash_policy, std::__detail::_Hashtable_traits<false, false, true>> |
| 0.3 | std::vector<int>::rbegin |
| 0.3 | std::allocator<std::shared_ptr<Part::GeometryExtension>> |
| 0.3 | std::tuple<float, float, float> |
| 0.3 | Base::ConsoleSingleton::log<const char *> |
| 0.3 | std::__new_allocator<std::shared_ptr<Part::GeometryExtension>> |
| 0.3 | std::vector<Part::TopoShape>::push_back |
| 0.3 | boost::basic_regex<char>::basic_regex |
| 0.3 | boost::basic_regex<char>::do_assign |

## Trace coverage

* Ninja log entries overwritten for repeated outputs: 0.
* Malformed Ninja log entries: 0.

### Missing traces

None.

### Invalid traces

None.

## src/Mod/Part/App/CMakeFiles/Part.dir/WireJoiner.cpp.o

Ninja 9.9 s; compiler 9.8 s; frontend 6.1 s; backend 3.7 s.

Top included files:

* 3.85 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry.hpp
* 3.85 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/geometry.hpp
* 1.85 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/radian_access.hpp
* 1.81 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/core/coordinate_promotion.hpp
* 1.78 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/multiprecision/cpp_bin_float.hpp
* 1.20 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/buffer.hpp
* 1.19 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/implementation.hpp
* 1.19 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffer_inserter.hpp
* 1.18 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/detail/buffer/buffered_piece_collection.hpp
* 1.13 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/geometry/algorithms/covered_by.hpp

Top template instantiations:

* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::remove
* 0.18 s — boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::raw_remove
* 0.18 s — boost::geometry::index::detail::rtree::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>
* 0.18 s — boost::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>> &>
* 0.18 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::apply_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>>
* 0.17 s — boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::internal_apply_visitor_impl<boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *>
* 0.17 s — boost::detail::variant::visitation_impl<mpl_::int_<0>, boost::detail::variant::visitation_impl_step<boost::mpl::l_iter<boost::mpl::l_item<mpl_::long_<2>, boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_item<mpl_::long_<1>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::mpl::l_end>>>, boost::mpl::l_iter<l_end>>, boost::detail::variant::invoke_visitor<boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>, false>, void *, boost::variant<boost::geometry::index::detail::rtree::variant_leaf<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::variant_internal_node<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::allocators<boost::container::new_allocator<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>>, std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, boost::geometry::model::box<boost::geometry::model::point<double, 3, boost::geometry::cs::cartesian>>, boost::geometry::index::detail::rtree::node_variant_static_tag>, boost::geometry::index::detail::rtree::node_variant_static_tag>>::has_fallback_type_>
* 0.17 s — boost::geometry::index::detail::rtree::visitors::remove<boost::geometry::index::rtree<std::_List_iterator<Part::WireJoiner::WireJoinerP::EdgeInfo>, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::BoxGetter>::members_holder>::operator()
* 0.16 s — boost::geometry::index::rtree<Part::WireJoiner::WireJoinerP::VertexInfo, boost::geometry::index::linear<16>, Part::WireJoiner::WireJoinerP::PntGetter>::remove

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShape.cpp.o

Ninja 7.9 s; compiler 7.8 s; frontend 2.2 s; backend 5.6 s.

Top included files:

* 0.17 s — src/Base/Writer.h
* 0.09 s — src/Mod/Part/App/FaceMakerBullseye.h
* 0.08 s — src/Base/UniqueNameManager.h
* 0.07 s — src/Mod/Part/App/FaceMaker.h
* 0.07 s — src/Base/Builder3D.h
* 0.06 s — src/Base/UnlimitedUnsigned.h
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.05 s — src/3rdParty/zipios++/zipoutputstream.h
* 0.05 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h

Top template instantiations:

* 0.56 s — boost::basic_regex<char>::assign
* 0.28 s — boost::basic_regex<char>::basic_regex
* 0.28 s — boost::basic_regex<char>::do_assign
* 0.27 s — boost::detail::create_implemenation<char, unsigned int, boost::regex_traits<char>>
* 0.14 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::assign
* 0.13 s — boost::re_detail_600::basic_regex_implementation<char, boost::regex_traits<char>>::basic_regex_implementation
* 0.13 s — boost::re_detail_600::basic_regex_parser<char, boost::regex_traits<char>>::parse
* 0.13 s — boost::re_detail_600::regex_data<char, boost::regex_traits<char>>::regex_data
* 0.13 s — boost::regex_traits_wrapper<boost::regex_traits<char>>::regex_traits_wrapper
* 0.13 s — boost::regex_traits<char>::regex_traits

## src/Mod/Part/App/CMakeFiles/Part.dir/TopoShapeExpansion.cpp.o

Ninja 7.7 s; compiler 7.6 s; frontend 2.0 s; backend 5.5 s.

Top included files:

* 0.11 s — /nix/store/njpvi46a41av7k4xqanvf94nawfci0f0-opencascade-occt-7.9.3/include/opencascade/OSD_Parallel.hxx
* 0.09 s — src/Mod/Part/App/TopoShapeMapper.h
* 0.09 s — src/Mod/Part/App/FaceMaker.h
* 0.08 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.08 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.07 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.07 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qabstracteventdispatcher.h
* 0.05 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qeventloop.h
* 0.04 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qdeadlinetimer.h

Top template instantiations:

* 0.07 s — std::unique_ptr<OSD_Parallel::IteratorInterface>
* 0.06 s — std::__uniq_ptr_data<OSD_Parallel::IteratorInterface, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.06 s — std::__uniq_ptr_impl<OSD_Parallel::IteratorInterface, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.05 s — QList<App::StringIDRef>::append
* 0.04 s — std::tuple<OSD_Parallel::IteratorInterface *, std::default_delete<OSD_Parallel::IteratorInterface>>
* 0.03 s — QList<App::StringIDRef>::operator+=
* 0.03 s — QtPrivate::QCommonArrayOps<App::StringIDRef>::growAppend
* 0.02 s — QArrayDataPointer<App::StringIDRef>::detachAndGrow
* 0.02 s — QArrayDataPointer<App::StringIDRef>::tryReadjustFreeSpace
* 0.02 s — Base::ConsoleSingleton::developerWarning<std::basic_string<char>>

## src/Mod/Part/App/CMakeFiles/Part.dir/Geometry.cpp.o

Ninja 6.9 s; compiler 6.8 s; frontend 2.6 s; backend 4.2 s.

Top included files:

* 0.24 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/mutex.hpp
* 0.24 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/pthread/mutex.hpp
* 0.20 s — src/Base/Writer.h
* 0.16 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/lock_types.hpp
* 0.15 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/thread.hpp
* 0.13 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/thread_time.hpp
* 0.11 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/date_time/posix_time/posix_time_types.hpp
* 0.10 s — /nix/store/0bin3mhz9h5x0rlhfi0hwnjc91i4vx77-boost-1.89.0-dev/include/boost/thread/thread_only.hpp
* 0.09 s — src/Base/UniqueNameManager.h
* 0.08 s — src/3rdParty/zipios++/zipoutputstream.h

Top template instantiations:

* 0.05 s — Base::ConsoleSingleton::warning<const char *&>
* 0.04 s — std::vector<int>::rbegin
* 0.03 s — std::reverse_iterator<__gnu_cxx::__normal_iterator<int *, std::vector<int>>>
* 0.03 s — Base::ConsoleSingleton::error<std::basic_string<char> &>
* 0.03 s — Base::ConsoleSingleton::send<Base::LogStyle::Warning, Base::IntendedRecipient::All, Base::ContentType::Untranslated, const char *&>
* 0.03 s — std::unique_ptr<std::basic_ostream<char>>
* 0.02 s — std::format<const char *&>
* 0.02 s — std::__uniq_ptr_data<std::basic_ostream<char>, std::default_delete<std::basic_ostream<char>>>
* 0.02 s — std::__uniq_ptr_impl<std::basic_ostream<char>, std::default_delete<std::basic_ostream<char>>>
* 0.02 s — std::make_unique<Part::GeometryMigrationExtension>

## src/Mod/Part/App/CMakeFiles/Part.dir/PartFeature.cpp.o

Ninja 4.8 s; compiler 4.7 s; frontend 1.9 s; backend 2.8 s.

Top included files:

* 0.18 s — src/App/Link.h
* 0.14 s — src/App/Document.h
* 0.10 s — src/Mod/Material/App/MaterialManager.h
* 0.09 s — src/App/Datums.h
* 0.09 s — src/Mod/Material/App/MaterialLibrary.h
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/QCoreApplication
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreapplication.h
* 0.06 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qcoreevent.h
* 0.06 s — src/Mod/Material/App/ModelLibrary.h
* 0.05 s — /nix/store/73fffgyahdpj0znw0p152i7q1xq5kkks-qtbase-6.11.1/include/QtCore/qbasictimer.h

Top template instantiations:

* 0.03 s — std::unique_ptr<std::map<QString, std::shared_ptr<Materials::Model>>>
* 0.03 s — QList<Data::MappedElement>::append
* 0.03 s — QList<Data::MappedElement>::push_back
* 0.03 s — QList<Data::MappedElement>::emplaceBack<Data::MappedElement>
* 0.03 s — QtPrivate::QGenericArrayOps<Data::MappedElement>::emplace<Data::MappedElement>
* 0.03 s — QArrayDataPointer<Data::MappedElement>::detachAndGrow
* 0.03 s — std::stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, (lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>
* 0.03 s — std::__uniq_ptr_data<std::map<QString, std::shared_ptr<Materials::Model>>, std::default_delete<std::map<QString, std::shared_ptr<Materials::Model>>>>
* 0.03 s — std::__uniq_ptr_impl<std::map<QString, std::shared_ptr<Materials::Model>>, std::default_delete<std::map<QString, std::shared_ptr<Materials::Model>>>>
* 0.03 s — std::__stable_sort<__gnu_cxx::__normal_iterator<std::pair<unsigned long, std::vector<int>> *, std::vector<std::pair<unsigned long, std::vector<int>>>>, __gnu_cxx::__ops::_Iter_comp_iter<(lambda at /home/user/dev/FreeCAD/src/Mod/Part/App/PartFeature.cpp:247:25)>>
