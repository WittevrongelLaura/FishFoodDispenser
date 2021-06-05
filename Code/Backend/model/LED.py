from RPi import GPIO


class LED:
    def __init__(self, led_green=16, led_yellow=20, led_red=21):
        self.led_green = led_green
        self.led_yellow = led_yellow
        self.led_red = led_red

        GPIO.setmode(GPIO.BCM)

        self.arr_leds = [self.led_green, self.led_yellow, self.led_red]
        for led in self.arr_leds:
            GPIO.setup(led, GPIO.OUT)
    
    def led_on(self, led):
        if led == "green": led = self.led_green
        if led == "yellow": led = self.led_yellow
        if led == "red": led = self.led_red
        GPIO.output(led, GPIO.HIGH)

    def led_off(self, led):
        GPIO.output(led, GPIO.LOW)

    def all_leds_off(self):
        for led in self.arr_leds:
            GPIO.output(led, GPIO.LOW)

