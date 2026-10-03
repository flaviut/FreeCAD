// SPDX-License-Identifier: LGPL-2.1-or-later

#include <gtest/gtest.h>

#include <FCConfig.h>

#include <App/Application.h>
#include <App/Document.h>
#include <App/Expression.h>
#include <App/ObjectIdentifier.h>
#include <Mod/Assembly/App/AssemblyObject.h>
#include <Mod/Assembly/App/AssemblyLink.h>
#include <Mod/Assembly/App/Groups.h>
#include <src/App/InitApplication.h>

class AssemblyObjectTest: public ::testing::Test
{
protected:
    static void SetUpTestSuite()
    {
        tests::initApplication();
    }

    void SetUp() override
    {
        _docName = App::GetApplication().getUniqueDocumentName("test");
        auto _doc = App::GetApplication().newDocument(_docName.c_str(), "testUser");
        _assemblyObj = _doc->addObject<Assembly::AssemblyObject>();
        _jointGroupObj = _assemblyObj->addObject<Assembly::JointGroup>("jointGroupTest");
    }

    void TearDown() override
    {
        App::GetApplication().closeDocument(_docName.c_str());
    }

    Assembly::AssemblyObject* getObject()
    {
        return _assemblyObj;
    }

private:
    // TODO: use shared_ptr or something else here?
    Assembly::AssemblyObject* _assemblyObj;
    Assembly::JointGroup* _jointGroupObj;
    std::string _docName;
};

TEST_F(AssemblyObjectTest, createAssemblyObject)  // NOLINT
{
    // Arrange

    // Act

    // Assert
}

TEST_F(AssemblyObjectTest, RecomputeRemovesObsoleteLinkedComponentsAfterExecution)
{
    auto* document = getObject()->getDocument();
    auto* link = document->addObject<Assembly::AssemblyLink>("LinkedAssembly");
    link->LinkedObject.setValue(getObject());
    const auto initialObjectCount = document->getObjects().size();
    auto* obsolete = document->addObject("App::Part", "ObsoleteComponent");
    link->Group.setValues({obsolete});
    link->enforceRecompute();

    EXPECT_TRUE(document->recomputeFeature(link));
    EXPECT_EQ(document->getObject("ObsoleteComponent"), nullptr);
    EXPECT_EQ(document->getObjects().size(), initialObjectCount);
    EXPECT_FALSE(App::Document::isAnyRecomputing());
}

TEST_F(AssemblyObjectTest, RigidLinkedAssemblyCleanupPreservesRecomputeBoundary)
{
    auto* document = getObject()->getDocument();
    auto* link = document->addObject<Assembly::AssemblyLink>("LinkedAssembly");
    link->LinkedObject.setValue(getObject());
    link->Rigid.setValue(true);
    auto* group = link->ensureJointGroup();
    auto* joint = document->addObject("App::FeaturePython", "ObsoleteJoint");
    group->Group.setValues({joint});
    const std::string groupName = group->getNameInDocument();
    link->enforceRecompute();

    EXPECT_TRUE(document->recomputeFeature(link));
    EXPECT_EQ(document->getObject("ObsoleteJoint"), nullptr);
    EXPECT_EQ(document->getObject(groupName.c_str()), nullptr);
    EXPECT_FALSE(App::Document::isAnyRecomputing());
}
