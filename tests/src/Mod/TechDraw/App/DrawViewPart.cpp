// SPDX-License-Identifier: LGPL-2.1-or-later

#include <gtest/gtest.h>
#include "src/App/InitApplication.h"
#include <App/Application.h>
#include <App/Document.h>
#include <Base/Interpreter.h>
#include <Mod/TechDraw/App/DrawViewPart.h>
#include <Mod/TechDraw/App/Geometry.h>
#include <BRepCheck_Analyzer.hxx>
#include <BRepBuilderAPI_MakeEdge.hxx>
#include <Mod/TechDraw/App/GeometryObject.h>
#include <Mod/TechDraw/App/Preferences.h>

class FaceTestView: public TechDraw::DrawViewPart
{
public:
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
        general->SetBool("NewFaceFinder", false);
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

    App::Document* doc = nullptr;
    FaceTestView* view = nullptr;
    bool previousFaceFinder = false;
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
