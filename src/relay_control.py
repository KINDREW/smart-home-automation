import RPi.GPIO as GPIO
import json

def control_appliance(state):
    with open('config/gpio_pins.json') as f:
        gpio_pins = json.load(f)
    relay_pin = gpio_pins['relay_pin']
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    
    if state == "on":
        GPIO.output(relay_pin, GPIO.HIGH)
    else:
        GPIO.output(relay_pin, GPIO.LOW)
