// SPDX-License-Identifier: LGPL-2.1-or-later

#include <algorithm>
#include <array>
#include <functional>
#include <map>
#include <memory>

#include <QAbstractAnimation>
#include <QApplication>
#include <QDialog>
#include <QEventLoop>
#include <QGridLayout>
#include <QGraphicsProxyWidget>
#include <QGraphicsView>
#include <QHeaderView>
#include <QImage>
#include <QLabel>
#include <QLineEdit>
#include <QScopeGuard>
#include <QTableView>
#include <QTimer>

#include <App/Application.h>
#include <App/Document.h>
#include <App/DocumentObject.h>
#include <Base/Interpreter.h>
#include <Gui/Application.h>
#include <Gui/Document.h>
#include <Gui/InputField.h>
#include <Gui/MainWindow.h>
#include <Gui/MDIView.h>
#include <Gui/ViewProvider.h>
#include <Gui/propertyeditor/PropertyEditor.h>
#include <Gui/PythonWrapper.h>

#include "ComponentZoo.h"
#include "ComponentZooCases.h"

namespace
{
using namespace Gui::PropertyEditor;

enum class Editors
{
    Closed,
    Open
};

QWidget* controls(const std::vector<Zoo::WidgetCase>& cases)
{
    auto* sheet = new QDialog;
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
            // Editor size hints can be smaller than the painted rows.
            height += view->visualRect(index).height();
            if (view->isExpanded(index)) {
                self(self, index);
            }
        }
    };
    visit(visit, QModelIndex());
    view->setFixedHeight(height);
}

// One tree per column, or one tree per property when each needs an open editor.
QWidget* propertySheet(const std::vector<Zoo::PropertyColumn>& columns, Editors editors)
{
    auto* sheet = new QDialog;
    auto* grid = new QGridLayout(sheet);
    for (int column = 0; column < static_cast<int>(columns.size()); ++column) {
        const auto& [title, properties] = columns[column];
        int row = 0;
        if (*title) {
            grid->addWidget(new QLabel(QString::fromUtf8(title)), row++, column);
        }

        if (editors == Editors::Closed) {
            PropertyModel::PropertyList list;
            for (auto* property : properties) {
                list.emplace_back(property->getName(), std::vector {property});
            }
            grid->addWidget(propertyView(sheet, std::move(list)), row, column);
            continue;
        }

        // Each view owns one active editor, as in the property panel.
        for (auto* property : properties) {
            auto* view = propertyView(sheet, {{property->getName(), {property}}});
            view->setProperty("activateEditor", column == 0);
            grid->addWidget(view, row++, column);
        }
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

void settleTheme()
{
    // Gui::ParamHandlers::addHandler() debounces changes for 100 ms; process its theme reload.
    QEventLoop loop;
    QTimer::singleShot(150, &loop, &QEventLoop::quit);
    loop.exec();
}

void openEditor(PropertyEditor* view)
{
    const auto visit = [&](auto&& self, const QModelIndex& parent) -> bool {
        for (int row = 0; row < view->model()->rowCount(parent); ++row) {
            const auto value = view->model()->index(row, 1, parent);
            if (value.flags() & Qt::ItemIsEditable) {
                view->openEditor(value);
                return true;
            }
            if (self(self, view->model()->index(row, 0, parent))) {
                return true;
            }
        }
        return false;
    };
    visit(visit, QModelIndex());
}

void prepare(QWidget* zoo)
{
    zoo->setLayoutDirection(Qt::LeftToRight);
    zoo->ensurePolished();
    zoo->resize(zoo->layout()->sizeHint());
    zoo->layout()->activate();

    // Scroll areas need show events to lay out; keep the entire lifecycle offscreen.
    zoo->setAttribute(Qt::WA_DontShowOnScreen);
    zoo->show();
    zoo->setFocus();
    QApplication::processEvents();
    for (auto* view : zoo->findChildren<PropertyEditor*>()) {
        if (view->property("activateEditor").toBool()) {
            openEditor(view);
        }
    }
    QApplication::processEvents();
    for (auto* view : zoo->findChildren<PropertyEditor*>()) {
        fitTree(view);
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
    }
}

QImage snapshot(QWidget* zoo)
{
    prepare(zoo);
    return renderSheet(zoo);
}

template<class T>
T* proxyWidget(QWidget* view)
{
    for (auto* graphics : view->findChildren<QGraphicsView*>()) {
        if (!graphics->scene()) {
            continue;
        }
        for (auto* item : graphics->scene()->items()) {
            auto* proxy = qgraphicsitem_cast<QGraphicsProxyWidget*>(item);
            if (auto* widget = proxy ? qobject_cast<T*>(proxy->widget()) : nullptr) {
                return widget;
            }
        }
    }
    throw Py::RuntimeError("Missing spreadsheet proxy widget");
}

// Replaces the text as typing would; insert() emits textEdited for live validation.
void type(QLineEdit* editor, const QString& text)
{
    if (!editor) {
        throw Py::RuntimeError("Missing spreadsheet editor");
    }
    editor->setFocus();
    editor->selectAll();
    editor->insert(text);
}

// Include both error and stale (#PENDING) cells in the production view.
App::DocumentObject* addSheet(App::Document* document)
{
    Base::Interpreter().runString("import SpreadsheetGui");
    auto* sheet = document->addObject("Spreadsheet::Sheet");
    Py::Object py(sheet->getPyObject(), true);
    const auto set = [&](const char* cell, const char* content) {
        py.callMemberFunction("set", Py::TupleN(Py::String(cell), Py::String(content)));
    };

    for (const auto& [cell, content] : {
             std::pair {"A2", "25"},
             std::pair {"A3", "25"},
             std::pair {"B2", "-25"},
             std::pair {"C2", "Sample text"},
             std::pair {"A5", "=1/0"},
             std::pair {"A6", "=A2 * 2"},
         }) {
        set(cell, content);
    }
    document->recompute();
    set("A6", "=A2 * 3");
    return sheet;
}

// Sheet views captured after an optional edit, e.g. an open cell editor.
struct SheetCase
{
    const char* title;
    void (*edit)(QWidget* view, QTableView* table);
};

const std::array<SheetCase, 4> sheetCases {{
    {"Cells / selection", nullptr},
    {"Cell editor",
     [](QWidget* view, QTableView* table) {
         table->edit(table->currentIndex());
         type(proxyWidget<QLineEdit>(view), QStringLiteral("=A2 * 2"));
     }},
    {"Content editor",
     [](QWidget* view, QTableView*) {
         type(view->findChild<QLineEdit*>(QStringLiteral("cellContent")), QStringLiteral("=A2 * 2"));
     }},
    {"Error / pending / invalid alias", [](QWidget* view, QTableView*) {
         type(
             view->findChild<QLineEdit*>(QStringLiteral("cellAlias")),
             QStringLiteral("invalid alias!")
         );
     }},
}};

QImage sheetSnapshot(App::Document* document, const SheetCase& sample)
{
    auto* sheet = addSheet(document);
    auto* provider = Gui::Application::Instance->getDocument(document)->getViewProvider(sheet);
    auto* view = provider ? provider->getMDIView() : nullptr;
    if (!view) {
        throw Py::RuntimeError("Spreadsheet sample requires an MDI view");
    }

    // Destroy the model before its document; deferred MDI deletion can outlive it.
    const auto closeView = qScopeGuard([&] {
        Gui::getMainWindow()->removeWindow(view);
        delete view;
    });

    // Capture the production view, including its graphics-proxy palette inheritance.
    view->setFixedSize(760, 320);
    Gui::getMainWindow()->setActiveWindow(view);
    auto* table = proxyWidget<QTableView>(view);
    table->setCurrentIndex(table->model()->index(2, 0));
    prepare(view);
    if (sample.edit) {
        sample.edit(view, table);
    }
    return renderSheet(view);
}

QImage spreadsheetPage(App::Document* document)
{
    QDialog page;
    auto* grid = new QGridLayout(&page);
    for (size_t i = 0; i < sheetCases.size(); ++i) {
        const int row = static_cast<int>(i / 2) * 2;
        const int column = static_cast<int>(i % 2);
        grid->addWidget(new QLabel(QString::fromLatin1(sheetCases[i].title)), row, column);
        auto* image = new QLabel;
        image->setPixmap(QPixmap::fromImage(sheetSnapshot(document, sheetCases[i])));
        grid->addWidget(image, row + 1, column);
    }
    return snapshot(&page);
}

using Page = std::function<QImage(App::Document*)>;

Page widgetPage(std::vector<Zoo::WidgetCase> (*cases)(App::DocumentObject*))
{
    return [cases](App::Document* document) {
        auto* values = document->addObject("App::VarSet", "Values");
        Zoo::addBoundValues(values);
        document->recompute();
        const std::unique_ptr<QWidget> sheet(controls(cases(values)));
        return snapshot(sheet.get());
    };
}

Page propertyPage(std::vector<Zoo::PropertyColumn> (*columns)(App::DocumentObject*), Editors editors)
{
    return [columns, editors](App::Document* document) {
        auto* values = document->addObject("App::VarSet", "Values");
        const auto sample = columns(values);
        document->recompute();
        const std::unique_ptr<QWidget> sheet(propertySheet(sample, editors));
        return snapshot(sheet.get());
    };
}

const std::map<std::string, Page>& pages()
{
    using Object = App::DocumentObject*;
    static const std::map<std::string, Page> registry {
        {"buttons", widgetPage([](Object) { return Zoo::buttons(); })},
        {"text", widgetPage(Zoo::text)},
        {"numbers", widgetPage(Zoo::numbers)},
        {"labels", widgetPage([](Object) { return Zoo::labels(); })},
        {"views", widgetPage(Zoo::views)},
        {"containers", widgetPage([](Object) { return Zoo::containers(); })},
        {"spreadsheet", spreadsheetPage},
        {"property-states", propertyPage(Zoo::propertyStates, Editors::Closed)},
        {"property-scalars", propertyPage(Zoo::propertyScalars, Editors::Closed)},
        {"property-geometry", propertyPage(Zoo::propertyGeometry, Editors::Closed)},
        {"property-collections", propertyPage(Zoo::propertyCollections, Editors::Closed)},
        {"property-editors-states", propertyPage(Zoo::propertyStates, Editors::Open)},
        {"property-editors-scalars", propertyPage(Zoo::propertyScalars, Editors::Open)},
        {"property-editors-geometry", propertyPage(Zoo::propertyGeometry, Editors::Open)},
        {"property-editors-collections", propertyPage(Zoo::propertyCollections, Editors::Open)},
    };
    return registry;
}

QPalette systemPalette(const QString& theme)
{
    auto palette = QApplication::style()->standardPalette();
    if (theme != "classic-dark") {
        return palette;
    }

    // Model a dark desktop palette without requiring a platform theme plugin.
    for (const auto role : {QPalette::Window, QPalette::Button}) {
        palette.setColor(role, QColor("#292c30"));
    }
    for (const auto role : {QPalette::WindowText, QPalette::Text, QPalette::ButtonText}) {
        palette.setColor(role, QColor("#eff0f1"));
    }
    palette.setColor(QPalette::Base, QColor("#141618"));
    palette.setColor(QPalette::AlternateBase, QColor("#202326"));
    palette.setColor(QPalette::Highlight, QColor("#1c627e"));
    palette.setColor(QPalette::HighlightedText, QColor("#eff0f1"));
    return palette;
}
}  // namespace

Py::Object TestGui::componentZoo(const char* themeName, const Py::List& names)
{
    const QString theme = QString::fromUtf8(themeName);
    if (theme != "classic-light" && theme != "classic-dark" && theme != "light" && theme != "dark") {
        throw Py::ValueError("Unknown component zoo theme");
    }

    const auto pack = ParameterManager::Create();
    const std::string packName = theme.startsWith("classic") ? "FreeCAD Classic"
        : theme == "dark"                                    ? "FreeCAD Dark"
                                                             : "FreeCAD Light";
    const std::string config = App::Application::getResourceDir() + "Gui/PreferencePacks/"
        + packName + "/" + packName + ".cfg";
    if (pack->LoadDocument(config.c_str()) != 1) {
        throw Py::RuntimeError("Cannot read component zoo theme preferences");
    }

    auto& preferences = App::GetApplication().GetUserParameter();
    const QPalette palette = QApplication::palette();
    const QString style = qApp->styleSheet();
    const auto restoreStyle = qScopeGuard([&] {
        // Qt callbacks must not consume a pending Python exception during cleanup.
        PyObject *error = nullptr, *value = nullptr, *traceback = nullptr;
        PyErr_Fetch(&error, &value, &traceback);
        QApplication::setPalette(palette);
        qApp->setStyleSheet(style);
        PyErr_Restore(error, value, traceback);
    });

    // Classic omits QtStyle; start each pack from the same base style.
    Gui::Application::Instance->setStyle(QStringLiteral("Fusion"));
    QApplication::setPalette(systemPalette(theme));
    // Import shipped preferences; production handlers select and load the theme.
    pack->insertTo(Base::Reference<ParameterGrp>(&preferences));
    settleTheme();

    Py::Dict images;
    Gui::PythonWrapper wrap;
    for (const auto& item : names) {
        const auto name = Py::String(item).as_std_string();
        const auto page = pages().find(name);
        if (page == pages().end()) {
            throw Py::ValueError("Unknown component zoo page: " + name);
        }

        auto* document = App::GetApplication().newDocument("ComponentZoo");
        const auto close = qScopeGuard([document] { App::GetApplication().closeDocument(document); });
        images[Py::String(name)] = wrap.fromQImage(page->second(document));
    }
    return images;
}
