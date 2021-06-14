from RPi import GPIO
import time
from model.LCD import LCD
#from LCD import LCD
# from Watertemp  import Watertemp
# from WaterLevel import Waterlevel
# from MCP import MCP




class Button:
    def __init__(self, capacity, watertemp, waterlevel, speaker, btn_up=17, btn_down=27, btn_back=25, btn_enter=24, lcd=LCD()):
        self.btn_up = btn_up
        self.btn_down = btn_down
        self.btn_back = btn_back
        self.btn_enter = btn_enter
        self.lcd = lcd
        

        self.state_lcd = None
        self.previous_state_lcd = None
        self.watertemp = watertemp
        self.waterlevel = waterlevel
        self.capacity = capacity

        if speaker == 0:
            self.speaker = "off"
        else:
            self.speaker = "on"

        print(self.capacity)
        print(self.watertemp)
        print(self.waterlevel)
        print(self.speaker)

        self.status = 1
        #ip-adress wordt getoond bij opstart
        # self.lcd.get_ipaddress()
        self.check_status(self.capacity, self.watertemp, self.waterlevel, self.speaker)
        self.previous_state_lcd = 1

        # self.value_watertemp = None
        # self.value_waterlevel = None

        GPIO.setmode(GPIO.BCM)

        self.arr_btns = [self.btn_up, self.btn_down, self.btn_back, self.btn_enter]
        self.arrow_btns = [self.btn_up, self.btn_down]
        self.control_btns = [self.btn_back, self.btn_enter]

        for btn in self.arr_btns:
            GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        
        
        GPIO.add_event_detect(self.btn_up, GPIO.FALLING, callback=self.callback_arrow_up, bouncetime=1500)
        GPIO.add_event_detect(self.btn_down, GPIO.FALLING, callback=self.callback_arrow_down, bouncetime=1500)
        GPIO.add_event_detect(self.btn_back, GPIO.FALLING, callback=self.callback_back, bouncetime=1500)
        GPIO.add_event_detect(self.btn_enter, GPIO.FALLING, callback=self.callback_enter, bouncetime=1500)
        

        # print(self.status)

    def callback_arrow_up(self, pin):
        #print("button up pressed")
        self.check_status(self.capacity, self.watertemp, self.waterlevel, self.speaker)
        
        self.status -= 1

        if self.status == 0:
            self.status = 5
        
        # self.lcd.write_message(str(self.status))
        #print(self.status)
        
    
        # print(self.watertemp.read_temp())
        # self.value_watertemp = self.watertemp.read_temp()
    
    def callback_arrow_down(self, pin):
        #print("button down pressed")
        
        
        self.status += 1

        if self.status == 6:
            self.status = 1
        self.check_status(self.capacity, self.watertemp, self.waterlevel, self.speaker)
        # self.lcd.write_message(str(self.status))
        #print(self.status)
        

    def callback_back(self, pin):
        print("button back pressed")
    
    def callback_enter(self, pin):
        print("button enter pressed")

     

    def check_status(self, capacity, watertemp, waterlevel, speaker):
        # , number_grams, feeding_time, state_speaker
        #1: ip-adres tonen
        #2: aantal gram per dag
        #3: tijdstip dat er gevoederd moet worden
        #4: speaker aan/uit zetten
        if self.status >= 1 and self.status <= 5:
            
            # if self.status != self.previous_state_lcd:
            
            if self.status == 1:
                print("ip")
                self.lcd.clear_display()
                #print("IP-address: {}".format(self.lcd.get_ipaddress()))
                self.lcd.get_ipaddress()

            elif self.status == 2:
                print("Capacity")
                self.lcd.clear_display()
                self.lcd.write_message("Capacity")
                self.lcd.send_instruction((0x80 | 0x40))
                print(capacity)
                self.lcd.write_message(capacity + " %")
            
            elif self.status == 3:
                print("Watertemp")
                self.lcd.clear_display()
                self.lcd.write_message("Watertemperature")
                self.lcd.send_instruction((0x80 | 0x40))
                print(watertemp)
                self.lcd.write_message(watertemp + " " + chr(39) + "C")


            elif self.status == 4:
                print("Waterlevel")
                self.lcd.clear_display()
                self.lcd.write_message("Waterlevel")
                self.lcd.send_instruction((0x80 | 0x40))
                print(waterlevel)
                self.lcd.write_message(waterlevel + " %")

                # self.previous_state_lcd = self.status
                # print("previous", self.previous_state_lcd)

            elif self.status == 5:
                print("speaker")
                self.lcd.clear_display()
                self.lcd.write_message("State speaker")
                self.lcd.send_instruction((0x80 | 0x40))
                print(speaker)
                self.lcd.write_message(speaker)
        print()
            
# try:
#     btn = Button(str(80),str(20), str(95), "on")
    
#     while True:
#         time.sleep(0.5)

# except KeyboardInterrupt as e:
#     print(e)

# finally:
#     btn.lcd.clear_display()
#     GPIO.cleanup()