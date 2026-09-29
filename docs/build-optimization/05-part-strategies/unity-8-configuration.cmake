
set_source_files_properties(
    AppPartPy.cpp
    FaceMakerBuildFace.cpp
    FaceMakerUnified.cpp
    FeaturePartFuse.cpp
    ImportIges.cpp
    ImportStep.cpp
    PartFeature.cpp
    PropertyTopoShape.cpp
    TopoShape.cpp
    TopoShapeExpansion.cpp
    TopoShapeMapper.cpp
    TopoShapePyImp.cpp
    WireJoiner.cpp
    PROPERTIES SKIP_UNITY_BUILD_INCLUSION ON)
set_target_properties(Part PROPERTIES UNITY_BUILD ON UNITY_BUILD_BATCH_SIZE 8)
