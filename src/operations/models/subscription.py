from . import User
from .abstract.abstract_models import Model
import re

from .abstract.foreign_key import ForeignKey

from .abstract.fields import Field, IndexField


SUBSCRIPTION_TYPE_CHOICES = {
    0: 'monthly_subscription',
    1: 'quarterly_subscription',
    2: 'half_yearly_subscription',
    3: 'annual_subscription',
    4: 'other'
}
PAYMENT_METHOD = {
    0: 'cash',
    1: 'check'
}

class Subscription(Model):
    table_name = "Subscriptions"

    def __init__(self):
        self.id = Field(database_name='ID', database_type="TEXT", pk=True)
        self.subscription_type = IndexField(ui_name='subType', database_name='SUBSCRIPTION_TYPE',
                                            database_type="INTEGER", choices=SUBSCRIPTION_TYPE_CHOICES)

        self.payment_method = Field(ui_name='paymentMethod', database_name='PAYMENT_METHOD', database_type="INTEGER", )
        self.duration = Field(database_name='DURATION', database_type="INTEGER")  # in months
        self.start_date = Field(ui_name="startDate", database_name="START_DATE", database_type="DATE")
        self.end_date = Field(database_name="END_DATE", database_type="DATE", ui_label="subscription_end_date")
        self.member = ForeignKey(User, "MEMBER", table_relation_id_key='id')

    @staticmethod
    def validate_item_inputs():
        return []
