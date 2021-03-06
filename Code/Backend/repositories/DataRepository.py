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
    # @staticmethod
    # def read_all_history():
    #     sql = "SELECT measuring_id, component_id, datetime, status, value, action_id FROM FishFooddispenserDB.Dispenser ORDER BY datetime desc;"
    #     return Database.get_rows(sql)

    

    @staticmethod
    def read_dates():
        sql = "SELECT distinct datetime FROM FishFooddispenserDB.Dispenser ORDER BY datetime desc;"
        return Database.get_rows(sql)


    @staticmethod
    def read_all_values_by_id(component_id):
        sql = "SELECT datetime, value FROM FishFooddispenserDB.Dispenser WHERE component_id = %s ORDER BY datetime desc;"
        params = [component_id]
        return Database.get_rows(sql, params)

    @staticmethod
    def read_latest_values():
        sql = "select value, component_id from FishFooddispenserDB.Dispenser order by datetime desc, component_id desc limit 3;"
        return Database.get_rows(sql)
    

    @staticmethod
    def create_value(component_id, datetime, status, value, action_id):
        sql = "INSERT INTO FishFooddispenserDB.Dispenser(component_id, datetime, status, value, action_id) VALUES(%s,%s,%s,%s,%s);"
        params = [component_id, datetime, status, value, action_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_value(component_id, datetime, status, value, action_id):
        sql = "UPDATE FishFooddispenserDB.Dispenser SET component_id = %s, datetime = %s, status = %s, value = %s, action_id = %s;"
        params = [component_id, datetime, status, value, action_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_value(measuring_id):
        sql = "DELETE FROM FishFooddispenserDB.Dispenser WHERE measuring_id = %s;"
        params = [measuring_id]
        return Database.execute_sql(sql, params)

    #########  Settings  #########
    @staticmethod
    def read_settings():
        sql = "SELECT numOfGrams, feedingTime, stateSpeaker FROM FishFooddispenserDB.Settings;"
        return Database.get_one_row(sql)

    @staticmethod
    def read_state_speaker():
        sql = "SELECT stateSpeaker FROM FishFooddispenserDB.Settings;"
        return Database.get_one_row(sql)

    @staticmethod
    def update_settings(numOfGrams, feedingTime, stateSpeaker):
        sql = "UPDATE FishFooddispenserDB.Settings SET numOfGrams = %s, feedingTime = %s, stateSpeaker = %s;"
        params = [numOfGrams, feedingTime, stateSpeaker]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_settings_speaker(stateSpeaker):
        sql = "UPDATE FishFooddispenserDB.Settings SET stateSpeaker = %s;"
        params = [stateSpeaker]
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