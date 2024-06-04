from .basic_services.generic_operations import ModelOperations
from ..models.subscription import Subscription


class SubscriptionsOperation (ModelOperations):
    model_class = Subscription
    form_slide_menu = 'rightMenu'
    ui_add_form_columns = ['subscription_type','start_date',"member","duration","expired","end_date"]



