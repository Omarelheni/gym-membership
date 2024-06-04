import os
import shutil

from PIL.ImageQt import QPixmap
from PySide6.QtCore import QRect
from PySide6.QtGui import QIcon, QPainter, QBrush, Qt, QPixmap
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from ...utils import generate_random_string


class Field:
    def __init__(self, ui_name=None, database_name=None, database_type="TEXT", value=None, pk=False):
        self.ui_name = ui_name
        self.database_name = database_name
        self.database_type = database_type
        self.value = value
        self.pk = pk


class FileField(Field):
    desired_ui_width = 80  # Set your desired width
    desired_ui_height = 80
    def __init__(self, ui_name: str, database_name: str, destination: str, file_variable_name: str,
                 display_dimensions=None):
        super().__init__(database_name=database_name, ui_name=ui_name)
        if display_dimensions is None:
            display_dimensions = {}
        self.destination = destination
        self.file_variable_name = file_variable_name
        self.display_dimensions = None

    def get_widget(self,item_str):
        image_path = os.path.join(self.destination, item_str)
        pixmap = QPixmap(image_path)

        pixmap = pixmap.scaled(self.desired_ui_height, self.desired_ui_width, Qt.KeepAspectRatio,
                               Qt.SmoothTransformation)

        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        # Create a QWidget and set its layout
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        return widget

    def save_file(self, uifunction):
        file = getattr(uifunction, uifunction.file_variable_name,None)
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

