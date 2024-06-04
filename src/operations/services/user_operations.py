from .basic_services.ui_generic_operations import ModelOperationsUi
from .subscription_operations import SubscriptionsOperation
from ..models import User
from ..utils import show_popup


class UsersOperations(ModelOperationsUi):
    model_class = User
    ui_table_widget_name = 'tableWidgetUsers'
    form_slide_menu = 'rightMenu'
    ui_table_columns = ['id', 'image_file', 'first_name', 'last_name', 'email', 'phone_number']
    ui_add_form_columns = ['image_file', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'address']
    def show_add_succes_message(self):
        pass
    def add_item(self, uifunction):
        last_id = super().add_item(uifunction)
        if last_id:
            ui = uifunction.main.ui
            duration_map = {
                "Abonnement mensuel": 1,
                "Abonnement trimestriel": 3,
                "Abonnement semestriel": 6,
                "Abonnement annuel": 12,
                "Autre": ui.subDuration.value if ui.subType.currentText() == "Autre" else None
            }
            duration = duration_map.get(ui.subType.currentText())

            subscriptions_operation = SubscriptionsOperation()
            subscriptions_operation.model_instance.duration.value = duration
            subscriptions_operation.model_instance.member.value = last_id
            subscriptions_operation.model_instance.expired.value = False
            subscriptions_operation.model_instance.end_date.value = ui.startDate.date().addMonths(duration).toPyDate()

            subscriptions_operation.add_item(uifunction=uifunction)
            show_popup("L'ajout a été fait avec succès")
