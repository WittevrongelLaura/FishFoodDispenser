from RPi import GPIO
import time
from model.Shiftregister import Shiftregister
#from Shiftregister import Shiftregister
from subprocess import check_output

class LCD:
    def __init__(self, RS=23, E=18, SR=Shiftregister()):
        GPIO.setmode(GPIO.BCM)
        self.RS = RS
        self.E = E
        self.SR = SR
        
        GPIO.setup(self.RS, GPIO.OUT)
        GPIO.setup(self.E,  GPIO.OUT)

        self.setup_display()

    
    def set_data_bits(self, byte):
        # mask = 0x01
        # for i in range(0,8):
        #     GPIO.output(self.bits[i], (byte & mask << i) > 0)
        self.SR.write_byte(byte)
        self.SR.copy_to_storage_register()


    def send_instruction(self, value):
        #RS moet laag staan voor instruction
        GPIO.output(self.RS, GPIO.LOW)
        GPIO.output(self.E, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(self.E, GPIO.LOW)
        GPIO.output(self.E, GPIO.HIGH)#op high zetten om te beginnen lezen
        time.sleep(0.01)

    def send_character(self, character):
        #RS moet hoog staan voor character
        GPIO.output(self.RS, GPIO.HIGH)
        self.set_data_bits(character)
        GPIO.output(self.E, GPIO.LOW)
        
        GPIO.output(self.E, GPIO.HIGH)
        time.sleep(0.01)

    def write_message(self, message):
        for char in message[0:16]:
            self.send_character(ord(char))   

        self.send_instruction((0x80 | 0x40))

        for char in message[16:]:
            self.send_character(ord(char))

    def read_display(self):
        pass

    def set_status(self, status):
        pass

    def clear_display(self):
        self.send_instruction(0x01)

    def get_ipaddress(self):
        self.clear_display()
        #ip-adres teruggeven
        ips = check_output(['hostname', '--all-ip-addresses']).split()
        #wordt encoded bytes teruggestuurd dus decoderen
        # print(ips[0].decode())
        # self.write_message(ips[0].decode())
        self.write_message("IP-address:")

        if len(ips) > 1:
            #als er meerdere ip-adressen worden gereturnt
            print(ips[1].decode())
            self.send_instruction((0x80 | 0x40))
            self.write_message(ips[1].decode())

    def setup_display(self):
        #LCD
        #function set
        self.send_instruction(0x38)
        #display on
        self.send_instruction(0x0f)
        #clear display
        self.clear_display()
        # #cursor home
        #send_instruction(0x40) 

    

# try:
#     lcd = LCD()
   
#     #lcd.send_character(ord("F"))
    
#     # text = "HALLO Laura"
#     # for char in text:
#     #     send_character(ord(char))
#     #send_character(65)#letter A schrijven
    
#     #lcd.write_message('Hello')

#     lcd.get_ipaddress()
#     time.sleep(1)

#     # message = input("What do you want to display? > ")
#     # lcd.write_message(message)
    
# except KeyboardInterrupt as e:
#     print(e)
# # finally:
#     #lcd.clear_display()