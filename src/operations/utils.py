import random, string

from PIL.ImageQt import QPixmap
from PySide6.QtGui import Qt, QBrush, QPainter
from PySide6.QtWidgets import QMessageBox, QLabel, QWidget, QVBoxLayout, QFrame

from datetime import datetime

from dateutil.relativedelta import relativedelta


def is_today_valid( date_str2, date_format="%Y-%m-%d"):
    # Parse the input date strings to datetime objects
    date2 = datetime.strptime(date_str2, date_format)

    # Get today's date
    today = datetime.today()
    new_date = today + relativedelta(months=5)

    # Check if today is between the two dates
    return new_date <= date2
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


def show_label_pixmap(pixmap_path, height, width,round=False):
    if round :
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