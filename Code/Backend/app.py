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

led = LED()
mcp = MCP(led)
waterlevel = Waterlevel()
watertemp = Watertemp()
lcd = LCD()
servo = Servo()
speaker = Speaker()
#print(datetime.now())

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
        global last_value_capacity
        value_capacity = mcp.get_capacity()
        print(value_capacity)

        while True:
            if value_capacity != last_value_capacity():
                emit("B2F_value_capacity", {"capacity":value_capacity}, broadcast=True)

            last_value_capacity = value_capacity

    @socketio.on('F2B_getWaterTemp')
    def get_value_watertemp(jsonObject):
        #while True:
        value_watertemp = watertemp.read_temp()
        print(value_watertemp)
        emit("B2F_value_watertemp", {"temp":value_watertemp}, broadcast=True)
        

    @socketio.on('F2B_getWaterlevel')
    def get_value_waterlevel(jsonObject):
        #while True:
        value_waterlevel = waterlevel.read_waterlevel()
        print(value_waterlevel)
        emit("B2F_value_waterlevel", {"level":value_waterlevel}, broadcast=True)
   

    @socketio.on('F2B_addToDb')
    def add_to_db(jsonObject):
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

    @socketio.on('F2B_startProcess')
    def starting_process():
        print("start process")


    @socketio.on('F2B_getDataFromDb')
    def get_data_from_db(jsonObject):
        print(jsonObject)
        # capacity = DataRepository.read_all_history_by_value("capacity")
        # watertemp = DataRepository.read_all_history_by_value("watertemp")
        # waterlevel = DataRepository.read_all_history_by_value("waterlevel")
        capacity = DataRepository.read_value_by_id(3)
        watertemp = DataRepository.read_value_by_id(1)
        waterlevel = DataRepository.read_value_by_id(2)
        emit("B2F_DataDb", {"capacity": capacity, "watertemp": watertemp, "waterlevel": waterlevel})
    

    

    def start_process():
        #### het proces manueel starten (ook met de button op index.html) ###

        #speaker maakt geluid
        speaker.getSound()

        #lcd geeft message: "starting process"
        lcd.write_message("Process started")

        #aantal gram ingesteld ophalen
        #lcd.read_display()

        #servo start met ingestelde grammen
        servo.start_servo(5)

        #lcd terug naar standby modus (ip-adres tonen)
        #lcd.setStatus(1)
        


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
    GPIO.cleanup()