// SPDX-License-Identifier: LGPL-2.1-or-later
/***************************************************************************
 *   Copyright (c) 2009 Jürgen Riegel <juergen.riegel@web.de>              *
 *                                                                         *
 *   This file is part of the FreeCAD CAx development system.              *
 *                                                                         *
 *   This library is free software; you can redistribute it and/or         *
 *   modify it under the terms of the GNU Library General Public           *
 *   License as published by the Free Software Foundation; either          *
 *   version 2 of the License, or (at your option) any later version.      *
 *                                                                         *
 *   This library  is distributed in the hope that it will be useful,      *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU Library General Public License for more details.                  *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this library; see the file COPYING.LIB. If not,    *
 *   write to the Free Software Foundation, Inc., 59 Temple Place,         *
 *   Suite 330, Boston, MA  02111-1307, USA                                *
 *                                                                         *
 ***************************************************************************/


#include <QMessageBox>
#include <QScopeGuard>
#include <QTimer>


#include <App/Document.h>
#include <Gui/Application.h>
#include <Gui/Document.h>
#include <Gui/MainWindow.h>
#include <Gui/View3DInventor.h>
#include <Gui/ViewProviderDocumentObject.h>


#include "TaskDialog.h"
#include "TaskView.h"

using namespace Gui::TaskView;

struct TaskDialog::DeferredAction
{
    fastsignals::connection connection;
    std::function<void()> action;

    ~DeferredAction()
    {
        connection.disconnect();
    }
};

bool TaskDialog::deferUntilStable(std::function<void()> action)
{
    if (!App::Document::isAnyRecomputing()) {
        return false;
    }
    if (deferredAction) {
        return true;
    }
    deferredAction = std::make_unique<DeferredAction>();
    deferredAction->action = std::move(action);
    QPointer<TaskDialog> alive(this);
    auto queue = [alive]() {
        if (!alive) {
            return;
        }
        QTimer::singleShot(0, alive, [alive]() {
            if (!alive || !alive->deferredAction) {
                return;
            }
            auto action = std::move(alive->deferredAction->action);
            alive->deferredAction.reset();
            action();
        });
    };
    for (auto* document : App::GetApplication().getDocuments()) {
        if (document->testStatus(App::Document::Recomputing)) {
            deferredAction->connection = document->signalBecameStable.connect(
                [queue](const App::Document&) { queue(); }
            );
            return true;
        }
    }
    queue();
    return true;
}

std::optional<bool> TaskDialog::tryClose(bool accepting)
{
    if (App::Document::isAnyRecomputing() || property("taskview_accept_or_reject").isValid()) {
        return std::nullopt;
    }

    QPointer<TaskDialog> alive(this);
    setProperty("taskview_accept_or_reject", true);
    if (!alive) {
        return std::nullopt;
    }
    const auto clear = qScopeGuard([alive]() {
        if (alive) {
            alive->setProperty("taskview_accept_or_reject", QVariant());
        }
    });
    return accepting ? accept() : reject();
}


//**************************************************************************
//**************************************************************************
// TaskDialog
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

TaskDialog::TaskDialog()
    : QObject(nullptr)
    , pos(North)
    , escapeButton(true)
    , autoCloseTransaction(false)
    , autoCloseResetEdit(false)
    , autoCloseDeletedDocument(false)
    , autoCloseClosedView(false)
{}

TaskDialog::~TaskDialog()
{
    deferredAction.reset();
    for (auto it : Content) {
        delete it;
        it = nullptr;
    }
}

//==== Slots ===============================================================

QWidget* TaskDialog::addTaskBox(QWidget* widget, bool expandable, QWidget* parent)
{
    return addTaskBox(QPixmap(), widget, expandable, parent);
}

QWidget* TaskDialog::addTaskBox(const QPixmap& icon, QWidget* widget, bool expandable, QWidget* parent)
{
    auto taskbox = new Gui::TaskView::TaskBox(icon, widget->windowTitle(), expandable, parent);
    taskbox->groupLayout()->addWidget(widget);
    Content.push_back(taskbox);
    return taskbox;
}

QWidget* TaskDialog::addTaskBoxWithoutHeader(QWidget* widget)
{
    auto taskbox = new Gui::TaskView::TaskBox();
    taskbox->groupLayout()->addWidget(widget);
    Content.push_back(taskbox);
    return taskbox;
}

const std::vector<QWidget*>& TaskDialog::getDialogContent() const
{
    return Content;
}

bool TaskDialog::canClose() const
{
    QMessageBox msgBox(Gui::getMainWindow());
    msgBox.setText(tr("A dialog is already open in the task panel"));
    msgBox.setInformativeText(QObject::tr("Close this dialog?"));
    msgBox.setStandardButtons(QMessageBox::Yes | QMessageBox::No);
    msgBox.setDefaultButton(QMessageBox::Yes);
    int ret = msgBox.exec();
    return (ret == QMessageBox::Yes);
}

void TaskDialog::associateToObject3dView(App::DocumentObject* obj)
{
    if (!obj) {
        return;
    }

    Gui::Document* guiDoc = Gui::Application::Instance->activeDocument();
    auto* vp = Gui::Application::Instance->getViewProvider(obj);
    auto* vpdo = static_cast<Gui::ViewProviderDocumentObject*>(vp);
    auto* view = guiDoc->openEditingView3D(vpdo);

    if (!view) {
        return;
    }

    setAssociatedView(view);
    setAutoCloseOnClosedView(true);
}

//==== calls from the TaskView ===============================================================

void TaskDialog::open()
{}

void TaskDialog::closed()
{}

void TaskDialog::autoClosedOnTransactionChange()
{}

void TaskDialog::autoClosedOnResetEdit()
{}

void TaskDialog::autoClosedOnDeletedDocument()
{}

void TaskDialog::autoClosedOnClosedView()
{}

void TaskDialog::clicked(int)
{}

bool TaskDialog::accept()
{
    return true;
}

bool TaskDialog::reject()
{
    return true;
}

void TaskDialog::helpRequested()
{}

void TaskDialog::onUndo()
{}

void TaskDialog::onRedo()
{}

void TaskDialog::activate()
{}

void TaskDialog::deactivate()
{}


#include "moc_TaskDialog.cpp"
