#include <QCoreApplication>
#include <QScopeGuard>
#include <QTest>
#include <QThread>
#include <QTimer>

#include <memory>

#include <Base/Exception.h>
#include <Gui/ProgressBar.h>
#include <Gui/ProgressDialog.h>

class TestSequencerBar: public Gui::SequencerBar
{
public:
    TestSequencerBar() = default;
    ~TestSequencerBar() override = default;
    using Base::SequencerBase::next;
    using Base::SequencerBase::start;
    using Base::SequencerBase::stop;
    using Base::SequencerBase::tryToCancel;
};

class TestSequencerDialog: public Gui::SequencerDialog
{
public:
    TestSequencerDialog()
    {
        for (auto* widget : QApplication::topLevelWidgets()) {
            if (auto* progress = qobject_cast<Gui::ProgressDialog*>(widget)) {
                dialog.reset(progress);
                break;
            }
        }
    }
    ~TestSequencerDialog() override = default;
    using Base::SequencerBase::next;
    using Base::SequencerBase::start;
    using Base::SequencerBase::stop;
    using Base::SequencerBase::tryToCancel;

    Gui::ProgressDialog* getProgressDialog() const
    {
        return dialog.get();
    }

private:
    std::unique_ptr<Gui::ProgressDialog> dialog;
};

class ProgressSequencerTest: public QObject
{
    Q_OBJECT

private Q_SLOTS:
    void barDoesNotDispatchEvents_data()
    {
        QTest::addColumn<int>("steps");
        QTest::addColumn<bool>("checkAbort");
        QTest::newRow("determinate") << 10 << false;
        QTest::newRow("indeterminate") << 0 << false;
        QTest::newRow("abort-check") << 10 << true;
    }

    void barDoesNotDispatchEvents()
    {
        QFETCH(int, steps);
        QFETCH(bool, checkAbort);
        QWidget owner;
        TestSequencerBar instance;
        auto* sequencer = &instance;
        sequencer->getProgressBar(&owner);
        sequencer->start("Progress regression", steps);
        const auto stop = qScopeGuard([sequencer]() { sequencer->stop(); });

        QObject context;
        bool dispatched = false;
        QTimer::singleShot(0, &context, [&dispatched]() { dispatched = true; });
        QThread::msleep(checkAbort ? 550 : 120);
        if (checkAbort) {
            sequencer->checkAbort();
        }
        else {
            sequencer->next();
        }
        QVERIFY(!dispatched);
        sequencer->stop();
        QVERIFY(!dispatched);
        QCoreApplication::processEvents();
        QVERIFY(dispatched);
    }

    void barCancellationDoesNotDispatchEvents()
    {
        QWidget owner;
        TestSequencerBar instance;
        auto* sequencer = &instance;
        sequencer->getProgressBar(&owner);
        sequencer->start("Cancellation regression", 10);
        const auto stop = qScopeGuard([sequencer]() { sequencer->stop(); });

        QObject context;
        bool dispatched = false;
        QTimer::singleShot(0, &context, [&dispatched]() { dispatched = true; });
        sequencer->tryToCancel();
        QVERIFY_EXCEPTION_THROWN(sequencer->next(true), Base::AbortException);
        QVERIFY(!dispatched);
        QCoreApplication::processEvents();
        QVERIFY(dispatched);
    }

    void dialogDoesNotDispatchEvents_data()
    {
        QTest::addColumn<int>("steps");
        QTest::newRow("determinate") << 10;
        QTest::newRow("indeterminate") << 0;
    }

    void dialogDoesNotDispatchEvents()
    {
        QFETCH(int, steps);
        TestSequencerDialog instance;
        auto* sequencer = &instance;
        sequencer->start("Progress regression", steps);
        const auto stop = qScopeGuard([sequencer]() { sequencer->stop(); });

        auto* dialog = sequencer->getProgressDialog();
        QVERIFY(dialog);
        dialog->setMinimumDuration(0);
        dialog->show();

        QObject context;
        bool dispatched = false;
        QTimer::singleShot(0, &context, [&dispatched]() { dispatched = true; });
        QThread::msleep(550);
        sequencer->next();
        QThread::msleep(550);
        sequencer->next();
        QVERIFY(!dispatched);
        sequencer->stop();
        QVERIFY(!dispatched);
        QCoreApplication::processEvents();
        QVERIFY(dispatched);
    }

    void dialogCancellationDoesNotDispatchEvents()
    {
        TestSequencerDialog instance;
        auto* sequencer = &instance;
        sequencer->start("Cancellation regression", 10);
        const auto stop = qScopeGuard([sequencer]() { sequencer->stop(); });

        QObject context;
        bool dispatched = false;
        QTimer::singleShot(0, &context, [&dispatched]() { dispatched = true; });
        sequencer->tryToCancel();
        QVERIFY_EXCEPTION_THROWN(sequencer->next(true), Base::AbortException);
        QVERIFY(!dispatched);
        QCoreApplication::processEvents();
        QVERIFY(dispatched);
    }
};

QTEST_MAIN(ProgressSequencerTest)

#include "ProgressSequencer.moc"
