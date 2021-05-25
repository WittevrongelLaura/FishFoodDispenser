from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    #########  waterlevel  #########
    @staticmethod
    def read_all_waterlevel():
        sql = "SELECT * from FishFoodDispenserDB.Waterlevel"
        return Database.get_rows(sql)

    @staticmethod
    def read_waterlevel_by_id(id_waterlevel):
        sql = "SELECT * from FishFoodDispenserDB.Waterlevel WHERE id_waterlevel = %s"
        params = [id_waterlevel]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_waterlevel(date, time, waterlevel):
        sql = "INSERT INTO FishFoodDispenserDB.Waterlevel(date, time, waterlevel) VALUES(%s,%s,%s)"
        params = [date, time, waterlevel]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_waterlevel(waterlevel_id, date, time, waterlevel):
        sql = "UPDATE FishFoodDispenserDB.Waterlevel SET date = %s, time = %s, waterlevel = %s WHERE waterlevel_id = %s"
        params = [date, time, waterlevel, waterlevel_id]
        #print(sql)
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_waterlevel(waterlevel_id):
        sql = "DELETE from FishFoodDispenserDB.Waterlevel WHERE waterlevel_id = %s"
        params = [waterlevel_id]
        return Database.execute_sql(sql, params)


    #########  fotodiode  #########
    @staticmethod
    def create_fotodiode(date, time, lightsensor):
        sql = "INSERT INTO FishFoodDispenserDB.fotodiode(date, time, lightsensor_value) VALUES(%s,%s,%s)"
        params = [date, time, lightsensor]
        return Database.execute_sql(sql, params)