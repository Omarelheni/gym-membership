from .basic_services.generic_operations import ModelOperations
from .basic_services.ui_generic_operations import ModelOperationsUi
from ..models.subscription import Subscription
from ..utils import show_popup


class SubscriptionsOperation (ModelOperationsUi):
    model_class = Subscription
    form_slide_menu = 'rightMenu'
    ui_add_form_columns = ['subscription_type','start_date',"member","duration","expired","end_date"]

    def show_add_success_message(self):
        pass

    def display_items(self):
        pass

    def add_subscription(self,ui,member_id):

        duration_map = {
            "Abonnement mensuel": 1,
            "Abonnement trimestriel": 3,
            "Abonnement semestriel": 6,
            "Abonnement annuel": 12,
            "Autre": ui.subDuration.value() if ui.subType.currentText() == "Autre" else None
        }
        duration = duration_map.get(ui.subType.currentText(), None)
        if not duration:
            show_popup("Echec dans la durée du l'abonnement")
            return

        self.model_instance.duration.value = duration
        self.model_instance.member.value = member_id
        try:
            self.model_instance.end_date.value = ui.startDate.date().addMonths(duration).toPyDate()
        except:
            show_popup("Echec dans la date de l'abonnment ")

        if self.add_item(ui=ui):
            return True
        return False


