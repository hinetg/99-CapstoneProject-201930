"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Montgomery Winslow.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Montgomery Winslow")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    spin_left_button = ttk.Button(frame, text='Spin Left')
    spin_left_button.grid()

    spin_left_entry = ttk.Entry(frame)
    spin_left_entry.grid()

    spin_right_button = ttk.Button(frame, text='Spin Right')
    spin_right_button.grid()

    spin_right_entry = ttk.Entry(frame)
    spin_right_entry.grid()

    distance_entry = ttk.Entry(frame)
    distance_entry.grid()

    spin_left_button['command'] = lambda : handle_spin_left
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
def handle_spin_left(spin_left_entry, distance_entry, mqtt_sender):
    print("spin_left")
    speed = int(spin_left_entry.get())
    distance = int(distance_entry.get())
    mqtt_sender.send("spin_left", [speed, distance])

def handle_spin_right(spin_right_entry, distance_entry, mqtt_sender):
    print("spin_left")
    speed = int(spin_right_entry.get())
    distance = int(distance_entry.get())
    mqtt_sender.send("spin_right", [speed, distance])

