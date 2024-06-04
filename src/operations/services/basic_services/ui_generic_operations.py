import os
import sqlite3
import sys
from abc import abstractmethod
from sqlite3 import Error
import re

from PySide6.QtWidgets import QTableWidgetItem, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, \
    QDateEdit

from .generic_operations import ModelOperations
from ...models.abstract.fields import FileField
from ...utils import show_popup


class ModelOperationsUi(ModelOperations):
    ui_table_widget_name = ""
    ui_table_columns = None
    ui_table_with_actions = True
    form_slide_menu = ""
    exclude_fields_show = []

    def show_add_succes_message(self):
        show_popup("L'ajout a été fait avec succès")

    def slide_menu(self, main=None):
        if main:
            slide_menu = getattr(main.ui, self.form_slide_menu)
            slide_menu.slideMenu()

    def display_items(self, main):
        rows_models = self.get_items(self.ui_table_columns)
        tableWidget = getattr(main.ui, self.ui_table_widget_name, None)

        #hide ID column
        #tableWidget.hideColumn(0)

        if tableWidget:
            tableWidget.setRowCount(0)  # Clear all existing rows
            for row_model in rows_models:
                rowPosition = tableWidget.rowCount()
                tableWidget.setRowCount(rowPosition + 1)

                for index_table_column, table_column in enumerate(self.ui_table_columns):
                    field = getattr(row_model, table_column)
                    item_str = str(field.value)
                    if isinstance(field, FileField):  # Check if the item is an image
                        widget = field.get_widget(item_str)
                        tableWidget.setCellWidget(rowPosition, index_table_column, widget)
                        tableWidget.setRowHeight(rowPosition, field.desired_ui_height + 10)  # Adding padding
                        tableWidget.setColumnWidth(index_table_column, field.desired_ui_width + 10)  # Adding padding
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
                    edit_button.clicked.connect(lambda: self.on_button_click(main))
                    show_button.clicked.connect(lambda: self.show_item_ui(main))
                    delete_button.clicked.connect(lambda: self.on_button_click(main))

                    layout.addWidget(edit_button)
                    layout.addWidget(show_button)
                    layout.addWidget(delete_button)
                    button_layout.setLayout(layout)
                    tableWidget.setCellWidget(rowPosition, len(self.ui_table_columns), button_layout)

    def show_item_ui(self, main):
        fields = self.model_instance.__dict__
        for key_field, field in fields.items():
            if field.ui_name:
                ui_field = getattr(main.ui, field.ui_name)
                if key_field in self.exclude_fields_show:
                    if callable(getattr(self, "setHidden", None)):
                        ui_field.setHidden(True)
                        continue
                # General check for read-only capability
                if hasattr(ui_field, 'setReadOnly'):
                    ui_field.setReadOnly(True)
                elif hasattr(ui_field, 'setEnabled'):
                    ui_field.setEnabled(False)

        self.slide_menu(main)


