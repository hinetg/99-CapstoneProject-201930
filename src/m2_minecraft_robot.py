# This is part of an independent side project; please do not touch this!
import paho.mqtt.client as mqtt
import time

import rosebot
import m1_robot_code as m1
import m2_robot_code as m2
import m3_robot_code as m3
import m0_run_this_on_ROBOT as master

def on_message(client, userdata, message):
    if message.payload.decode('utf-8') == 'up':
        robot.drive_system.stop()

    if message.payload.decode('utf-8') == 'down':
        robot.drive_system.stop()

    if message.payload.decode('utf-8') == 'right':
        robot.drive_system.stop()
        robot.drive_system.right_motor.reset_position()
        robot.drive_system.go(-100, 100)
        while True:
            if robot.drive_system.right_motor.get_position() >= 90 * 4.572 * 1.1 * (355 / 360):
                break

    if message.payload.decode('utf-8') == 'left':
        robot.drive_system.stop()
        robot.drive_system.left_motor.reset_position()
        robot.drive_system.go(100, -100)
        while True:
            if robot.drive_system.right_motor.get_position() >= 90 * 4.572 * 1.1 * (355 / 360):
                break

    if message.payload.decode('utf-8') == 'forward':
        robot.drive_system.stop()
        robot.drive_system.go(30, 30)

    if message.payload.decode('utf-8') == 'backward':
        robot.drive_system.stop()
        robot.drive_system.go(-30, -30)

    if message.payload.decode('utf-8') == 'stop':
        robot.drive_system.stop()

robot = rosebot.RoseBot()

delegate = master.DelegateForRobotCode(robot)

client = mqtt.Client('receiver')

client.on_message = on_message

client.connect("mosquitto.csse.rose-hulman.edu")

time.sleep(1)
while True:
    client.loop_start()

    client.subscribe('minecraft')

    time.sleep(1)

    client.loop_stop()