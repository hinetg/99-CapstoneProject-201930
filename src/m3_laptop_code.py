"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Emily Millard.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Emily Millard")
    frame_label.grid()
    speed_label = ttk.Label(frame, text="Speed")
    speed_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    speed_entry_box = ttk.Entry(frame, width=8)
    speed_entry_box.insert(0, "100")
    arm_calibrate_button = ttk.Button(frame, text="Calibrate Arm")

    location_label = ttk.Label(frame, text="New Arm Location")
    arm_location_entry_box = ttk.Entry(frame, width=8)
    arm_location_entry_box.insert(0, "5")

    arm_to_button = ttk.Button(frame, text="Arm to Location")
    arm_up_button = ttk.Button(frame, text="Arm Up")
    arm_down_button = ttk.Button(frame, text="Arm Down")

    color_label = ttk.Label(frame, text="Color to Stop")
    stop_color_entry_box = ttk.Entry(frame, width=8)
    stop_color_entry_box.insert(0, "Red")
    forward_until_color_button = ttk.Button(frame, text="Forward Until Color")

    speed_entry_box.grid()
    arm_calibrate_button.grid()
    arm_calibrate_button['command'] = lambda: arm_calibration(speed_entry_box, mqtt_sender)
    location_label.grid()
    arm_location_entry_box.grid()
    arm_to_button.grid()
    arm_to_button['command'] = lambda: arm_to(speed_entry_box, arm_location_entry_box, mqtt_sender)
    arm_up_button.grid()
    arm_up_button['command'] = lambda: handle_arm_up(speed_entry_box, mqtt_sender)
    arm_down_button.grid()
    arm_down_button['command'] = lambda: handle_arm_down(speed_entry_box, mqtt_sender)
    color_label.grid()
    stop_color_entry_box.grid()
    forward_until_color_button.grid()
    forward_until_color_button['command'] = lambda: \
        forward_until_color(speed_entry_box, stop_color_entry_box, mqtt_sender)
    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
def handle_arm_up(speed_entry_box, mqtt_sender):
    print("handle arm up:", speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("arm_up", [speed])


def handle_arm_down(speed_entry_box, mqtt_sender):
    print("handle arm down:", speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("arm_down", [speed])


def arm_calibration(speed_entry_box, mqtt_sender):
    print("Calibrating")
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message("arm_calibrate", [speed])


def arm_to(speed_entry_box, arm_location_entry_box, mqtt_sender):
    print("moving arm to:", arm_location_entry_box.get())
    speed = int(speed_entry_box.get())
    location = int(arm_location_entry_box.get())
    mqtt_sender.send_message("arm_to", [speed, location])


def forward_until_color(speed_entry_box, stop_color_entry_box, mqtt_sender):
    print("forward until detection of color:", stop_color_entry_box.get())
    speed = int(speed_entry_box.get())
    color = str(stop_color_entry_box.get())
    mqtt_sender.send_message("forward_to_color", [speed, color])
