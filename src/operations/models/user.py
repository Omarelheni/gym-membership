from PIL.ImageQt import QPixmap
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from .abstract.abstract_models import Model
from .abstract.fields import Field, FileField, ImageField

import re

from ..utils import  show_label_pixmap, is_today_valid


class User(Model):
    table_name = "Users"

    def __init__(self):
        self.id = Field(database_name='ID', pk=True)
        self.first_name = Field("firstName", "FIRST_NAME", "TEXT", ui_label="surname")
        self.last_name = Field("lastName", "LAST_NAME", "TEXT", ui_label="name")
        self.email = Field("email", "EMAIL", "TEXT", ui_label="email")
        self.phone_number = Field("phoneNb", "PHONE_NUMBER", "TEXT", ui_label="telephone_number")
        self.address = Field("address", "ADDRESS", "TEXT", ui_label="adress")
        self.birth_date = Field("birthDate", "BIRTH_DATE", "DATE", ui_label="birth_date")
        self.image_file = ImageField("imageLabel", "IMAGE", "images-users", "user_add_file_variable", ui_label="image")

    @property
    def last_subscription(self):
        from ..services import SubscriptionsOperation

        sub_operation = SubscriptionsOperation()
        results = sub_operation.get_search_items({'member': self.id.value}, order_by='start_date')

        # Check if the results list is not empty
        if results:
            result = results[-1]  # Get the last item in the list
        else:
            result = None

        return result

    @property
    def subscription_end_date(self):
        if self.last_subscription is None:
            return None

        try:
            return self.last_subscription.end_date
        except AttributeError:
            return None


    @property
    def is_subscription_valid(self):
        class FieldSubs:
            def __init__(self, is_valid):
                self.ui_label = 'subscription'
                self.is_valid = is_valid

            def get_widget(self):
                pixmap_path = ":/feather/special/valid.png" if self.is_valid else ":/feather/special/not_valid.png"
                widget = show_label_pixmap(pixmap_path, 40, 40)
                return widget

        if not self.last_subscription:
            return FieldSubs(False)

        is_valid = is_today_valid(self.last_subscription.end_date.value)
        return FieldSubs(is_valid)


    def validate_item_inputs(self):
        errors = []

        if not self.image_file.value:
            errors.append("* Veuillez ajouter une image.")

        if (
                not self.last_name.value or not self.first_name.value) or not self.last_name.value.isalpha() or not self.first_name.value.isalpha():
            errors.append("* Veuillez entrer un nom valide (pas de chiffres).")

        if not self.email.value or not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.value):
            errors.append("* Veuillez entrer une adresse e-mail valide.")

        if not self.phone_number.value or not self.phone_number.value.isdigit() or len(self.phone_number.value) != 8:
            errors.append("* Veuillez entrer un numéro de téléphone valide \n (8 chiffres, pas de caractères).")

        return errors
