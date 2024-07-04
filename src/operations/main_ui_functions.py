from PySide6.QtCore import QDate
from PySide6.QtWidgets import QFileDialog, QDateEdit

from .services.subscription_operations import SubscriptionsOperation
from .services.user_operations import UsersOperations
import os

from .utils import LanguageManager


class GenericsUiFunction:
    operation_class = None
    add_item_ui_btn = None
    main = None
    operation_instance = None

    def initial_interface(self):
        self.operation_instance = self.operation_class(main=self.main)


class HomeInterface(GenericsUiFunction):
    operation_class = UsersOperations

    def initial_interface(self):
        super().initial_interface()
        self.main.ui.startDate.setDate(QDate.currentDate())
        self.main.ui.birthDate.setDate(QDate(2000, 1, 1))

        self.main.ui.subDurationW.setHidden(True)
        self.main.ui.subType.currentIndexChanged.connect(self.on_combobox_type_change)

    def on_combobox_type_change(self):
        if self.main.ui.subType.currentText() == "Autre":
            self.main.ui.subDurationW.setHidden(False)
        else:
            self.main.ui.subDurationW.setHidden(True)


class AllUiFunctions:

    def __init__(self):
        self.ui_functions = [HomeInterface()]

    def change_language(self, text):
        if text == "ENG":
            self.ui.retranslateUiEng(self)
        if text == "FR":
            self.ui.retranslateUi(self)
        if text == "AR":
            self.ui.retranslateUiAr(self)

        LanguageManager().set_language(text)

        for ui_function in self.ui_functions:
            ui_function.operation_instance.translate_table_columns()

    def set_main_ui_functions(self):
        for ui_function in self.ui_functions:
            ui_function.main = self
            ui_function.initial_interface()
        self.ui.LanguageBox.currentTextChanged.connect(self.change_language)
        LanguageManager().set_language(self.ui.LanguageBox.currentText())
