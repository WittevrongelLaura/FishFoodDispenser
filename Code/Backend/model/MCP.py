import spidev
from model.LED import LED
#from LED import LED
import time

class MCP:

    def __init__(self, bus=0, device=0, led=LED()):
        # initialiseer een SpiDev-object
        self.spi = spidev.SpiDev()
        # slave kiezen, bus is het nr van de SPI-bus, device is nr van SS/CE/CS-lijn
        self.spi.open(0, 0)  # bus 0(SPI0)  device 0(slave op CE 0)
        # klokfreq intstellen op 100kHz
        self.spi.max_speed_hz = 10 ** 5

        self.led = led

    def convert_to_percentage(self, value_up, value_under):
        return (100/value_under) * value_up

    def closespi(self):
        self.spi.close()

    def read_channel(self, ch):
        # ch is 0 of 1
        # commandobyte samenstellen
        channel = ch << 4 | 128
        # 0 << 4 = 0000 | 128 = 10000000 = dec:128
        # 1 << 4 = 1000 | 128 = 10001000 = dec:144
        # print(channel)
        # list met de 3 te versturen bytes
        bytes_out = [0b00000001, channel, 0b00000000]
        # print(bytes_out)
        # versturen en 3 bytes terugkrijgen
        bytes_in = self.spi.xfer(bytes_out)

        # meetwaarde uithalen
        # print(bytes_in)
        byte1 = bytes_in[1]
        byte2 = bytes_in[2]
        # bytes aan elkaar hangen
        #print("{0:b} & {1:b}".format(byte1, byte2))
        result = byte1 << 8 | byte2

        # meetwaarde afdrukken
        if ch == 0:
            # print(result)
            # print(format(self.OmzettenInPercentage(result), '.2f') + " %")
            # return format(self.value_to_percentage(result), '.2f')
            return result
        elif ch == 1:
            # print(result)
            # print(format(self.OmzettenInPercentage(result), '.2f') + " %")
            # return format(self.value_to_percentage(result), '.2f')
            return result

    # def convert_to_percentage(self, value):
    #     return(value/1023.0) * 100

    def get_capacity(self):
        value_up = self.read_channel(0)
        value_under = self.read_channel(1)
        print(value_up)
        print(value_under)
        # print()
        # print(round(self.convert_to_percentage(value_up, value_under)))
        # print()
        # print()
        self.capacity_percentage =  round(self.convert_to_percentage(value_up, value_under))
        self.run_leds(self.capacity_percentage)
        return self.capacity_percentage
        # difference = value_up - value_under
        # #positief maken
        # difference = abs(difference)
        # print(difference)
        # if difference >= 0 and difference <=20:
        #     print("Leeg")
        #     self.led.led_on("red")
        
        # if difference > 20:
        #     print("vol")
        #     self.led.led_on("green")

    def run_leds(self, percentage):
        # difference = value_up - value_under
        # #positief maken
        # difference = abs(difference)
        # print(difference)

        
        if percentage >= 0 and percentage <= 5:
            self.led.all_leds_off()
            print("emtpy")
            self.led.led_on("red")
        elif percentage > 5 and percentage <= 20:
            self.led.all_leds_off()
            print("almost empty")
            self.led.led_on("yellow")
        elif percentage > 20 and percentage <= 100:
            self.led.all_leds_off()
            print("full")
            self.led.led_on("green")

        

# led = LED()
# mcp = MCP(led)

# try:
#     print(mcp.read_channel(0))
#     # while True:
#     #     print(mcp.get_capacity())
#     #     time.sleep(1)
#     #     print()
# except KeyboardInterrupt as e:
#     print(e)
# finally:
#     led.all_leds_off() 


