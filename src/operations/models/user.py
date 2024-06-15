from .abstract.abstract_models import Model
from .abstract.fields import Field, FileField

import re


class User(Model):

    table_name = "Users"

    def __init__(self):
        self.id = Field(database_name='ID', pk=True)
        self.first_name = Field("firstName", "FIRST_NAME",ui_label="Prenom")
        self.last_name = Field("lastName", "LAST_NAME",ui_label="Nom")
        self.email = Field("email", "EMAIL",ui_label="E-mail")
        self.phone_number = Field("phoneNb", "PHONE_NUMBER",ui_label="Numero Telephone")
        self.address = Field("address", "ADDRESS",ui_label="Adresse")
        self.birth_date = Field("birthDate", "BIRTH_DATE", "DATE",ui_label="Date de naissance")
        self.image_file = FileField("imageLabel", "IMAGE", "images-users", "user_add_file_variable",ui_label="Image")

    def validate_item_inputs(self):
        errors = []

        if not self.image_file.value:
            errors.append("* Veuillez ajouter une image.")

        if (not self.last_name.value or not self.first_name.value) or not self.last_name.value.isalpha() or not self.first_name.value.isalpha():
            errors.append("* Veuillez entrer un nom valide (pas de chiffres).")

        if not self.email.value or not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.value):
            errors.append("* Veuillez entrer une adresse e-mail valide.")

        if not self.phone_number.value or not self.phone_number.value.isdigit() or len(self.phone_number.value) != 8:
            errors.append("* Veuillez entrer un numéro de téléphone valide \n (8 chiffres, pas de caractères).")

        return errors
