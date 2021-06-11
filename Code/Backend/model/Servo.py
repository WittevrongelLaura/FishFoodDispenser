from RPi import GPIO
import time


class Servo:
    def __init__(self, servo=12):
        self.servo = servo

        self.pwm_servo = None

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.servo, GPIO.OUT)

        self.setup_pwm(self.servo)

    def setup_pwm(self, pin):
        self.pwm_servo = GPIO.PWM(self.servo, 50)

    def start_servo(self):
        time.sleep(0.3)
        self.set_duty_cycle(2)  # rechts
        time.sleep(0.3)
        self.set_duty_cycle(6)  # links

    def set_duty_cycle(self, dutycycle):
        return self.pwm_servo.ChangeDutyCycle(dutycycle)

    def stop_servo(self):
        self.pwm_servo.stop()

    def calc_time_from_grams(self, grams):
        #voor 10 gr duurt het 20sec
        return 20/10*grams

    def start_feeding(self, grams):
        time = self.calc_time_from_grams(grams)
        self.pwm_servo.start(0)
        self.counter = 0

        while True:
            self.start_servo()
            self.counter +=1
            
            if (time == self.counter):
                break


# servo = Servo()

# try: 
#     servo.start_feeding(5)
    
# except KeyboardInterrupt as e:
#     print(e)

# finally:
#     servo.stop_servo()
#     servo.pwm.stop()
#     GPIO.cleanup()
