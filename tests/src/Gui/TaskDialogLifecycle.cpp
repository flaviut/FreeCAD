#include <QCoreApplication>
#include <QPointer>
#include <QTest>
#include <QScopeGuard>
#include <QThread>

#include <functional>
#include <stdexcept>
#include <future>
#include <chrono>

#include <App/Application.h>
#include <App/Document.h>
#include <Base/Exception.h>
#include <Gui/TaskView/TaskDialog.h>
#include <src/App/InitApplication.h>

class CallbackDialog: public Gui::TaskView::TaskDialog
{
public:
    bool accept() override
    {
        ++acceptCount;
        return callback ? callback() : true;
    }

    bool reject() override
    {
        ++rejectCount;
        return callback ? callback() : true;
    }

    std::function<bool()> callback;
    int acceptCount = 0;
    int rejectCount = 0;
};

class TaskDialogLifecycleTest: public QObject
{
    Q_OBJECT

private Q_SLOTS:
    void initTestCase()
    {
        tests::initApplication();
    }

    void init()
    {
        name = App::GetApplication().getUniqueDocumentName("TaskDialogLifecycle");
        document = App::GetApplication().newDocument(name.c_str());
        feature = document->addObject("App::FeaturePython", "Feature");
        feature->enforceRecompute();
    }

    void cleanup()
    {
        connection.disconnect();
        App::GetApplication().closeDocument(name.c_str());
    }

    void nestedCloseCannotClearOuterProtection_data()
    {
        QTest::addColumn<bool>("accepting");
        QTest::addColumn<bool>("nestedAccepting");
        QTest::newRow("accept-accept") << true << true;
        QTest::newRow("accept-reject") << true << false;
        QTest::newRow("reject-accept") << false << true;
        QTest::newRow("reject-reject") << false << false;
    }

    void nestedCloseCannotClearOuterProtection()
    {
        QFETCH(bool, accepting);
        QFETCH(bool, nestedAccepting);
        CallbackDialog dialog;
        bool protectedAfterNested = false;
        bool nestedSkipped = false;
        dialog.callback = [&]() {
            nestedSkipped = !dialog.tryClose(nestedAccepting).has_value();
            protectedAfterNested = dialog.property("taskview_accept_or_reject").isValid();
            return true;
        };

        const auto result = dialog.tryClose(accepting);
        QVERIFY(result.has_value());
        QVERIFY(*result);
        QVERIFY(nestedSkipped);
        QVERIFY(protectedAfterNested);
        QCOMPARE(dialog.acceptCount, accepting ? 1 : 0);
        QCOMPARE(dialog.rejectCount, accepting ? 0 : 1);
        QVERIFY(!dialog.property("taskview_accept_or_reject").isValid());
    }

    void callbackExceptionRestoresCloseProtection()
    {
        CallbackDialog dialog;
        dialog.callback = []() -> bool {
            throw std::runtime_error("Close failure");
        };
        QVERIFY_EXCEPTION_THROWN(dialog.tryClose(true), std::runtime_error);
        QVERIFY(!dialog.property("taskview_accept_or_reject").isValid());
        dialog.callback = {};
        QVERIFY(dialog.tryClose(false).value());
    }

    void callbackDeletionDoesNotAccessDestroyedDialog()
    {
        QPointer<CallbackDialog> dialog = new CallbackDialog;
        dialog->callback = [&]() {
            delete dialog.data();
            return true;
        };
        const auto result = dialog->tryClose(true);
        QVERIFY(result.has_value());
        QVERIFY(dialog.isNull());
    }

    void closeRequestWaitsUntilRecomputeCallerReturns_data()
    {
        QTest::addColumn<bool>("accepting");
        QTest::addColumn<bool>("recursive");
        QTest::newRow("accept-feature") << true << false;
        QTest::newRow("reject-feature") << false << false;
        QTest::newRow("accept-document") << true << true;
        QTest::newRow("reject-document") << false << true;
    }

    void closeRequestWaitsUntilRecomputeCallerReturns()
    {
        QFETCH(bool, accepting);
        QFETCH(bool, recursive);
        CallbackDialog dialog;
        bool deferred = false;
        bool skipped = false;
        bool callerReturned = false;
        bool ranAfterReturn = false;
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            skipped = !dialog.tryClose(accepting).has_value();
            deferred = dialog.deferUntilStable([&]() {
                ranAfterReturn = callerReturned;
                dialog.tryClose(accepting);
            });
        });
        QVERIFY(document->recomputeFeature(feature, recursive));
        callerReturned = true;
        QVERIFY(deferred);
        QVERIFY(skipped);
        QCOMPARE(dialog.acceptCount + dialog.rejectCount, 0);
        QTRY_VERIFY(ranAfterReturn);
        QCOMPARE(dialog.acceptCount, accepting ? 1 : 0);
        QCOMPARE(dialog.rejectCount, accepting ? 0 : 1);
    }

    void firstDeferredActionWins()
    {
        CallbackDialog dialog;
        int firstCount = 0;
        int secondCount = 0;
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            dialog.deferUntilStable([&]() { ++firstCount; });
            dialog.deferUntilStable([&]() { ++secondCount; });
        });
        QVERIFY(document->recomputeFeature(feature));
        QTRY_COMPARE(firstCount, 1);
        QCOMPARE(secondCount, 0);
    }

    void destroyingDialogCancelsDeferredAction()
    {
        auto* dialog = new CallbackDialog;
        int actionCount = 0;
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            dialog->deferUntilStable([&]() { ++actionCount; });
            delete dialog;
        });
        QVERIFY(document->recomputeFeature(feature));
        QCoreApplication::processEvents();
        QCOMPARE(actionCount, 0);
    }

    void failedRecomputeStillReleasesDeferredAction()
    {
        CallbackDialog dialog;
        int actionCount = 0;
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            dialog.deferUntilStable([&]() { ++actionCount; });
            throw std::runtime_error("Recompute observer failure");
        });
        QVERIFY_EXCEPTION_THROWN(document->recomputeFeature(feature), std::runtime_error);
        QCOMPARE(actionCount, 0);
        QTRY_COMPARE(actionCount, 1);
    }

    void destroyingDialogAfterCompletionCancelsQueuedAction()
    {
        auto* dialog = new CallbackDialog;
        int actionCount = 0;
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            dialog->deferUntilStable([&]() { ++actionCount; });
        });
        QVERIFY(document->recomputeFeature(feature));
        delete dialog;
        QCoreApplication::processEvents();
        QCOMPARE(actionCount, 0);
    }

    void workerNotificationRestrictsEditsOnMainThreadAndReturnsExceptionsToWorker()
    {
        App::MainThreadSignalConfig::setHooks(
            []() { return QThread::currentThread() == qApp->thread(); },
            [](std::function<void()>&& callback, bool blocking) {
                QMetaObject::invokeMethod(
                    qApp,
                    std::move(callback),
                    blocking ? Qt::BlockingQueuedConnection : Qt::QueuedConnection
                );
            }
        );
        const auto restore = qScopeGuard([]() {
            App::MainThreadSignalConfig::setHooks(nullptr, nullptr);
        });
        const std::string label = feature->Label.getValue();
        bool notifiedOnMainThread = false;
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            notifiedOnMainThread = QThread::currentThread() == qApp->thread();
            feature->Label.setValue("Forbidden edit");
        });
        auto result = std::async(std::launch::async, [&]() {
            try {
                document->recomputeFeature(feature);
                return false;
            }
            catch (const Base::RuntimeError&) {
                return true;
            }
        });
        QTRY_VERIFY_WITH_TIMEOUT(
            result.wait_for(std::chrono::milliseconds(0)) == std::future_status::ready,
            3000
        );
        QVERIFY(result.get());
        QVERIFY(notifiedOnMainThread);
        QCOMPARE(feature->Label.getValue(), label);
        QVERIFY(!App::Document::isAnyRecomputing());
        feature->Label.setValue("Allowed edit");
        QCOMPARE(feature->Label.getValue(), std::string("Allowed edit"));
    }

    void internalCleanupWaitsUntilRecomputeCallerReturns()
    {
        auto* helper = document->addObject("App::FeaturePython", "Helper");
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            document->removeObjectAfterRecompute("Helper");
        });
        QVERIFY(document->recomputeFeature(feature));
        QCOMPARE(document->getObject("Helper"), helper);
        QCoreApplication::processEvents();
        QCOMPARE(document->getObject("Helper"), nullptr);
    }

    void deferredCleanupDoesNotDeleteReplacementObject()
    {
        document->addObject("App::FeaturePython", "Helper");
        connection = document->signalBeforeRecompute.connect([&](const App::Document&) {
            document->removeObjectAfterRecompute("Helper");
        });
        QVERIFY(document->recomputeFeature(feature));
        document->removeObject("Helper");
        auto* replacement = document->addObject("App::FeaturePython", "Helper");
        QCoreApplication::processEvents();
        QCOMPARE(document->getObject("Helper"), replacement);
    }

    void stableObserverCannotDeleteOwnerBeforeRecomputeReturns()
    {
        QPointer<CallbackDialog> owner = new CallbackDialog;
        bool callerReturned = false;
        bool deletedAfterReturn = false;
        connection = document->signalBecameStable.connect([&](const App::Document&) {
            deletedAfterReturn = callerReturned;
            delete owner.data();
        });
        QVERIFY(document->recomputeFeature(feature));
        QVERIFY(owner);
        callerReturned = true;
        QTRY_VERIFY(owner.isNull());
        QVERIFY(deletedAfterReturn);
    }

    void staleStableNotificationDoesNotReachReplacementDocument()
    {
        const auto identity = document->Uid.getValue();
        bool oldNotified = false;
        bool replacementNotified = false;
        connection = document->signalBecameStable.connect([&](const App::Document&) {
            oldNotified = true;
        });
        QVERIFY(document->recomputeFeature(feature));
        QVERIFY(App::GetApplication().closeDocument(name.c_str()));
        document = App::GetApplication().newDocument(name.c_str());
        document->Uid.setValue(identity);
        auto replacement = document->signalBecameStable.connect([&](const App::Document&) {
            replacementNotified = true;
        });
        const auto disconnect = qScopeGuard([&]() { replacement.disconnect(); });
        QCoreApplication::processEvents();
        QVERIFY(!oldNotified);
        QVERIFY(!replacementNotified);
    }

private:
    std::string name;
    App::Document* document = nullptr;
    App::DocumentObject* feature = nullptr;
    fastsignals::connection connection;
};

QTEST_GUILESS_MAIN(TaskDialogLifecycleTest)

#include "TaskDialogLifecycle.moc"
