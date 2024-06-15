import os

from PySide6.QtWidgets import QFileDialog

from .basic_services.ui_generic_operations import ModelOperationsUi
from .subscription_operations import SubscriptionsOperation
from ..models import User
from ..models.subscription import Subscription
from ..utils import show_popup


class UsersOperations(ModelOperationsUi):
    model_class = User
    ui_table_widget_name = 'tableWidgetUsers'
    form_slide_menu = 'rightMenu'
    ui_table_fields = [ 'image_file', 'first_name', 'last_name', 'email', 'phone_number']
    ui_add_form_columns = ['image_file', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'address']
    ui_details_fields = ['first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'address']
    fields_to_update = ['first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'address','image_file']
    add_item_ui_btn = 'addUserBtn'
    close_form_slide_menu_button = 'closeRightMenu'
    open_form_slide_menu_button = 'showUserFormBtn'
    update_button_label = "Modifier un membre"


    def __init__(self, main):
        super().__init__(main)
        self.main.ui.imageBtn.clicked.connect(lambda: self.open_file_dialog(self.model_instance.image_file))
        self.subscription = Subscription()


    def clear_form(self):
        super().clear_form()
        for field in self.subscription.get_fields():
            ui_field = getattr(self.main.ui, field.ui_name,None)
            if ui_field:
                ui_field.setHidden(False)
        self.main.ui.labeldate.setHidden(False)
        self.main.ui.addUserBtn.setText("Ajouter un membre")

    def update_item_ui(self, model_instance):
        for field in self.subscription.get_fields():
            ui_field = getattr(self.main.ui, field.ui_name,None)
            if ui_field:
                ui_field.setHidden(True)
        self.main.ui.labeldate.setHidden(True)
        super().update_item_ui(model_instance)

    def show_add_success_message(self):
        pass

    def show_update_success_message(self):
        show_popup("Le membre a été modifié avec succès", "success")

    def add_item(self):
        last_id = super().add_item()
        if last_id:
            ui = self.main.ui
            duration_map = {
                "Abonnement mensuel": 1,
                "Abonnement trimestriel": 3,
                "Abonnement semestriel": 6,
                "Abonnement annuel": 12,
                "Autre": ui.subDuration.value() if ui.subType.currentText() == "Autre" else None
            }
            duration = duration_map.get(ui.subType.currentText(),None)
            if not duration:
                show_popup("Echec dans la durée du l'abonnement")
                return

            subscriptions_operation = SubscriptionsOperation(main=self.main)
            subscriptions_operation.model_instance.duration.value = duration
            subscriptions_operation.model_instance.member.value = last_id
            subscriptions_operation.model_instance.expired.value = False
            try:
                subscriptions_operation.model_instance.end_date.value = ui.startDate.date().addMonths(duration).toPyDate()
            except:
                show_popup("Echec dans la date de l'abonnment ")

            if subscriptions_operation.add_item():
                show_popup("Le membre a été ajouté avec succès", "success")



