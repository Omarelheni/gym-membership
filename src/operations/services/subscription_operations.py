from .basic_services.generic_operations import ModelOperations
from .basic_services.ui_generic_operations import ModelOperationsUi
from ..models.subscription import Subscription


class SubscriptionsOperation (ModelOperationsUi):
    model_class = Subscription
    form_slide_menu = 'rightMenu'
    ui_add_form_columns = ['subscription_type','start_date',"member","duration","expired","end_date"]

    def show_add_success_message(self):
        pass



