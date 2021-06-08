from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    #########  Historiek/Dispenser  #########
    @staticmethod
    def read_all_history():
        sql = "SELECT measuring_id, component_id, datetime, status, value, action_id FROM FishFooddispenser;"
        return Database.get_rows(sql)

    @staticmethod
    def read_hystory_by_id(measuring_id):
        sql = "SELECT measuring_id, component_id, datetime, status, value, action_id FROM FishFooddispenser WHERE measuring_id = %s;"
        params = [measuring_id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_history(component_id, datetime, status, value, action_id):
        sql = "INSERT INTO FishFooddispenserDB.Dispenser(component_id, datetime, status, value, action_id) VALUES(%s,%s,%s,%s,%s);"
        params = [component_id, datetime, status, value, action_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_history(component_id, datetime, status, value, action_id):
        sql = "UPDATE FishFooddispenser.Dispenser SET component_id = %s, datetime = %s, status = %s, value = %s, action_id = %s;"
        params = [component_id, datetime, status, value, action_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_history(measuring_id):
        sql = "DELETE FROM FishFooddispenser.Dispenser WHERE measuring_id = %s;"
        params = [measuring_id]
        return Database.execute_sql(sql, params)

    #########  Component  #########
    @staticmethod
    def create_component(component_name, measuring_unit):
        sql = "INSERT INTO FishFooddispenserDB.Component(component_name, measuring_unit) VALUES(%s,%s);"
        params = [component_name, measuring_unit]
        return Database.execute_sql(sql, params)

    #########  Action  #########
    @staticmethod
    def create_action(action):
        sql = "INSERT INTO FishFooddispenserDB.Action(action) VALUES(%s);"
        params = [action]
        return Database.execute_sql(sql, params)