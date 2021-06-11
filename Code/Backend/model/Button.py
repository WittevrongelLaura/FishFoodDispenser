from RPi import GPIO
import time
#from model.LCD import LCD
from LCD import LCD
from Watertemp  import Watertemp
from WaterLevel import Waterlevel
# from MCP import MCP


class Button:
    def __init__(self, btn_up=17, btn_down=27, btn_back=14, btn_enter=15, lcd=LCD(), watertemp = Watertemp(), waterlevel = Waterlevel()):
        self.btn_up = btn_up
        self.btn_down = btn_down
        self.btn_back = btn_back
        self.btn_enter = btn_enter
        self.lcd = lcd
        self.watertemp = watertemp
        self.waterlevel = waterlevel
        # self.mcp = mcp

        self.status = 1
        self.counter = 0

        # self.value_watertemp = None
        # self.value_waterlevel = None

        GPIO.setmode(GPIO.BCM)

        self.arr_btns = [self.btn_up, self.btn_down, self.btn_back, self.btn_enter]
        self.arrow_btns = [self.btn_up, self.btn_down]
        self.control_btns = [self.btn_back, self.btn_enter]

        for btn in self.arr_btns:
            GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        
        GPIO.add_event_detect(self.btn_up, GPIO.FALLING, callback=self.callback_arrow_up, bouncetime=200)
        GPIO.add_event_detect(self.btn_down, GPIO.FALLING, callback=self.callback_arrow_down, bouncetime=200)
        GPIO.add_event_detect(self.btn_back, GPIO.FALLING, callback=self.callback_back, bouncetime=200)
        GPIO.add_event_detect(self.btn_enter, GPIO.FALLING, callback=self.callback_enter, bouncetime=200)
        

        print(self.status)

    def callback_arrow_up(self, pin):
        print("button up pressed")
        self.check_status()
        self.counter += 1

        self.status += 1

        if self.status == 8:
            self.status = 1
        
        self.lcd.write_message(str(self.status))
        print(self.status)
        
    
        print(self.watertemp.read_temp())
        self.value_watertemp = self.watertemp.read_temp()
    

        
    
    def callback_arrow_down(self, pin):
        print("button down pressed")
        
        self.counter -= 1

        self.status -= 1

        if self.status == 0:
            self.status = 7
        
        self.lcd.write_message(str(self.status))
        print(self.status)
        

    def callback_back(self, pin):
        print("button back pressed")
    
    def callback_enter(self, pin):
        print("button enter pressed")

        

    def check_status(self):
        # , number_doses, number_grams, feeding_time, state_waterlevel, state_watertemp, state_speaker
        #1: ip-adres tonen
        #2: aantal dosissen per dag
        #3: aantal gram per dag
        #4: tijdstip dat er gevoederd moet worden
        #5: waterlevel sensor aan/uit zetten
        #6: Watertemp sensor aan/uit zetten
        #7: speaker aan/uit zetten
        if self.status >= 1 and self.status <= 7:
            if self.status == 1:
                self.lcd.clear_display()
                print("ip-addresses: {}".format(self.lcd.get_ipaddress()))
                self.lcd.get_ipaddress()

            elif self.status == 2:
                self.lcd.clear_display()
                self.lcd.write_message("Num of doses")
                # self.lcd.write_message(number_doses)

            elif self.status == 3:
                self.lcd.clear_display()
                self.lcd.write_message("Num of grams")
                # self.lcd.write_message(number_grams)

            elif self.status == 4:
                self.lcd.clear_display()
                self.lcd.write_message("Feedingtime")
                # self.lcd.write_message(feeding_time)

            elif self.status == 5:
                self.lcd.clear_display()
                self.lcd.write_message("State waterlevel")
                # self.lcd.write_message(state_waterlevel)

            elif self.status == 6:
                self.lcd.clear_display()
                self.lcd.write_message("Watertemperature")
                #self.lcd.write_message(valuewatertemp)

            elif self.status == 7:
                self.lcd.clear_display()
                self.lcd.write_message("State speaker")
                # self.lcd.write_message(state_speaker)
        



# try:
#     btn = Button()
    
#     while True:
#         time.sleep(0.5)

# except KeyboardInterrupt as e:
#     print(e)

# finally:
#     GPIO.cleanup()