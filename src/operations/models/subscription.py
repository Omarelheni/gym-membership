from . import User
from .abstract.abstract_models import Model
import re

from .abstract.foreign_key import ForeignKey


from .abstract.fields import Field



class Subscription(Model):

    table_name = "Subscriptions"

    def __init__(self):
        self.id = Field(database_name='ID', database_type="TEXT",pk=True)
        self.subscription_type = Field(ui_name='subType',database_name='SUBSCRIPTION_TYPE', database_type="TEXT",)
        self.duration = Field(database_name='DURATION',database_type="INTEGER") # in months
        self.start_date = Field(ui_name="startDate",database_name= "START_DATE",database_type= "DATE")
        self.end_date = Field( database_name="END_DATE", database_type="DATE",ui_label="subscription_end_date")
        self.member = ForeignKey(User,"MEMBER",table_relation_id_key = 'id')
    @staticmethod
    def validate_item_inputs():
        return []
