"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Daniel Su, Jason Ims, Christina Rogers.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    position_entry.insert(0, "0")
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drive_system_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Drive System')
    left_speed_label = ttk.Label(frame, text='Left speed:')
    right_speed_label = ttk.Label(frame, text='Right speed:')
    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8)
    right_speed_entry.insert(0, "100")
    go_button = ttk.Button(frame, text='Go')
    stop_button = ttk.Button(frame, text='Stop')
    seconds_label = ttk.Label(frame, text='Seconds:')
    seconds_entry = ttk.Entry(frame, width=10)
    seconds_entry.insert(0, "0")
    inches_label = ttk.Label(frame, text='Inches:')
    inches_entry = ttk.Entry(frame, width=10)
    inches_entry.insert(0, "0")
    seconds_button = ttk.Button(frame, text='Seconds')
    inches_using_time = ttk.Button(frame, text='Inches-- time')
    inches_using_encoder = ttk.Button(frame, text='Inches-- encoder')

    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)
    go_button.grid(row=3, column=0)
    stop_button.grid(row=3, column=2)
    seconds_label.grid(row=4, column=0)
    seconds_entry.grid(row=4, column=1)
    inches_label.grid(row=5, column=0)
    inches_entry.grid(row=5, column=1)
    seconds_button.grid(row=6, column=0)
    inches_using_time.grid(row=6, column=1)
    inches_using_encoder.grid(row=6, column=2)

    go_button["command"] = lambda: go(mqtt_sender, left_speed_entry, right_speed_entry)
    stop_button["command"] = lambda: stop(mqtt_sender)
    seconds_button["command"] = lambda: go_seconds(mqtt_sender, left_speed_entry, right_speed_entry, seconds_entry)
    inches_using_time["command"] = lambda: go_inches_time(mqtt_sender, left_speed_entry, right_speed_entry,
                                                          inches_entry)
    inches_using_encoder["command"] = lambda: go_inches_encoder(mqtt_sender, left_speed_entry, right_speed_entry,
                                                                inches_entry)

    return frame


def beep_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Beep System')
    beep_number_label = ttk.Label(frame, text='Number of beeps:')
    beep_number_entry = ttk.Entry(frame, width=8)
    beep_button = ttk.Button(frame, text='Beep')
    tone_duration_label = ttk.Label(frame, text='Duration of Tone:')
    tone_duration_entry = ttk.Entry(frame, width=8)
    tone_frequency_label = ttk.Label(frame, text='Frequency of tone:')
    tone_frequency_entry = ttk.Entry(frame, width=8)
    tone_button = ttk.Button(frame, text='Tone')
    phrase_entry = ttk.Entry(frame, width=8)
    phrase_label = ttk.Label(frame, text='Enter the phrase here:')
    phrase_buttton = ttk.Button(frame, text='Speak the phrase')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    beep_number_label.grid(row=1, column=0)
    beep_number_entry.grid(row=1, column=1)
    beep_button.grid(row=2, column=0)
    tone_duration_label.grid(row=3, column=0)
    tone_duration_entry.grid(row=3, column=1)
    tone_frequency_label.grid(row=4, column=0)
    tone_frequency_entry.grid(row=4, column=1)
    tone_button.grid(row=5, column=0)
    phrase_label.grid(row=6, column=0)
    phrase_entry.grid(row=6, column=1)
    phrase_buttton.grid(row=7, column=0)

    beep_button["command"] = lambda: beep(mqtt_sender, beep_number_entry)
    tone_button['command'] = lambda: tone(mqtt_sender, tone_duration_entry, tone_frequency_entry)
    phrase_buttton['command'] = lambda: phrase(mqtt_sender, phrase_entry)

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    s = [int(left_entry_box.get()), int(right_entry_box.get())]
    mqtt_sender.send_message('forward', s)


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    s = [-int(left_entry_box.get()), -int(right_entry_box.get())]
    mqtt_sender.send_message('forward', s)


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    s = [int(left_entry_box.get()), -int(right_entry_box.get())]
    mqtt_sender.send_message('forward', s)


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    s = [-int(left_entry_box.get()), int(right_entry_box.get())]
    mqtt_sender.send_message('forward', s)


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    mqtt_sender.send_message('forward', [0, 0])


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    mqtt_sender.send_message("raise_arm")


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    mqtt_sender.send_message('move_arm',[int(arm_position_entry.get())])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """


###############################################################################
# Handlers for Buttons in the Drive System frame.
###############################################################################
def go(mqtt_sender, left_speed_entry, right_speed_entry):
    """
        :type  left_speed_entry  ttk.Entry
        :type  right_speed_entry  ttk.Entry
        :type  mqtt_sender:        com.MqttClient
      """
    print('go', int(left_speed_entry.get()), int(right_speed_entry.get()))
    mqtt_sender.send_message('forward', [int(left_speed_entry.get()), int(right_speed_entry.get())])


def stop(mqtt_sender):
    mqtt_sender.send_message('forward', [0, 0])


def go_seconds(mqtt_sender, left_speed_entry, right_speed_entry, seconds_entry):
    mqtt_sender.send_message('go_seconds', [int(left_speed_entry.get()), int(seconds_entry.get())])


def go_inches_time(mqtt_sender, left_speed_entry, right_speed_entry, inches_entry):
    mqtt_sender.send_message('go_inches_time', [int(left_speed_entry.get()), int(inches_entry.get())])


def go_inches_encoder(mqtt_sender, left_speed_entry, right_speed_entry, inches_entry):
    mqtt_sender.send_message('go_inches_encoder', [int(left_speed_entry.get()), int(inches_entry.get())])

###############################################################################
# Handlers for Buttons in the Beep frame.
###############################################################################
def beep(mqtt_sender, number_beep_entry):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    mqtt_sender('beep', [int(number_beep_entry.get())])


def tone(mqtt_sender, duration_entry, frequency_entry):
    mqtt_sender('tone', [int(duration_entry.get()), int(frequency_entry.get())])

def phrase(mqtt_sender, phrase_entry):
    mqtt_sender('phrase', [str(phrase_entry.get())])