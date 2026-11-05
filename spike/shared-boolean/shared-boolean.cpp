// Disposable component-level probe of TopoShape::makeElementBoolean's OCCT seam.
#include <BOPAlgo_PaveFiller.hxx>
#include <BRepAlgoAPI_Cut.hxx>
#include <BRepAlgoAPI_Common.hxx>
#include <BRepBndLib.hxx>
#include <BRepCheck_Analyzer.hxx>
#include <BRepGProp.hxx>
#include <BRepTools.hxx>
#include <BRep_Builder.hxx>
#include <Bnd_Box.hxx>
#include <GProp_GProps.hxx>
#include <OSD_Parallel.hxx>
#include <Standard_Failure.hxx>
#include <Standard_Version.hxx>
#include <TopExp.hxx>
#include <TopTools_IndexedMapOfShape.hxx>
#include <TopTools_ListOfShape.hxx>
#include <TopoDS_Iterator.hxx>
#include <sys/resource.h>
#include <chrono>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>

using Clock = std::chrono::steady_clock;
static double seconds(Clock::time_point start) {
    return std::chrono::duration<double>(Clock::now() - start).count();
}

// Same recursive compound-only expansion as TopoShapeExpansion.cpp::expandCompound.
// Solids/shells/compsolids remain intact; no preliminary fuse of overlapping tools.
static void expandCompound(const TopoDS_Shape& shape, TopTools_ListOfShape& tools) {
    if (shape.ShapeType() != TopAbs_COMPOUND) {
        tools.Append(shape);
        return;
    }
    for (TopoDS_Iterator it(shape); it.More(); it.Next()) {
        expandCompound(it.Value(), tools);
    }
}

static void configure(BRepAlgoAPI_BooleanOperation& op,
                      const TopTools_ListOfShape& arguments,
                      const TopTools_ListOfShape& tools) {
    op.SetArguments(arguments);
    op.SetTools(tools);
    op.SetRunParallel(true);
    // FCBRepAlgoAPI_BooleanOperation's default, not OCCT's default.
    op.SetNonDestructive(true);
    op.SetFuzzyValue(1e-7);
}

struct Stats {
    double volume;
    int solids;
    bool valid;
};
static Stats inspect(const char* label, const TopoDS_Shape& shape) {
    if (shape.IsNull()) throw std::runtime_error("null output");
    GProp_GProps props;
    BRepGProp::VolumeProperties(shape, props);
    TopTools_IndexedMapOfShape solids, faces;
    TopExp::MapShapes(shape, TopAbs_SOLID, solids);
    TopExp::MapShapes(shape, TopAbs_FACE, faces);
    Bnd_Box bounds;
    BRepBndLib::Add(shape, bounds);
    double x0, y0, z0, x1, y1, z1;
    bounds.Get(x0, y0, z0, x1, y1, z1);
    const bool valid = BRepCheck_Analyzer(shape).IsValid();
    std::cout << "SHAPE " << label << " valid=" << valid
              << " solids=" << solids.Extent() << " faces=" << faces.Extent()
              << " volume_mm3=" << props.Mass()
              << " bounds_mm=" << x0 << ',' << y0 << ',' << z0 << ','
              << x1 << ',' << y1 << ',' << z1 << std::endl;
    if (!valid || solids.Extent() == 0 || !std::isfinite(props.Mass()) || props.Mass() <= 0)
        throw std::runtime_error("invalid or implausible output");
    return {props.Mass(), solids.Extent(), valid};
}

int main(int argc, char** argv) {
    try {
        if (argc != 4 || (std::string(argv[1]) != "baseline" && std::string(argv[1]) != "candidate"))
            throw std::runtime_error("usage: shared-boolean baseline|candidate base.brep tool.brep");
        std::cout << std::setprecision(12) << "IDENTITY OCCT=" << OCC_VERSION_COMPLETE
                  << " mode=" << argv[1] << " fuzzy=1e-7 parallel=1 nondestructive=1" << std::endl;
        auto constructionStart = Clock::now();
        BRep_Builder reader;
        TopoDS_Shape base, tool;
        if (!BRepTools::Read(base, argv[2], reader) || !BRepTools::Read(tool, argv[3], reader))
            throw std::runtime_error("cannot read frozen operands");
        TopTools_ListOfShape arguments, tools;
        arguments.Append(base);
        expandCompound(tool, tools);
        if (tools.IsEmpty()) throw std::runtime_error("unexpected empty tool compound");
        OSD_Parallel::SetUseOcctThreads(true);
        std::cout << "CONSTRUCTION read_expand_s=" << seconds(constructionStart)
                  << " tool_entries=" << tools.Size() << std::endl;
        auto operationStart = Clock::now();
        std::unique_ptr<BOPAlgo_PaveFiller> filler;
        std::unique_ptr<BRepAlgoAPI_Cut> cut;
        std::unique_ptr<BRepAlgoAPI_Common> common;
        if (std::string(argv[1]) == "candidate") {
            auto prepareStart = Clock::now();
            filler = std::make_unique<BOPAlgo_PaveFiller>();
            TopTools_ListOfShape all;
            all.Append(base);
            for (TopTools_ListOfShape::Iterator it(tools); it.More(); it.Next()) all.Append(it.Value());
            filler->SetArguments(all);
            filler->SetRunParallel(true);
            filler->SetNonDestructive(true);
            filler->SetFuzzyValue(1e-7);
            filler->Perform();
            if (filler->HasErrors()) {
                filler->DumpErrors(std::cerr);
                throw std::runtime_error("preparation failed");
            }
            std::cout << "TIMING prepare_s=" << seconds(prepareStart) << std::endl;
            cut = std::make_unique<BRepAlgoAPI_Cut>(*filler);
            common = std::make_unique<BRepAlgoAPI_Common>(*filler);
        } else {
            cut = std::make_unique<BRepAlgoAPI_Cut>();
            common = std::make_unique<BRepAlgoAPI_Common>();
        }
        auto cutStart = Clock::now();
        configure(*cut, arguments, tools);
        cut->Build();
        if (!cut->IsDone() || cut->HasErrors()) {
            cut->DumpErrors(std::cerr);
            throw std::runtime_error("cut failed");
        }
        std::cout << "TIMING cut_s=" << seconds(cutStart) << std::endl;
        auto commonStart = Clock::now();
        configure(*common, arguments, tools);
        common->Build();
        if (!common->IsDone() || common->HasErrors()) {
            common->DumpErrors(std::cerr);
            throw std::runtime_error("common failed");
        }
        std::cout << "TIMING common_s=" << seconds(commonStart)
                  << " total_operation_s=" << seconds(operationStart) << std::endl;
        auto validationStart = Clock::now();
        auto baseStats = inspect("base", base);
        auto cutStats = inspect("cut", cut->Shape());
        auto commonStats = inspect("common", common->Shape());
        // Smoke only: no extra boolean and no assumption that compound component
        // volume sums equal the union. Report the diagnostic rather than asserting it.
        std::cout << "CHECK removed_mm3=" << baseStats.volume - cutStats.volume
                  << " common_minus_removed_mm3="
                  << commonStats.volume - (baseStats.volume - cutStats.volume) << std::endl;
        if (cutStats.solids != 1 || cutStats.volume >= baseStats.volume ||
            commonStats.volume >= baseStats.volume)
            throw std::runtime_error("implausible result for this cylinder fixture");
        struct rusage usage;
        getrusage(RUSAGE_SELF, &usage);
        std::cout << "VALIDATION elapsed_s=" << seconds(validationStart)
                  << " peak_rss_kib=" << usage.ru_maxrss << std::endl;
        return 0;
    } catch (const Standard_Failure& e) {
        std::cerr << "OCCT_FAILURE " << e.GetMessageString() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "FAILURE " << e.what() << std::endl;
    }
    return 1;
}
