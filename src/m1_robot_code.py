"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Triston Hine.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # TODO: Add methods here as needed.
    def move_forward(self, speed, dist):
        avg = 0
        distance = dist
        distanceMes = setDistance()
        while distanceMes > distance:
            self.go(speed, speed)
            avg = takeAvg()
            distanceMes = avg
        self.robot.drive_system.stop()

    def move_backward(self, speed, dist):
        avg = 0
        distance = dist
        distanceMes = setDistance()
        while distanceMes < distance:
            self.go(-speed, -speed)
            avg = takeAvg()
            distanceMes = avg
        self.robot.drive_system.stop()


def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

def setDistance():
    distance = rosebot.InfraredProximitySensor(4)
    numinches = distance.get_distance_in_inches()
    return numinches

def takeAvg():
    smallest = 100
    biggest = 0
    avg = 0
    read1 = setDistance()
    read2 = setDistance()
    read3 = setDistance()
    read4 = setDistance()
    read5 = setDistance()
    if smallest > read1:
        smallest = read1
    if smallest > read2:
        smallest = read2
    if smallest > read3:
        smallest = read3
    if smallest > read4:
        smallest = read4
    if smallest > read5:
        smallest = read5
    if biggest < read1:
        biggest = read1
    if biggest < read2:
        biggest = read2
    if biggest < read2:
        biggest = read2
    if biggest < read2:
        biggest = read2
    if biggest < read2:
        biggest = read2
    avg = (read1+read2+read3+read4+read5-smallest-biggest)/3
    return avg
