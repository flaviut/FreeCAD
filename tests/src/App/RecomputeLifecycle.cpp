#include <gtest/gtest.h>

#include <functional>
#include <stdexcept>
#include <string>

#include <App/Application.h>
#include <App/Document.h>
#include <App/DocumentObject.h>
#include <App/PropertyStandard.h>
#include <Base/Exception.h>
#include <src/App/InitApplication.h>

enum class RecomputeMode
{
    Document,
    Feature,
    RecursiveFeature
};

class CallbackFeature: public App::DocumentObject
{
public:
    App::DocumentObjectExecReturn* execute() override
    {
        callback();
        return StdReturn;
    }

    std::function<void()> callback;
};

class RecomputeLifecycleTest: public testing::TestWithParam<RecomputeMode>
{
protected:
    static void SetUpTestSuite()
    {
        tests::initApplication();
    }

    void SetUp() override
    {
        auto& application = App::GetApplication();
        name = application.getUniqueDocumentName("RecomputeLifecycle");
        document = application.newDocument(name.c_str());
        feature = document->addObject("App::FeaturePython", "Feature");
        feature->enforceRecompute();
    }

    void TearDown() override
    {
        before.disconnect();
        objectFinished.disconnect();
        finished.disconnect();
        stable.disconnect();
        if (App::GetApplication().getDocument(name.c_str())) {
            App::GetApplication().closeDocument(name.c_str());
        }
    }

    bool recompute()
    {
        if (GetParam() == RecomputeMode::Document) {
            bool error = false;
            document->recompute({feature}, true, &error);
            return !error;
        }
        return document->recomputeFeature(feature, GetParam() == RecomputeMode::RecursiveFeature);
    }

    void checkBoundary()
    {
        EXPECT_TRUE(document->testStatus(App::Document::Recomputing));
        EXPECT_TRUE(App::Document::isAnyRecomputing());
        EXPECT_TRUE(App::Document::isRecomputingOnCurrentThread());
    }

    std::string name;
    App::Document* document = nullptr;
    App::DocumentObject* feature = nullptr;
    fastsignals::connection before;
    fastsignals::connection objectFinished;
    fastsignals::connection finished;
    fastsignals::connection stable;
};

TEST_P(RecomputeLifecycleTest, BoundaryIncludesAllObserversAndEndsBeforeStableNotification)
{
    int beforeCount = 0;
    int objectCount = 0;
    int finishedCount = 0;
    int stableCount = 0;
    before = document->signalBeforeRecompute.connect([&](const App::Document&) {
        ++beforeCount;
        checkBoundary();
    });
    objectFinished = document->signalRecomputedObject.connect([&](const App::DocumentObject&) {
        ++objectCount;
        checkBoundary();
    });
    finished = document->signalRecomputed.connect([&](const App::Document&, const auto&) {
        ++finishedCount;
        checkBoundary();
    });
    stable = document->signalBecameStable.connect([&](const App::Document&) {
        ++stableCount;
        EXPECT_FALSE(document->testStatus(App::Document::Recomputing));
        EXPECT_FALSE(App::Document::isAnyRecomputing());
        EXPECT_FALSE(App::Document::isRecomputingOnCurrentThread());
        EXPECT_FALSE(feature->testStatus(App::ObjectStatus::PendingRecompute));
    });

    EXPECT_TRUE(recompute());
    EXPECT_EQ(beforeCount, 1);
    EXPECT_EQ(objectCount, 1);
    EXPECT_EQ(finishedCount, GetParam() == RecomputeMode::Feature ? 0 : 1);
    EXPECT_EQ(stableCount, 1);
}

TEST_P(RecomputeLifecycleTest, RecursiveEntryFailsWithoutClearingTheOuterBoundary)
{
    int attempts = 0;
    auto attempt = [&]() {
        ++attempts;
        EXPECT_THROW(document->recompute(), Base::RuntimeError);
        EXPECT_THROW(document->recomputeFeature(feature), Base::RuntimeError);
        EXPECT_THROW(document->recomputeFeature(feature, true), Base::RuntimeError);
        EXPECT_THROW(document->recomputeFeatureForDependency(feature), Base::RuntimeError);
        checkBoundary();
    };
    before = document->signalBeforeRecompute.connect([&](const App::Document&) { attempt(); });
    objectFinished = document->signalRecomputedObject.connect([&](const App::DocumentObject&) {
        attempt();
    });
    finished = document->signalRecomputed.connect([&](const App::Document&, const auto&) {
        attempt();
    });

    EXPECT_TRUE(recompute());
    EXPECT_EQ(attempts, GetParam() == RecomputeMode::Feature ? 2 : 3);
    EXPECT_FALSE(App::Document::isAnyRecomputing());
}

TEST_P(RecomputeLifecycleTest, DestructiveCallbacksLeaveObjectsAndTransactionsIntact)
{
    const int transaction = document->openTransaction("Create feature");
    auto* created = document->addObject("App::FeaturePython", "Created");
    const std::string createdName = created->getNameInDocument();
    bool checked = false;
    before = document->signalBeforeRecompute.connect([&](const App::Document&) {
        checked = true;
        EXPECT_THROW(document->abortTransaction(), Base::RuntimeError);
        EXPECT_THROW(document->commitTransaction(), Base::RuntimeError);
        EXPECT_THROW(document->openTransaction("Nested"), Base::RuntimeError);
        EXPECT_THROW(document->setActiveTransaction({.name = "Nested"}), Base::RuntimeError);
        EXPECT_THROW(document->undo(), Base::RuntimeError);
        EXPECT_THROW(document->redo(), Base::RuntimeError);
        EXPECT_THROW(document->clearUndos(), Base::RuntimeError);
        EXPECT_THROW(document->clearDocument(), Base::RuntimeError);
        EXPECT_THROW(document->removeObject(feature), Base::RuntimeError);
        EXPECT_THROW(document->removeObject(created), Base::RuntimeError);
        EXPECT_FALSE(App::GetApplication().closeDocument(name.c_str()));
        EXPECT_THROW(App::GetApplication().closeAllDocuments(), Base::RuntimeError);
        EXPECT_FALSE(App::GetApplication().abortTransaction(transaction));
        EXPECT_FALSE(App::GetApplication().commitTransaction(transaction));
        EXPECT_EQ(App::GetApplication().setActiveTransaction({.name = "Nested"}), App::NullTransaction);
        EXPECT_EQ(document->getBookedTransactionID(), transaction);
        EXPECT_EQ(document->getObject(createdName.c_str()), created);
    });

    EXPECT_TRUE(recompute());
    EXPECT_TRUE(checked);
    before.disconnect();
    document->abortTransaction();
    EXPECT_EQ(document->getObject(createdName.c_str()), nullptr);
}

TEST_P(RecomputeLifecycleTest, LinkedDocumentCannotBeDestroyedOrRolledBack)
{
    auto& application = App::GetApplication();
    const std::string sourceName = application.getUniqueDocumentName("RecomputeSource");
    auto* source = application.newDocument(sourceName.c_str());
    const int transaction = source->openTransaction("Source changes");
    auto* sourceFeature = source->addObject("App::FeaturePython", "Source");
    before = document->signalBeforeRecompute.connect([&](const App::Document&) {
        EXPECT_FALSE(application.closeDocument(sourceName.c_str()));
        EXPECT_THROW(source->clearDocument(), Base::RuntimeError);
        EXPECT_THROW(source->removeObject(sourceFeature), Base::RuntimeError);
        EXPECT_THROW(source->abortTransaction(), Base::RuntimeError);
        EXPECT_FALSE(application.abortTransaction(transaction));
        EXPECT_THROW(document->moveObject(sourceFeature), Base::RuntimeError);
        EXPECT_EQ(source->getObject("Source"), sourceFeature);
    });

    EXPECT_TRUE(recompute());
    before.disconnect();
    EXPECT_TRUE(application.closeDocument(sourceName.c_str()));
}

TEST_P(RecomputeLifecycleTest, BeforeObserverExceptionRestoresBoundary)
{
    int stableCount = 0;
    stable = document->signalBecameStable.connect([&](const App::Document&) { ++stableCount; });
    before = document->signalBeforeRecompute.connect([](const App::Document&) {
        throw std::runtime_error("Observer failure");
    });

    EXPECT_THROW(recompute(), std::runtime_error);
    EXPECT_EQ(stableCount, 1);
    EXPECT_FALSE(document->testStatus(App::Document::Recomputing));
    EXPECT_FALSE(App::Document::isAnyRecomputing());
    EXPECT_FALSE(App::Document::isRecomputingOnCurrentThread());
    before.disconnect();
    EXPECT_TRUE(recompute());
}

TEST_P(RecomputeLifecycleTest, RecomputeObserversCannotEditInputsOrPropertyStructure)
{
    auto* input = static_cast<App::PropertyInteger*>(
        feature->addDynamicProperty("App::PropertyInteger", "Input")
    );
    input->setValue(42);
    const std::string label = feature->Label.getValue();
    const std::string documentLabel = document->Label.getValue();
    int checked = 0;
    auto check = [&]() {
        ++checked;
        EXPECT_THROW(input->setValue(100), Base::RuntimeError);
        EXPECT_THROW(feature->Label.setValue("Changed"), Base::RuntimeError);
        EXPECT_THROW(document->Label.setValue("Changed"), Base::RuntimeError);
        EXPECT_THROW(feature->removeDynamicProperty("Input"), Base::RuntimeError);
        EXPECT_THROW(feature->addDynamicProperty("App::PropertyInteger", "Added"), Base::RuntimeError);
        EXPECT_THROW(document->addObject("App::FeaturePython", "Added"), Base::RuntimeError);
        EXPECT_THROW(App::GetApplication().newDocument("ForbiddenDocument"), Base::RuntimeError);
        EXPECT_EQ(input->getValue(), 42);
        EXPECT_EQ(feature->Label.getValue(), label);
        EXPECT_EQ(document->Label.getValue(), documentLabel);
        EXPECT_EQ(feature->getPropertyByName("Added"), nullptr);
        EXPECT_EQ(document->getObject("Added"), nullptr);
        EXPECT_EQ(App::GetApplication().getDocument("ForbiddenDocument"), nullptr);
    };
    before = document->signalBeforeRecompute.connect([&](const App::Document&) { check(); });
    finished = document->signalRecomputed.connect([&](const App::Document&, const auto&) { check(); });

    EXPECT_TRUE(recompute());
    EXPECT_EQ(checked, GetParam() == RecomputeMode::Feature ? 1 : 2);
    input->setValue(100);
    EXPECT_EQ(input->getValue(), 100);
}

TEST_P(RecomputeLifecycleTest, FeatureExecutionCanWriteComputedProperties)
{
    document->removeObject(feature);
    feature = document->addObject("App::FeatureTest", "Feature");
    auto* count = static_cast<App::PropertyInteger*>(feature->getPropertyByName("ExecCount"));
    ASSERT_NE(count, nullptr);
    const long initialCount = count->getValue();
    feature->enforceRecompute();

    EXPECT_TRUE(recompute());
    EXPECT_EQ(count->getValue(), initialCount + 1);
}

TEST_P(RecomputeLifecycleTest, ObjectCompletionCanPropagateDerivedProperties)
{
    auto* derived = static_cast<App::PropertyInteger*>(
        feature->addDynamicProperty("App::PropertyInteger", "Derived")
    );
    bool propagated = false;
    objectFinished = document->signalRecomputedObject.connect([&](const App::DocumentObject&) {
        checkBoundary();
        derived->setValue(42);
        propagated = true;
    });

    EXPECT_TRUE(recompute());
    EXPECT_TRUE(propagated);
    EXPECT_EQ(derived->getValue(), 42);
}

TEST_P(RecomputeLifecycleTest, FeatureFailureIsNotReportedAsSuccess)
{
    document->removeObject(feature);
    feature = document->addObject("App::FeatureTest", "Feature");
    auto* exception = static_cast<App::PropertyInteger*>(feature->getPropertyByName("ExceptionType"));
    ASSERT_NE(exception, nullptr);
    exception->setValue(2);
    feature->enforceRecompute();

    EXPECT_FALSE(recompute());
    EXPECT_FALSE(App::Document::isAnyRecomputing());
    EXPECT_TRUE(feature->isError());
    exception->setValue(0);
    feature->enforceRecompute();
    EXPECT_TRUE(recompute());
}

TEST_P(RecomputeLifecycleTest, ExplicitDependencyExecutionKeepsTheOuterBoundary)
{
    document->removeObject(feature);
    auto* executing = new CallbackFeature;
    document->addObject(executing, "Executing");
    feature = executing;
    auto* dependency = document->addObject("App::FeatureTest", "Dependency");
    auto* count = static_cast<App::PropertyInteger*>(dependency->getPropertyByName("ExecCount"));
    ASSERT_NE(count, nullptr);
    const long initialCount = count->getValue();
    int stableCount = 0;
    stable = document->signalBecameStable.connect([&](const App::Document&) { ++stableCount; });
    executing->callback = [&]() {
        checkBoundary();
        EXPECT_THROW(document->recomputeFeature(dependency), Base::RuntimeError);
        EXPECT_THROW(document->recomputeFeatureForDependency(executing), Base::RuntimeError);
        EXPECT_TRUE(document->recomputeFeatureForDependency(dependency));
        EXPECT_EQ(count->getValue(), initialCount + 1);
        EXPECT_EQ(stableCount, 0);
        checkBoundary();
    };
    feature->enforceRecompute();

    EXPECT_TRUE(recompute());
    EXPECT_EQ(stableCount, 1);
    EXPECT_FALSE(App::Document::isAnyRecomputing());
}

TEST_P(RecomputeLifecycleTest, InternalCleanupWaitsUntilComputationFinishes)
{
    auto* helper = document->addObject("App::FeaturePython", "Helper");
    const std::string helperName = helper->getNameInDocument();
    before = document->signalBeforeRecompute.connect([&](const App::Document&) {
        document->removeObjectAfterRecompute(helperName.c_str());
        EXPECT_EQ(document->getObject(helperName.c_str()), helper);
    });
    objectFinished = document->signalRecomputedObject.connect([&](const App::DocumentObject&) {
        EXPECT_EQ(document->getObject(helperName.c_str()), helper);
    });

    EXPECT_TRUE(recompute());
    EXPECT_EQ(document->getObject(helperName.c_str()), nullptr);
}

TEST_P(RecomputeLifecycleTest, CompletionObserverExceptionRestoresPendingFlags)
{
    int stableCount = 0;
    stable = document->signalBecameStable.connect([&](const App::Document&) { ++stableCount; });
    objectFinished = document->signalRecomputedObject.connect([](const App::DocumentObject&) {
        throw std::runtime_error("Observer failure");
    });

    EXPECT_THROW(recompute(), std::runtime_error);
    EXPECT_EQ(stableCount, 1);
    EXPECT_FALSE(document->testStatus(App::Document::Recomputing));
    EXPECT_FALSE(feature->testStatus(App::ObjectStatus::PendingRecompute));
    EXPECT_FALSE(App::Document::isAnyRecomputing());
    objectFinished.disconnect();
    feature->enforceRecompute();
    EXPECT_TRUE(recompute());
}

TEST_P(RecomputeLifecycleTest, StableObserverCanCloseDocumentAfterAllCleanup)
{
    bool closed = false;
    stable = document->signalBecameStable.connect([&](const App::Document&) {
        closed = App::GetApplication().closeDocument(name.c_str());
    });

    EXPECT_TRUE(recompute());
    EXPECT_TRUE(closed);
    EXPECT_EQ(App::GetApplication().getDocument(name.c_str()), nullptr);
    EXPECT_FALSE(App::Document::isAnyRecomputing());
    document = nullptr;
    feature = nullptr;
}

INSTANTIATE_TEST_SUITE_P(
    AllEntryPoints,
    RecomputeLifecycleTest,
    testing::Values(RecomputeMode::Document, RecomputeMode::Feature, RecomputeMode::RecursiveFeature)
);
