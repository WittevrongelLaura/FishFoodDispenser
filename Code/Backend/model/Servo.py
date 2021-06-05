from RPi import GPIO
import time


class Servo:
    def __init__(self, servo_up=12, servo_left=24, servo_right=25):
        self.servo_up = servo_up
        self.servo_left = servo_left
        self.servo_right = servo_right

        self.pwm_servo_up = None
        self.pwm_servo_left = None
        self.pwm_servo_right = None

        self.is_running = False

        GPIO.setmode(GPIO.BCM)
        self.arr_servos = [servo_up, servo_left, servo_right]

        for servo in self.arr_servos:
            GPIO.setup(servo, GPIO.OUT)

        self.setup_pwm(self.arr_servos)

    def setup_pwm(self, pin):
        self.pwm_servo_up = GPIO.PWM(self.arr_servos[0], 50)
        self.pwm_servo_left = GPIO.PWM(self.arr_servos[1], 50)
        self.pwm_servo_right = GPIO.PWM(self.arr_servos[2], 50)
        # for pin in arr_pins:
        #     pwm.append(GPIO.PWM(pin, 50))


    def start_servo(self, servo):
        # self.angle = self.calc_angle(value)
        # self.duty = self.angle / 18 + 2
        # self.pwm.start(self.duty)
        # time.sleep(1)
        if servo == "up":
            self.pwm_servo_right.start(0)
            time.sleep(1)
            self.set_duty_cycle("up", 3)
            time.sleep(1)
            self.set_duty_cycle("up", 12)

        if servo == "left":
            self.pwm_servo_left.start(0)
            time.sleep(1)
            self.set_duty_cycle("left", 3)
            time.sleep(1)
            self.set_duty_cycle("left", 12)

        if servo == "right":
            self.pwm_servo_right.start(0)
            time.sleep(1)
            self.set_duty_cycle("right", 3)
            time.sleep(1)
            self.set_duty_cycle("right", 12)

    def set_duty_cycle(self,servo, dutycycle):
        if servo == "up": return self.pwm_servo_up.ChangeDutyCycle(dutycycle)
        if servo == "left": return self.pwm_servo_left.ChangeDutyCycle(dutycycle)
        if servo == "right": return self.pwm_servo_right.ChangeDutyCycle(dutycycle)


    def stop_one_servo(self, servo):
        if servo == "up": self.pwm_servo_up.stop()
        if servo == "left": self.pwm_servo_left.stop()
        if servo == "right": self.pwm_servo_right.stop()

    def stop_servos(self):
        # self.pwm.stop()
        self.pwm_servo_up.stop()
        self.pwm_servo_left.stop()
        self.pwm_servo_right.stop()

    def start_feeding(self):
        self.is_running = True
        self.start_servo("up")
        self.stop_one_servo("up")
        self.start_servo("left")
        self.stop_one_servo("left")
        self.start_servo("right")
        self.stop_one_servo("right")
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
    servo.stop_servos()
    #pwm.stop()
    GPIO.cleanup()
