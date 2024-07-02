import os

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QWidget, QHBoxLayout, QPushButton, QDialog, QDialogButtonBox, QLineEdit

from .basic_services.ui_generic_operations import ModelOperationsUi
from .subscription_operations import SubscriptionsOperation
from ..models import User
from ..models.subscription import Subscription
from ..utils import show_popup
from src.renew_subs_interface import RenewSubDialog


class UsersOperations(ModelOperationsUi):
    model_class = User
    ui_table_widget_name = 'tableWidgetUsers'
    form_slide_menu = 'rightMenu'
    ui_table_fields = ['image_file', 'is_subscription_valid', 'first_name', 'last_name', 'email', 'phone_number']
    ui_add_form_columns = ['image_file', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'cin','program']
    ui_details_fields = ['image_file','first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'cin','program','subscription_end_date']
    fields_to_update = ['first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'cin', 'image_file','program']
    add_item_ui_btn = 'addUserBtn'
    close_form_slide_menu_button = 'closeRightMenu'
    open_form_slide_menu_button = 'showUserFormBtn'
    update_button_label = "Modifier un membre"
    column_table_width = {'email':200 ,'phone_number':180}
    search_fields=['first_name','last_name']


    def __init__(self, main):
        super().__init__(main)

        self.main.ui.imageBtn.clicked.connect(lambda: self.open_file_dialog(self.model_instance.image_file))
        self.subscription = Subscription()
        self.subscription_operation = SubscriptionsOperation()
        self.search_value = ""

        self.main.ui.searchUserBtn.clicked.connect(lambda: (self.update_search_value(), self.display_items()))

    def update_search_value(self):
        self.search_value = self.main.ui.searchUser.text()
    def clear_form(self):
        super().clear_form()
        for field in self.subscription.get_fields():
            ui_field = getattr(self.main.ui, field.ui_name, None)
            if ui_field:
                ui_field.setHidden(False)
        self.main.ui.labeldate.setHidden(False)
        self.main.ui.dureeMois.setHidden(False)
        self.main.ui.paymentLabel.setHidden(False)
        self.main.ui.addUserBtn.setText("Ajouter un membre")

    def update_item_ui(self, model_instance):
        for field in self.subscription.get_fields():
            ui_field = getattr(self.main.ui, field.ui_name, None)
            if ui_field:
                ui_field.setHidden(True)
        self.main.ui.labeldate.setHidden(True)
        self.main.ui.dureeMois.setHidden(True)
        self.main.ui.paymentLabel.setHidden(True)

        super().update_item_ui(model_instance)

    def show_add_success_message(self):
        pass

    def show_update_success_message(self):
        show_popup("Le membre a été modifié avec succès", "success")

    def add_item(self):
        last_id = super().add_item()
        if last_id:
            ui = self.main.ui
            if self.subscription_operation.add_subscription(ui, last_id):
                show_popup("Le membre a été ajouté avec succès", "success")
                self.display_items()

    def define_actions(self, table_widget, row, column, instance):
        if self.ui_table_with_actions:
            # Add layout with buttons to the last column
            button_layout = QWidget()
            layout = QHBoxLayout()

            edit_button = QPushButton("")
            icon = QIcon()
            icon.addFile(u":/feather/icons/feather/edit.png", QSize(), QIcon.Normal, QIcon.Off)
            edit_button.setIcon(icon)

            show_button = QPushButton("")
            icon = QIcon()
            icon.addFile(u":/font_awesome/solid/icons/font_awesome/solid/circle-user.png", QSize(), QIcon.Normal, QIcon.Off)
            show_button.setIcon(icon)

            delete_button = QPushButton("")
            icon = QIcon()
            icon.addFile(u":/feather/icons/feather/x-octagon.png", QSize(), QIcon.Normal, QIcon.Off)
            delete_button.setIcon(icon)

            renew_button = QPushButton("")
            icon = QIcon()
            icon.addFile(u":/material_design/icons/material_design/autorenew.png", QSize(), QIcon.Normal, QIcon.Off)
            renew_button.setIcon(icon)

            layout.addWidget(edit_button)
            layout.addWidget(show_button)
            layout.addWidget(delete_button)
            layout.addWidget(renew_button)

            button_layout.setLayout(layout)
            table_widget.setCellWidget(row, column, button_layout)
            show_button.clicked.connect(
                lambda _=None, row_instance=instance: self.show_item_ui(row_instance))
            edit_button.clicked.connect(
                lambda _=None, row_instance=instance: self.update_item_ui(row_instance))
            delete_button.clicked.connect(
                lambda _=None, row_instance=instance: self.delete_item_ui(row_instance))
            renew_button.clicked.connect(
                lambda _=None, row_instance=instance: self.show_renew_subscription(row_instance))

    def show_renew_subscription(self, instance):
        dlg = QDialog(self.main)
        dlg.setWindowTitle("Abonnement")
        show_dialog = RenewSubDialog()
        show_dialog.setupUi(dlg)
        apply_button = show_dialog.buttonBox.button(QDialogButtonBox.Apply)
        apply_button.clicked.connect(lambda _=None, id_member=instance.id.value,ui=show_dialog: self.apply_subscription(id_member,ui))
        dlg.exec()

    def apply_subscription(self,id_member,ui):
        if self.subscription_operation.add_subscription(ui, id_member):
            show_popup("L'abonnement a été appliqué avec succès", "success")

        self.display_items()
