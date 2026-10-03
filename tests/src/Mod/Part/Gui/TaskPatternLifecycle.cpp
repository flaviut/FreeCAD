#include <QApplication>
#include <QCoreApplication>
#include <QPointer>
#include <QScopeGuard>
#include <QTest>
#include <QThread>
#include <QTimer>
#include <QWidget>

#include <App/Application.h>
#include <App/Document.h>
#include <Base/Interpreter.h>
#include <Gui/ProgressBar.h>
#include <Mod/Part/App/LinkArrayPath.h>
#include <Mod/Part/Gui/TaskPatternParameters.h>
#include <src/App/InitApplication.h>

struct PreviewState
{
    bool finished = false;
    bool deletedDuringRecompute = false;
};

class PatternPanel: public QWidget, public PartGui::TaskPatternParameters
{
public:
    PatternPanel(Part::LinkArrayPath* object, App::DocumentObject* feature, PreviewState& state)
        : object(object)
        , feature(feature)
        , state(state)
    {
        auto* placeholder = new QWidget(this);
        setupPathPatternParameterUI(
            this,
            placeholder,
            this,
            &object->Path,
            &object->Count,
            &object->SpacingMode,
            &object->Spacing,
            &object->StartOffset,
            &object->EndOffset,
            &object->ReversePath,
            &object->Align
        );
        kickUpdateViewTimer();
    }

    ~PatternPanel() override
    {
        cancelPendingUpdate();
    }

protected:
    App::DocumentObject* getPatternObject() const override
    {
        return object;
    }
    void fillDirectionCombo(Gui::ComboLinks&, Part::LinearPatternDirection) override
    {}
    void onReferenceSelectionRequested() override
    {}
    void onPatternParametersChanged() override
    {
        kickUpdateViewTimer();
    }
    void setupPatternTransaction() override
    {}

    void recomputePatternFeature() override
    {
        QPointer<PatternPanel> alive(this);
        auto* result = &state;
        QTimer::singleShot(0, qApp, [this]() { delete this; });
        feature->getDocument()->recompute({feature}, true);
        result->deletedDuringRecompute = alive.isNull();
        result->finished = true;
    }

private:
    Part::LinkArrayPath* object;
    App::DocumentObject* feature;
    PreviewState& state;
};

class TaskPatternLifecycleTest: public QObject
{
    Q_OBJECT

private Q_SLOTS:
    void queuedDeletionWaitsForPreview()
    {
        tests::initApplication();
        Base::Interpreter().loadModule("Part");
        Gui::SequencerBar::instance()->getProgressBar();
        auto parameters = App::GetApplication().GetParameterGroupByPath(
            "User parameter:BaseApp/Preferences/Document"
        );
        const bool canAbort = parameters->GetBool("CanAbortRecompute", true);
        parameters->SetBool("CanAbortRecompute", true);
        const auto restore = qScopeGuard([parameters, canAbort]() {
            parameters->SetBool("CanAbortRecompute", canAbort);
        });
        auto* document = App::GetApplication().newDocument("PatternLifecycle");
        const auto close = qScopeGuard([document]() {
            App::GetApplication().closeDocument(document->getName());
        });
        auto* object = document->addObject<Part::LinkArrayPath>("PathPattern");
        auto* feature = document->addObject("App::FeaturePython", "SlowFeature");
        feature->enforceRecompute();
        bool recomputedFeature = false;
        auto connection = document->signalRecomputedObject.connect(
            [feature, &recomputedFeature](const App::DocumentObject& recomputed) {
                if (&recomputed == feature) {
                    recomputedFeature = true;
                    QThread::msleep(120);
                }
            }
        );
        const auto disconnect = qScopeGuard([&connection]() { connection.disconnect(); });

        PreviewState state;
        QPointer<PatternPanel> panel = new PatternPanel(object, feature, state);
        const auto cleanup = qScopeGuard([&panel]() { delete panel.data(); });
        QTRY_VERIFY_WITH_TIMEOUT(state.finished, 3000);
        QVERIFY(recomputedFeature);
        QVERIFY(!state.deletedDuringRecompute);
        QTRY_VERIFY_WITH_TIMEOUT(panel.isNull(), 3000);
    }
};

QTEST_MAIN(TaskPatternLifecycleTest)

#include "TaskPatternLifecycle.moc"
