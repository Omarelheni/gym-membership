from PySide6.QtCore import QDate
from PySide6.QtWidgets import QFileDialog

from .services.subscription_operations import SubscriptionsOperation
from .services.user_operations import UsersOperations
import os

from .utils import LocalizationManager


class GenericsUiFunction:
    operation_class = None
    add_item_ui_btn = None
    main = None
    operation_instance= None

    def set_main_ui_functions(self):
        self.operation_instance = self.operation_class(main=self.main)


class UserUiFunction(GenericsUiFunction):
    operation_class = UsersOperations
    def set_main_ui_functions(self):
        super().set_main_ui_functions()
        self.main.ui.startDate.setDate(QDate.currentDate())
        self.main.ui.subDurationW.setHidden(True)
        self.main.ui.subType.currentIndexChanged.connect(self.on_combobox_type_change)

    def on_combobox_type_change(self):
        if self.main.ui.subType.currentText() == "Autre":
            self.main.ui.subDurationW.setHidden(False)
        else:
            self.main.ui.subDurationW.setHidden(True)



class AllUiFunctions:

    def __init__(self):
        self.ui_functions = [UserUiFunction()]
        self.localization_manager = LocalizationManager("./i18n/localization.json")

    def change_language(self,text):
        if text == "ENG":
            self.ui.retranslateUiEng(self)
        if text == "FR":
            self.ui.retranslateUi(self)
        if text == "AR":
            self.ui.retranslateUiAr(self)
        self.localization_manager.language = text
        for ui_function in self.ui_functions:
            ui_function.operation_instance.translate_table_columns()

    def set_main_ui_functions(self):
        for ui_function in self.ui_functions:
            ui_function.main = self
            ui_function.set_main_ui_functions()
        self.ui.LanguageBox.currentTextChanged.connect(self.change_language)



