"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Montgomery Winslow.
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

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()

    # TODO: Add methods here as needed.

    def spin_left(self, speed, distance):
        print('spin left')
        distance = distance * 4.572
        self.robot.drive_system.right_motor.turn_on()
        self.robot.drive_system.left_motor.turn_on()
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.go(speed, -1 * speed)
        while True:
            if self.robot.drive_system.right_motor.get_position() >= distance:
                break
        self.robot.drive_system.right_motor.turn_off()
        self.robot.drive_system.left_motor.turn_off()


    def spin_right(self, speed, distance):
        print('spin right')
        distance = distance * 4.572
        self.robot.drive_system.right_motor.turn_on()
        self.robot.drive_system.left_motor.turn_on()
        self.robot.drive_system.right_motor.reset_position()
        self.robot.drive_system.go(-1 * speed, speed)
        while True:
            if self.robot.drive_system.right_motor.get_position() >= distance:
                break
        self.robot.drive_system.right_motor.turn_off()
        self.robot.drive_system.left_motor.turn_off()

def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

