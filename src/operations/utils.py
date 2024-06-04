import random, string

from PySide6.QtWidgets import QMessageBox


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
