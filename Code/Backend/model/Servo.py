from RPi import GPIO
import time

class Servo:
    def __init__(self, servo_up=12, servo_left=24, servo_right=25):
        self.servo_up = servo_up
        self.servo_left = servo_left
        self.servo_right = servo_right

        GPIO.setmode(GPIO.BCM)
        self.arr_servos = [servo_up, servo_left, servo_right]
        
        for servo in self.arr_servos:
            GPIO.setup(servo, GPIO.OUT)

        self.setup_pwm(self.arr_servos)

    def setup_pwm(self, arr_pins):
        pwm = None
        for pin in arr_pins:
            pwm += GPIO.PWM(pin, 50)
        
        pwm.start(0)

    def calc_angle(self, value):
        return (value / 1023.0) * 180

    def start_servo(self, value):
        self.angle = self.calc_angle(value)
        self.duty = self.angle / 18 + 2
        self.pwm.start(self.duty) 
        time.sleep(1)

    def pwm_stop(self):
        self.pwm.stop()

try:
    servo = Servo()
    servo.start_servo(100)
except KeyboardInterrupt as e:
    print(e)

finally:
    servo.pwm_stop()
    GPIO.cleanup()