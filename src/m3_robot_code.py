"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Emily Millard.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


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
        self.robot.sensor_system.color_sensor.get_color()

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # DONE: Add methods here as needed.
    def arm_up(self, speed):
        """ Moves the arm all the way to its touch sensor """
        print(speed)
        self.robot.arm_and_claw.motor.turn_on(speed)
        while True:
            if self.robot.arm_and_claw.touch_sensor.is_pressed():
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_calibrate(self, speed):
        self.arm_up(speed)
        self.robot.arm_and_claw.motor.reset_position()
        self.robot.arm_and_claw.motor.turn_on(-speed)
        while True:
            print(self.robot.arm_and_claw.motor.get_position())
            if self.robot.arm_and_claw.motor.get_position() <= -14.2 * 360:
                self.robot.arm_and_claw.motor.reset_position()
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_to(self, speed, location):
        """ Moves the arm to the position given """
        current_position = self.robot.arm_and_claw.motor.get_position()
        print_message_received("arm_to", current_position)
        move = location - current_position
        if move > 0:
            self.robot.arm_and_claw.motor.turn_on(speed)
            while True:
                if self.robot.arm_and_claw.motor.get_position() >= location:
                    self.robot.arm_and_claw.motor.turn_off()
                    break
        elif move < 0:
            self.robot.arm_and_claw.motor.turn_on(-speed)
            while True:
                if self.robot.arm_and_claw.motor.get_position() <= location:
                    self.robot.arm_and_claw.motor.turn_off()
                    break

    def arm_down(self, speed):
        """ Moves the arm all the way to position zero """
        self.arm_to(speed, 0)

    def forward_to_color(self, speed, color):
        color_number = self.robot.sensor_system.color_sensor.get_color_number_from_color_name(color)
        print(color_number, color)
        while True:
            self.robot.drive_system.go(speed, speed)
            if self.robot.drive_system.sensor_system.color_sensor.get_color() == color_number:
                self.robot.drive_system.stop()
                break


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# DONE: Add functions here as needed.

