import os

from PySide6.QtCore import QSignalMapper, Qt
from PySide6.QtWidgets import QTableWidgetItem, QWidget, QHBoxLayout, QPushButton, QDialog, QFileDialog, QLineEdit, \
    QMessageBox, QLabel
from .generic_operations import ModelOperations
from ...models.abstract.fields import FileField, ImageField, Field
from ...utils import show_popup, LanguageManager
from src.show_dialog_interface import Ui_Dialog
from copy import copy, deepcopy


class SlideMenuUi:
    close_form_slide_menu_button = ""
    open_form_slide_menu_button = ""
    main = None
    model_instance = None
    add_item = None
    add_item_ui_btn = ""
    form_slide_menu = ""
    search_value = ""

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
                lambda: self.add_item_ui())
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
    ui_table_fields = []
    ui_details_fields = []
    add_item_ui_btn = ""
    update_button_label = ""
    column_table_width = {}
    errors_label = ""

    def __init__(self, main=None):
        self.main = main
        super().__init__()
        self.create_table()
        self.items = self.get_items()
        self.display_items()
        if self.add_item_ui_btn and hasattr(self.main.ui, self.add_item_ui_btn):
            add_item_ui_btn = getattr(self.main.ui, self.add_item_ui_btn)
            add_item_ui_btn.clicked.connect(self.add_item_ui)

    def add_item_ui(self):
        pass

    def open_file_dialog(self, field_image):
        file_path, _ = QFileDialog.getOpenFileName(self.main, "Select File")
        field_image.qfile_variable = file_path

        if file_path:
            # Define the destination directory and create it if it doesn't exist
            file_name = os.path.basename(file_path)
            # Update the label with the filename
            self.main.ui.imageLabel.setText(f"Selected file: {file_name}")

    def display_items(self):
        self.items = self.get_items()
        # Get the translation function from the localization manager
        translate = LanguageManager().get_translation

        # Get the table widget from the UI using its name
        table_widget = getattr(self.main.ui, self.ui_table_widget_name, None)

        # If the table widget does not exist, exit the function
        if not table_widget:
            return

        # Determine the number of columns in the table
        table_length = len(self.ui_table_fields)

        # Create a list of column labels using translations and model attributes
        columns_labels = [
            translate(getattr(self.model_instance, column).__dict__.get('ui_label', ''))
            for column in self.ui_table_fields
            if getattr(self.model_instance, column) is not None
        ]
        # Add an "Actions" column if required
        if self.ui_table_with_actions:
            table_length += 1
            columns_labels.append('Actions')

        # Set the number of columns and header labels for the table widget
        table_widget.setColumnCount(table_length)
        table_widget.setHorizontalHeaderLabels(columns_labels)

        # Set the width for each column based on predefined settings
        for field, width in self.column_table_width.items():
            ui_label = getattr(self.model_instance, field).ui_label
            column_index = columns_labels.index(translate(ui_label))
            table_widget.setColumnWidth(column_index, width)

        # Add a specific width for the "Actions" column if it exists
        actions_column_width = 180  # Set the width for the Actions column
        if self.ui_table_with_actions:
            actions_column_index = columns_labels.index('Actions')
            table_widget.setColumnWidth(actions_column_index, actions_column_width)

        # Clear all existing rows in the table
        table_widget.setRowCount(0)

        # Populate the table with items
        for row_model in self.items:
            # Add a new row to the table
            row_position = table_widget.rowCount()
            table_widget.setRowCount(row_position + 1)

            # Iterate over each column and add the corresponding widget
            for index_table_column, table_column in enumerate(self.ui_table_fields):
                field = getattr(row_model, table_column)
                widget = field.get_widget()

                # Check if the item is an image and adjust the row/column sizes accordingly
                if isinstance(field, ImageField):
                    table_widget.setRowHeight(row_position, field.desired_ui_height + 10)  # Adding padding
                    table_widget.setColumnWidth(index_table_column, field.desired_ui_width + 10)  # Adding padding

                # If no widget is provided, create a QLabel to display the value
                if not widget:
                    widget = QLabel(str(field.output))
                    widget.setAlignment(Qt.AlignCenter)  # Center align text

                # Set the widget in the table cell
                table_widget.setCellWidget(row_position, index_table_column, widget)

            # Define actions for the current row
            self.define_actions(table_widget, row_position, len(self.ui_table_fields), row_model)

    def define_actions(self, table_widget, row, column, instance):
        if self.ui_table_with_actions:
            # Add layout with buttons to the last column
            button_layout = QWidget()
            layout = QHBoxLayout()
            edit_button = QPushButton("Edit")
            show_button = QPushButton("Show")
            delete_button = QPushButton("Delete")

            layout.addWidget(edit_button)
            layout.addWidget(show_button)
            layout.addWidget(delete_button)
            button_layout.setLayout(layout)
            table_widget.setCellWidget(row, column, button_layout)
            show_button.clicked.connect(
                lambda _=None, row_instance=instance: self.show_item_ui(row_instance))
            edit_button.clicked.connect(
                lambda _=None, row_instance=instance: self.update_item_ui(row_instance))
            delete_button.clicked.connect(
                lambda _=None, row_instance=instance: self.delete_item_ui(row_instance))

    def show_item_ui(self, instance):
        translate = LanguageManager().get_translation

        dlg = QDialog(self.main)
        dlg.setWindowTitle("Affichage")
        show_dialog = Ui_Dialog()
        show_dialog.setupUi(dlg)
        for key_field in self.ui_details_fields:
            field = getattr(instance, key_field)
            if isinstance(field, ImageField):
                field.desired_ui_width = 150
                field.desired_ui_height = 150
                show_dialog.addFieldToWidget(widget=field.get_widget(round=True), type="Image")
                continue

            if hasattr(field, 'ui_label'):
                show_dialog.addFieldToWidget(field.ui_name, self.table_name, field.output, translate(field.ui_label))
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

    def delete_item_ui(self, instance):
        reply = QMessageBox.question(self.main, 'Confirm Deletion',
                                     "Are you sure you want to delete this item?",
                                     QMessageBox.Yes | QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.delete_item(instance)

    def translate_table_columns(self):
        # Get the translation function from the localization manager
        translate = LanguageManager().get_translation

        # Get the table widget from the UI using its name
        table_widget = getattr(self.main.ui, self.ui_table_widget_name, None)

        # If the table widget does not exist, exit the function
        if not table_widget:
            return

        # Determine the number of columns in the table
        table_length = len(self.ui_table_fields)

        # Create a list of column labels using translations and model attributes
        columns_labels = [
            translate(getattr(self.model_instance, column).__dict__.get('ui_label', ''))
            for column in self.ui_table_fields
            if getattr(self.model_instance, column) is not None
        ]

        # Add an "Actions" column if required
        if self.ui_table_with_actions:
            table_length += 1
            columns_labels.append(translate('Actions'))

        # Set the number of columns and header labels for the table widget
        table_widget.setColumnCount(table_length)
        table_widget.setHorizontalHeaderLabels(columns_labels)

    def show_add_success_message(self):
        show_popup("L'ajout a été fait avec succès")

    def show_delete_success_message(self):
        show_popup("La suppréssion a été fait avec succès")
