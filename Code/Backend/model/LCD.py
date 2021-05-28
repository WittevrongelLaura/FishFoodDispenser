from RPi import GPIO
import time

class LCD:
    def __init__(self, RS=21, E=21, bits=[16,12,25,24,23,26,19,13]):
        GPIO.setmode(GPIO.BCM)
        self.RS = RS
        self.E = E
        self.bits = bits

        for bit in self.bits:
            GPIO.setup(bit, GPIO.OUT,initial=GPIO.LOW)
        
        GPIO.setup(self.RS, GPIO.OUT,  initial=GPIO.LOW)
        GPIO.setup(self.E,  GPIO.OUT, initial=GPIO.HIGH)

        self.setup_display()

    
    def set_data_bits(self, byte):
        mask = 0x01
        for i in range(0,8):
            GPIO.output(self.bits[i], (byte & mask << i) > 0)


    def send_instruction(self, value):
        #RS moet laag staan voor instruction
        GPIO.output(self.RS, GPIO.LOW)
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

    def clear_display(self):
        self.send_instruction(0x01)

    def setup_display(self):
        #LCD
        #function set
        self.send_instruction(0x38)
        #display on
        self.send_instruction(0x0f)
        #clear display
        self.clear_display
        # #cursor home
        #send_instruction(0x40) 

try:
    lcd = LCD()
   
    #send_character(ord("A"))
    # text = "HALLO Laura"
    # for char in text:
    #     send_character(ord(char))
    #send_character(65)#letter A schrijven
    #lcd.write_message('Hellooooohelloooooooooj')

    message = input("What do you want to display? > ")
    lcd.write_message(message)
    
except KeyboardInterrupt as e:
    print(e)
finally:
    lcd.clear_display()
    GPIO.cleanup()
    