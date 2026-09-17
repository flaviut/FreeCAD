# GUI dialog catalog

This catalog is the static baseline for the [GUI dialog policy](GuiDialogPolicy.md).
It was generated from the source tree on 2026-09-16 and records independently shown
FreeCAD dialogs that could be established from source. The accompanying
[audit](GuiDialogAudit.md) contains the actionable findings.

## Scope and method

The discovery scan considered 214 candidates: 146 top-level
Designer `QDialog` forms, 37 direct C++ or Python subclasses not
paired with a same-named form, and 31 direct constructions.
Each candidate was then inspected with its implementation and call sites. Forms used only
as task panels or embedded widgets, duplicate representations, tests, templates, comments,
and non-dialog utility containers were screened out.

The dimension columns are Parent, Layout, Content structure, Native controls, and
Keyboard/accessibility. `Y` conforms, `N` has a finding, `?` needs human follow-up, and
`-` is not applicable. A pass is based on idiomatic Qt source and does not imply redundant
runtime testing.

## Dialogs

| ID | Area | Dialog | Definition | Kind | P | L | C | N | K | Result |
| --- | --- | --- | --- | --- | :-: | :-: | :-: | :-: | :-: | --- |
| dialog-041 | AddonManager | Add Button | [`src/Mod/AddonManager/add_toolbar_button_dialog.ui:1`](../Mod/AddonManager/add_toolbar_button_dialog.ui#L1) | designer | N | Y | Y | N | Y | Follow-up |
| dialog-038 | AddonManager | Addon Manager | [`src/Mod/AddonManager/AddonManager.ui:1`](../Mod/AddonManager/AddonManager.ui#L1) | designer | N | Y | Y | N | Y | Follow-up |
| dialog-043 | AddonManager | Addon Manager Warning | [`src/Mod/AddonManager/first_run.ui:1`](../Mod/AddonManager/first_run.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-044 | AddonManager | Addon progress dialog | [`src/Mod/AddonManager/progress.ui:1`](../Mod/AddonManager/progress.ui#L1) | designer | N | Y | Y | Y | Y | Follow-up |
| dialog-039 | AddonManager | Custom Repository | [`src/Mod/AddonManager/AddonManagerOptions_AddCustomRepository.ui:1`](../Mod/AddonManager/AddonManagerOptions_AddCustomRepository.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-042 | AddonManager | DependencyResolutionDialog | [`src/Mod/AddonManager/dependency_resolution_dialog.ui:1`](../Mod/AddonManager/dependency_resolution_dialog.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-045 | AddonManager | Proxy Login Required | [`src/Mod/AddonManager/proxy_authentication.ui:1`](../Mod/AddonManager/proxy_authentication.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-040 | AddonManager | PythonDependencyUpdateDialog | [`src/Mod/AddonManager/PythonDependencyUpdateDialog.ui:1`](../Mod/AddonManager/PythonDependencyUpdateDialog.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-046 | AddonManager | Select Toolbar | [`src/Mod/AddonManager/select_toolbar_dialog.ui:1`](../Mod/AddonManager/select_toolbar_dialog.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-048 | AddonManager | Update Addons | [`src/Mod/AddonManager/update_all.ui:1`](../Mod/AddonManager/update_all.ui#L1) | designer | N | Y | Y | Y | Y | Follow-up |
| dialog-202 | Assembly | Assembly BOM Help | [`src/Mod/Assembly/CommandCreateBom.py:356`](../Mod/Assembly/CommandCreateBom.py#L356) | construction | Y | N | Y | Y | Y | Follow-up |
| dialog-056 | BIM | Add IFC Property | [`src/Mod/BIM/Resources/ui/dialogAddProperty.ui:1`](../Mod/BIM/Resources/ui/dialogAddProperty.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-055 | BIM | Add standard IFC PSet | [`src/Mod/BIM/Resources/ui/dialogAddPSet.ui:1`](../Mod/BIM/Resources/ui/dialogAddPSet.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-204 | BIM | BIM Material | [`src/Mod/BIM/bimcommands/BimMaterial.py:79`](../Mod/BIM/bimcommands/BimMaterial.py#L79) | construction | N | N | N | N | N | Follow-up |
| dialog-074 | BIM | BIM Project Setup | [`src/Mod/BIM/Resources/ui/dialogProjectManager.ui:1`](../Mod/BIM/Resources/ui/dialogProjectManager.ui#L1) | designer | N | N | Y | N | N | Follow-up |
| dialog-076 | BIM | BIM Setup | [`src/Mod/BIM/Resources/ui/dialogSetup.ui:1`](../Mod/BIM/Resources/ui/dialogSetup.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-079 | BIM | BIM Welcome | [`src/Mod/BIM/Resources/ui/dialogWelcome.ui:1`](../Mod/BIM/Resources/ui/dialogWelcome.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-053 | BIM | BimServer Login | [`src/Mod/BIM/Resources/ui/DialogBimServerLogin.ui:1`](../Mod/BIM/Resources/ui/DialogBimServerLogin.ui#L1) | designer | ? | Y | Y | Y | N | Review |
| dialog-171 | BIM | CheatsheetDialog | [`src/Mod/BIM/ArchReport.py:2470`](../Mod/BIM/ArchReport.py#L2470) | subclass | Y | N | Y | Y | Y | Follow-up |
| dialog-057 | BIM | Classification Manager | [`src/Mod/BIM/Resources/ui/dialogClassification.ui:1`](../Mod/BIM/Resources/ui/dialogClassification.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-059 | BIM | Convert to IFC Type | [`src/Mod/BIM/Resources/ui/dialogConvertType.ui:1`](../Mod/BIM/Resources/ui/dialogConvertType.ui#L1) | designer | N | Y | Y | Y | Y | Follow-up |
| dialog-060 | BIM | Default Structure | [`src/Mod/BIM/Resources/ui/dialogCreateProject.ui:1`](../Mod/BIM/Resources/ui/dialogCreateProject.ui#L1) | designer | N | Y | Y | Y | Y | Follow-up |
| dialog-061 | BIM | IFC Difference | [`src/Mod/BIM/Resources/ui/dialogDiff.ui:1`](../Mod/BIM/Resources/ui/dialogDiff.ui#L1) | designer | N | Y | Y | N | Y | Follow-up |
| dialog-063 | BIM | IFC Elements Manager | [`src/Mod/BIM/Resources/ui/dialogIfcElements.ui:1`](../Mod/BIM/Resources/ui/dialogIfcElements.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-203 | BIM | IFC Explorer | [`src/Mod/BIM/bimcommands/BimIfcExplorer.py:107`](../Mod/BIM/bimcommands/BimIfcExplorer.py#L107) | construction | N | N | Y | Y | Y | Follow-up |
| dialog-067 | BIM | IFC Import Options | [`src/Mod/BIM/Resources/ui/dialogImport.ui:1`](../Mod/BIM/Resources/ui/dialogImport.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-065 | BIM | IFC Properties Editor | [`src/Mod/BIM/Resources/ui/dialogIfcPropertiesRedux.ui:1`](../Mod/BIM/Resources/ui/dialogIfcPropertiesRedux.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-064 | BIM | IFC Properties Manager | [`src/Mod/BIM/Resources/ui/dialogIfcProperties.ui:1`](../Mod/BIM/Resources/ui/dialogIfcProperties.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-066 | BIM | IFC Quantities Manager | [`src/Mod/BIM/Resources/ui/dialogIfcQuantities.ui:1`](../Mod/BIM/Resources/ui/dialogIfcQuantities.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-078 | BIM | IFC Representation | [`src/Mod/BIM/Resources/ui/dialogTree.ui:1`](../Mod/BIM/Resources/ui/dialogTree.ui#L1) | designer | N | N | N | Y | Y | Follow-up |
| dialog-062 | BIM | IFC save confirmation dialog | [`src/Mod/BIM/Resources/ui/dialogExport.ui:1`](../Mod/BIM/Resources/ui/dialogExport.ui#L1) | designer | N | N | Y | Y | Y | Follow-up |
| dialog-068 | BIM | Layers Manager | [`src/Mod/BIM/Resources/ui/dialogLayersIFC.ui:1`](../Mod/BIM/Resources/ui/dialogLayersIFC.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-170 | BIM | ManagePresetsDialog | [`src/Mod/BIM/ArchReport.py:2171`](../Mod/BIM/ArchReport.py#L2171) | subclass | Y | N | N | N | Y | Follow-up |
| dialog-070 | BIM | Material chooser | [`src/Mod/BIM/Resources/ui/dialogMaterialChooser.ui:1`](../Mod/BIM/Resources/ui/dialogMaterialChooser.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-071 | BIM | Nudge | [`src/Mod/BIM/Resources/ui/dialogNudgeValue.ui:1`](../Mod/BIM/Resources/ui/dialogNudgeValue.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-051 | BIM | Schedule Definition | [`src/Mod/BIM/Resources/ui/ArchSchedule.ui:1`](../Mod/BIM/Resources/ui/ArchSchedule.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-069 | BIM | Select Material to Merge To | [`src/Mod/BIM/Resources/ui/dialogListWidget.ui:1`](../Mod/BIM/Resources/ui/dialogListWidget.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-073 | BIM | Test Results | [`src/Mod/BIM/Resources/ui/dialogPreflightResults.ui:1`](../Mod/BIM/Resources/ui/dialogPreflightResults.ui#L1) | designer | N | N | Y | N | Y | Follow-up |
| dialog-174 | CAM | CAM Inspect | [`src/Mod/CAM/Path/Main/Gui/Inspect.py:35`](../Mod/CAM/Path/Main/Gui/Inspect.py#L35) | subclass | N | Y | N | Y | N | Follow-up |
| dialog-092 | CAM | Create Property | [`src/Mod/CAM/Gui/Resources/panels/PropertyCreate.ui:1`](../Mod/CAM/Gui/Resources/panels/PropertyCreate.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-091 | CAM | FeedsSpeedsPresetEdit | [`src/Mod/CAM/Gui/Resources/panels/FeedsSpeedsPresetEdit.ui:1`](../Mod/CAM/Gui/Resources/panels/FeedsSpeedsPresetEdit.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-176 | CAM | GCodeEditorDialog | [`src/Mod/CAM/Path/Post/Utils.py:189`](../Mod/CAM/Path/Post/Utils.py#L189) | subclass | Y | Y | Y | Y | Y | Pass |
| dialog-173 | CAM | Import Machine from MTConnect | [`src/Mod/CAM/Machine/ui/mtconnect_import_dialog.py:83`](../Mod/CAM/Machine/ui/mtconnect_import_dialog.py#L83) | subclass | Y | Y | N | Y | N | Follow-up |
| dialog-084 | CAM | Job Template Export | [`src/Mod/CAM/Gui/Resources/panels/DlgJobTemplateExport.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgJobTemplateExport.ui#L1) | designer | N | N | Y | N | N | Follow-up |
| dialog-098 | CAM | Library Manager | [`src/Mod/CAM/Gui/Resources/panels/ToolBitLibraryEdit.ui:1`](../Mod/CAM/Gui/Resources/panels/ToolBitLibraryEdit.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-180 | CAM | LibraryPropertyDialog | [`src/Mod/CAM/Path/Tool/library/ui/properties.py:31`](../Mod/CAM/Path/Tool/library/ui/properties.py#L31) | subclass | N | N | N | Y | N | Follow-up |
| dialog-178 | CAM | Machinability Material Dialog | [`src/Mod/CAM/Path/Tool/Gui/MaterialPicker.py:47`](../Mod/CAM/Path/Tool/Gui/MaterialPicker.py#L47) | subclass | Y | Y | Y | Y | Y | Pass |
| dialog-172 | CAM | MachineEditorDialog | [`src/Mod/CAM/Machine/ui/editor/machine_editor.py:345`](../Mod/CAM/Machine/ui/editor/machine_editor.py#L345) | subclass | N | N | N | Y | N | Follow-up |
| dialog-082 | CAM | New Job | [`src/Mod/CAM/Gui/Resources/panels/DlgJobCreate.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgJobCreate.ui#L1) | designer | N | Y | Y | N | N | Follow-up |
| dialog-085 | CAM | Post Processing | [`src/Mod/CAM/Gui/Resources/panels/DlgPostProcess.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgPostProcess.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-086 | CAM | Post Processor | [`src/Mod/CAM/Gui/Resources/panels/DlgSelectPostProcessor.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgSelectPostProcessor.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-081 | CAM | Processor Selection | [`src/Mod/CAM/Gui/DlgProcessorChooser.ui:1`](../Mod/CAM/Gui/DlgProcessorChooser.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-093 | CAM | ShapeSelector | [`src/Mod/CAM/Gui/Resources/panels/ShapeSelector.ui:1`](../Mod/CAM/Gui/Resources/panels/ShapeSelector.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-177 | CAM | Suggest Feeds & Speeds | [`src/Mod/CAM/Path/Tool/Gui/FeedsSpeedsDialog.py:309`](../Mod/CAM/Path/Tool/Gui/FeedsSpeedsDialog.py#L309) | subclass | Y | Y | N | Y | N | Follow-up |
| dialog-088 | CAM | Tool Controller Editor | [`src/Mod/CAM/Gui/Resources/panels/DlgToolControllerEdit.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgToolControllerEdit.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-087 | CAM | Tool Controller Selection | [`src/Mod/CAM/Gui/Resources/panels/DlgTCChooser.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgTCChooser.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-179 | CAM | Tool Updates Available | [`src/Mod/CAM/Path/Tool/Gui/UpdateDocumentToolsDlg.py:112`](../Mod/CAM/Path/Tool/Gui/UpdateDocumentToolsDlg.py#L112) | subclass | Y | N | Y | N | N | Follow-up |
| dialog-097 | CAM | Toolbit Parameter Editor | [`src/Mod/CAM/Gui/Resources/panels/ToolBitEditor.ui:1`](../Mod/CAM/Gui/Resources/panels/ToolBitEditor.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-207 | CAM | Toolbit Selector | [`src/Mod/CAM/Path/Tool/library/ui/dock.py:60`](../Mod/CAM/Path/Tool/library/ui/dock.py#L60) | construction | N | N | Y | N | N | Follow-up |
| dialog-206 | CAM | Workplan | [`src/Mod/CAM/Path/Post/Gui/DlgPostProcess.py:816`](../Mod/CAM/Path/Post/Gui/DlgPostProcess.py#L816) | construction | Y | Y | Y | Y | Y | Follow-up |
| dialog-003 | Core GUI | AboutApplication | [`src/Gui/Dialogs/AboutApplication.ui:1`](../Gui/Dialogs/AboutApplication.ui#L1) | designer | Y | N | N | N | Y | Follow-up |
| dialog-005 | Core GUI | Add Property | [`src/Gui/Dialogs/DlgAddProperty.ui:1`](../Gui/Dialogs/DlgAddProperty.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-034 | Core GUI | Attach to Remote Debugger | [`src/Gui/RemoteDebugger.ui:1`](../Gui/RemoteDebugger.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-154 | Core GUI | CameraDialog | [`src/Gui/PreferencePages/DlgSettingsNavigation.h:70`](../Gui/PreferencePages/DlgSettingsNavigation.h#L70) | subclass | Y | Y | Y | Y | N | Follow-up |
| dialog-027 | Core GUI | CheckListDialog | [`src/Gui/Dialogs/DlgTreeWidget.ui:1`](../Gui/Dialogs/DlgTreeWidget.ui#L1) | designer | ? | Y | N | Y | N | Follow-up |
| dialog-004 | Core GUI | Choose Window | [`src/Gui/Dialogs/DlgActivateWindow.ui:1`](../Gui/Dialogs/DlgActivateWindow.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-157 | Core GUI | ContainerDialog | [`src/Gui/WidgetFactory.h:262`](../Gui/WidgetFactory.h#L262) | subclass | N | N | ? | N | ? | Follow-up |
| dialog-150 | Core GUI | Customize | [`src/Gui/Dialogs/DlgCustomizeImp.h:52`](../Gui/Dialogs/DlgCustomizeImp.h#L52) | subclass | Y | N | Y | N | Y | Follow-up |
| dialog-006 | Core GUI | DlgAuthorization | [`src/Gui/Dialogs/DlgAuthorization.ui:1`](../Gui/Dialogs/DlgAuthorization.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-007 | Core GUI | DlgCheckableMessageBox | [`src/Gui/Dialogs/DlgCheckableMessageBox.ui:1`](../Gui/Dialogs/DlgCheckableMessageBox.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-009 | Core GUI | DlgCreateNewPreferencePack | [`src/Gui/Dialogs/DlgCreateNewPreferencePack.ui:1`](../Gui/Dialogs/DlgCreateNewPreferencePack.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-012 | Core GUI | DlgInputDialogImp | [`src/Gui/Dialogs/DlgInputDialog.ui:1`](../Gui/Dialogs/DlgInputDialog.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-013 | Core GUI | DlgMacroExecute | [`src/Gui/Dialogs/DlgMacroExecute.ui:1`](../Gui/Dialogs/DlgMacroExecute.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-014 | Core GUI | DlgMacroRecord | [`src/Gui/Dialogs/DlgMacroRecord.ui:1`](../Gui/Dialogs/DlgMacroRecord.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-024 | Core GUI | DlgRunExternal | [`src/Gui/Dialogs/DlgRunExternal.ui:1`](../Gui/Dialogs/DlgRunExternal.ui#L1) | designer | ? | N | N | N | N | Follow-up |
| dialog-025 | Core GUI | DlgSettingsColorGradient | [`src/Gui/Dialogs/DlgSettingsColorGradient.ui:1`](../Gui/Dialogs/DlgSettingsColorGradient.ui#L1) | designer | Y | Y | N | Y | Y | Follow-up |
| dialog-026 | Core GUI | DlgThemeEditor | [`src/Gui/Dialogs/DlgThemeEditor.ui:1`](../Gui/Dialogs/DlgThemeEditor.ui#L1) | designer | N | N | Y | Y | N | Follow-up |
| dialog-151 | Core GUI | DlgUnitsCalculator | [`src/Gui/Dialogs/DlgUnitsCalculatorImp.h:43`](../Gui/Dialogs/DlgUnitsCalculatorImp.h#L43) | subclass | Y | N | N | N | N | Follow-up |
| dialog-021 | Core GUI | Document Information | [`src/Gui/Dialogs/DlgProjectInformation.ui:1`](../Gui/Dialogs/DlgProjectInformation.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-010 | Core GUI | Document Object | [`src/Gui/Dialogs/DlgDocumentObject.ui:1`](../Gui/Dialogs/DlgDocumentObject.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-029 | Core GUI | Document Recovery | [`src/Gui/DocumentRecovery.ui:1`](../Gui/DocumentRecovery.ui#L1) | designer | Y | N | Y | N | N | Follow-up |
| dialog-022 | Core GUI | Document Utility | [`src/Gui/Dialogs/DlgProjectUtility.ui:1`](../Gui/Dialogs/DlgProjectUtility.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-011 | Core GUI | Expression Editor | [`src/Gui/Dialogs/DlgExpressionInput.ui:1`](../Gui/Dialogs/DlgExpressionInput.ui#L1) | designer | Y | N | N | N | N | Follow-up |
| dialog-018 | Core GUI | Find | [`src/Gui/Dialogs/DlgParameterFind.ui:1`](../Gui/Dialogs/DlgParameterFind.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-148 | Core GUI | IconDialog | [`src/Gui/Dialogs/DlgActionsImp.h:101`](../Gui/Dialogs/DlgActionsImp.h#L101) | subclass | Y | Y | Y | Y | Y | Pass |
| dialog-008 | Core GUI | IconDialog (DlgChooseIcon) | [`src/Gui/Dialogs/DlgChooseIcon.ui:1`](../Gui/Dialogs/DlgChooseIcon.ui#L1) | designer | Y | Y | Y | Y | Y | Pass |
| dialog-149 | Core GUI | IconFolders | [`src/Gui/Dialogs/DlgActionsImp.h:118`](../Gui/Dialogs/DlgActionsImp.h#L118) | subclass | Y | N | N | Y | N | Follow-up |
| dialog-031 | Core GUI | Input Vector | [`src/Gui/InputVector.ui:1`](../Gui/InputVector.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-019 | Core GUI | Manage Preference Packs | [`src/Gui/Dialogs/DlgPreferencePackManagement.ui:1`](../Gui/Dialogs/DlgPreferencePackManagement.ui#L1) | designer | Y | N | Y | Y | Y | Follow-up |
| dialog-015 | Core GUI | Material Properties | [`src/Gui/Dialogs/DlgMaterialProperties.ui:1`](../Gui/Dialogs/DlgMaterialProperties.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-032 | Core GUI | Mouse Buttons | [`src/Gui/MouseButtons.ui:1`](../Gui/MouseButtons.ui#L1) | designer | Y | Y | Y | Y | Y | Pass |
| dialog-016 | Core GUI | Object Selection | [`src/Gui/Dialogs/DlgObjectSelection.ui:1`](../Gui/Dialogs/DlgObjectSelection.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-017 | Core GUI | Parameter Editor | [`src/Gui/Dialogs/DlgParameter.ui:1`](../Gui/Dialogs/DlgParameter.ui#L1) | designer | Y | N | N | N | N | Follow-up |
| dialog-033 | Core GUI | Placement | [`src/Gui/Placement.ui:1`](../Gui/Placement.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-020 | Core GUI | Preferences | [`src/Gui/Dialogs/DlgPreferences.ui:1`](../Gui/Dialogs/DlgPreferences.ui#L1) | designer | Y | N | Y | N | N | Follow-up |
| dialog-191 | Core GUI | Property map editor dialog | [`src/Gui/propertyeditor/PropertyItem.cpp:4932`](../Gui/propertyeditor/PropertyItem.cpp#L4932) | construction | Y | Y | Y | N | Y | Follow-up |
| dialog-190 | Core GUI | Property Uses | [`src/Gui/propertyeditor/PropertyEditor.cpp:1115`](../Gui/propertyeditor/PropertyEditor.cpp#L1115) | construction | Y | Y | Y | Y | Y | Pass |
| dialog-023 | Core GUI | Revert to Backup Config | [`src/Gui/Dialogs/DlgRevertToBackupConfig.ui:1`](../Gui/Dialogs/DlgRevertToBackupConfig.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-035 | Core GUI | Scene Inspector | [`src/Gui/SceneInspector.ui:1`](../Gui/SceneInspector.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-152 | Core GUI | SelectModule | [`src/Gui/FileDialog.h:328`](../Gui/FileDialog.h#L328) | subclass | Y | N | Y | Y | N | Follow-up |
| dialog-159 | Core GUI | StatusWidget | [`src/Gui/Widgets.h:500`](../Gui/Widgets.h#L500) | subclass | Y | N | Y | Y | Y | Follow-up |
| dialog-037 | Core GUI | VectorListEditor | [`src/Gui/VectorListEditor.ui:1`](../Gui/VectorListEditor.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-028 | Core GUI | Version Migrator | [`src/Gui/Dialogs/DlgVersionMigrator.ui:1`](../Gui/Dialogs/DlgVersionMigrator.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-002 | Core GUI | View Turntable | [`src/Gui/DemoMode.ui:1`](../Gui/DemoMode.ui#L1) | designer | N | N | N | N | N | Follow-up |
| dialog-100 | Draft | Annotation Styles Editor | [`src/Mod/Draft/Resources/ui/dialog_AnnotationStyleEditor.ui:1`](../Mod/Draft/Resources/ui/dialog_AnnotationStyleEditor.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-101 | Draft | DxfImportDialog | [`src/Mod/Draft/Resources/ui/preferences-dxf-import.ui:1`](../Mod/Draft/Resources/ui/preferences-dxf-import.ui#L1) | designer | N | N | N | N | Y | Follow-up |
| dialog-099 | Draft | Layers Manager | [`src/Mod/Draft/Resources/ui/dialogLayers.ui:1`](../Mod/Draft/Resources/ui/dialogLayers.ui#L1) | designer | N | N | Y | N | N | Follow-up |
| dialog-210 | Fem | Data Summary dialog | [`src/Mod/Fem/femguiutils/data_extraction.py:113`](../Mod/Fem/femguiutils/data_extraction.py#L113) | construction | Y | Y | N | Y | Y | Follow-up |
| dialog-209 | Fem | Data view dialog | [`src/Mod/Fem/femguiutils/data_extraction.py:99`](../Mod/Fem/femguiutils/data_extraction.py#L99) | construction | Y | N | Y | Y | Y | Follow-up |
| dialog-181 | Fem | FEM solver report dialog | [`src/Mod/Fem/femsolver/reportdialog.py:43`](../Mod/Fem/femsolver/reportdialog.py#L43) | subclass | Y | Y | N | Y | Y | Follow-up |
| dialog-211 | Fem | Histogram data table dialog | [`src/Mod/Fem/femtaskpanels/task_post_histogram.py:138`](../Mod/Fem/femtaskpanels/task_post_histogram.py#L138) | construction | Y | Y | Y | Y | Y | Pass |
| dialog-182 | Fem | SettingsDialog | [`src/Mod/Fem/femtaskpanels/base_fempreviewpanel.py:56`](../Mod/Fem/femtaskpanels/base_fempreviewpanel.py#L56) | subclass | N | Y | Y | Y | N | Follow-up |
| dialog-192 | Import | OCAF Browser | [`src/Mod/Import/Gui/OCAFBrowser.cpp:313`](../Mod/Import/Gui/OCAFBrowser.cpp#L313) | construction | Y | Y | N | Y | Y | Follow-up |
| dialog-105 | Material | Array2D | [`src/Mod/Material/Gui/Array2D.ui:1`](../Mod/Material/Gui/Array2D.ui#L1) | designer | N | N | Y | Y | Y | Follow-up |
| dialog-106 | Material | Array3D | [`src/Mod/Material/Gui/Array3D.ui:1`](../Mod/Material/Gui/Array3D.ui#L1) | designer | N | Y | N | Y | ? | Follow-up |
| dialog-110 | Material | ListEdit | [`src/Mod/Material/Gui/ListEdit.ui:1`](../Mod/Material/Gui/ListEdit.ui#L1) | designer | N | Y | Y | Y | Y | Follow-up |
| dialog-113 | Material | Material Models | [`src/Mod/Material/Gui/ModelSelect.ui:1`](../Mod/Material/Gui/ModelSelect.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-114 | Material | MaterialEditor | [`src/Mod/Material/Gui/Resources/ui/materials-editor.ui:1`](../Mod/Material/Gui/Resources/ui/materials-editor.ui#L1) | designer | N | N | N | Y | N | Follow-up |
| dialog-111 | Material | MaterialSave | [`src/Mod/Material/Gui/MaterialSave.ui:1`](../Mod/Material/Gui/MaterialSave.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-112 | Material | MaterialsEditor | [`src/Mod/Material/Gui/MaterialsEditor.ui:1`](../Mod/Material/Gui/MaterialsEditor.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-109 | Material | MatGui::ImageEdit | [`src/Mod/Material/Gui/ImageEdit.ui:1`](../Mod/Material/Gui/ImageEdit.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-115 | Material | TextEdit | [`src/Mod/Material/Gui/TextEdit.ui:1`](../Mod/Material/Gui/TextEdit.ui#L1) | designer | N | Y | N | Y | N | Follow-up |
| dialog-118 | Mesh | DlgRegularSolid | [`src/Mod/Mesh/Gui/DlgRegularSolid.ui:1`](../Mod/Mesh/Gui/DlgRegularSolid.ui#L1) | designer | Y | N | Y | N | N | Follow-up |
| dialog-117 | Mesh | Evaluation Settings | [`src/Mod/Mesh/Gui/DlgEvaluateSettings.ui:1`](../Mod/Mesh/Gui/DlgEvaluateSettings.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-162 | Mesh | ParametersDialog | [`src/Mod/Mesh/Gui/SegmentationBestFit.h:67`](../Mod/Mesh/Gui/SegmentationBestFit.h#L67) | subclass | Y | Y | Y | Y | N | Follow-up |
| dialog-160 | Mesh | SmoothingDialog | [`src/Mod/Mesh/Gui/DlgSmoothing.h:79`](../Mod/Mesh/Gui/DlgSmoothing.h#L79) | subclass | N | Y | Y | Y | N | Follow-up |
| dialog-124 | Part | DlgPartCylinder | [`src/Mod/Part/Gui/DlgPartCylinder.ui:1`](../Mod/Part/Gui/DlgPartCylinder.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-125 | Part | IGES Input File | [`src/Mod/Part/Gui/DlgPartImportIges.ui:1`](../Mod/Part/Gui/DlgPartImportIges.ui#L1) | designer | ? | N | Y | Y | N | Follow-up |
| dialog-130 | Part | Shape From Mesh | [`src/Mod/Part/Gui/ShapeFromMesh.ui:1`](../Mod/Part/Gui/ShapeFromMesh.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-165 | Part | STEP Import Settings | [`src/Mod/Part/Gui/DlgImportStep.h:74`](../Mod/Part/Gui/DlgImportStep.h#L74) | subclass | Y | N | Y | Y | N | Follow-up |
| dialog-163 | Part | TaskExportStep | [`src/Mod/Part/Gui/DlgExportStep.h:91`](../Mod/Part/Gui/DlgExportStep.h#L91) | subclass | Y | N | Y | Y | N | Follow-up |
| dialog-131 | PartDesign | Active Body Required | [`src/Mod/PartDesign/Gui/DlgActiveBody.ui:1`](../Mod/PartDesign/Gui/DlgActiveBody.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-213 | PartDesign | Gear dialog | [`src/Mod/PartDesign/Scripts/Gear.py:270`](../Mod/PartDesign/Scripts/Gear.py#L270) | construction | N | Y | N | Y | N | Follow-up |
| dialog-132 | PartDesign | Reference | [`src/Mod/PartDesign/Gui/DlgReference.ui:1`](../Mod/PartDesign/Gui/DlgReference.ui#L1) | designer | Y | N | N | Y | N | Follow-up |
| dialog-183 | PartDesign | SprocketDialog | [`src/Mod/PartDesign/fcsprocket/fcsprocketdialog.py:38`](../Mod/PartDesign/fcsprocket/fcsprocketdialog.py#L38) | subclass | N | Y | N | Y | Y | Follow-up |
| dialog-133 | Points | ASCII Points Import | [`src/Mod/Points/Gui/DlgPointsRead.ui:1`](../Mod/Points/Gui/DlgPointsRead.ui#L1) | designer | ? | N | N | N | N | Follow-up |
| dialog-134 | Sketcher | Edit Text | [`src/Mod/Sketcher/Gui/EditTextDialog.ui:1`](../Mod/Sketcher/Gui/EditTextDialog.ui#L1) | designer | N | Y | Y | Y | N | Follow-up |
| dialog-135 | Sketcher | InsertDatum | [`src/Mod/Sketcher/Gui/InsertDatum.ui:1`](../Mod/Sketcher/Gui/InsertDatum.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-138 | Sketcher | SketcherGui::SketchRectangularArrayDialog | [`src/Mod/Sketcher/Gui/SketchRectangularArrayDialog.ui:1`](../Mod/Sketcher/Gui/SketchRectangularArrayDialog.ui#L1) | designer | Y | Y | Y | N | N | Follow-up |
| dialog-139 | Sketcher | SketcherRegularPolygonDialog | [`src/Mod/Sketcher/Gui/SketcherRegularPolygonDialog.ui:1`](../Mod/Sketcher/Gui/SketcherRegularPolygonDialog.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-136 | Sketcher | SketchMirrorDialog | [`src/Mod/Sketcher/Gui/SketchMirrorDialog.ui:1`](../Mod/Sketcher/Gui/SketchMirrorDialog.ui#L1) | designer | Y | N | Y | Y | N | Follow-up |
| dialog-137 | Sketcher | SketchOrientationDialog | [`src/Mod/Sketcher/Gui/SketchOrientationDialog.ui:1`](../Mod/Sketcher/Gui/SketchOrientationDialog.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-142 | Spreadsheet | Cell Properties | [`src/Mod/Spreadsheet/Gui/PropertiesDialog.ui:1`](../Mod/Spreadsheet/Gui/PropertiesDialog.ui#L1) | designer | N | N | Y | N | N | Follow-up |
| dialog-140 | Spreadsheet | DlgBindSheet | [`src/Mod/Spreadsheet/Gui/DlgBindSheet.ui:1`](../Mod/Spreadsheet/Gui/DlgBindSheet.ui#L1) | designer | N | Y | Y | N | N | Follow-up |
| dialog-141 | Spreadsheet | Setup Configuration Table | [`src/Mod/Spreadsheet/Gui/DlgSheetConf.ui:1`](../Mod/Spreadsheet/Gui/DlgSheetConf.ui#L1) | designer | N | Y | Y | N | N | Follow-up |
| dialog-144 | TechDraw | Change Editable Field | [`src/Mod/TechDraw/Gui/DlgTemplateField.ui:1`](../Mod/TechDraw/Gui/DlgTemplateField.ui#L1) | designer | Y | Y | Y | N | N | Follow-up |
| dialog-168 | TechDraw | DirectionEditDialog | [`src/Mod/TechDraw/Gui/TaskProjGroup.h:181`](../Mod/TechDraw/Gui/TaskProjGroup.h#L181) | subclass | N | N | N | N | N | Follow-up |
| dialog-143 | TechDraw | DlgPageChooser | [`src/Mod/TechDraw/Gui/DlgPageChooser.ui:1`](../Mod/TechDraw/Gui/DlgPageChooser.ui#L1) | designer | Y | Y | Y | Y | N | Follow-up |
| dialog-201 | TechDraw | Document Source | [`src/Mod/TechDraw/Gui/mrichtextedit.cpp:253`](../Mod/TechDraw/Gui/mrichtextedit.cpp#L253) | construction | Y | N | N | N | N | Follow-up |
| dialog-214 | TechDraw | Fill Template Fields In <page label> | [`src/Mod/TechDraw/TechDrawTools/TaskFillTemplateFields.py:134`](../Mod/TechDraw/TechDrawTools/TaskFillTemplateFields.py#L134) | construction | N | N | Y | Y | N | Follow-up |
| dialog-200 | TechDraw | Prefix Text | [`src/Mod/TechDraw/Gui/CommandExtensionDims.cpp:118`](../Mod/TechDraw/Gui/CommandExtensionDims.cpp#L118) | construction | Y | Y | N | Y | N | Follow-up |
| dialog-145 | TechDraw | SymbolChooser | [`src/Mod/TechDraw/Gui/SymbolChooser.ui:1`](../Mod/TechDraw/Gui/SymbolChooser.ui#L1) | designer | Y | Y | N | Y | N | Follow-up |
| dialog-146 | Test | UnitTest | [`src/Mod/Test/Gui/UnitTest.ui:1`](../Mod/Test/Gui/UnitTest.ui#L1) | designer | Y | N | N | N | N | Follow-up |

## Screened-out candidates

These entries remain listed so that the discovery boundary is reviewable.

| ID | Area | Candidate | Definition | Disposition | Reason |
| --- | --- | --- | --- | --- | --- |
| dialog-047 | AddonManager | Add toolbar button dialog | [`src/Mod/AddonManager/toolbar_button.ui:1`](../Mod/AddonManager/toolbar_button.ui#L1) | duplicate | Duplicate representation of dialog-041. |
| dialog-049 | AddonManager | Updating Addons | [`src/Mod/AddonManager/update_all_progress.ui:1`](../Mod/AddonManager/update_all_progress.ui#L1) | duplicate | Duplicate representation of dialog-044. |
| dialog-050 | Assembly | TaskAssemblyCreateSimulation | [`src/Mod/Assembly/Gui/Resources/panels/TaskAssemblyCreateSimulation.ui:1`](../Mod/Assembly/Gui/Resources/panels/TaskAssemblyCreateSimulation.ui#L1) | excluded | Excluded: although the Designer root is QDialog (TaskAssemblyCreateSimulation.ui:4), the form is loaded into a Python task object (CommandCreateSimulation.py:779,804) and shown via Gui.Control.showDialog (95-96,275-276), which embeds it in the task panel rather than independently showing a QDialog. |
| dialog-052 | BIM | BimServer | [`src/Mod/BIM/Resources/ui/BimServerTaskPanel.ui:1`](../Mod/BIM/Resources/ui/BimServerTaskPanel.ui#L1) | excluded | Excluded: although the Designer root is QDialog (BimServerTaskPanel.ui:4), the filename identifies a task panel, and no in-tree implementation or independent dialog call site exists. BIM only optionally imports external BIMServer support and registers WebTools_BimServer (InitGui.py:439-450); the form is merely bundled as a resource (Arch.qrc:225). |
| dialog-054 | BIM | DialogDisplayText | [`src/Mod/BIM/Resources/ui/DialogDisplayText.ui:1`](../Mod/BIM/Resources/ui/DialogDisplayText.ui#L1) | excluded | The form is a QDialog (DialogDisplayText.ui:4), but no implementation, loader, constructor, or caller references it; the only non-translation reference is resource registration at Arch.qrc:227. It is not demonstrably independently shown. |
| dialog-058 | BIM | Single IFC Document | [`src/Mod/BIM/Resources/ui/dialogConvertDocument.ui:1`](../Mod/BIM/Resources/ui/dialogConvertDocument.ui#L1) | excluded | Excluded: no source reference loads or shows dialogConvertDocument.ui. IFC_ConvertDocument.Activated directly calls ifc_tools.convert_document at src/Mod/BIM/nativeifc/ifc_commands.py:122-131; the active options dialog is dialogImport.ui at ifc_import.py:150-168. |
| dialog-072 | BIM | Dialog | [`src/Mod/BIM/Resources/ui/dialogPhases.ui:1`](../Mod/BIM/Resources/ui/dialogPhases.ui#L1) | excluded | The QDialog form is only registered as a resource at src/Mod/BIM/Resources/Arch.qrc:263; no callers or loadUi references independently construct or show it. It is therefore excluded as unused. |
| dialog-075 | BIM | Quantity Surveying dialog | [`src/Mod/BIM/Resources/ui/dialogQuantitySurveying.ui:1`](../Mod/BIM/Resources/ui/dialogQuantitySurveying.ui#L1) | excluded | Excluded: dialogQuantitySurveying.ui is only registered as a resource. The active survey implementation constructs a custom QWidget task panel at ArchCommands.py:1317 and shows it via Control.showDialog at lines 1094-1095; no independent QDialog use was found. |
| dialog-077 | BIM | Spaces Manager | [`src/Mod/BIM/Resources/ui/dialogSpaces.ui:1`](../Mod/BIM/Resources/ui/dialogSpaces.ui#L1) | excluded | The form is a QDialog (src/Mod/BIM/Resources/ui/dialogSpaces.ui:4) but has no implementation or caller; source search finds only its resource registration (src/Mod/BIM/Resources/Arch.qrc:270) and translation references. It is not independently shown. |
| dialog-205 | BIM | IFC Explorer | [`src/Mod/BIM/importers/importIFClegacy.py:2149`](../Mod/BIM/importers/importIFClegacy.py#L2149) | duplicate | Duplicate representation of dialog-203. |
| dialog-080 | CAM | DlgJobChooser | [`src/Mod/CAM/Gui/DlgJobChooser.ui:1`](../Mod/CAM/Gui/DlgJobChooser.ui#L1) | excluded | Excluded: the QDialog form is not built by src/Mod/CAM/Gui/CMakeLists.txt (lines 21-42), is absent from Resources/Path.qrc (lines 115-124), and has no construction or exec/show caller in the source tree. It is therefore not an independently shown dialog candidate. |
| dialog-083 | CAM | Base Model Selection | [`src/Mod/CAM/Gui/Resources/panels/DlgJobModelSelect.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgJobModelSelect.ui#L1) | excluded | Excluded: the QDialog form is registered in Path.qrc (line 117) but has no current implementation or caller reference. Current model selection uses DlgJobCreate.ui via JobDlg.py:61 and Job.py:1774-1777. |
| dialog-089 | CAM | DlgJobChooser | [`src/Mod/CAM/Gui/Resources/panels/DlgToolCopy.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgToolCopy.ui#L1) | excluded | Excluded: only a QDialog resource at DlgToolCopy.ui:4, registered in Path.qrc:123; no caller independently loads or shows it. |
| dialog-090 | CAM | Tool Editor | [`src/Mod/CAM/Gui/Resources/panels/DlgToolEdit.ui:1`](../Mod/CAM/Gui/Resources/panels/DlgToolEdit.ui#L1) | excluded | The QDialog form is only registered as a resource; no current implementation, loadUi call, or show/exec caller references DlgToolEdit.ui. The active tool editor uses ToolBitEditor.ui as an embedded QWidget. |
| dialog-094 | CAM | TaskPathSimulator | [`src/Mod/CAM/Gui/Resources/panels/TaskCAMSimulator.ui:1`](../Mod/CAM/Gui/Resources/panels/TaskCAMSimulator.ui#L1) | excluded | The form is embedded in CAMSimTaskUi: SimulatorGL.py:68 loads TaskCAMSimulator.ui, and SimulatorGL.py:228 passes the task wrapper to FreeCADGui.Control.showDialog. It is therefore an embedded task panel despite its QDialog root. |
| dialog-095 | CAM | Path Simulator | [`src/Mod/CAM/Gui/Resources/panels/TaskPathCamoticsSim.ui:1`](../Mod/CAM/Gui/Resources/panels/TaskPathCamoticsSim.ui#L1) | excluded | Excluded: the QDialog-root Designer form is loaded into CAMoticsUI and passed to FreeCADGui.Control.showDialog as a task panel, not independently shown as a QDialog. |
| dialog-096 | CAM | Path Simulator | [`src/Mod/CAM/Gui/Resources/panels/TaskPathSimulator.ui:1`](../Mod/CAM/Gui/Resources/panels/TaskPathSimulator.ui#L1) | excluded | Excluded: although the Designer root is QDialog (TaskPathSimulator.ui:4), CAMSimTaskUi loads it as a FreeCAD task form (Simulator.py:48-52) and shows it through FreeCADGui.Control.showDialog (Simulator.py:87-103), so it is an embedded task panel rather than an independently shown QDialog. |
| dialog-175 | CAM | Assign Stock Material | [`src/Mod/CAM/Path/Main/Gui/Job.py:382`](../Mod/CAM/Path/Main/Gui/Job.py#L382) | duplicate | Duplicate representation of dialog-178. |
| dialog-001 | Core GUI | Clipping | [`src/Gui/Clipping.ui:1`](../Gui/Clipping.ui#L1) | excluded | Excluded: Clipping is embedded in a QDockWidget. makeDockWidget constructs it without a parent and passes it to DockWindowManager (src/Gui/Clipping.cpp:201-208); addDockWindow explicitly reparents the widget to the dock (src/Gui/DockWindowManager.cpp:261-287). The sole caller uses makeDockWidget (src/Gui/CommandView.cpp:699-703), so it is not independently shown as a QDialog. |
| dialog-147 | Core GUI | AboutDialog | [`src/Gui/Dialogs/DlgAbout.h:77`](../Gui/Dialogs/DlgAbout.h#L77) | duplicate | Duplicate representation of dialog-003. |
| dialog-184 | Core GUI | Authorization dialog | [`src/Gui/DownloadItem.cpp:193`](../Gui/DownloadItem.cpp#L193) | duplicate | Duplicate representation of dialog-006. |
| dialog-185 | Core GUI | Authorization dialog | [`src/Gui/DownloadItem.cpp:218`](../Gui/DownloadItem.cpp#L218) | duplicate | Duplicate representation of dialog-006. |
| dialog-030 | Core GUI | DownloadManager | [`src/Gui/DownloadManager.ui:1`](../Gui/DownloadManager.ui#L1) | excluded | Although the Designer root is QDialog (src/Gui/DownloadManager.ui:4), the constructor embeds it in a QDockWidget via addDockWindow (src/Gui/DownloadManager.cpp:76-84). addDockWindow reparents the widget to the dock and sets it as the dock widget (src/Gui/DockWindowManager.cpp:285-287), so it is not an independently shown dialog. |
| dialog-186 | Core GUI | local dialog at line 182 | [`src/Gui/InputVector.cpp:182`](../Gui/InputVector.cpp#L182) | duplicate | Duplicate representation of dialog-031. |
| dialog-187 | Core GUI | Input Vector dialog | [`src/Gui/InputVector.cpp:237`](../Gui/InputVector.cpp#L237) | duplicate | Duplicate representation of dialog-031. |
| dialog-153 | Core GUI | LocationDialog | [`src/Gui/InputVector.h:78`](../Gui/InputVector.h#L78) | excluded | LocationDialog is an abstract base with a protected constructor and pure virtual methods at src/Gui/InputVector.h:78-97; it is not independently constructible or shown. Concrete subclasses pass their parent through at src/Mod/Part/Gui/DlgPartCylinderImp.cpp:32-34, and the cylinder dialog is shown with Gui::getMainWindow() as parent at src/Mod/Part/Gui/CommandSimple.cpp:66-67. The QDialog created at src/Gui/InputVector.cpp:237-243 is a nested temporary editor, not this candidate. |
| dialog-188 | Core GUI | Authorization | [`src/Gui/NetworkRetriever.cpp:469`](../Gui/NetworkRetriever.cpp#L469) | duplicate | Duplicate representation of dialog-006. |
| dialog-189 | Core GUI | Mouse Buttons | [`src/Gui/PreferencePages/DlgSettingsNavigation.cpp:310`](../Gui/PreferencePages/DlgSettingsNavigation.cpp#L310) | duplicate | Duplicate representation of dialog-032. |
| dialog-155 | Core GUI | Scene Inspector | [`src/Gui/SceneInspector.h:75`](../Gui/SceneInspector.h#L75) | duplicate | Duplicate representation of dialog-035. |
| dialog-036 | Core GUI | TextureMapping | [`src/Gui/TextureMapping.ui:1`](../Gui/TextureMapping.ui#L1) | excluded | Excluded: TextureMapping is embedded in TaskTextureMapping via addTaskBox at TextureMapping.cpp:193-197; the command shows TaskTextureMapping through Control::showDialog at CommandView.cpp:3138-3142. No independent QDialog showing call was found. |
| dialog-156 | Core GUI | Transform | [`src/Gui/Transform.h:71`](../Gui/Transform.h#L71) | excluded | Excluded: Transform is embedded in a task panel, not independently shown. TaskTransform constructs it at src/Gui/Transform.cpp:472 and adds it via addTaskBox at :474; addTaskBox embeds widgets in a TaskBox layout at src/Gui/TaskView/TaskDialog.cpp:72-76. The shown object is TaskTransform via src/Gui/CommandDoc.cpp:1939. |
| dialog-158 | Core GUI | CheckListDialog | [`src/Gui/Widgets.h:202`](../Gui/Widgets.h#L202) | duplicate | Duplicate representation of dialog-027. |
| dialog-208 | Draft | DXF Import | [`src/Mod/Draft/DxfImportDialog.py:14`](../Mod/Draft/DxfImportDialog.py#L14) | duplicate | Duplicate representation of dialog-101. |
| dialog-102 | Fem | MeshGroupXDMFExport | [`src/Mod/Fem/Gui/Resources/ui/MeshGroupXDMFExport.ui:1`](../Mod/Fem/Gui/Resources/ui/MeshGroupXDMFExport.ui#L1) | excluded | Excluded: although the Designer root is QDialog (MeshGroupXDMFExport.ui:4), it is used only as a FEM task panel, not an independently shown secondary dialog. |
| dialog-103 | Fem | Constraint Temperature legacy task panel form | [`src/Mod/Fem/Gui/TaskPanelConstraintTemperature.ui:1`](../Mod/Fem/Gui/TaskPanelConstraintTemperature.ui#L1) | excluded | The QDialog-rooted form is not referenced by the current build or implementation. The active constraint UI is TaskFemConstraintTemperature.ui, a QWidget installed into a TaskView task dialog; the candidate is therefore not an independently shown QDialog. |
| dialog-104 | Fem | Initial temperature task panel | [`src/Mod/Fem/Gui/TaskPanelInitialTemperature.ui:1`](../Mod/Fem/Gui/TaskPanelInitialTemperature.ui#L1) | excluded | The candidate root is QDialog at TaskPanelInitialTemperature.ui:3-4, but the active flow shows TaskDlgFemConstraintInitialTemperature at ViewProviderFemConstraintInitialTemperature.cpp:54, constructs a QWidget task panel at TaskFemConstraintInitialTemperature.cpp:52-56, and uses the QWidget-rooted counterpart at TaskFemConstraintInitialTemperature.ui:3-4. CMakeLists.txt:73 and 169-171 list only the active counterpart. |
| dialog-212 | Fem | Lineplot data table dialog | [`src/Mod/Fem/femtaskpanels/task_post_lineplot.py:132`](../Mod/Fem/femtaskpanels/task_post_lineplot.py#L132) | duplicate | Duplicate representation of dialog-211. |
| dialog-107 | Material | Display Properties | [`src/Mod/Material/Gui/DlgDisplayProperties.ui:1`](../Mod/Material/Gui/DlgDisplayProperties.ui#L1) | excluded | Excluded: DlgDisplayPropertiesImp is constructed for and embedded in the task panel, not shown as an independent dialog. |
| dialog-108 | Material | Material task-panel form | [`src/Mod/Material/Gui/DlgMaterial.ui:1`](../Mod/Material/Gui/DlgMaterial.ui#L1) | excluded | The QDialog root in DlgMaterial.ui:4 is used as an embedded widget: DlgMaterialImp constructs it with floating=false at DlgMaterialImp.cpp:258, then adds it to a TaskBox layout at lines 259-261. No independent DlgMaterialImp construction or show/exec call was found; the floating dock path is unused by callers. |
| dialog-116 | Mesh | Evaluate and Repair Mesh | [`src/Mod/Mesh/Gui/DlgEvaluateMesh.ui:1`](../Mod/Mesh/Gui/DlgEvaluateMesh.ui#L1) | excluded | Excluded: DlgEvaluateMeshImp is only instantiated as DockEvaluateMeshImp with Gui::getMainWindow() (DlgEvaluateMeshImp.cpp:1350-1355), then embedded in a QScrollArea and QDockWidget (DlgEvaluateMeshImp.cpp:1379-1396). No independent QDialog construction or showing was found. |
| dialog-161 | Mesh | RemoveComponentsDialog | [`src/Mod/Mesh/Gui/RemoveComponents.h:84`](../Mod/Mesh/Gui/RemoveComponents.h#L84) | excluded | The QDialog wrapper is defined at src/Mod/Mesh/Gui/RemoveComponents.h:84-99 but has no in-tree construction or show call. The command creates TaskRemoveComponents instead, embedding RemoveComponents as a task panel at RemoveComponents.cpp:246-250 and Command.cpp:1183-1190. |
| dialog-119 | MeshPart | CrossSections | [`src/Mod/MeshPart/Gui/CrossSections.ui:1`](../Mod/MeshPart/Gui/CrossSections.ui#L1) | excluded | Excluded: TaskCrossSections constructs CrossSections without a parent and inserts it into a TaskBox via addTaskBox at CrossSections.cpp:633-637; addTaskBox embeds the widget in its layout at TaskDialog.cpp:72-77. The command shows the TaskDialog, not CrossSections, at Command.cpp:284-299. |
| dialog-120 | Part | Cross Sections | [`src/Mod/Part/Gui/CrossSections.ui:1`](../Mod/Part/Gui/CrossSections.ui#L1) | excluded | The Designer root is QDialog (CrossSections.ui:4), but TaskCrossSections constructs it without a parent and embeds it via addTaskBox (CrossSections.cpp:591-595). The command shows TaskCrossSections through the task-view controller (Command.cpp:1671-1683); no independent CrossSections dialog presentation was found. |
| dialog-121 | Part | Block Definition | [`src/Mod/Part/Gui/DlgBlock.ui:1`](../Mod/Part/Gui/DlgBlock.ui#L1) | excluded | Orphaned Designer form; static references do not establish an independently shown dialog. |
| dialog-122 | Part | DlgExtrusion | [`src/Mod/Part/Gui/DlgExtrusion.ui:1`](../Mod/Part/Gui/DlgExtrusion.ui#L1) | excluded | Although the Designer root is QDialog (src/Mod/Part/Gui/DlgExtrusion.ui:4), TaskExtrusion constructs it with no parent and immediately embeds it via addTaskBox (src/Mod/Part/Gui/DlgExtrusion.cpp:911-915). The command shows TaskExtrusion as the task dialog (src/Mod/Part/Gui/Command.cpp:1443-1446); it is not independently shown as a secondary QDialog. |
| dialog-164 | Part | FilletEdgesDialog | [`src/Mod/Part/Gui/DlgFilletEdges.h:143`](../Mod/Part/Gui/DlgFilletEdges.h#L143) | excluded | No in-tree caller constructs FilletEdgesDialog. Fillet and chamfer commands instead show TaskFilletEdges/TaskChamferEdges (Command.cpp:1590,1618), whose DlgFilletEdges widgets are embedded via addTaskBox (DlgFilletEdges.cpp:1169-1172,1221-1224). |
| dialog-123 | Part | DlgPartBox | [`src/Mod/Part/Gui/DlgPartBox.ui:1`](../Mod/Part/Gui/DlgPartBox.ui#L1) | excluded | The form is compiled and wrapped by DlgPartBoxImp (DlgPartBoxImp.cpp:39-40), but no in-tree caller constructs, shows, or executes it; unlike the analogous cylinder dialog, no command references DlgPartBoxImp. Therefore it is not an independently shown QDialog candidate. |
| dialog-126 | Part | DlgPartImportStep | [`src/Mod/Part/Gui/DlgPartImportStep.ui:1`](../Mod/Part/Gui/DlgPartImportStep.ui#L1) | duplicate | Duplicate of the IGES input-file dialog template; no independent call site was found. |
| dialog-127 | Part | DlgRevolution | [`src/Mod/Part/Gui/DlgRevolution.ui:1`](../Mod/Part/Gui/DlgRevolution.ui#L1) | excluded | Excluded: DlgRevolution is only constructed without a parent at DlgRevolution.cpp:665 and immediately embedded via addTaskBox at DlgRevolution.cpp:666; the task panel is shown by Command.cpp:1562. It is not an independently shown QDialog. |
| dialog-128 | Part | DlgScale | [`src/Mod/Part/Gui/DlgScale.ui:1`](../Mod/Part/Gui/DlgScale.ui#L1) | excluded | Excluded: although the Designer root is QDialog (DlgScale.ui:4), DlgScale is constructed without a parent and immediately embedded in TaskScale via addTaskBox (DlgScale.cpp:372-376). TaskDialog::addTaskBox reparents it through groupLayout()->addWidget (TaskDialog.cpp:72-76); the command shows TaskScale, not DlgScale, (Command.cpp:1471-1476). No independent DlgScale show/exec call was found. The form uses layouts and native controls, with explicit tab stops; spinbox labels have no buddies (DlgScale.ui:20-31, 61-67, 109-115, 176-181, 229-237), so keyboard labeling is unclear but outside the top-level dialog catalog. |
| dialog-129 | Part | Persistent Section Cut | [`src/Mod/Part/Gui/SectionCutting.ui:1`](../Mod/Part/Gui/SectionCutting.ui#L1) | excluded | The Designer root is QDialog (SectionCutting.ui:3-4), but SectionCut::makeDockWidget constructs it and adds it to a dock widget (SectionCutting.cpp:1455-1464); the sole command caller invokes that dock path (Command.cpp:2477-2484). |
| dialog-193 | PartDesign | Reference | [`src/Mod/PartDesign/Gui/Command.cpp:1147`](../Mod/PartDesign/Gui/Command.cpp#L1147) | duplicate | Duplicate representation of dialog-132. |
| dialog-194 | PartDesign | Reference | [`src/Mod/PartDesign/Gui/ReferenceSelection.cpp:335`](../Mod/PartDesign/Gui/ReferenceSelection.cpp#L335) | duplicate | Duplicate representation of dialog-132. |
| dialog-195 | PartDesign | Reference | [`src/Mod/PartDesign/Gui/SketchWorkflow.cpp:318`](../Mod/PartDesign/Gui/SketchWorkflow.cpp#L318) | duplicate | Duplicate representation of dialog-132. |
| dialog-196 | PartDesign | Reference | [`src/Mod/PartDesign/Gui/TaskDatumParameters.cpp:137`](../Mod/PartDesign/Gui/TaskDatumParameters.cpp#L137) | duplicate | Duplicate representation of dialog-132. |
| dialog-197 | PartDesign | Reference | [`src/Mod/PartDesign/Gui/TaskPipeParameters.cpp:548`](../Mod/PartDesign/Gui/TaskPipeParameters.cpp#L548) | duplicate | Duplicate representation of dialog-132. |
| dialog-166 | Robot | TrajectorySimulate | [`src/Mod/Robot/Gui/TrajectorySimulate.h:42`](../Mod/Robot/Gui/TrajectorySimulate.h#L42) | excluded | Excluded: the command creates TaskDlgSimulate and shows it via TaskView at Command.cpp:287-288; no caller constructs or shows TrajectorySimulate. The class is only declared/implemented at TrajectorySimulate.h:42-52 and TrajectorySimulate.cpp:39-51. |
| dialog-198 | Sketcher | Insert Datum / Snell's law ratio dialog | [`src/Mod/Sketcher/Gui/CommandConstraints.cpp:10250`](../Mod/Sketcher/Gui/CommandConstraints.cpp#L10250) | duplicate | Duplicate representation of dialog-135. |
| dialog-199 | Sketcher | Edit datum dialog | [`src/Mod/Sketcher/Gui/EditDatumDialog.cpp:121`](../Mod/Sketcher/Gui/EditDatumDialog.cpp#L121) | duplicate | Duplicate representation of dialog-135. |
| dialog-167 | TechDraw | DlgTemplateField | [`src/Mod/TechDraw/Gui/DlgTemplateField.h:53`](../Mod/TechDraw/Gui/DlgTemplateField.h#L53) | duplicate | Duplicate representation of dialog-144. |
| dialog-169 | Test | UnitTestDialog | [`src/Mod/Test/Gui/UnitTestImp.h:37`](../Mod/Test/Gui/UnitTestImp.h#L37) | duplicate | Duplicate representation of dialog-146. |
