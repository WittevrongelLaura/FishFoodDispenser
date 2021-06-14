from logging import captureWarnings
from os import stat
from threading import Thread
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
time_for_timer = None

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


    def start_process():
        #### het proces manueel starten (ook met de button op index.html) ###

        #lcd geeft message: "starting process"
        lcd.write_message("Process started")

        #speaker maakt geluid
        speaker.get_sound()

        #servo start met ingestelde grammen
        print(num_grams)
        servo.start_feeding(num_grams)

        #lcd terug naar standby modus (ip-adres tonen)
        #lcd.setStatus(1)

    
    

    
    ############socketio#######################
    @socketio.on('connect')
    def connection():
        print('A new client connected')
        user = request.sid
        emit("B2F_connection", f"Welkom nieuwe client {user}")

    @socketio.on('F2B_startProcess')
    def starting_process():
        print("start process")
        start_process()

    

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
                #print('verschillend')
                emit("B2F_value_watertemp", value_watertemp)
                time.sleep(0.25)
            else:
                #print('hetzelfde')
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
        list_datetime = []
        list_capacity = []
        list_watertemp = []
        list_waterlevel = []
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
        dates = DataRepository.read_dates()
        all_capacity = DataRepository.read_all_values_by_id(capacity_id)
        all_watertemp = DataRepository.read_all_values_by_id(watertemp_id)
        all_waterlevel = DataRepository.read_all_values_by_id(waterlevel_id)
        #print(dates)
        print(all_capacity)

        print(all_capacity[0]['datetime'])
        print(all_capacity[0]['value'])

        for i in range(len(all_capacity)):
            value_datetime = all_capacity[i]['datetime']
            value_capacity = all_capacity[i]['value']
            list_datetime.append(str(value_datetime))
            list_capacity.append(value_capacity)
        
        print(list_datetime)
        print(list_capacity)

        for i in range(len(all_watertemp)):
            value_watertemp = all_watertemp[i]['value']
            list_watertemp.append(value_watertemp)

        print(list_watertemp)

        for i in range(len(all_waterlevel)):
            value_waterlevel = all_waterlevel[i]['value']
            list_waterlevel.append(value_waterlevel)
        
        print(list_waterlevel)

        #print(all_capacity.values())
        #all_capacity.update({'datetime': str(all_capacity.value())})
        
        emit("B2F_DataFromDb", [list_datetime, list_capacity, list_watertemp, list_waterlevel])

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

    @socketio.on('F2B_settingsChanged')
    def change_grams(jsonObject):
        global num_grams
        global feeding_time
        global state_speaker
        
        num_grams = jsonObject[0]
        feeding_time = jsonObject[1]
        state_speaker = jsonObject[2]
        # print(num_grams)
        # print(feeding_time)

        if state_speaker:
            #true = speaker activated
            state_speaker = 1
        else:
            state_speaker = 0
        #print(state_speaker)
        
        DataRepository.update_settings(num_grams, feeding_time, state_speaker)

        
        
    @socketio.on("F2B_getSettingsFromDb")
    def settingsFromDb():
        global num_grams
        global feeding_time
        global state_speaker
        
        #print('send data from settings table')
        settings = DataRepository.read_settings()
        #print(settings)



        num_grams = settings['numOfGrams']
        feeding_time = str(settings['feedingTime'])
        state_speaker =  settings['stateSpeaker']

        list_hours = ('0:', '1:', '2:', '3:', '4:', '5:', '6:', '7:', '8:', '9:')

        if feeding_time.startswith(list_hours):
            feeding_time = '0' + feeding_time

        
        # print(num_grams)
        # print(feeding_time)
        # print(state_speaker)

        emit("B2F_settings", [num_grams, feeding_time, state_speaker])

    @socketio.on('F2B_sendTimeAgain')
    def get_time_again(jsonObject):
        global time_for_timer
        print("send time again: ",jsonObject)
        time_for_timer = jsonObject


    #@socketio.on('F2B_sendValuesToStart')
    
    def timer():
        global feeding_time
        #global time_for_timer
        while True:
            #print("time for timer", time_for_timer)
            time_now = datetime.now().strftime("%H:%M:%S")
            print("time controleren")
            print(feeding_time)
            
            if time_now == feeding_time:
                print("it\'s time to eat!")
                print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                #start_process()
                #add_to_db()
            time.sleep(1)
    
        
    # thread = Thread(target=timer)
    # thread.start()
        

    
    
    # @app.route('/api/v1/dates', methods=['GET'])
    # def all_dates():
    #     if request.method == 'GET':
    #         data = DataRepository.read_dates()
    #         print(data)
    #         return jsonify(data), 200

    # @app.route('/api/v1/capacity', methods=['GET'])
    # def all_capacity():
    #     if request.method == 'GET':
    #         data = DataRepository.read_capacity()
    #         print(data)
    #         return jsonify(data), 200

    if __name__ == "__main__":
        #app.run(debug=True)
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)



except KeyboardInterrupt as e:
    print(e)

finally:
    watertemp.close_file()
    mcp.closespi()
    waterlevel.close_waterlevel()
    lcd.stop_program()
    GPIO.cleanup()