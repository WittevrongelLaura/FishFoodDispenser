from RPi import GPIO
import time


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

led = LED()
mcp = MCP(led)
waterlevel = Waterlevel()
watertemp = Watertemp()
lcd = LCD()
#print(datetime.now())

try:
    # Start app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Secret!aBcdXyZ'
    socketio = SocketIO(app, cors_allowed_origins="*")
    CORS(app)  
    print("*** Program started ***")
    value_watertemp = watertemp.read_temp()
    print(value_watertemp)
    # print(mcp.read_channel(0))
    # print(mcp.read_channel(1))
    #lcd.write_message("hello")
    
    # lcd.get_ipaddress()

    
    
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

    @socketio.on('F2B_getWaterTemp')
    def get_value_watertemp(jsonObject):
        value_watertemp = watertemp.read_temp()
        print(value_watertemp)
        emit("B2F_value_watertemp", {"temp":value_watertemp}, broadcast=True)

    @socketio.on('F2B_getWaterlevel')
    def get_value_waterlevel(jsonObject):
        value_waterlevel = waterlevel.read_waterlevel()
        print(value_waterlevel)
        emit("B2F_value_watertemp", {"temp":value_waterlevel}, broadcast=True)

          

        

    # @socketio.on('F2B_getCapacity')
    # def get_value_capacity(jsonObject):
    #     value_capacity = mcp.get_capacity()

    def add_to_Database():
        if watertemp.read_temp() > 0 :
            status = 1
        else:
            status = 0
        DataRepository.create_history(1, None, status, watertemp.read_temp(), 1)

    
    

    if __name__ == "__main__":
        #app.run(debug=True)
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)

except KeyboardInterrupt as e:
    print(e)

finally:
    mcp.closespi()
    # waterlevel.close_waterlevel()
    watertemp.close_file()
    GPIO.cleanup()