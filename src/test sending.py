# This is part of an independent side project; please do not touch this!
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print(str(message.payload.decode('utf-8')))


client = mqtt.Client('test2')

client.on_message = on_message

client.connect("mosquitto.csse.rose-hulman.edu")

time.sleep(1)
while True:
    client.loop_start()

    client.subscribe('minecraft')

    time.sleep(1)

    client.loop_stop()
