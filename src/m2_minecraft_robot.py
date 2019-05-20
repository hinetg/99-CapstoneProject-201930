# This is part of an independent side project; please do not touch this!
import paho.mqtt.client as mqtt
import time
import rosebot


def on_message(client, userdata, message):
    print(message.payload.decode('utf-8'))
    if message.payload.decode('utf-8') == 'up':
        robot.drive_system.stop()

    if message.payload.decode('utf-8') == 'down':
        robot.drive_system.stop()

    if message.payload.decode('utf-8') == 'right':
        robot.drive_system.stop()
        robot.drive_system.left_motor.reset_position()
        robot.drive_system.go(100, -100)
        while True:
            if robot.drive_system.left_motor.get_position() >= 90 * 4.572 * 1.1 * (355 / 360):
                robot.drive_system.stop()
                break
            if message.payload.decode('utf-8') == 'stop':
                robot.drive_system.stop()
                break

    if message.payload.decode('utf-8') == 'left':
        robot.drive_system.stop()
        robot.drive_system.right_motor.reset_position()
        robot.drive_system.go(-100, 100)
        while True:
            if robot.drive_system.right_motor.get_position() >= 90 * 4.572 * 1.1 * (355 / 360):
                robot.drive_system.stop()
                break
            if message.payload.decode('utf-8') == 'stop':
                robot.drive_system.stop()
                break

    if message.payload.decode('utf-8') == 'forward':
        robot.drive_system.stop()
        robot.drive_system.go(100, 100)

    if message.payload.decode('utf-8') == 'backward':
        robot.drive_system.stop()
        robot.drive_system.go(100, 100)

    if message.payload.decode('utf-8') == 'stop':
        robot.drive_system.stop()


robot = rosebot.RoseBot()

client = mqtt.Client('receiver')

client.on_message = on_message

client.connect("mosquitto.csse.rose-hulman.edu")

time.sleep(3)
print('connected.')
while True:
    client.loop_start()

    client.subscribe('minecraft')

    time.sleep(.1)

    client.loop_stop()

