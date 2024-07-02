import os
import shutil

from PIL.ImageQt import QPixmap
from PySide6.QtCore import QRect
from PySide6.QtGui import QIcon, QPainter, QBrush, Qt, QPixmap
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from ...utils import generate_random_string, show_label_pixmap


class Field:
    def __init__(self, ui_name='', database_name=None, database_type="TEXT", value=None, pk=False, ui_label=''):
        self.ui_name = ui_name
        self.database_name = database_name
        self.database_type = database_type
        self.value = value
        self.pk = pk
        self.ui_label = ui_label

    def get_widget(self):
        pass


class FileField(Field):

    def __init__(self, ui_name: str, database_name: str, destination: str, file_variable_name: str, ui_label: str):
        super().__init__(database_name=database_name, ui_name=ui_name, ui_label=ui_label)
        self.qfile_variable = None
        self.destination = destination
        self.file_variable_name = file_variable_name

    def save_file(self):
        if self.qfile_variable:
            file = self.qfile_variable
            if file is None:
                return None
            file_name = os.path.basename(file)
            if not os.path.exists(self.destination):
                os.makedirs(self.destination)

            destination_path = os.path.join(self.destination, file_name)

            # Check if the file already exists
            while os.path.exists(destination_path):
                # Split the file name into name and extension
                name, ext = os.path.splitext(file_name)
                # Generate a new file name with a random string appended
                file_name = f"{name}_{generate_random_string()}{ext}"
                destination_path = os.path.join(self.destination, file_name)

            shutil.copy(file, destination_path)
            return file_name


class ImageField(FileField):

    def __init__(self, ui_name: str, database_name: str, destination: str, file_variable_name: str, ui_label: str):
        super().__init__(ui_name, database_name, destination, file_variable_name, ui_label)
        self.desired_ui_width = 80
        self.desired_ui_height = 80

    def get_widget(self,round=False):
        # creating an image for the table
        image_path = os.path.join(self.destination, self.value)

        return show_label_pixmap(image_path, self.desired_ui_height, self.desired_ui_width,round)

class IndexField(Field):
    def __init__(self, ui_name='', database_name=None, database_type="TEXT", value=None, pk=False, ui_label='',
                 choices=None):
        super().__init__(ui_name, database_name, database_type, value, pk, ui_label)
        if choices is None:
            choices = {}
        self.choices = choices
