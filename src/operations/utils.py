import json
import random, string
from pathlib import Path
import os
from PIL.ImageQt import QPixmap
from PySide6.QtGui import Qt, QBrush, QPainter
from PySide6.QtWidgets import QMessageBox, QLabel, QWidget, QVBoxLayout, QFrame

from datetime import datetime


def load_localization_data():
    file_path = os.path.join(os.getcwd(),'i18n','localization.json')
    with open(file_path, 'r',encoding='utf-8') as file:
        return json.load(file)


class LanguageManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LanguageManager, cls).__new__(cls)
            cls._instance.current_language = 'FR'
            cls._instance.translation_data = load_localization_data()
        return cls._instance

    def set_language(self, language):
        self.current_language = language

    def get_translation(self, message_key):
        return self.translation_data.get(self.current_language, {}).get(message_key, "")


def is_today_valid(date_str2, date_format="%Y-%m-%d"):
    # Parse the input date strings to datetime objects
    date2 = datetime.strptime(date_str2, date_format)

    # Get today's date
    today = datetime.today()

    # Check if today is between the two dates
    return today <= date2


def generate_random_string(length=6):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def show_popup(message, popup_type="info"):
    msg = QMessageBox()

    if popup_type == "info":
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
    elif popup_type == "error":
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")

    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class RoundLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.NoFrame)  # Set frame style to NoFrame

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother edges
        pixmap = self.pixmap()
        if pixmap.isNull():
            return
        radius = min(self.width(), self.height()) / 2  # Calculate the radius for a circle
        painter.setBrush(QBrush(pixmap))
        painter.setPen(Qt.NoPen)  # Set pen to NoPen to remove the border
        painter.drawEllipse(0, 0, radius * 2, radius * 2)


def show_label_pixmap(pixmap_path, height, width, round=False):
    if round:
        label = RoundLabel()  # Use the RoundLabel subclass
    else:
        label = QLabel()
    pixmap = QPixmap(pixmap_path)
    pixmap = pixmap.scaled(height, width, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label.setPixmap(pixmap)

    widget = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.setAlignment(Qt.AlignCenter)
    layout.setContentsMargins(0, 0, 0, 0)
    widget.setLayout(layout)

    return widget
