import Adafruit_DHT
import paho.mqtt.client as mqtt
import json

def monitor_temperature_humidity():
    with open('config/gpio_pins.json') as f:
        gpio_pins = json.load(f)
    sensor = Adafruit_DHT.DHT22
    pin = gpio_pins['temperature_pin']
    
    mqtt_client = mqtt.Client()
    mqtt_client.connect("localhost", 1883, 60)
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        mqtt_client.publish("home/temperature", temperature)
        mqtt_client.publish("home/humidity", humidity)
