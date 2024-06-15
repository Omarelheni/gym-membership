from .fields import Field


class ForeignKey(Field):
    def __init__(self,model,database_name,table_relation_id_key):
        super().__init__(database_name=database_name,database_type='INTEGER')
        self.table_relation_id_key = table_relation_id_key
        self.model = model()
