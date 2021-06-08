from RPi import GPIO
import time


class Servo:
    def __init__(self, servo=12):
        self.servo = servo

        self.pwm_servo = None

        self.is_running = False

        GPIO.setmode(GPIO.BCM)
                
        GPIO.setup(self.servo, GPIO.OUT)

        self.setup_pwm(self.servo)

    def setup_pwm(self, pin):
        self.pwm_servo = GPIO.PWM(self.servo, 50)
        
        # for pin in arr_pins:
        #     pwm.append(GPIO.PWM(pin, 50))


    def start_servo(self):
        # self.angle = self.calc_angle(value)
        # self.duty = self.angle / 18 + 2
        # self.pwm.start(self.duty)
        # time.sleep(1)
        
        
        time.sleep(0.5)
        self.set_duty_cycle(3)
        time.sleep(0.5)
        self.set_duty_cycle(12)

    def set_duty_cycle(self, dutycycle):
        return self.pwm_servo.ChangeDutyCycle(dutycycle)
        # if servo == "left": return self.pwm_servo_left.ChangeDutyCycle(dutycycle)
        # if servo == "right": return self.pwm_servo_right.ChangeDutyCycle(dutycycle)


    def stop_servo(self):
        self.pwm_servo.stop()
        # if servo == "left": self.pwm_servo_left.stop()
        # if servo == "right": self.pwm_servo_right.stop()

    
        

    def start_feeding(self):
        self.pwm_servo.start(0)
        self.is_running = True
        self.start_servo()
        time.sleep(0.02)
        # self.stop_servo()
        self.is_running = False


servo = Servo()
#servo.start_servo()
# servo_up = 12
# servo_left = 24
# servo_right = 25
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servo_right, GPIO.OUT)
#arr_servos = [servo_up, servo_left, servo_right]

# pwm = GPIO.PWM(servo_right, 50)
# pwm.start(0)
# pwm.start(80)
try:
    while True:
        servo.start_feeding()
    # while True:
        # time.sleep(1)
        # pwm.ChangeDutyCycle(3)
        # time.sleep(1)
        # pwm.ChangeDutyCycle(12)
        # servo.start_servo("up")
        # servo.stop_one_servo("up")
        # time.sleep(1)
        # servo.start_servo("left")
        # servo.stop_one_servo("left")
        # time.sleep(1)
        # servo.start_servo("right")
        # servo.stop_one_servo("right")
        # time.sleep(1)


except KeyboardInterrupt as e:
    print(e)

finally:
    servo.stop_servo()
    #pwm.stop()
    GPIO.cleanup()
