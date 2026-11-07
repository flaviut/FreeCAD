// SPDX-License-Identifier: LGPL-2.1-or-later

#include "ComponentZooCases.h"

#include <functional>
#include <limits>
#include <string>
#include <type_traits>
#include <vector>

#include <QAction>
#include <QApplication>
#include <QCheckBox>
#include <QComboBox>
#include <QDialogButtonBox>
#include <QDoubleSpinBox>
#include <QFontComboBox>
#include <QGroupBox>
#include <QKeySequence>
#include <QLabel>
#include <QLineEdit>
#include <QListWidget>
#include <QMenu>
#include <QMenuBar>
#include <QPlainTextEdit>
#include <QProgressBar>
#include <QPushButton>
#include <QRadioButton>
#include <QScrollArea>
#include <QSlider>
#include <QSpinBox>
#include <QSplitter>
#include <QStandardItemModel>
#include <QTabWidget>
#include <QTableWidget>
#include <QTextEdit>
#include <QToolBar>
#include <QToolBox>
#include <QToolButton>
#include <QTreeView>
#include <QTreeWidget>
#include <QVBoxLayout>

#include <App/Document.h>
#include <App/DocumentObject.h>
#include <App/Expression.h>
#include <App/Material.h>
#include <App/ObjectIdentifier.h>
#include <App/PropertyFile.h>
#include <App/PropertyGeo.h>
#include <App/PropertyLinks.h>
#include <App/PropertyStandard.h>
#include <App/PropertyUnits.h>
#include <Base/Tools.h>
#include <Gui/ElideCheckBox.h>
#include <Gui/ElideLabel.h>
#include <Gui/ExpressionCompleter.h>
#include <Gui/FileDialog.h>
#include <Gui/FontScaledSVG.h>
#include <Gui/InputField.h>
#include <Gui/InputVector.h>
#include <Gui/QuantitySpinBox.h>
#include <Gui/SpinBox.h>
#include <Gui/StatusBarLabel.h>
#include <Gui/TextEdit.h>
#include <Gui/Widgets.h>

namespace
{
using Zoo::WidgetCase;

template<class T>
WidgetCase control(const char* variant = "", std::function<void(T&)> setup = {})
{
    return {variant, [setup] {
                auto* widget = new T(nullptr);
                if (auto* button = qobject_cast<QAbstractButton*>(widget)) {
                    button->setText(QStringLiteral("Sample option"));
                }
                if (setup) {
                    setup(*widget);
                }
                return widget;
            }};
}

template<class T>
WidgetCase checkbox(Qt::CheckState state)
{
    const char* variant = state == Qt::Unchecked ? "unchecked"
        : state == Qt::Checked                   ? "checked"
                                                 : "mixed";
    return control<T>(variant, [state](auto& widget) {
        widget.setCheckState(state);
        if constexpr (std::is_same_v<T, Gui::ElideCheckBox>) {
            widget.setText(QStringLiteral("A long checkbox label that needs eliding"));
            widget.setFixedWidth(220);
        }
    });
}

void treeItems(QTreeWidget& tree)
{
    tree.setHeaderLabels({QStringLiteral("Name"), QStringLiteral("Value")});
    auto* parent = new QTreeWidgetItem(&tree, {QStringLiteral("Group"), QString()});
    auto* child = new QTreeWidgetItem(parent, {QStringLiteral("Selected"), QStringLiteral("12.5")});
    child->setCheckState(0, Qt::Checked);
    child->setSelected(true);
    auto* disabled = new QTreeWidgetItem(parent, {QStringLiteral("Disabled"), QStringLiteral("42")});
    disabled->setDisabled(true);
    tree.expandAll();
    tree.setFixedHeight(135);
}

// Adds dynamic properties named <prefix><suffix> to one property group.
class Values
{
public:
    Values(App::DocumentObject* object, std::string prefix, const char* group)
        : object(object)
        , prefix(std::move(prefix))
        , group(group)
    {}

    template<class P>
    P* add(const char* suffix)
    {
        const auto name = prefix + suffix;
        const auto type = P::getClassTypeId().getName();
        auto* property = static_cast<P*>(object->addDynamicProperty(type, name.c_str(), group));
        added.push_back(property);
        return property;
    }

    // Binds the most recently added properties in order, e.g. {"0", "42"}.
    void bind(const std::vector<const char*>& expressions)
    {
        const size_t first = added.size() - expressions.size();
        for (size_t i = 0; i < expressions.size(); ++i) {
            object->setExpression(
                App::ObjectIdentifier(*added[first + i]),
                App::Expression::parse(object, expressions[i])
            );
        }
    }

    const std::vector<App::Property*>& lock()
    {
        for (auto* property : added) {
            property->setStatus(App::Property::ReadOnly, true);
        }
        return added;
    }

    const std::vector<App::Property*>& properties() const
    {
        return added;
    }

private:
    App::DocumentObject* object;
    std::string prefix;
    const char* group;
    std::vector<App::Property*> added;
};

// Fills the same properties twice to compare editable and read-only rendering.
std::vector<Zoo::PropertyColumn> editableAndLocked(
    App::DocumentObject* object,
    const std::function<void(Values&)>& fill
)
{
    Values editable(object, "Normal", "Values");
    Values locked(object, "ReadOnly", "Values");
    fill(editable);
    fill(locked);
    return {{"Editable", editable.properties()}, {"Read-only", locked.lock()}};
}
}  // namespace

namespace Zoo
{
void addBoundValues(App::DocumentObject* object)
{
    Values values(object, "", nullptr);
    values.add<App::PropertyLength>("Length")->setValue(12.5);
    values.add<App::PropertyMap>("Map");
    values.add<App::PropertyLength>("BoundLength")->setValue(12.5);
    values.add<App::PropertyInteger>("BoundInteger")->setValue(42);
    values.add<App::PropertyString>("BoundString")->setValue("Sample text");
    values.bind({"Length", "42", "<<Sample text>>"});
}

std::vector<PropertyColumn> propertyStates(App::DocumentObject* object)
{
    struct Group
    {
        const char* name;
        const char* prefix;
        bool bound;
        bool locked;
    };
    const Group groups[] {
        {"Editable", "Editable", false, false},
        {"Read-only", "Locked", false, true},
        {"Expression", "Bound", true, false},
        {"Read-only expression", "LockedBound", true, true},
    };

    std::vector<App::Property*> properties;
    for (const auto& group : groups) {
        Values values(object, group.prefix, group.name);
        values.add<App::PropertyBool>("False")->setValue(false);
        values.add<App::PropertyBool>("True")->setValue(true);
        values.add<App::PropertyInteger>("Integer")->setValue(42);
        values.add<App::PropertyFloat>("Float")->setValue(12.5);
        values.add<App::PropertyString>("String")->setValue("Sample text");
        if (group.bound) {
            values.bind({"0", "1", "42", "12.5", "<<Sample text>>"});
        }
        const auto& added = group.locked ? values.lock() : values.properties();
        properties.insert(properties.end(), added.begin(), added.end());
    }
    return {{"", properties}};
}

std::vector<PropertyColumn> propertyScalars(App::DocumentObject* object)
{
    return editableAndLocked(object, [](Values& values) {
        values.add<App::PropertyBool>("Boolean")->setValue(true);
        values.add<App::PropertyInteger>("Integer")->setValue(42);
        values.add<App::PropertyIntegerConstraint>("IntegerConstraint")->setValue(42);
        values.add<App::PropertyPercent>("Percent")->setValue(40);
        values.add<App::PropertyFloat>("Float")->setValue(12.5);
        values.add<App::PropertyFloatConstraint>("FloatConstraint")->setValue(12.5);
        values.add<App::PropertyPrecision>("Precision")->setValue(0.001);
        auto* quantity = values.add<App::PropertyQuantity>("Quantity");
        quantity->setUnit(Base::Unit::Length);
        quantity->setValue(12.5);
        values.add<App::PropertyLength>("Length")->setValue(12.5);
        values.add<App::PropertyAngle>("Angle")->setValue(45.0);
        values.add<App::PropertyString>("String")->setValue("Sample text");
        values.add<App::PropertyFont>("Font")->setValue("Noto Sans");
        auto* enumeration = values.add<App::PropertyEnumeration>("Enumeration");
        enumeration->setEnums(std::vector<std::string> {"First", "Second", "Third"});
        enumeration->setValue(1L);
        values.add<App::PropertyColor>("Color")->setValue(0.2F, 0.5F, 0.9F);
        values.add<App::PropertyFile>("File")->setValue("/models/sample.FCStd");
        values.add<App::PropertyPath>("Path")->setValue("/models");
        values.add<App::PropertyFileIncluded>("IncludedFile");
    });
}

std::vector<PropertyColumn> propertyGeometry(App::DocumentObject* object)
{
    const Base::Vector3d offset(12.5, 25, -5);
    const Base::Rotation rotation(Base::Vector3d(0, 0, 1), Base::toRadians(45.0));
    Base::Matrix4D matrix;
    matrix.move(offset);
    return editableAndLocked(object, [&](Values& values) {
        values.add<App::PropertyVector>("Vector")->setValue(1, 2, 3);
        values.add<App::PropertyVectorDistance>("VectorDistance")->setValue(offset);
        values.add<App::PropertyPosition>("Position")->setValue(offset);
        values.add<App::PropertyDirection>("Direction")->setValue(0, 0, 1);
        values.add<App::PropertyMatrix>("Matrix")->setValue(matrix);
        values.add<App::PropertyRotation>("Rotation")->setValue(rotation);
        values.add<App::PropertyPlacement>("Placement")->setValue(Base::Placement(offset, rotation));
    });
}

std::vector<PropertyColumn> propertyCollections(App::DocumentObject* object)
{
    auto* target = object->getDocument()->addObject("App::VarSet", "Target");
    target->Label.setValue("Linked object");
    return editableAndLocked(object, [target](Values& values) {
        values.add<App::PropertyStringList>("Strings")->setValues(
            std::vector<std::string> {"First", "Second", "Third"}
        );
        values.add<App::PropertyIntegerList>("Integers")->setValues({1, 2, 42});
        values.add<App::PropertyFloatList>("Floats")->setValues({1.25, 2.5, 12.5});
        values.add<App::PropertyVectorList>("Vectors")->setValues(
            {Base::Vector3d(1, 2, 3), Base::Vector3d(12.5, 25, -5)}
        );
        values.add<App::PropertyMap>("Map")->setValues({{"Name", "Sample"}, {"Size", "12.5"}});
        auto* material = values.add<App::PropertyMaterial>("Material");
        material->setValue(App::Material());
        material->setStatus(App::Property::MaterialEdit, true);
        values.add<App::PropertyMaterialList>("Materials")->setValues({App::Material()});
        values.add<App::PropertyLink>("Link")->setValue(target);
        values.add<App::PropertyLinkList>("Links")->setValues(
            std::vector<App::DocumentObject*> {target}
        );
        values.add<App::PropertyLinkSub>("SubLink")->setValue(target);
        values.add<App::PropertyLinkSubList>("SubLinks")->setValue(target, "");
    });
}

std::vector<WidgetCase> buttons()
{
    return {
        control<QPushButton>(),
        control<QPushButton>("default", [](auto& w) { w.setDefault(true); }),
        control<QPushButton>(
            "checked",
            [](auto& w) {
                w.setCheckable(true);
                w.setChecked(true);
            }
        ),
        control<QToolButton>("arrow", [](auto& w) { w.setArrowType(Qt::DownArrow); }),
        control<QToolButton>(
            "split menu",
            [](auto& w) {
                auto* menu = new QMenu(&w);
                menu->addAction(QStringLiteral("First action"));
                w.setMenu(menu);
                w.setPopupMode(QToolButton::MenuButtonPopup);
            }
        ),
        checkbox<QCheckBox>(Qt::Unchecked),
        checkbox<QCheckBox>(Qt::Checked),
        checkbox<QCheckBox>(Qt::PartiallyChecked),
        checkbox<Gui::ElideCheckBox>(Qt::Unchecked),
        checkbox<Gui::ElideCheckBox>(Qt::Checked),
        checkbox<Gui::ElideCheckBox>(Qt::PartiallyChecked),
        control<QRadioButton>("unchecked"),
        control<QRadioButton>(
            "checked",
            [](auto& w) {
                w.setAutoExclusive(false);
                w.setChecked(true);
            }
        ),
        control<Gui::ColorButton>(
            "opaque",
            [](auto& w) {
                w.setText(QString());
                w.setColor(QColor("#3288ed"));
            }
        ),
        control<Gui::ColorButton>(
            "transparent",
            [](auto& w) {
                w.setText(QString());
                w.setAllowTransparency(true);
                w.setColor(QColor(50, 136, 237, 100));
            }
        ),
        control<QDialogButtonBox>("OK / Cancel", [](auto& w) {
            w.setStandardButtons(QDialogButtonBox::Ok | QDialogButtonBox::Cancel);
            for (auto* button : w.buttons()) {
                button->setIcon(QIcon());
            }
        }),
    };
}

std::vector<WidgetCase> text(App::DocumentObject* object)
{
    return {
        control<QLineEdit>("text", [](auto& w) { w.setText(QStringLiteral("Sample text")); }),
        control<QLineEdit>(
            "read-only",
            [](auto& w) {
                w.setText(QStringLiteral("Read-only text"));
                w.setReadOnly(true);
            }
        ),
        control<QLineEdit>(
            "placeholder",
            [](auto& w) { w.setPlaceholderText(QStringLiteral("Search")); }
        ),
        control<QLineEdit>(
            "password",
            [](auto& w) {
                w.setText(QStringLiteral("password"));
                w.setEchoMode(QLineEdit::Password);
            }
        ),
        control<Gui::ClearLineEdit>("", [](auto& w) { w.setText(QStringLiteral("Search text")); }),
        control<Gui::ModifierLineEdit>("", [](auto& w) { w.setText(QStringLiteral("Ctrl+Shift")); }),
        control<Gui::AccelLineEdit>(
            "",
            [](auto& w) { w.setKeySequence(QKeySequence(QStringLiteral("Ctrl+Shift+S"))); }
        ),
        control<Gui::ExpressionLineEdit>(
            "",
            [object](auto& w) {
                w.setDocumentObject(object);
                w.setText(QStringLiteral("Values.Length * 2"));
            }
        ),
        control<Gui::ExpLineEdit>(
            "bound",
            [object](auto& w) {
                w.bind(App::ObjectIdentifier(*object->getPropertyByName("BoundString")));
                w.setText(QStringLiteral("Sample text"));
            }
        ),
        control<QPlainTextEdit>(
            "",
            [](auto& w) {
                w.setPlainText(QStringLiteral("First line\nSecond line"));
                w.setFixedHeight(75);
            }
        ),
        control<QTextEdit>(
            "rich text",
            [](auto& w) {
                w.setHtml(QStringLiteral("<b>Bold</b>, <i>italic</i>, and plain text"));
                w.setFixedHeight(65);
            }
        ),
        control<Gui::ExpressionTextEdit>(
            "",
            [object](auto& w) {
                w.setDocumentObject(object);
                w.setPlainText(QStringLiteral("Values.Length * 2\n+ 5 mm"));
                w.setFixedHeight(75);
            }
        ),
        control<Gui::TextEdit>(
            "",
            [](auto& w) {
                w.setPlainText(QStringLiteral("result = 12.5\nprint(result)"));
                w.setFixedHeight(75);
            }
        ),
        control<Gui::PropertyListEditor>("", [](auto& w) {
            w.setPlainText(QStringLiteral("First item\nSecond item\nThird item"));
            w.setFixedHeight(85);
        }),
    };
}

std::vector<WidgetCase> numbers(App::DocumentObject* object)
{
    return {
        control<QSpinBox>(
            "",
            [](auto& w) {
                w.setRange(-100, 100);
                w.setValue(-42);
            }
        ),
        control<QDoubleSpinBox>("", [](auto& w) { w.setValue(12.5); }),
        control<Gui::IntSpinBox>("", [](auto& w) { w.setValue(42); }),
        control<Gui::IntSpinBox>(
            "bound",
            [object](auto& w) {
                w.bind(App::ObjectIdentifier(*object->getPropertyByName("BoundInteger")));
                w.setValue(42);
            }
        ),
        control<Gui::UIntSpinBox>(
            "large value",
            [](auto& w) {
                w.setRange(0, std::numeric_limits<unsigned>::max());
                w.setValue(4000000000U);
            }
        ),
        control<Gui::DoubleSpinBox>("", [](auto& w) { w.setValue(12.5); }),
        control<Gui::QuantitySpinBox>(
            "length",
            [](auto& w) {
                w.setUnit(Base::Unit::Length);
                w.setValue(12.5);
            }
        ),
        control<Gui::QuantitySpinBox>(
            "read-only",
            [](auto& w) {
                w.setUnit(Base::Unit::Length);
                w.setValue(12.5);
                w.setReadOnly(true);
            }
        ),
        control<Gui::QuantitySpinBox>(
            "bound",
            [object](auto& w) {
                w.setUnit(Base::Unit::Length);
                w.bind(App::ObjectIdentifier(*object->getPropertyByName("BoundLength")));
                w.setValue(12.5);
            }
        ),
        control<Gui::InputField>(
            "valid",
            [](auto& w) {
                w.setUnit(Base::Unit::Length);
                w.setValue(12.5);
            }
        ),
        control<Gui::InputField>(
            "invalid",
            [](auto& w) {
                w.setUnit(Base::Unit::Length);
                w.setProperty("invalidText", QStringLiteral("not a quantity"));
            }
        ),
        control<Gui::InputField>(
            "bound",
            [object](auto& w) {
                w.setUnit(Base::Unit::Length);
                w.bind(App::ObjectIdentifier(*object->getPropertyByName("BoundLength")));
                w.setValue(12.5);
            }
        ),
        control<QSlider>(
            "",
            [](auto& w) {
                w.setOrientation(Qt::Horizontal);
                w.setValue(40);
            }
        ),
        control<QProgressBar>("", [](auto& w) { w.setValue(40); }),
        control<Gui::LocationWidget>("", [](auto& w) {
            w.setPosition(Base::Vector3d(12.5, 25, -5));
            w.setFixedHeight(145);
        }),
    };
}

std::vector<WidgetCase> labels()
{
    return {
        control<QLabel>("plain", [](auto& w) { w.setText(QStringLiteral("Sample label")); }),
        control<QLabel>("rich text", [](auto& w) { w.setText(QStringLiteral("<b>Bold</b> label")); }),
        control<Gui::FontScaledSVG>(
            "",
            [](auto& w) { w.setSvg(QStringLiteral(":/icons/button_valid.svg")); }
        ),
        control<Gui::ElideLabel>(
            "",
            [](auto& w) {
                w.setText(QStringLiteral("A long label that needs eliding to fit the available space"));
                w.setFixedWidth(260);
            }
        ),
        control<Gui::UrlLabel>(
            "",
            [](auto& w) {
                w.setText(QStringLiteral("FreeCAD documentation"));
                w.setUrl(QStringLiteral("https://www.freecad.org"));
                w.setLaunchExternal(false);
            }
        ),
        control<Gui::StatefulLabel>(
            "error",
            [](auto& w) {
                w.registerState(QStringLiteral("error"), QColor("#e05555"));
                w.setState(QStringLiteral("error"));
                w.setText(QStringLiteral("Invalid value"));
            }
        ),
        control<Gui::StatefulLabel>(
            "warning",
            [](auto& w) {
                w.registerState(QStringLiteral("warning"), QColor("#b08020"));
                w.setState(QStringLiteral("warning"));
                w.setText(QStringLiteral("Value outside recommended range"));
            }
        ),
        control<Gui::StatusBarLabel>(
            "elided",
            [](auto& w) {
                w.setText(QStringLiteral("A long status message that needs eliding to fit"));
                w.setElideMode(Qt::ElideRight);
                w.setFixedWidth(260);
            }
        ),
        control<Gui::LabelButton>("", [](auto& w) { w.setValue(QStringLiteral("Sample value")); }),
        control<Gui::LabelEditor>("", [](auto& w) { w.setText(QStringLiteral("Sample label")); }),
        control<Gui::FileChooser>(
            "file",
            [](auto& w) { w.setFileName(QStringLiteral("/models/sample.FCStd")); }
        ),
        control<Gui::FileChooser>("directory", [](auto& w) {
            w.setMode(Gui::FileChooser::Directory);
            w.setFileName(QStringLiteral("/models"));
        }),
    };
}

std::vector<WidgetCase> views(App::DocumentObject* object)
{
    return {
        control<QListWidget>(
            "selection / checks",
            [](auto& w) {
                auto* first = new QListWidgetItem(QStringLiteral("Selected item"), &w);
                first->setSelected(true);
                auto* second = new QListWidgetItem(QStringLiteral("Checked item"), &w);
                second->setCheckState(Qt::Checked);
                auto* third = new QListWidgetItem(QStringLiteral("Disabled item"), &w);
                third->setFlags(third->flags() & ~Qt::ItemIsEnabled);
                w.setFixedHeight(100);
            }
        ),
        control<QTreeWidget>("expanded", [](auto& w) { treeItems(w); }),
        control<QTreeView>(
            "",
            [](auto& w) {
                auto* model = new QStandardItemModel(&w);
                model->setHorizontalHeaderLabels({QStringLiteral("Name"), QStringLiteral("Value")});
                auto* parent = new QStandardItem(QStringLiteral("Group"));
                parent->appendRow(
                    {new QStandardItem(QStringLiteral("Child")),
                     new QStandardItem(QStringLiteral("12.5"))}
                );
                model->appendRow(parent);
                w.setModel(model);
                w.expandAll();
                w.setFixedHeight(115);
            }
        ),
        control<QTableWidget>(
            "headers / selection",
            [](auto& w) {
                w.setColumnCount(2);
                w.setRowCount(3);
                w.setHorizontalHeaderLabels({QStringLiteral("Name"), QStringLiteral("Value")});
                for (int row = 0; row < 3; ++row) {
                    w.setItem(row, 0, new QTableWidgetItem(QStringLiteral("Item %1").arg(row + 1)));
                    w.setItem(row, 1, new QTableWidgetItem(QString::number((row + 1) * 12.5)));
                }
                w.selectRow(1);
                w.setFixedHeight(145);
            }
        ),
        control<Gui::PropertyMapEditor>(
            "",
            [object](auto& w) {
                w.bind(App::ObjectIdentifier(*object->getPropertyByName("Map")));
                w.setMap(
                    {{QStringLiteral("Length"), QStringLiteral("12.5 mm")},
                     {QStringLiteral("Name"), QStringLiteral("Sample")}}
                );
                w.setFixedHeight(120);
            }
        ),
        control<Gui::ActionSelector>("", [](auto& w) {
            new QTreeWidgetItem(w.availableTreeWidget(), {QStringLiteral("Available action")});
            new QTreeWidgetItem(w.selectedTreeWidget(), {QStringLiteral("Selected action")});
            w.setFixedHeight(180);
        }),
    };
}

std::vector<WidgetCase> containers()
{
    return {
        control<QComboBox>(
            "list",
            [](auto& w) {
                w.addItems({QStringLiteral("First option"), QStringLiteral("Second option")});
            }
        ),
        control<QComboBox>(
            "editable",
            [](auto& w) {
                w.setEditable(true);
                w.addItems({QStringLiteral("Custom value"), QStringLiteral("Second option")});
            }
        ),
        control<QFontComboBox>("", [](auto& w) { w.setCurrentFont(QApplication::font()); }),
        control<QGroupBox>(
            "checked",
            [](auto& w) {
                w.setTitle(QStringLiteral("Options"));
                w.setCheckable(true);
                auto* layout = new QVBoxLayout(&w);
                layout->addWidget(new QLineEdit(QStringLiteral("Sample value")));
            }
        ),
        control<QGroupBox>(
            "unchecked",
            [](auto& w) {
                w.setTitle(QStringLiteral("Options"));
                w.setCheckable(true);
                auto* layout = new QVBoxLayout(&w);
                layout->addWidget(new QLineEdit(QStringLiteral("Sample value")));
                w.setChecked(false);
            }
        ),
        control<QTabWidget>(
            "",
            [](auto& w) {
                w.addTab(new QLabel(QStringLiteral("First page")), QStringLiteral("First"));
                w.addTab(new QLabel(QStringLiteral("Second page")), QStringLiteral("Second"));
                w.setTabEnabled(1, false);
                w.setFixedHeight(80);
            }
        ),
        control<QToolBox>(
            "",
            [](auto& w) {
                w.addItem(new QLabel(QStringLiteral("First page")), QStringLiteral("First"));
                w.addItem(new QLabel(QStringLiteral("Second page")), QStringLiteral("Second"));
                w.setFixedHeight(110);
            }
        ),
        control<QSplitter>(
            "",
            [](auto& w) {
                w.addWidget(new QLineEdit(QStringLiteral("Left pane")));
                w.addWidget(new QLineEdit(QStringLiteral("Right pane")));
            }
        ),
        control<QScrollArea>(
            "scrollbars",
            [](auto& w) {
                auto* content = new QLabel(QStringLiteral("Scrollable content"));
                content->setFixedSize(800, 160);
                content->setAlignment(Qt::AlignLeft | Qt::AlignTop);
                w.setWidget(content);
                w.setFixedHeight(80);
            }
        ),
        control<QMenu>(
            "actions",
            [](auto& w) {
                w.setWindowFlags(Qt::Widget);
                w.addAction(QStringLiteral("Normal action"));
                auto* check = w.addAction(QStringLiteral("Checked action"));
                check->setCheckable(true);
                check->setChecked(true);
                w.addSeparator();
                w.addAction(QStringLiteral("Disabled action"))->setEnabled(false);
            }
        ),
        control<QMenuBar>(
            "",
            [](auto& w) {
                w.setNativeMenuBar(false);
                w.addMenu(QStringLiteral("File"));
                w.addMenu(QStringLiteral("Edit"));
            }
        ),
        control<QToolBar>("", [](auto& w) {
            w.addAction(QStringLiteral("First action"));
            w.addSeparator();
            w.addAction(QStringLiteral("Disabled"))->setEnabled(false);
        }),
    };
}

}  // namespace Zoo
