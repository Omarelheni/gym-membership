from PySide6.QtCore import QDate
from PySide6.QtWidgets import QFileDialog

from .services.subscription_operations import SubscriptionsOperation
from .services.user_operations import UsersOperations
import os


class GenericsUiFunction:
    operation_class = None
    add_item_ui_btn = None
    main = None

    def set_main_ui_functions(self):
        operation_class_ins = self.operation_class(main=self.main)



class SubscriptionUiFunction(GenericsUiFunction):
    operation_class = SubscriptionsOperation

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


class UserUiFunction(GenericsUiFunction):
    operation_class = UsersOperations
    add_item_ui_btn = 'addUserBtn'
    file_variable_name = 'user_add_file_variable'

    def set_main_ui_functions(self):
        super().set_main_ui_functions()


class AllUiFunctions:
    def __init__(self):
        self.user_ui_function = UserUiFunction()
        self.subscription_ui_function = SubscriptionUiFunction()
        # Add any other UI function instances here

    def set_main_ui_functions(self):
        self.user_ui_function.main = self
        self.user_ui_function.set_main_ui_functions()

        self.subscription_ui_function.main = self
        self.subscription_ui_function.set_main_ui_functions()
