// SPDX-License-Identifier: LGPL-2.1-or-later

#include <algorithm>
#include <memory>

#include <QAbstractAnimation>
#include <QApplication>
#include <QCheckBox>
#include <QComboBox>
#include <QDir>
#include <QFile>
#include <QFontDatabase>
#include <QGridLayout>
#include <QGroupBox>
#include <QHeaderView>
#include <QImage>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QRadioButton>
#include <QScopeGuard>
#include <QScrollBar>
#include <QSet>
#include <QStyleFactory>
#include <QTest>
#include <QTextStream>

#include <App/Application.h>
#include <App/Document.h>
#include <App/DocumentObject.h>
#include <App/Expression.h>
#include <App/ObjectIdentifier.h>
#include <App/PropertyStandard.h>
#include <Base/UnitsApi.h>
#include <Gui/ElideCheckBox.h>
#include <Gui/InputField.h>
#include <Gui/QuantitySpinBox.h>
#include <Gui/propertyeditor/PropertyEditor.h>
#include <src/App/InitApplication.h>

#include "ComponentZooCases.h"

namespace
{
using namespace Gui::PropertyEditor;

enum class Theme
{
    Light,
    Dark
};
enum class State
{
    Editable,
    ReadOnly,
    Expression,
    ReadOnlyExpression
};

QPalette paletteFor(Theme theme)
{
    QPalette palette = QApplication::style()->standardPalette();
    const QColor text = theme == Theme::Dark ? QColor("#eeeeee") : QColor("#202020");
    const QColor window = theme == Theme::Dark ? QColor("#353535") : QColor("#efefef");
    const QColor base = theme == Theme::Dark ? QColor("#252525") : QColor("#ffffff");

    for (auto group : {QPalette::Active, QPalette::Inactive, QPalette::Disabled}) {
        palette.setColor(group, QPalette::Window, window);
        palette.setColor(group, QPalette::Base, base);
        palette.setColor(group, QPalette::AlternateBase, window);
        palette.setColor(group, QPalette::Button, window);
        palette.setColor(group, QPalette::Text, text);
        palette.setColor(group, QPalette::WindowText, text);
        palette.setColor(group, QPalette::ButtonText, text);
        palette.setColor(group, QPalette::BrightText, text);
        palette.setColor(group, QPalette::Link, QColor("#3288ed"));
        palette.setColor(group, QPalette::Highlight, QColor("#305b88"));
        palette.setColor(group, QPalette::HighlightedText, Qt::white);
    }
    for (auto role : {QPalette::Text, QPalette::WindowText, QPalette::ButtonText}) {
        palette.setColor(QPalette::Disabled, role, QColor("#888888"));
    }
    return palette;
}

void fillProperties(App::DocumentObject* object, PropertyModel::PropertyList& properties)
{
    for (auto state :
         {State::Editable, State::ReadOnly, State::Expression, State::ReadOnlyExpression}) {
        const char* group = state == State::Editable ? "Editable"
            : state == State::ReadOnly               ? "Read-only"
            : state == State::Expression             ? "Expression"
                                                     : "Read-only expression";
        const std::string prefix = state == State::Editable ? "Editable"
            : state == State::ReadOnly                      ? "Locked"
            : state == State::Expression                    ? "Bound"
                                                            : "LockedBound";

        for (const std::string suffix : {"False", "True", "Integer", "Float", "String"}) {
            const std::string name = prefix + suffix;
            const std::string kind = suffix == "Integer" ? "Integer"
                : suffix == "Float"                      ? "Float"
                : suffix == "String"                     ? "String"
                                                         : "Bool";
            auto* property
                = object->addDynamicProperty(("App::Property" + kind).c_str(), name.c_str(), group);
            const char* expression = "42";
            if (auto* value = dynamic_cast<App::PropertyBool*>(property)) {
                value->setValue(suffix == "True");
                expression = value->getValue() ? "1" : "0";
            }
            if (auto* value = dynamic_cast<App::PropertyInteger*>(property)) {
                value->setValue(42);
            }
            if (auto* value = dynamic_cast<App::PropertyFloat*>(property)) {
                value->setValue(12.5);
                expression = "12.5";
            }
            if (auto* value = dynamic_cast<App::PropertyString*>(property)) {
                value->setValue("Sample text");
                expression = "<<Sample text>>";
            }
            if (state == State::Expression || state == State::ReadOnlyExpression) {
                object->setExpression(
                    App::ObjectIdentifier(*property),
                    App::Expression::parse(object, expression)
                );
            }
            property->setStatus(
                App::Property::ReadOnly,
                state == State::ReadOnly || state == State::ReadOnlyExpression
            );
            properties.emplace_back(name, std::vector<App::Property*> {property});
        }
    }
}

const QStringList pages {
    "buttons",
    "text",
    "numbers",
    "labels",
    "views",
    "containers",
    "property-states",
    "property-scalars",
    "property-geometry",
    "property-collections"
};

QWidget* controls(const std::vector<Zoo::WidgetCase>& cases)
{
    auto* sheet = new QWidget;
    auto* grid = new QGridLayout(sheet);
    grid->addWidget(new QLabel(QStringLiteral("Component")), 0, 0);
    grid->addWidget(new QLabel(QStringLiteral("Enabled")), 0, 1);
    grid->addWidget(new QLabel(QStringLiteral("Disabled")), 0, 2);
    grid->setColumnMinimumWidth(0, 290);
    grid->setColumnMinimumWidth(1, 340);
    grid->setColumnMinimumWidth(2, 340);

    int row = 1;
    for (const auto& sample : cases) {
        for (int column : {1, 2}) {
            auto* widget = sample.make();
            widget->setEnabled(column == 1);
            const int width = std::min(widget->maximumWidth(), 340);
            widget->setMaximumWidth(width);
            widget->setMinimumWidth(std::min(width, 260));
            widget->setProperty("expectedBinding", QString::fromUtf8(sample.variant) == "bound");
            grid->addWidget(widget, row, column);
            if (column != 1) {
                continue;
            }
            const QString type = QString::fromUtf8(widget->metaObject()->className());
            const QString variant = QString::fromUtf8(sample.variant);
            auto* label = new QLabel(variant.isEmpty() ? type : type + "\n" + variant);
            grid->addWidget(label, row, 0);
        }
        ++row;
    }
    return sheet;
}

PropertyEditor* propertyView(QWidget* parent, PropertyModel::PropertyList properties)
{
    auto* view = new PropertyEditor(parent);
    view->setGroupBackground(parent->palette().color(QPalette::Window));
    view->setGroupTextColor(parent->palette().color(QPalette::Text));
    view->setProperty("caseCount", static_cast<int>(properties.size()));
    view->buildUp(std::move(properties));
    view->expandAll();
    view->header()->setSectionResizeMode(QHeaderView::Fixed);
    view->header()->resizeSection(0, 240);
    view->header()->setStretchLastSection(true);
    view->setFixedWidth(600);
    return view;
}

void fitTree(PropertyEditor* view)
{
    int height = 2 * view->frameWidth() + 4;
    const auto visit = [&](auto&& self, const QModelIndex& parent) -> void {
        for (int row = 0; row < view->model()->rowCount(parent); ++row) {
            const auto index = view->model()->index(row, 0, parent);
            height += view->sizeHintForIndex(index).height();
            if (view->isExpanded(index)) {
                self(self, index);
            }
        }
    };
    visit(visit, QModelIndex());
    view->setFixedHeight(height);
}

QWidget* propertySheet(App::DocumentObject* object, const std::vector<Zoo::PropertyCase>& cases)
{
    auto* sheet = new QWidget;
    auto* grid = new QGridLayout(sheet);
    for (int column : {0, 1}) {
        const std::string prefix = column == 0 ? "Normal" : "ReadOnly";
        PropertyModel::PropertyList properties;
        for (const auto& sample : cases) {
            const std::string name = prefix + sample.name;
            auto* property = object->addDynamicProperty(sample.type.c_str(), name.c_str(), "Values");
            sample.setup(*property);
            property->setStatus(App::Property::ReadOnly, column == 1);
            properties.emplace_back(name, std::vector<App::Property*> {property});
        }
        grid->addWidget(
            new QLabel(column == 0 ? QStringLiteral("Editable") : QStringLiteral("Read-only")),
            0,
            column
        );
        grid->addWidget(propertyView(sheet, std::move(properties)), 1, column);
    }
    return sheet;
}

QImage renderSheet(QWidget* sheet)
{
    // Capture the final state, not a frame of a clear-button fade or another transition.
    for (auto* animation : sheet->findChildren<QAbstractAnimation*>()) {
        if (animation->state() == QAbstractAnimation::Running && animation->totalDuration() > 0) {
            animation->setCurrentTime(animation->totalDuration());
        }
    }
    QApplication::processEvents();

    QImage image(sheet->size(), QImage::Format_ARGB32);
    image.setDotsPerMeterX(3780);
    image.setDotsPerMeterY(3780);
    image.fill(Qt::transparent);
    sheet->render(&image);
    return image;
}

QString directory(const char* variable, const char* fallback)
{
    const QString value = qEnvironmentVariable(variable);
    return value.isEmpty() ? QString::fromUtf8(fallback) : value;
}
}  // namespace

class ComponentZoo: public QObject
{
    Q_OBJECT

private Q_SLOTS:
    void initTestCase()
    {
        tests::initApplication();
        Base::UnitsApi::setSchema("Internal");
        PropertyStringItem::init();
        PropertyFontItem::init();
        PropertyIntegerItem::init();
        PropertyIntegerConstraintItem::init();
        PropertyFloatItem::init();
        PropertyUnitItem::init();
        PropertyFloatConstraintItem::init();
        PropertyPrecisionItem::init();
        PropertyUnitConstraintItem::init();
        PropertyAngleItem::init();
        PropertyBoolItem::init();
        PropertyVectorItem::init();
        PropertyVectorListItem::init();
        PropertyVectorDistanceItem::init();
        PropertyPositionItem::init();
        PropertyDirectionItem::init();
        PropertyMatrixItem::init();
        PropertyPlacementItem::init();
        PropertyRotationItem::init();
        PropertyEnumItem::init();
        PropertyStringListItem::init();
        PropertyFloatListItem::init();
        PropertyIntegerListItem::init();
        PropertyColorItem::init();
        PropertyMaterialItem::init();
        PropertyMaterialListItem::init();
        PropertyFileItem::init();
        PropertyPathItem::init();
        PropertyTransientFileItem::init();
        PropertyLinkItem::init();
        PropertyLinkListItem::init();
        PropertyMapItem::init();
        QApplication::setStyle(QStyleFactory::create(QStringLiteral("Fusion")));
        QLocale::setDefault(QLocale::c());

        const int id = QFontDatabase::addApplicationFont(QStringLiteral(ZOO_FONT));
        QVERIFY(id >= 0);
        const auto families = QFontDatabase::applicationFontFamilies(id);
        QVERIFY(!families.isEmpty());
        QFont font(families.front());
        font.setPixelSize(14);
        QApplication::setFont(font);
        QApplication::setCursorFlashTime(0);
    }

    void cleanupTestCase()
    {
        const QDir output(directory("FC_VISUAL_OUT_DIR", ZOO_OUTPUT));
        QFile gallery(output.filePath("index.html"));
        QVERIFY(gallery.open(QIODevice::WriteOnly | QIODevice::Truncate));
        QTextStream stream(&gallery);
        stream << "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\">"
                  "<title>Component zoo</title><style>"
                  "body{font:14px sans-serif}img{max-width:560px}"
                  "td{vertical-align:top}</style><h1>Component zoo</h1>";
        for (const auto& name : captures) {
            stream << "<h2>" << name << "</h2><table><tr>";
            for (const auto& folder : {"expected", "actual", "diff"}) {
                const QString file = QStringLiteral("%1/%2.png").arg(folder, name);
                stream << "<td>" << folder << "<br>";
                if (output.exists(file)) {
                    stream << "<a href=\"" << file << "\"><img src=\"" << file << "\"></a>";
                }
                stream << "</td>";
            }
            stream << "</tr></table>";
        }
        stream << "</html>\n";

        if (captures.size() != pages.size() * 2) {
            return;
        }
        for (const auto& type : PropertyItemFactory::instance().CanProduce()) {
            const QString name = QString::fromStdString(type);
            if (name == "Gui::PropertyEditor::PropertyItem"
                || name == "Gui::PropertyEditor::PropertySeparatorItem") {
                continue;
            }
            QVERIFY2(covered.contains(name), qPrintable("No rendered fixture for " + name));
        }
    }

    void snapshots_data()
    {
        QTest::addColumn<QString>("page");
        QTest::addColumn<bool>("dark");
        for (const auto& page : pages) {
            for (bool dark : {false, true}) {
                const auto tag = (page + (dark ? "-dark" : "-light")).toUtf8();
                QTest::newRow(tag.constData()) << page << dark;
            }
        }
    }

    void snapshots()
    {
        try {
            capture();
        }
        catch (const Base::Exception& error) {
            QFAIL(error.what());
        }
    }

private:
    void capture()
    {
        QFETCH(QString, page);
        QFETCH(bool, dark);
        const QString snapshot = QString::fromUtf8(QTest::currentDataTag());
        captures.append(snapshot);
        QApplication::setPalette(paletteFor(dark ? Theme::Dark : Theme::Light));

        auto& app = App::GetApplication();
        const auto name = app.getUniqueDocumentName("ComponentZoo");
        auto* document = app.newDocument(name.c_str(), "testUser");
        const auto close = qScopeGuard([&] { app.closeDocument(name.c_str()); });
        auto* object = document->addObject("App::VarSet", "Values");
        PropertyModel::PropertyList properties;
        fillProperties(object, properties);
        auto* length = static_cast<App::PropertyLength*>(
            object->addDynamicProperty("App::PropertyLength", "Length")
        );
        length->setValue(12.5);
        auto* bound = object->addDynamicProperty("App::PropertyLength", "BoundLength");
        object->setExpression(App::ObjectIdentifier(*bound), App::Expression::parse(object, "Length"));
        object->addDynamicProperty("App::PropertyMap", "Map");
        auto* target = document->addObject("App::VarSet", "Target");
        target->Label.setValue("Linked object");
        document->recompute();

        std::unique_ptr<QWidget> zoo;
        if (page == "property-states") {
            zoo = std::make_unique<QWidget>();
            auto* grid = new QGridLayout(zoo.get());
            grid->addWidget(propertyView(zoo.get(), std::move(properties)));
        }
        else if (page == "property-scalars") {
            zoo.reset(propertySheet(object, Zoo::scalars()));
        }
        else if (page == "property-geometry") {
            zoo.reset(propertySheet(object, Zoo::geometry()));
        }
        else if (page == "property-collections") {
            zoo.reset(propertySheet(object, Zoo::collections(target)));
        }
        else {
            const auto cases = page == "buttons" ? Zoo::buttons()
                : page == "text"                 ? Zoo::text(object)
                : page == "numbers"              ? Zoo::numbers(object)
                : page == "labels"               ? Zoo::labels()
                : page == "views"                ? Zoo::views(object)
                                                 : Zoo::containers();
            zoo.reset(controls(cases));
        }
        zoo->setLayoutDirection(Qt::LeftToRight);
        zoo->ensurePolished();
        for (auto* view : zoo->findChildren<PropertyEditor*>()) {
            fitTree(view);
        }
        zoo->resize(zoo->layout()->sizeHint());
        zoo->layout()->activate();

        // Scroll areas need show events to lay out; keep the entire lifecycle offscreen.
        zoo->setAttribute(Qt::WA_DontShowOnScreen);
        zoo->show();
        zoo->setFocus();
        QApplication::processEvents();
        auto image = renderSheet(zoo.get());
        for (auto* view : zoo->findChildren<PropertyEditor*>()) {
            view->setFixedHeight(view->height() + view->verticalScrollBar()->maximum());
        }
        zoo->resize(zoo->layout()->sizeHint());
        zoo->layout()->activate();
        QApplication::processEvents();
        // InputField::showEvent() restores formatted text, so apply invalid edits afterward.
        for (auto* field : zoo->findChildren<Gui::InputField*>()) {
            const QVariant invalid = field->property("invalidText");
            if (!invalid.isValid()) {
                continue;
            }
            field->setText(invalid.toString());
            QVERIFY(!field->hasAcceptableInput());
        }
        image = renderSheet(zoo.get());

        int expressions = 0;
        for (auto* view : zoo->findChildren<PropertyEditor*>()) {
            int count = 0;
            auto* model = view->model();
            for (int group = 0; group < model->rowCount(); ++group) {
                const auto parent = model->index(group, 0);
                for (int row = 0; row < model->rowCount(parent); ++row) {
                    ++count;
                    const auto index = model->index(row, 1, parent);
                    auto* item = static_cast<PropertyItem*>(index.internalPointer());
                    QVERIFY(!item->getPropertyData().empty());
                    covered.insert(QString::fromUtf8(item->metaObject()->className()));
                    if (item->hasExpression()) {
                        ++expressions;
                        QVERIFY(index.data(Qt::ForegroundRole).isValid());
                    }
                }
            }
            QCOMPARE(count, view->property("caseCount").toInt());
            QCOMPARE(view->verticalScrollBar()->maximum(), 0);
        }
        QCOMPARE(expressions, page == "property-states" ? 10 : 0);
        for (auto* widget : zoo->findChildren<QWidget*>()) {
            if (!widget->property("expectedBinding").toBool()) {
                continue;
            }
            auto* binding = dynamic_cast<Gui::ExpressionBinding*>(widget);
            QVERIFY(binding);
            QVERIFY(binding->hasExpression());
        }

        for (auto* renderer : zoo->findChildren<QSvgRenderer*>()) {
            QVERIFY(renderer->isValid());
        }
        compare(image, snapshot);
    }

private:
    QStringList captures;
    QSet<QString> covered;

    void compare(const QImage& actual, const QString& name)
    {
        const QDir output(directory("FC_VISUAL_OUT_DIR", ZOO_OUTPUT));
        const QDir baselines(directory("FC_VISUAL_BASELINE_DIR", ZOO_BASELINES));
        for (const auto& folder : {"expected", "diff"}) {
            const QString file = output.filePath(QStringLiteral("%1/%2.png").arg(folder, name));
            QVERIFY(!QFile::exists(file) || QFile::remove(file));
        }
        QVERIFY(QDir().mkpath(output.filePath("actual")));
        QVERIFY(actual.save(output.filePath("actual/" + name + ".png")));

        const QString update = qEnvironmentVariable("FC_VISUAL_UPDATE_BASELINE").toLower();
        if (update == "1" || update == "true") {
            QVERIFY(QDir().mkpath(baselines.path()));
            QVERIFY(actual.save(baselines.filePath(name + ".png")));
            return;
        }
        if (qEnvironmentVariable("FC_VISUAL_MODE") == "record") {
            return;
        }

        const QImage expected(baselines.filePath(name + ".png"));
        QVERIFY2(
            !expected.isNull(),
            qPrintable("Missing baseline: " + baselines.filePath(name + ".png"))
        );
        QVERIFY(QDir().mkpath(output.filePath("expected")));
        QVERIFY(expected.save(output.filePath("expected/" + name + ".png")));
        QCOMPARE(actual.size(), expected.size());

        // Global image similarity can hide a regression confined to one small label.
        QImage diff(actual.size(), QImage::Format_ARGB32);
        int mismatches = 0;
        for (int y = 0; y < actual.height(); ++y) {
            for (int x = 0; x < actual.width(); ++x) {
                const QColor a = actual.pixelColor(x, y);
                const QColor e = expected.pixelColor(x, y);
                const int delta = std::max(
                    {std::abs(a.red() - e.red()),
                     std::abs(a.green() - e.green()),
                     std::abs(a.blue() - e.blue()),
                     std::abs(a.alpha() - e.alpha())}
                );
                mismatches += delta > 2;
                diff.setPixelColor(x, y, delta > 2 ? QColor(Qt::red) : a.darker(200));
            }
        }
        QVERIFY(QDir().mkpath(output.filePath("diff")));
        QVERIFY(diff.save(output.filePath("diff/" + name + ".png")));
        QVERIFY2(
            mismatches == 0,
            qPrintable(
                QStringLiteral("%1 changed pixels; artifacts: %2").arg(mismatches).arg(output.path())
            )
        );
    }
};

int main(int argc, char** argv)
{
    // Set the platform before QApplication so this executable cannot open desktop windows.
    qputenv("QT_QPA_PLATFORM", "offscreen");
    qputenv("QT_SCALE_FACTOR", "1");
    qputenv("QT_FONT_DPI", "96");
    QApplication application(argc, argv);
    ComponentZoo test;
    return QTest::qExec(&test, argc, argv);
}

#include "ComponentZoo.moc"
