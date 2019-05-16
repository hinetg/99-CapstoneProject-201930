"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Triston Hine.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Triston")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    move_until_button = ttk.Button(frame, text="Move Until")
    move_until_button['command'] = lambda: move_until(speed_entry_box, distance_entry_box, mqtt_sender)
    move_until_button.grid()
    distance_entry_box = ttk.Entry(frame, width=8, text="Distance:")
    distance_entry_box.insert(0, "5")
    distance_entry_box.grid()

    forward_button = ttk.Button(frame, text="Forward")
    speed_entry_box = ttk.Entry(frame, width=8)
    speed_entry_box.insert(0, "100")
    forward_button.grid()
    speed_entry_box.grid()
    forward_button['command'] = lambda: move_forward(speed_entry_box, distance_entry_box, mqtt_sender)

    backward_button = ttk.Button(frame, text="Backward")
    speed_entry_box2 = ttk.Entry(frame, width=8)
    speed_entry_box2.insert(0, "100")
    backward_button.grid()
    speed_entry_box2.grid()
    backward_button['command'] = lambda: move_backward(speed_entry_box2,distance_entry_box, mqtt_sender)

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
def move_forward(speed_entry_box, distance_entry_box, mqtt_sender):
    print("Move Forward: ", speed_entry_box.get()), "  Distance: ", distance_entry_box.get()
    speed = int(speed_entry_box.get())
    dist = int(distance_entry_box.get())
    mqtt_sender.send_message("move_forward", [speed, dist])


def move_backward(speed_entry_box2, distance_entry_box, mqtt_sender):
    print("Move Backward: ", speed_entry_box2.get()), "  Distance: ", distance_entry_box.get()
    speed = int(speed_entry_box2.get())
    dist = int(distance_entry_box.get())
    mqtt_sender.send_message("move_backward", [speed, dist])

def move_until(speed_entry_box, distance_entry_box, mqtt_sender):
    print("Move Until: ", distance_entry_box, " Inches, ", speed_entry_box)
    speed = int(speed_entry_box.get())
    dist = int(distance_entry_box.get())
    mqtt_sender.send_message("move_until", [speed, dist])