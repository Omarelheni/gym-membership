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
        operation_class_ins = self.operation_class()
        operation_class_ins.create_table()
        operation_class_ins.display_items(main=self.main)
        if self.add_item_ui_btn :
            getattr(self.main.ui, self.add_item_ui_btn).clicked.connect(lambda: operation_class_ins.add_item(uifunction=self))


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
        self.main.ui.imageBtn.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main,"Select File")
        self.user_add_file_variable = file_path
        if file_path:
            # Define the destination directory and create it if it doesn't exist
            file_name = os.path.basename(file_path)
            # Update the label with the filename
            self.main.ui.imageLabel.setText(f"Selected file: {file_name}")


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
