import os
import sqlite3
from abc import abstractmethod
from sqlite3 import Error

from PySide6.QtWidgets import QMessageBox

from ...models.abstract.fields import Field
from ...models.abstract.foreign_key import ForeignKey
from ...utils import show_popup


class SQLLiteFunctions:
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

        print('Please set the db file!')
        return False

    def create_table_sql(self, model_class):
        fields = model_class.get_fields()
        columns = [f"{field.database_name} {field.database_type}" for field in fields if
                   field.database_name != 'ID' or isinstance(field, ForeignKey)]
        foreign_keys = [field for field in fields if isinstance(field, ForeignKey)]

        # Create foreign key constraints
        foreign_key_constraints = []
        for fk in foreign_keys:
            foreign_key_constraints.append(
                f"FOREIGN KEY ({fk.database_name}) REFERENCES {fk.model.table_name}({fk.table_relation_id_key})")

        columns_string = ", ".join(columns + foreign_key_constraints)
        create_table_query = f"CREATE TABLE {model_class.table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {columns_string});"
        print('create_table_query ==>', create_table_query)

        if self.execute_function(create_table_query):
            print('Table created successfully!')
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
            initial_fields = [field for key, field in model_class.__dict__.items() if key in field_to_add]
            database_names = [getattr(field, 'database_name') for field in initial_fields]
            values = [getattr(field, 'value') for field in initial_fields]

        # Ensure we have the same number of database names and values
        if len(database_names) != len(values):
            raise ValueError("Mismatch between database field names and values")

        # Construct the query parts
        placeholders = ','.join(['?'] * len(values))
        database_names_part_query = f"({','.join(database_names)})"
        insert_item = f"""
        INSERT INTO {model_class.table_name} {database_names_part_query} VALUES ({placeholders});
        """

        return self.execute_function(insert_item, commit=True, values=values, fetch_last_inserted=True)

    def update_item_sql(self, model_class, item_id, fields_to_update=None):
        # Get field names and values
        database_names = model_class.get_fields_attribute_value('database_name')
        values = model_class.get_fields_attribute_value('value')

        if fields_to_update is not None:
            # Filter fields based on fields_to_update
            update_fields = [field for key, field in model_class.__dict__.items() if key in fields_to_update]
            database_names = [getattr(field, 'database_name') for field in update_fields]
            values = [getattr(field, 'value') for field in update_fields]

        # Ensure we have the same number of database names and values
        if len(database_names) != len(values):
            raise ValueError("Mismatch between database field names and values")

        # Construct the query parts
        set_clause = ', '.join([f"{name} = ?" for name in database_names])
        update_query = f"""
        UPDATE {model_class.table_name} SET {set_clause} WHERE ID = ?;
        """

        values.append(item_id)  # Add the item ID to the values list

        return self.execute_function(update_query, commit=True, values=values)


class ModelOperations(SQLLiteFunctions):
    create_table_query = ""
    table_name = ""
    model_class = None
    ui_table_widget_name = ""
    ui_table_columns = None
    ui_table_with_actions = True
    ui_add_form_columns = None
    fields_to_update = None
    main = None

    def __init__(self):
        super().__init__()
        self.model_instance = self.model_class()  # Create an instance of the model class when needed

    def create_table(self):
        self.create_table_sql(self.model_instance)

    def get_items(self):
        columns = [key for key, value in self.model_instance.__dict__.items() if isinstance(value, Field)]
        raw_items = self.get_items_sql(columns, self.model_instance)
        # Map the list of values to a list of instance type Field
        items = []
        for raw_item in raw_items:
            model_class_new = self.model_class()
            for index, raw_value in enumerate(raw_item):
                field = getattr(model_class_new, columns[index])
                field.value = raw_value

            items.append(model_class_new)

        return items

    def add_item(self):
        self.model_instance.set_values_from_ui(main=self.main)
        # Perform validation checks
        errors = self.model_instance.validate_item_inputs()

        if errors:
            self.main.ui.controlErrorsUser.setText("\n".join(errors))
            show_popup("\n".join(errors), "error")
            return
        else:
            self.main.ui.controlErrorsUser.setText("")

        try:
            result = self.add_item_sql(self.model_instance, self.fields_to_update)
            if result:
                self.model_instance.set_ui_values_free(self.main.ui)
                self.display_items()
                self.show_add_success_message()
                return result
        except:
            show_popup("Failed to add item")

    def update_item(self):
        self.model_instance.set_values_from_ui(main=self.main)
        # Perform validation checks
        errors = self.model_instance.validate_item_inputs()

        if errors:
            self.main.ui.controlErrorsUser.setText("\n".join(errors))
            show_popup("\n".join(errors), "error")
            return
        else:
            self.main.ui.controlErrorsUser.setText("")

        try:
            result = self.update_item_sql(self.model_instance, self.model_instance.id.value, self.ui_add_form_columns)
            if result:
                self.display_items()
                self.show_update_success_message()
                return result
        except:
            show_popup("Failed to update item")

    def display_items(self):
        # Your implementation to display items in the UI
        pass

    def show_add_success_message(self):
        show_popup("Item added successfully", "success")

    def show_update_success_message(self):
        show_popup("Item updated successfully", "success")
