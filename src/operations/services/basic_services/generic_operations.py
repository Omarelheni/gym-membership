import os
import sqlite3
from abc import abstractmethod
from sqlite3 import Error

from PySide6.QtWidgets import QMessageBox

from ...models.abstract.foreign_key import ForeignKey


class SQLLiteFunctions():
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/gym_membership_db.db'))

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        return conn

    def execute_function(self, sql_query, return_response=False, commit=False, values=None, fetch_last_inserted=False):

        if self.db_file:
            conn = self.create_connection()
            try:
                c = conn.cursor()
                if values:
                    resp = c.execute(sql_query, values)
                else:
                    resp = c.execute(sql_query)
                if commit:
                    conn.commit()
                if fetch_last_inserted:
                    return c.lastrowid  # Fetch the last inserted row ID
                if return_response:
                    return resp.fetchall()  # Fetch all results if return_response is True
            except Error as e:
                print(e)
            finally:
                conn.close()  # Ensure the connection is closed
            return True

        print('Please set the db File !')
        return False

    def create_table_sql(self, model_class):
        fields = model_class.get_fields()
        columns = [f"{field.database_name} {field.database_type}" for field in fields if field.database_name != 'ID' or isinstance(field, ForeignKey)]
        foreign_keys = [field for field in fields if isinstance(field, ForeignKey)]

        # Create foreign key constraints
        foreign_key_constraints = []
        for fk in foreign_keys:
            foreign_key_constraints.append(
                f"FOREIGN KEY ({fk.database_name}) REFERENCES {fk.model.table_name}({fk.table_relation_id_key})")

        columns_string = ", ".join(columns + foreign_key_constraints)
        create_table_query = f"CREATE TABLE {model_class.table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {columns_string});"
        print('create_table_query ==>',create_table_query)

        if self.execute_function(create_table_query):
            print('Tables created successfully !')
        else:
            print('Error in creating table!')

    def get_items_sql(self, columns, model_class):
        fields_and_keys = model_class.__dict__

        if columns:
            columns_sql = [fields_and_keys[key].database_name for key in columns if
                           key in fields_and_keys]
        else:
            columns_sql = [field.database_name for field in model_class.get_fields()]

        columns_sql_string = ','.join(columns_sql) if columns else '*'
        get_all_items = f"SELECT {columns_sql_string} FROM {model_class.table_name};"
        raw_items = self.execute_function(get_all_items, True)
        return raw_items

    def add_item_sql(self, model_class, field_to_add=None):
        # Get all field names and values
        database_names = model_class.get_fields_attribute_value('database_name')
        values = model_class.get_fields_attribute_value('value')

        if field_to_add is not None:
            # Filter the initial fields based on field_to_add
            inital_fields = [field for key, field in model_class.__dict__.items() if key in field_to_add]
            database_names = [getattr(field, 'database_name') for field in inital_fields]
            values = [getattr(field, 'value') for field in inital_fields]

        # Ensure we have the same number of database names and values
        if len(database_names) != len(values):
            raise ValueError("Mismatch between database field names and values")

        # Construct the query parts
        placeholders = ','.join(['?'] * len(values))
        database_names_part_query = f"({','.join(database_names)})"
        insert_user = f"""
        INSERT INTO {model_class.table_name} {database_names_part_query} VALUES ({placeholders});
        """

        return self.execute_function(insert_user, commit=True, values=values,fetch_last_inserted=True)


class ModelOperations(SQLLiteFunctions):
    create_table_query = ""
    table_name = ""
    model_class = None
    ui_table_widget_name = ""
    ui_table_columns = None
    ui_table_with_actions = True
    ui_add_form_columns = None

    def __init__(self):
        super().__init__()
        self.model_instance = self.model_class()  # Create an instance of User when needed


    def create_table(self):
        self.create_table_sql(self.model_instance)

    def get_items(self, columns=None):

        raw_items = self.get_items_sql(columns, self.model_instance)
        # Map the list of values to a list of instance type Field
        items = []
        for raw_item in raw_items:
            model_class_new = self.model_class()
            for index, raw_value in enumerate(raw_item):
                field = getattr(model_class_new, self.ui_table_columns[index])
                field.value = raw_value

            items.append(model_class_new)

        return items

    def add_item(self, uifunction):
        # Perform validation checks
        errors = self.model_instance.validate_item_inputs()

        if errors:
            uifunction.main.ui.controlErrorsUser.setText("\n".join(errors))
            show_popup("\n".join(errors),"error")
            return
        else:
            uifunction.main.ui.controlErrorsUser.setText("")



        result = self.add_item_sql(self.model_instance, self.ui_add_form_columns)
        if result :
            self.model_instance.set_ui_values_free(uifunction.main.ui)
            self.display_items(uifunction.main)
            self.show_succes_message()
            return result




    def display_items(self, main):
        pass

    def show_succes_message(self):
        pass
