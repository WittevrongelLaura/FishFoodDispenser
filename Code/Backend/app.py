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
button = None
#btn = Button(mcp.get_capacity(), watertemp.read_temp(), waterlevel.read_waterlevel(), speaker.state_speaker())

#print(datetime.now())
previous_value_capacity = None
previous_value_temp = None
previous_value_level = None

num_grams = None
feeding_time = None
state_speaker = None
time_for_timer = None

value_capacity = None
value_watertemp = None
value_waterlevel = None

try:
    # Start app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Secret!aBcdXyZ'
    socketio = SocketIO(app, cors_allowed_origins="*")
    CORS(app)  
    print("*** Program started ***")
    
    #current time
    time_now = datetime.now().strftime("%H:%M:%S")
    print("Current time", time_now)

    def get_values_for_lcd():
        print("get values for lcd")
        global lcd_temp
        global lcd_level
        global lcd_capacity
        global btn

        speaker = DataRepository.read_state_speaker()
        print(speaker)
        data = DataRepository.read_latest_values()
        print(data)

        print(data[0]['component_id'])

        for element in data:
            if element['component_id'] == 1:
                lcd_temp = element['value']
            if element['component_id'] == 2:
                lcd_level = element['value']
            if element['component_id'] == 3:
                lcd_capacity = element['value']
        
        print("lcd temp: ", lcd_temp)
        print("lcd level: ", lcd_level)
        print("lcd capacity: ", lcd_capacity)

        btn = Button(str(lcd_capacity), str(lcd_temp), str(lcd_level), speaker)

    # get_values_for_lcd()
    


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

    @socketio.on('F2B_getCapacity')
    def get_value_capacity():
        global previous_value_capacity
        global value_capacity

        while True:
            value_capacity = mcp.get_capacity()
            #print(value_capacity, "%")
            if value_capacity != previous_value_capacity:
                emit("B2F_value_capacity", {"capacity":value_capacity}, broadcast=True)
                time.sleep(0.25)
            previous_value_capacity = value_capacity

    @socketio.on('F2B_getWaterTemp')
    def get_value_watertemp():
        global previous_value_temp
        global value_watertemp

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
    def get_value_waterlevel():
        global previous_value_level
        global value_waterlevel

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
               
        list_datetime = []
        list_capacity = []
        list_watertemp = []
        list_waterlevel = []
        
        dates = DataRepository.read_dates()
        all_capacity = DataRepository.read_all_values_by_id(capacity_id)
        all_watertemp = DataRepository.read_all_values_by_id(watertemp_id)
        all_waterlevel = DataRepository.read_all_values_by_id(waterlevel_id)
        #print(dates)
        # print(all_capacity)

        # print(all_capacity[0]['datetime'])
        # print(all_capacity[0]['value'])

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
        
        emit("B2F_DataFromDb", [list_datetime, list_capacity, list_watertemp, list_waterlevel])


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
        print("state sp from db", state_speaker)
        
       

        

        emit("B2F_settingsFromDb", [num_grams, feeding_time, state_speaker])


    @socketio.on('F2B_sendTimeAgain')
    def get_time_again(jsonObject):
        global time_for_timer
        print("send time again: ",jsonObject)
        time_for_timer = jsonObject


    # @socketio.on('F2B_values_for_lcd')
    # def start_lcd(jsonObject):
    #     print('values for lcd')
    #     print(jsonObject)


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

    def start_process():
        #### het proces manueel starten (ook met de button op index.html) ###

        #lcd geeft message: "starting process"
        lcd.write_message("Process started")

        print(state_speaker)
        
        #speaker maakt geluid
        speaker.get_sound()

        #servo start met ingestelde grammen
        print(num_grams)
        servo.start_feeding(num_grams)

        #lcd terug naar standby modus (ip-adres tonen)
        #lcd.setStatus(1)

    #start_process()

    
    

    if __name__ == "__main__":
        #app.run(debug=True)
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)



except KeyboardInterrupt as e:
    print(e)

finally:
    lcd.clear_display()
    watertemp.close_file()
    mcp.closespi()
    waterlevel.close_waterlevel()
    lcd.stop_program()
    led.all_leds_off
    GPIO.cleanup()