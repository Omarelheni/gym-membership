from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QLineEdit, QComboBox, QCheckBox, QRadioButton, QTextEdit, QLabel, QDateEdit, QSpinBox, \
    QDoubleSpinBox

from .fields import Field, FileField


class Model:

    def get_fields(self):
        fields = [value for key, value in self.__dict__.items() if isinstance(value, Field)]
        return fields


    @property
    def pk_field(self):
        return next((value for value in self.__dict__.values() if isinstance(value, Field) and value.pk), None)

    def get_fields_attribute_value(self, attr=""):
        return [getattr(field, attr) for field in self.get_fields()]

    def get_fields_values_sql_query(self, attr=""):
        return "('" + "','".join(self.get_fields_attribute_value(attr)) + "')"

    def set_values_from_ui(self,ui):
        for field in self.get_fields():
            if field.ui_name:
                ui_field = getattr(ui, field.ui_name, None)

                if isinstance(field, FileField):
                    file = field.save_file()
                    if file :
                        field.value = file
                    elif isinstance(ui_field, QLabel):
                        field.value = ui_field.text()

                elif ui_field:
                    if isinstance(ui_field, QLineEdit):
                        field.value = ui_field.text()
                    elif isinstance(ui_field, QComboBox):
                        field.value = ui_field.currentIndex()
                    elif isinstance(ui_field, QCheckBox):
                        field.value = ui_field.isChecked()
                    elif isinstance(ui_field, QRadioButton):
                        field.value = ui_field.isChecked()
                    elif isinstance(ui_field, QTextEdit):
                        field.value = ui_field.toPlainText()
                    elif isinstance(ui_field, QDateEdit):
                        field.value = ui_field.date().toPyDate()  # Convert date to ISO format string
                    if isinstance(ui_field, QLabel):
                        field.value = ui_field.text()


    def set_ui_from_values(self,main):
        for field in self.get_fields():
            ui_field = getattr(main.ui, field.ui_name, None)

            if isinstance(ui_field, QLineEdit):
                ui_field.setText(field.value)
            elif isinstance(ui_field, QComboBox):
                index = ui_field.findText(field.value)
                if index >= 0:
                    ui_field.setCurrentIndex(index)
            elif isinstance(ui_field, QCheckBox):
                ui_field.setChecked(bool(field.value))
            elif isinstance(ui_field, QTextEdit):
                ui_field.setPlainText(field.value)
            elif isinstance(ui_field, QRadioButton):
                ui_field.setChecked(bool(field.value))
            elif isinstance(ui_field, QDateEdit):
                date_value = QDate.fromString(field.value, "yyyy-MM-dd")
                ui_field.setDate(date_value)
            elif isinstance(ui_field, QSpinBox):
                ui_field.setValue(int(field.value))
            elif isinstance(ui_field, QDoubleSpinBox):
                ui_field.setValue(float(field.value))
            elif isinstance(ui_field, QLabel):
                ui_field.setText(field.value)
    def set_ui_values_free(self, ui):
        for field in self.get_fields():
            if field.ui_name:
                ui_field = getattr(ui, field.ui_name, None)
                if ui_field:
                    if isinstance(ui_field, QLineEdit):
                        ui_field.clear()  # Clear text
                    elif isinstance(ui_field, QComboBox):
                        ui_field.setCurrentIndex(-1)  # Reset to no selection
                    elif isinstance(ui_field, QCheckBox):
                        ui_field.setChecked(False)  # Uncheck
                    elif isinstance(ui_field, QRadioButton):
                        ui_field.setAutoExclusive(False)
                        ui_field.setChecked(False)  # Uncheck
                        ui_field.setAutoExclusive(True)
                    elif isinstance(ui_field, QTextEdit):
                        ui_field.clear()  # Clear text
                    elif isinstance(ui_field, QLabel):
                        ui_field.clear()  # Clear text
                    elif isinstance(ui_field, QDateEdit):
                        ui_field.setDate(QDate.currentDate())  # Set date to current date
