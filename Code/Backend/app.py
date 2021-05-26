from RPi import GPIO
import time


from flask import Flask, json, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from repositories.DataRepository import DataRepository
from datetime import date, datetime

from model.MCP import MCP


mcp = MCP()

print("app.py")
try:
    # Start app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Secret!aBcdXyZ'
    socketio = SocketIO(app, cors_allowed_origins="*")
    print(mcp.read_channel(0))
    print(mcp.read_channel(1))
    # DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  mcp.read_channel(0))
    # DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  mcp.read_channel(1))
    CORS(app)

    # Custom endpoint
    endpoint = '/api/v1'

    #ROUTES
    @app.route('/')
    def index():
        return 'index'

    @app.route(endpoint + '/fotodiode/<id>', methods=['GET'])
    def get_data_fotodiode(id):
        if request.method == 'GET':
            print("get data")
            print(id)
            if id == 0:
                print(id)
                return mcp.read_channel(0)
            elif id == 1:
                return mcp.read_channel(1)
        return "fout"

    # @app.route(endpoint + '/fotodiode1', methods=['GET'])
    # def get_data_fotodiode1():
    #     if request.method == 'GET':
    #         return mcp.read_channel(1)
    
    #     return "fout"

    @app.route(endpoint + '/create_photodiode', methods=['GET'])
    def create_photodiode():
        if request.method == 'GET':
            DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  mcp.read_channel(0))
            DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  mcp.read_channel(1))
            return "done"
        return "create done"
    
    
    #socketio
    @socketio.on('connect')
    def connection():
        print('A new client connected')
        user = request.sid
        emit("B2F_connection", f"Welkom nieuwe client {user}")

    @socketio.on('F2B_getValuesPhotodiodes')
    def get_values_photodiodes(jsonObject):
        print("De backend kreeg dit het jsonObject binnen: ")
        print(jsonObject)
        emit('B2F_getValuesPhotodiodes', [mcp.read_channel(0),  mcp.read_channel(1)])

    @socketio.on('F2B_createPhotodiodes')
    def create_photodiodes_in_db(jsonObject):
        print(jsonObject)
        boven = jsonObject[0]
        onder = jsonObject[1]
        DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  boven)
        DataRepository.create_fotodiode(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"),  onder)

    if __name__ == "__main__":
        #app.run(debug=True)
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)

except KeyboardInterrupt as e:
    print(e)

finally:
    mcp.closespi()
    #GPIO.cleanup()