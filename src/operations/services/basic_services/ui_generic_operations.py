import os

from PySide6.QtCore import QSignalMapper, Qt
from PySide6.QtWidgets import QTableWidgetItem, QWidget, QHBoxLayout, QPushButton, QDialog, QFileDialog, QLineEdit
from .generic_operations import ModelOperations
from ...models.abstract.fields import FileField
from ...utils import show_popup
from .show_dialog_interface import Ui_Dialog
from copy import copy, deepcopy


class SlideMenuUi:
    close_form_slide_menu_button = ""
    open_form_slide_menu_button = ""
    main = None
    model_instance = None
    add_item = None
    add_item_ui_btn = ""
    form_slide_menu = ""

    def __init__(self):
        if self.close_form_slide_menu_button:
            getattr(self.main.ui, self.close_form_slide_menu_button).clicked.connect(
                lambda: self.clear_form())

        if self.open_form_slide_menu_button:
            getattr(self.main.ui, self.open_form_slide_menu_button).clicked.connect(
                lambda: self.clear_form())
            getattr(self.main.ui, self.open_form_slide_menu_button).clicked.connect(
                lambda: self.open_form())

    def clear_form(self):
        for field in self.model_instance.get_fields():
            ui_field = getattr(self.main.ui, field.ui_name, None)
            if ui_field:
                ui_field.setHidden(False)

        if self.add_item_ui_btn:
            button = getattr(self.main.ui, self.add_item_ui_btn)
            button.clicked.disconnect()
            button.clicked.connect(
                lambda: self.add_item())
            button.setText("Add Item")

        self.model_instance.set_ui_values_free(self.main.ui)

    def close_form(self):
        if self.main:
            slide_menu = getattr(self.main.ui, self.form_slide_menu)
            if not slide_menu.collapsed:
                slide_menu.slideMenu()

    def open_form(self):
        if self.main:
            slide_menu = getattr(self.main.ui, self.form_slide_menu)
            if slide_menu.collapsed:
                slide_menu.slideMenu()


class ModelOperationsUi(ModelOperations, SlideMenuUi):
    ui_table_widget_name = ""
    ui_table_with_actions = True
    ui_table_fields = None
    ui_details_fields = []
    add_item_ui_btn = ""
    update_button_label = ""


    def __init__(self, main):
        self.main = main
        super().__init__()
        self.create_table()
        self.display_items()
        if self.add_item_ui_btn:
            add_item_ui_btn = getattr(self.main.ui, self.add_item_ui_btn)
            add_item_ui_btn.clicked.connect(
                lambda: self.add_item())

    def open_file_dialog(self, field_image):
        file_path, _ = QFileDialog.getOpenFileName(self.main, "Select File")
        field_image.qfile_variable = file_path

        if file_path:
            # Define the destination directory and create it if it doesn't exist
            file_name = os.path.basename(file_path)
            # Update the label with the filename
            self.main.ui.imageLabel.setText(f"Selected file: {file_name}")

    def show_add_success_message(self):
        show_popup("L'ajout a été fait avec succès")

    def display_items(self):

        if getattr(self.main.ui, self.ui_table_widget_name, None):
            rows_models = self.get_items()
            tableWidget = getattr(self.main.ui, self.ui_table_widget_name, None)
            table_length = len(self.ui_table_fields)
            columns_labels = [getattr(self.model_instance, column).__dict__.get('ui_label', '') for column in
                              self.ui_table_fields]

            if self.ui_table_with_actions:
                table_length += 1
                columns_labels.append('Actions')

            tableWidget.setColumnCount(table_length)
            # Set the column headers
            tableWidget.setHorizontalHeaderLabels(columns_labels)

            if tableWidget:
                tableWidget.setRowCount(0)  # Clear all existing rows
                for row_model in rows_models:
                    rowPosition = tableWidget.rowCount()
                    tableWidget.setRowCount(rowPosition + 1)

                    for index_table_column, table_column in enumerate(self.ui_table_fields):
                        field = getattr(row_model, table_column)
                        item_str = str(field.value)
                        if isinstance(field, FileField):  # Check if the item is an image
                            widget = field.get_widget(item_str)
                            tableWidget.setCellWidget(rowPosition, index_table_column, widget)
                            tableWidget.setRowHeight(rowPosition, field.desired_ui_height + 10)  # Adding padding
                            tableWidget.setColumnWidth(index_table_column,
                                                       field.desired_ui_width + 10)  # Adding padding
                        else:
                            qtablewidgetitem = QTableWidgetItem(item_str)
                            tableWidget.setItem(rowPosition, index_table_column, qtablewidgetitem)

                    if self.ui_table_with_actions:
                        # Add layout with buttons to the last column
                        button_layout = QWidget()
                        layout = QHBoxLayout()
                        edit_button = QPushButton("Edit")
                        show_button = QPushButton("Show")
                        delete_button = QPushButton("Delete")

                        #                       delete_button.clicked.connect(lambda: self.on_button_click(self.main))

                        layout.addWidget(edit_button)
                        layout.addWidget(show_button)
                        layout.addWidget(delete_button)
                        button_layout.setLayout(layout)
                        tableWidget.setCellWidget(rowPosition, len(self.ui_table_fields), button_layout)
                        show_button.clicked.connect(
                            lambda _=None, row_instance=row_model: self.show_item_ui(row_instance))
                        edit_button.clicked.connect(
                            lambda _=None, row_instance=row_model: self.update_item_ui(row_instance))

    def show_item_ui(self, instance):
        dlg = QDialog(self.main)
        dlg.setWindowTitle("Affichage")
        show_dialog = Ui_Dialog()
        show_dialog.setupUi(dlg)
        fields = instance.__dict__
        for key_field, field in fields.items():
            if field.ui_name:
                if key_field in self.ui_details_fields:
                    show_dialog.addFieldToWidget(field.ui_name, self.table_name, field.value, field.ui_label)

        dlg.exec()

    def update_item_ui(self, instance):
        self.model_instance = instance
        # Part 1 : Only show the fields that are relevant to the update
        fields_to_hide = [value for key, value in self.model_instance.__dict__.items() if
                          key not in self.fields_to_update]
        for field in fields_to_hide:
            ui_field = getattr(self.main.ui, field.ui_name, None)
            if ui_field:
                ui_field.setHidden(True)

        self.model_instance.set_ui_from_values(self.main)

        # Part 2 : change the add button label to update button and set the signal
        if self.add_item_ui_btn:
            button = getattr(self.main.ui, self.add_item_ui_btn)
            button.setText(self.update_button_label if self.update_button_label else "Update Item")
            button.clicked.disconnect()
            getattr(self.main.ui, self.add_item_ui_btn).clicked.connect(
                lambda: self.update_item())
        self.open_form()
