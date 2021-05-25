from RPi import GPIO
import time
import spidev

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from repositories.DataRepository import DataRepository


class MCP:

    def __init__(self, bus=0, device=0):
        # initialiseer een SpiDev-object
        self.spi = spidev.SpiDev()
        # slave kiezen, bus is het nr van de SPI-bus, device is nr van SS/CE/CS-lijn
        self.spi.open(0, 0)  # bus 0(SPI0)  device 0(slave op CE 0)
        # klokfreq intstellen op 100kHz
        self.spi.max_speed_hz = 10 ** 5

    def OmzettenInPercentage(self, waarde):
        return (waarde/1023.0) * 100

    def closespi(self):
        self.spi.close()

    def read_channel(self, ch):
        fotodiode = 1
        # ch is 0 of 1
        # commandobyte samenstellen
        channel = ch << 4 | 128
        # 0 << 4 = 0000 | 128 = 10000000 = dec:128
        # 1 << 4 = 1000 | 128 = 10001000 = dec:144
        #print(channel)
        # list met de 3 te versturen bytes
        bytes_out = [0b00000001, channel, 0b00000000]
        #print(bytes_out)
        # versturen en 3 bytes terugkrijgen
        bytes_in = self.spi.xfer(bytes_out)

        # meetwaarde uithalen
        #print(bytes_in)
        byte1 = bytes_in[1]
        byte2 = bytes_in[2]
        # bytes aan elkaar hangen
        #print("{0:b} & {1:b}".format(byte1, byte2))
        result = byte1 << 8 | byte2

        # meetwaarde afdrukken
        if ch == 0:
            
            # print(result)
            # print(format(self.OmzettenInPercentage(result), '.2f') + " %")
            return format(self.OmzettenInPercentage(result), '.2f')
        elif ch == 1:
            # print(result)
            # print(format(self.OmzettenInPercentage(result), '.2f') + " %")
            return format(self.OmzettenInPercentage(result), '.2f')
        



mcp = MCP()

print("app.py")
try:
    #mcp.read_channel(0)
    #mcp.read_channel(1)
    #time.sleep(1)
    
    # Start app
    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins="*")
    CORS(app)

    # Custom endpoint
    endpoint = '/api/v1'

    #ROUTES
    @app.route('/')
    def index():
        return 'index'

    @app.route(endpoint + '/fotodiode0', methods=['GET'])
    def get_data_fotodiode0():
        print("helloooooo")
        if request.method == 'GET':
            print(mcp.read_channel(0))
            return mcp.read_channel(0)
        
        return "fout"

    @app.route(endpoint + '/fotodiode1', methods=['GET'])
    def get_data_fotodiode1():
        print("2222222222222222222")
        if request.method == 'GET':
            return mcp.read_channel(1)
    
        return "fout"

    #socketio
    

    if __name__ == "__main__":
        app.run(debug=True)

except KeyboardInterrupt as e:
    print(e)

finally:
    mcp.closespi()
    #GPIO.cleanup()