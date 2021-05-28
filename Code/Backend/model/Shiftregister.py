import time
from RPi import GPIO

# default pin numbers (BCM) - pas aan indien nodig
DS = 17  # serial data
OE = 27  # output enable (active low)
STCP = 22  # storage register clock pulse
SHCP = 5  # shift register clock pulse
MR = 6  # master reset (active low)
bit = 0

DELAY = 0.001

class ShiftRegister:
    def __init__(self, ds_pin=DS, shcp_pin=SHCP, stcp_pin=STCP, mr_pin=MR, oe_pin=OE):
        self.ds_pin = ds_pin
        self.shcp_pin = shcp_pin
        self.stcp_pin = stcp_pin
        self.mr_pin = mr_pin
        self.oe_pin = oe_pin
        GPIO.setmode(GPIO.BCM)
        
        for pin in self.ds_pin, self.oe_pin, self.shcp_pin, self.stcp_pin, self.mr_pin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        GPIO.output(self.mr_pin, GPIO.HIGH)

    def write_bit(self, bit):
        #1 bit doorsturen
        GPIO.output(self.ds_pin, bit)
        print(bit)
        time.sleep(DELAY)
        GPIO.output(self.shcp_pin, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(self.ds_pin, GPIO.LOW)
        GPIO.output(self.shcp_pin, GPIO.LOW)
        time.sleep(DELAY)
      
    

    def copy_to_storage_register(self):
        #klokpuls op het storageregister om data te kopiëren
        GPIO.output(self.stcp_pin, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(self.stcp_pin, GPIO.LOW)
        
               
        
    def write_byte(self, value):
        mask = 0x01
        for i in range(0,8):
            bit = (value & mask << (7-i)) 
            self.write_bit(bit)
        
        #mask = 0x80
        # for i in range(0,8):
        #     bit = (value & (mask >> i))
        #     self.write_bit(bit)
        
        #mask = 0x01
        # for i in range(7, -1, -1):
        #     bit = (value >> i) & mask
        #     self.write_bit(bit)

        

    @property
    def output_enabled(self):
        return not GPIO.input(self.oe_pin)

    @output_enabled.setter
    def output_enabled(self, value):
        GPIO.output(self.oe_pin, not value)

    def reset_shift_register(self):
        GPIO.output(self.mr_pin, GPIO.LOW)
        time.sleep(DELAY)
        GPIO.output(self.mr_pin, GPIO.HIGH)
        time.sleep(DELAY)

    def reset_storage_register(self):
        self.reset_shift_register()
        self.copy_to_storage_register()