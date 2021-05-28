import time
from RPi import GPIO

class Shiftregister:
    def __init__(self, ds_pin=5, shcp_pin=19, stcp_pin=13, mr_pin=26, oe_pin=6):
        self.ds_pin = ds_pin # serial data
        self.shcp_pin = shcp_pin # shift register clock pulse
        self.stcp_pin = stcp_pin # storage register clock pulse
        self.mr_pin = mr_pin # master reset (active low)
        self.oe_pin = oe_pin # output enable (active low)

        self.delay = 0.001

        GPIO.setmode(GPIO.BCM)
        
        for pin in self.ds_pin, self.oe_pin, self.shcp_pin, self.stcp_pin, self.mr_pin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        GPIO.output(self.mr_pin, GPIO.HIGH)

    def write_bit(self, bit):
        #1 bit doorsturen
        GPIO.output(self.ds_pin, bit)
        #print(bit)
        time.sleep(self.delay)
        GPIO.output(self.shcp_pin, GPIO.HIGH)
        time.sleep(self.delay)
        GPIO.output(self.ds_pin, GPIO.LOW)
        GPIO.output(self.shcp_pin, GPIO.LOW)
        time.sleep(self.delay)
      
    

    def copy_to_storage_register(self):
        #klokpuls op het storageregister om data te kopiëren
        GPIO.output(self.stcp_pin, GPIO.HIGH)
        time.sleep(self.delay)
        GPIO.output(self.stcp_pin, GPIO.LOW)
        
               
        
    def write_byte(self, value):
        # mask = 0x01
        # for i in range(0,8):
        #     bit = (value & mask << (7-i)) 
        #     self.write_bit(bit)
        
        #mask = 0x80
        # for i in range(0,8):
        #     bit = (value & (mask >> i))
        #     self.write_bit(bit)
        
        mask = 0x01
        for i in range(7, -1, -1):
            bit = (value >> i) & mask
            self.write_bit(bit)

        

    @property
    def output_enabled(self):
        return not GPIO.input(self.oe_pin)

    @output_enabled.setter
    def output_enabled(self, value):
        GPIO.output(self.oe_pin, not value)

    def reset_shift_register(self):
        GPIO.output(self.mr_pin, GPIO.LOW)
        time.sleep(self.delay)
        GPIO.output(self.mr_pin, GPIO.HIGH)
        time.sleep(self.delay)

    def reset_storage_register(self):
        self.reset_shift_register()
        self.copy_to_storage_register()