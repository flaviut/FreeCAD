// SPDX-License-Identifier: LGPL-2.1-or-later

#include <string>
#include <vector>

#include <gtest/gtest.h>
#include "src/App/InitApplication.h"

#include <BRep_Builder.hxx>
#include <BRepGProp.hxx>
#include <BRepPrimAPI_MakeBox.hxx>
#include <GProp_GProps.hxx>
#include <TopoDS_Compound.hxx>

#include <App/Application.h>
#include <App/Document.h>
#include <Base/Console.h>
#include <Mod/PartDesign/App/FeatureAddSub.h>

// NOLINTBEGIN(readability-magic-numbers,cppcoreguidelines-avoid-magic-numbers)

namespace
{
class PreviewWarnings: public Base::ILogger
{
public:
    PreviewWarnings()
    {
        Base::Console().attachObserver(this);
    }

    ~PreviewWarnings() override
    {
        Base::Console().detachObserver(this);
    }

    void sendLog(
        const std::string& notifier,
        const std::string& message,
        Base::LogStyle level,
        Base::IntendedRecipient recipient,
        Base::ContentType content
    ) override
    {
        if (notifier == "Preview" && level == Base::LogStyle::Warning) {
            EXPECT_EQ(recipient, Base::IntendedRecipient::User);
            EXPECT_EQ(content, Base::ContentType::Translated);
            messages.push_back(message);
        }
    }

    const std::vector<std::string>& getMessages() const
    {
        return messages;
    }

private:
    std::vector<std::string> messages;
};

TopoDS_Shape box(double x, double y, double z, double length, double width, double height)
{
    return BRepPrimAPI_MakeBox(gp_Pnt(x, y, z), length, width, height).Shape();
}

TopoDS_Shape compound(const TopoDS_Shape& first, const TopoDS_Shape& second)
{
    BRep_Builder builder;
    TopoDS_Compound result;
    builder.MakeCompound(result);
    builder.Add(result, first);
    builder.Add(result, second);
    return result;
}
}  // namespace

class FeatureAddSubPreviewTest: public ::testing::Test
{
protected:
    static void SetUpTestSuite()
    {
        tests::initApplication();
    }

    void SetUp() override
    {
        doc = App::GetApplication().newDocument("FeatureAddSubPreview_test");
        auto base = doc->addObject<PartDesign::Feature>("Base");
        base->Shape.setValue(box(0, 0, 0, 10, 10, 10));
        feature = doc->addObject<PartDesign::FeatureAddSub>("Feature");
        feature->BaseFeature.setValue(base);
    }

    void TearDown() override
    {
        App::GetApplication().closeDocument(doc->getName());
    }

    void checkPreview(
        const TopoDS_Shape& tool,
        const char* operation,
        double expectedVolume,
        bool expectWarning
    )
    {
        feature->Operation.setValue(operation);
        feature->AddSubShape.setValue(tool);
        PreviewWarnings warnings;
        feature->invalidatePreview();
        feature->updatePreview();

        GProp_GProps properties;
        BRepGProp::VolumeProperties(feature->PreviewShape.getValue(), properties);
        EXPECT_NEAR(properties.Mass(), expectedVolume, 1e-7);
        ASSERT_EQ(warnings.getMessages().size(), expectWarning ? 1U : 0U);
        if (expectWarning) {
            EXPECT_NE(
                warnings.getMessages().front().find("no material will be removed"),
                std::string::npos
            );
        }
    }

private:
    App::Document* doc = nullptr;
    PartDesign::FeatureAddSub* feature = nullptr;
};

TEST_F(FeatureAddSubPreviewTest, SubtractionMissWarns)
{
    checkPreview(box(20, 0, 0, 10, 10, 10), "Subtraction", 0, true);
}

TEST_F(FeatureAddSubPreviewTest, SubtractionPartialOverlap)
{
    checkPreview(box(5, 0, 0, 10, 10, 10), "Subtraction", 500, false);
}

TEST_F(FeatureAddSubPreviewTest, SubtractionToolContainedInBase)
{
    checkPreview(box(1, 1, 1, 2, 2, 2), "Subtraction", 8, false);
}

TEST_F(FeatureAddSubPreviewTest, SubtractionBaseContainedInTool)
{
    checkPreview(box(-1, -1, -1, 12, 12, 12), "Subtraction", 1000, false);
}

TEST_F(FeatureAddSubPreviewTest, CommonNoChangeWarns)
{
    checkPreview(box(-1, -1, -1, 12, 12, 12), "Common", 1000, true);
}

TEST_F(FeatureAddSubPreviewTest, CommonPartialOverlap)
{
    checkPreview(box(5, 0, 0, 10, 10, 10), "Common", 500, false);
}

TEST_F(FeatureAddSubPreviewTest, CommonMissRemovesEntireBase)
{
    checkPreview(box(20, 0, 0, 10, 10, 10), "Common", 0, false);
}

TEST_F(FeatureAddSubPreviewTest, CommonToolContainedInBase)
{
    checkPreview(box(1, 1, 1, 2, 2, 2), "Common", 8, false);
}

TEST_F(FeatureAddSubPreviewTest, SubtractionOverlappingCompound)
{
    checkPreview(compound(box(0, 0, 0, 7, 10, 10), box(3, 0, 0, 5, 10, 10)), "Subtraction", 800, false);
}

TEST_F(FeatureAddSubPreviewTest, CommonOverlappingCompoundPartial)
{
    // Summing the tool solids would double-count their overlap and incorrectly warn.
    checkPreview(compound(box(0, 0, 0, 7, 10, 10), box(3, 0, 0, 5, 10, 10)), "Common", 800, false);
}

TEST_F(FeatureAddSubPreviewTest, CommonOverlappingCompoundNoChangeWarns)
{
    checkPreview(compound(box(0, 0, 0, 7, 10, 10), box(3, 0, 0, 7, 10, 10)), "Common", 1000, true);
}

TEST_F(FeatureAddSubPreviewTest, UnionPreviewsTool)
{
    checkPreview(box(20, 0, 0, 2, 2, 2), "Union", 8, false);
}

// NOLINTEND(readability-magic-numbers,cppcoreguidelines-avoid-magic-numbers)
