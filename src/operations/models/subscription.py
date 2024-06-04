from . import User
from .abstract.abstract_models import Model
import re

from .abstract.foreign_key import ForeignKey


from .abstract.fields import Field



class Subscription(Model):

    table_name = "Subscriptions"

    def __init__(self):
        self.id = Field(database_name='ID', pk=True)
        self.subscription_type = Field(ui_name='subType',database_name='SUBSCRIPTION_TYPE')
        self.duration = Field(database_name='DURATION',database_type="INTEGER") # in months
        self.start_date = Field(ui_name="startDate",database_name= "START_DATE",database_type= "DATE")
        self.end_date = Field( database_name="END_DATE", database_type="DATE")
        self.expired = Field( database_name="EXPIRED", database_type="BOOLEAN")

        self.member = ForeignKey(User,"MEMBER",table_relation_id_key = 'id')

    def validate_item_inputs(self):
        errors = []
        return errors
