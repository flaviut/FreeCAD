// SPDX-License-Identifier: LGPL-2.1-or-later

#pragma once

#include <functional>
#include <vector>

class QWidget;

namespace App
{
class DocumentObject;
class Property;
}  // namespace App

namespace Zoo
{
struct WidgetCase
{
    const char* variant;
    std::function<QWidget*()> make;
};

// One property tree; an empty title omits the column header.
struct PropertyColumn
{
    const char* title;
    std::vector<App::Property*> properties;
};

// Adds the expression-bound values that widget cases reference by name.
void addBoundValues(App::DocumentObject* object);

std::vector<WidgetCase> buttons();
std::vector<WidgetCase> text(App::DocumentObject* object);
std::vector<WidgetCase> numbers(App::DocumentObject* object);
std::vector<WidgetCase> labels();
std::vector<WidgetCase> views(App::DocumentObject* object);
std::vector<WidgetCase> containers();

std::vector<PropertyColumn> propertyStates(App::DocumentObject* object);
std::vector<PropertyColumn> propertyScalars(App::DocumentObject* object);
std::vector<PropertyColumn> propertyGeometry(App::DocumentObject* object);
std::vector<PropertyColumn> propertyCollections(App::DocumentObject* object);
}  // namespace Zoo
