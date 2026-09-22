// SPDX-License-Identifier: LGPL-2.1-or-later

#include <gtest/gtest.h>
#include "src/App/InitApplication.h"
#include <App/Application.h>
#include <App/Document.h>
#include <Base/Interpreter.h>
#include <Mod/Part/App/PartFeature.h>
#include <Mod/TechDraw/App/DrawViewPart.h>
#include <Mod/TechDraw/App/Geometry.h>
#include <BRepCheck_Analyzer.hxx>
#include <BRepBuilderAPI_MakeEdge.hxx>
#include <BRepAlgoAPI_Cut.hxx>
#include <BRepClass_FaceClassifier.hxx>
#include <BRepPrimAPI_MakeBox.hxx>
#include <BRep_Builder.hxx>
#include <Mod/TechDraw/App/GeometryObject.h>
#include <Mod/TechDraw/App/Preferences.h>
#ifdef TECHDRAW_TEST_GUI
# include <Mod/TechDraw/Gui/PathBuilder.h>
# include <Mod/TechDraw/Gui/Rez.h>

// Rendering topology is independent of the GUI's millimeter-to-pixel scale.
// Keep PathBuilder in model units without GUI preference initialization.
double TechDrawGui::Rez::guiX(double value)
{
    return value;
}
#endif

class FaceTestView: public TechDraw::DrawViewPart
{
public:
    void project(TopoDS_Shape shape, const Base::Vector3d& direction = Base::Vector3d(0, 0, 1))
    {
        Direction.setValue(direction);
        XDirection.setValue(direction.x == 0 ? Base::Vector3d(1, 0, 0) : Base::Vector3d(1, -1, 0));
        partExec(shape);
    }

    void buildFaces(const std::vector<TechDraw::BaseGeomPtr>& edges)
    {
        geometryObject = std::make_shared<TechDraw::GeometryObject>(getNameInDocument(), this);
        geometryObject->setEdgeGeometry(edges);
        extractFaces();
    }
};

class TechDrawFaces: public ::testing::Test
{
protected:
    static void SetUpTestSuite()
    {
        tests::initApplication();
        Base::Interpreter().runString("import Part, TechDraw");
    }

    void SetUp() override
    {
        auto general = TechDraw::Preferences::getPreferenceGroup("General");
        previousFaceFinder = general->GetBool("NewFaceFinder", false);
        previousHandleFaces = general->GetBool("HandleFaces", true);
        general->SetBool("NewFaceFinder", false);
        general->SetBool("HandleFaces", true);
        doc = App::GetApplication().newDocument("TechDrawFaces");
        view = new FaceTestView;
        doc->addObject(view, "View");
    }

    void TearDown() override
    {
        App::GetApplication().closeDocument(doc->getName());
        TechDraw::Preferences::getPreferenceGroup("General")->SetBool(
            "NewFaceFinder",
            previousFaceFinder
        );
        TechDraw::Preferences::getPreferenceGroup("General")->SetBool("HandleFaces", previousHandleFaces);
    }

    void addEdge(const gp_Pnt& first, const gp_Pnt& last)
    {
        auto edge = TechDraw::BaseGeom::baseFactory(BRepBuilderAPI_MakeEdge(first, last).Edge());
        edge->setHlrVisible(true);
        edge->setClassOfEdge(TechDraw::EdgeClass::HARD);
        edges.push_back(edge);
    }

    void addSquare()
    {
        addEdge({0, 0, 0}, {10, 0, 0});
        addEdge({10, 0, 0}, {10, 10, 0});
        addEdge({10, 10, 0}, {0, 10, 0});
        addEdge({0, 10, 0}, {0, 0, 0});
    }

    bool covers(double x, double y)
    {
        for (const auto& face : view->getFaceGeometry()) {
            BRepClass_FaceClassifier classifier(face->toOccFace(), gp_Pnt(x, y, 0), 1e-7);
            if (classifier.State() == TopAbs_IN) {
                return true;
            }
        }
        return false;
    }

    void expectConnectedFaceWires()
    {
        for (const auto& face : view->getFaceGeometry()) {
            for (const auto* wire : face->wires) {
                const auto& geoms = wire->geoms;
                ASSERT_FALSE(geoms.empty());
                for (size_t i = 0; i < geoms.size(); ++i) {
                    const auto& current = geoms[i];
                    const auto& next = geoms[(i + 1) % geoms.size()];
                    // PathBuilder reverses the curve's parameter direction
                    // when drawing reversed edges. connectPath inserts an
                    // unwanted straight segment if these endpoints differ.
                    const auto end = current->getReversed() ? current->getStartPoint()
                                                            : current->getEndPoint();
                    const auto start = next->getReversed() ? next->getEndPoint()
                                                           : next->getStartPoint();
                    EXPECT_NEAR((end - start).Length(), 0.0, 1e-7);
                }
            }
        }
    }

    TopoDS_Shape boxyTorus()
    {
        const auto block = BRepPrimAPI_MakeBox(10, 10, 2).Shape();
        const auto hole = BRepPrimAPI_MakeBox(gp_Pnt(3, 3, -1), 4, 4, 4).Shape();
        return BRepAlgoAPI_Cut(block, hole).Shape();
    }

    App::Document* doc = nullptr;
    FaceTestView* view = nullptr;
    bool previousFaceFinder = false;
    bool previousHandleFaces = true;
    std::vector<TechDraw::BaseGeomPtr> edges;
};

TEST_F(TechDrawFaces, CrossingBoundaries)
{
    addSquare();
    // The diagonals intersect away from their endpoints. Without splitting that
    // intersection, the legacy walker creates a self-intersecting face.
    addEdge({0, 0, 0}, {10, 10, 0});
    addEdge({10, 0, 0}, {0, 10, 0});
    view->buildFaces(edges);
    const auto faces = view->getFaceGeometry();
    // The revised finder includes the outer boundary, followed by four regions.
    ASSERT_EQ(faces.size(), 5);
    EXPECT_NEAR(faces.front()->getArea(), 100.0, 1e-7);
    for (size_t i = 1; i < faces.size(); ++i) {
        EXPECT_NEAR(faces[i]->getArea(), 25.0, 1e-7);
    }
    for (const auto& face : faces) {
        EXPECT_TRUE(BRepCheck_Analyzer(face->toOccFace()).IsValid());
    }
}

TEST_F(TechDrawFaces, KeepsValidLegacyFaces)
{
    addSquare();
    addEdge({0, 0, 0}, {10, 10, 0});
    view->buildFaces(edges);
    const auto faces = view->getFaceGeometry();
    // The legacy finder keeps the outer face at index zero and the two
    // triangular regions at indices one and two.
    ASSERT_EQ(faces.size(), 3);
    EXPECT_NEAR(faces.front()->getArea(), 100.0, 1e-7);
    EXPECT_NEAR(faces[1]->getArea(), 50.0, 1e-7);
    EXPECT_NEAR(faces[2]->getArea(), 50.0, 1e-7);
    for (const auto& face : faces) {
        EXPECT_TRUE(BRepCheck_Analyzer(face->toOccFace()).IsValid());
    }
}

TEST_F(TechDrawFaces, ThroughHoleIsNotAFace)
{
    const auto ring = boxyTorus();
    for (bool newFinder : {false, true}) {
        TechDraw::Preferences::getPreferenceGroup("General")->SetBool("NewFaceFinder", newFinder);
        view->project(ring);
        EXPECT_FALSE(covers(0, 0));
        EXPECT_TRUE(covers(4, 0));
        const auto faces = view->getFaceGeometry();
        ASSERT_EQ(faces.size(), 1);
        EXPECT_NEAR(faces.front()->getArea(), 84.0, 1e-7);
        EXPECT_TRUE(BRepCheck_Analyzer(faces.front()->toOccFace()).IsValid());
        expectConnectedFaceWires();
    }
}

TEST_F(TechDrawFaces, SurfaceBehindHoleIsStillAFace)
{
    TopoDS_Compound assembly;
    BRep_Builder builder;
    builder.MakeCompound(assembly);
    builder.Add(assembly, boxyTorus());
    builder.Add(assembly, BRepPrimAPI_MakeBox(gp_Pnt(0, 0, -2), 10, 10, 1).Shape());
    view->project(assembly);
    EXPECT_TRUE(covers(0, 0));
    EXPECT_TRUE(covers(4, 0));
}

TEST_F(TechDrawFaces, BoxyTorusPerspectiveOpening)
{
    view->Perspective.setValue(true);
    view->Focus.setValue(100);
    view->project(boxyTorus());
    EXPECT_FALSE(covers(0, 0));
    EXPECT_TRUE(covers(4, 0));
}

TEST_F(TechDrawFaces, BoxyTorusAngledFaces)
{
    for (bool newFinder : {false, true}) {
        TechDraw::Preferences::getPreferenceGroup("General")->SetBool("NewFaceFinder", newFinder);
        view->project(boxyTorus(), Base::Vector3d(-1, -1, 1));
        const auto faces = view->getFaceGeometry();
        ASSERT_GT(faces.size(), 1);
        for (const auto& face : faces) {
            EXPECT_TRUE(BRepCheck_Analyzer(face->toOccFace()).IsValid());
        }
        EXPECT_FALSE(covers(0, 0));
        EXPECT_TRUE(covers(4, 0));
        expectConnectedFaceWires();
    }
}

TEST_F(TechDrawFaces, LinkedBoxyTorusWithViewTransform)
{
    auto* source = static_cast<Part::Feature*>(doc->addObject("Part::Feature", "Ring"));
    source->Shape.setValue(boxyTorus());
    Base::Interpreter().runString(
        "import FreeCAD as App\n"
        "link = App.ActiveDocument.addObject('App::Link', 'Link')\n"
        "link.setLink(App.ActiveDocument.Ring)\n"
        "link.LinkPlacement.Base = App.Vector(40, -20, 10)\n"
    );
    view->Source.setValues({doc->getObject("Link")});
    view->Scale.setValue(2);
    view->Rotation.setValue(30);
    view->project(view->getSourceShape());
    EXPECT_FALSE(covers(0, 0));
    EXPECT_TRUE(covers(6.928203230275509, -4));
    ASSERT_EQ(view->getFaceGeometry().size(), 1);
    EXPECT_NEAR(view->getFaceGeometry().front()->getArea(), 336.0, 1e-7);
}

#ifdef TECHDRAW_TEST_GUI
TEST_F(TechDrawFaces, BoxyTorusPainterPathsMatchFaces)
{
    // QPainterPath and PathBuilder need no QApplication or visible window.
    TechDrawGui::PathBuilder builder;
    for (const auto& direction : {Base::Vector3d(0, 0, 1), Base::Vector3d(-1, -1, 1)}) {
        view->project(boxyTorus(), direction);
        for (const auto& face : view->getFaceGeometry()) {
            QPainterPath path;
            for (const auto* wire : face->wires) {
                QPainterPath boundary;
                for (const auto& edge : wire->geoms) {
                    boundary.connectPath(builder.geomToPainterPath(edge, 0));
                }
                path.addPath(boundary);
            }
            path.setFillRule(Qt::OddEvenFill);
            const auto shape = face->toOccFace();
            // Compare the actual rendering curves with OCC, including the
            // hole and the concave faces in the angled projection.
            for (double x = -8.137; x < 8; x += 0.37) {
                for (double y = -8.213; y < 8; y += 0.41) {
                    BRepClass_FaceClassifier classifier(shape, gp_Pnt(x, y, 0), 1e-7);
                    if (classifier.State() == TopAbs_ON) {
                        continue;
                    }
                    EXPECT_EQ(path.contains(QPointF(x, y)), classifier.State() == TopAbs_IN)
                        << x << ", " << y;
                }
            }
        }
    }
}
#endif
