import RPi.GPIO as GPIO
import time
import json

def detect_motion():
    with open('config/gpio_pins.json') as f:
        gpio_pins = json.load(f)
    motion_pin = gpio_pins['motion_pin']
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motion_pin, GPIO.IN)
    
    try:
        while True:
            if GPIO.input(motion_pin):
                print("Motion detected!")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
