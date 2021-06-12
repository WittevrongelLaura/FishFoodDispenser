from logging import captureWarnings
from RPi import GPIO
import time
from datetime import datetime


from flask import Flask, json, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from repositories.DataRepository import DataRepository
from datetime import date, datetime

from model.MCP import MCP
from model.WaterLevel import Waterlevel
from model.Watertemp import Watertemp
from model.LCD import LCD
from model.LED import LED
from model.Servo import Servo
from model.Speaker import Speaker
from model.Button import Button

led = LED()
mcp = MCP(led)
waterlevel = Waterlevel()
watertemp = Watertemp()
lcd = LCD()
servo = Servo()
speaker = Speaker()
#btn = Button(mcp.get_capacity(), watertemp.read_temp(), waterlevel.read_waterlevel(), speaker.state_speaker())

#print(datetime.now())
previous_value_capacity = None
previous_value_temp = None
previous_value_level = None

num_grams = None
feeding_time = None
state_speaker = None

try:
    # Start app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Secret!aBcdXyZ'
    socketio = SocketIO(app, cors_allowed_origins="*")
    CORS(app)  
    print("*** Program started ***")
    # value_watertemp = watertemp.read_temp()
    # print(value_watertemp)
    
    #lcd.write_message("hello")
    
    #lcd.get_ipaddress()
    #current time
    time_now = datetime.now().strftime("%H:%M:%S")
    print("Current time", time_now)

    
    ############socketio#######################
    @socketio.on('connect')
    def connection():
        print('A new client connected')
        user = request.sid
        emit("B2F_connection", f"Welkom nieuwe client {user}")

    # @socketio.on('F2B_getValuesPhotodiodes')
    # def get_values_photodiodes(jsonObject):
    #     print("De backend kreeg dit het jsonObject binnen: ")
    #     #print(jsonObject)
    #     emit('B2F_getValuesPhotodiodes', [mcp.read_channel(0),  mcp.read_channel(1)])

    # @socketio.on('F2B_createPhotodiodes')
    # def create_photodiodes_in_db(jsonObject):
    #     #print(jsonObject)
    #     up = jsonObject[0]
    #     under = jsonObject[1]
    #     # DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  up)
    #     # DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  under)

    @socketio.on('F2B_getCapacity')
    def get_value_capacity(jsonObject):
        global previous_value_capacity
        while True:
            value_capacity = mcp.get_capacity()
            #print(value_capacity, "%")
            if value_capacity != previous_value_capacity:
                emit("B2F_value_capacity", {"capacity":value_capacity}, broadcast=True)
                time.sleep(0.25)
            previous_value_capacity = value_capacity

    @socketio.on('F2B_getWaterTemp')
    def get_value_watertemp(jsonObject):
        global previous_value_temp
        while True:
            value_watertemp = watertemp.read_temp()
            #print(value_watertemp, "°C")
            if value_watertemp != previous_value_temp:
                print('verschillend')
                emit("B2F_value_watertemp", value_watertemp)
                time.sleep(0.25)
            else:
                print('hetzelfde')
                time.sleep(0.25)
            previous_value_temp = value_watertemp

    @socketio.on('F2B_getWaterlevel')
    def get_value_waterlevel(jsonObject):
        global previous_value_level
        
        while True:
            value_waterlevel = waterlevel.read_waterlevel()
            #print(value_waterlevel, "%")
            if value_waterlevel != previous_value_level:
                emit("B2F_value_waterlevel", {"level":value_waterlevel}, broadcast=True)
                time.sleep(0.25)
        
            previous_value_level = value_waterlevel
   

    @socketio.on('F2B_addToDb')
    def add_to_db(jsonObject):
        #bij het starten van het proces worden de waardes doorgestuurd naar de db
        print("De backend kreeg dit object binnen: ", jsonObject)
        value_watertemp = jsonObject['watertemp']
        value_waterlevel = jsonObject['waterlevel']
        value_capacity = jsonObject['capacity']
        print("Watertemp: ", watertemp)
        print("Waterlevel: ", value_waterlevel)
        print("Capacity: ", value_capacity)
        
        
        status = None
        print("status", status)
        if float(value_watertemp) > 0:
            status = 1
        else:
            status = 0
        print("status", status)  
        DataRepository.create_value(1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, value_watertemp, 1)

        
        status = None
        if value_waterlevel != None or value_waterlevel > 0:
            status = 1
        else:
            status = 0
        DataRepository.create_value(2, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, value_waterlevel, 2)

        
        status = None
        if value_capacity > 0:
            status = 1
        else:
            status = 0
        DataRepository.create_value(3, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, value_capacity, 3)

        print("Toegevoegd aan db")

    @socketio.on('F2B_startProcess')
    def starting_process():
        print("start process")


    @socketio.on('F2B_getDataFromDb')
    def get_data_from_db(jsonObject):
        print(jsonObject)
        capacity_id = 3
        watertemp_id = 1
        waterlevel_id = 2
        # capacity = DataRepository.read_value_by_id(capacity_id)
        # watertemp = DataRepository.read_value_by_id(watertemp_id)
        # waterlevel = DataRepository.read_value_by_id(waterlevel_id)
        
        # dict met alle rows in
        # print(DataRepository.read_all_history())
        # data = DataRepository.read_all_history()

        listData = []
        dictData = {}
        listDatetime = []
        listCapacity = []
        listWatertemp = []
        listWaterlevel = []
        listValues = []
        # datetime = str(data[0]["datetime"])
        # value = data[0]["value"]
        # print(datetime)
        # print(value)
        # # for row in data:
        # #     if row.value in datetime:
        # #         print("ja")
                
        #     else:
        #         print("nee")
        #         dictData[datetime] = value

        #     listData.append(dictData)

        
        # dictData[datetime] = 
        
        # for row in data:
        #     datetime = str(row["datetime"])
        #     print(datetime)
        #     if datetime not in listDatetime:
        #         listDatetime.append(datetime)
            


            
                
        # print("listdatetime")
        # print (listDatetime)
        # print("dict")
        # print(listData)

        #emit("B2F_DataFromDb", {"capacity": capacity, "watertemp": watertemp, "waterlevel": waterlevel})
        #emit("B2F_DataFromDb", jsonify(datadb=data))

        all_capacity = DataRepository.read_all_values_by_id(capacity_id)
        all_watertemp = DataRepository.read_all_values_by_id(watertemp_id)
        all_waterlevel = DataRepository.read_all_values_by_id(waterlevel_id)
        print(all_capacity)
        print(all_capacity.values())
        #all_capacity.update({'datetime': str(all_capacity.value())})
        
        emit("B2F_DataFromDb", [all_capacity, all_watertemp, all_waterlevel])

        # for row in all_capacity:
            
        #     print(row)
        #     print(row['datetime'])
        #     print(row['value'])
        #     listCapacity.append(row['value'])
        #     # print(row2['value'])
        #     # print(row3['value'])
        #     #dictData[str(row['datetime'])] = [row['value'], row2['value'], row3['value']]
        #     dictData[str(row['datetime'])] = listCapacity
                    
        # for row2 in all_watertemp:
        #     print(row2)
        #     if row2['value'] not in dictData.values():
        #         print('dicttttttttttt')
        #         print(dictData.values())
        #         dictData[str(row2['datetime'])] = [row2['value']]
        #         #dictData.values().append(row2['value'])

        # for row3 in all_waterlevel:
        #     print(row3)
        #     if row3['value'] not in dictData.values():
        #         dictData[str(row3['datetime'])] = [row3['value']]
        #         #dictData.values().append(row2['value'])
                
        # print(dictData)
        # listData.append(dictData)
        # print(listData)
        #emit("B2F_DataFromDb", dictData)

    @socketio.on('F2B_grams')
    def change_grams(jsonObject):
        global num_grams
        print(jsonObject)
        num_grams = jsonObject

    @socketio.on('F2B_time')
    def change_grams(jsonObject):
        global feeding_time
        print(jsonObject)
        feeding_time = jsonObject

    @socketio.on('F2B_stateSpeaker')
    def change_grams(jsonObject):
        global state_speaker
        print(jsonObject)
        if jsonObject:
            #true = speaker activated
            state_speaker = "on"
        else:
            state_speaker = "off"



    

    def start_process():
        #### het proces manueel starten (ook met de button op index.html) ###

        # #speaker maakt geluid
        # speaker.getSound()

        # #lcd geeft message: "starting process"
        # lcd.write_message("Process started")

        # #aantal gram ingesteld ophalen
        # #lcd.read_display()

        # #servo start met ingestelde grammen
        # servo.start_servo(5)

        #lcd terug naar standby modus (ip-adres tonen)
        #lcd.setStatus(1)
        pass
        


    #if time_now == lcd.setted_time()
        #start_process()
        #add_to_db()
        

    if __name__ == "__main__":
        #app.run(debug=True)
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)

except KeyboardInterrupt as e:
    print(e)

finally:
    mcp.closespi()
    waterlevel.close_waterlevel()
    watertemp.close_file()
    lcd.stop_program()
    GPIO.cleanup()