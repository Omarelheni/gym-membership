from .abstract.abstract_models import Model
from .abstract.fields import Field, FileField

import re


class User(Model):

    table_name = "Users"

    def __init__(self):
        self.id = Field(database_name='ID', pk=True)
        self.first_name = Field("firstName", "FIRST_NAME")
        self.last_name = Field("lastName", "LAST_NAME")
        self.email = Field("email", "EMAIL")
        self.phone_number = Field("phoneNb", "PHONE_NUMBER")
        self.address = Field("address", "ADDRESS")
        self.birth_date = Field("birthDate", "BIRTH_DATE", "DATE")
        self.image_file = FileField("imageLabel", "IMAGE", "images-users", "user_add_file_variable")

    def validate_item_inputs(self):
        errors = []
        if self.image_file.value is None:
            errors.append("* Veuillez ajouter une image.")

        if not self.last_name.value.isalpha() or not self.first_name.value.isalpha():
            errors.append("* Veuillez entrer un nom valide (pas de chiffres).")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.value):
            errors.append("* Veuillez entrer une adresse e-mail valide.")

        if not self.phone_number.value.isdigit() or len(self.phone_number.value) != 8:
            errors.append("* Veuillez entrer un numéro de téléphone valide \n (8 chiffres, pas de caractères).")

        return errors
