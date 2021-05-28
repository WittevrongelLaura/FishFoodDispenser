from RPi import GPIO
import time

class Button:
    def __init__(self, btn1=17, btn2=27, btn3=14, btn4=15):
        self.btn1 = btn1
        self.btn2 = btn2
        self.btn3 = btn3
        self.btn4 = btn4

        GPIO.setmode(GPIO.BCM)

        self.arr_btns = [self.btn1, self.btn2, self.btn3, self.btn4]

        for btn in self.arr_btns:
            GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(btn, GPIO.FALLING, callback=self.clb_btn, bouncetime=200)

    def clb_btn(self, pin):
        print("button pressed")

# try:
#     btn = Button()
#     while True:
#         time.sleep(0.5)

# except KeyboardInterrupt as e:
#     print(e)

# finally:
#     GPIO.cleanup()