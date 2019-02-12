"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Daniel Su.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project Winter 2018-2019")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, camera_frame = get_shared_frames(main_frame, mqtt_sender)



    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame,camera_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    beep_frame = shared_gui.beep_frame(main_frame, mqtt_sender)
    camera_frame = camera_test(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame,camera_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame,camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=0, column=1)
    beep_frame.grid(row=1, column=1)
    camera_frame.grid(row=2, column=1)

def camera_test(window, mqtt_sender):
    """ :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient"""

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Color Methods")
    speed_label = ttk.Label(frame, text="Wheel speed (0 to 100)")
    intensity_label = ttk.Label(frame, text="Intensity (1 to 100)")
    color_label = ttk.Label(frame, text='color(either int or str)')

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    intensity_entry = ttk.Entry(frame, width=8)
    intensity_entry.insert(0, "100")
    color_entry = ttk.Entry(frame, width=8)
    color_entry.insert(0,'100')

    straight_less_intensity_button = ttk.Button(frame, text="Until Intensity is less than")
    straight_geater_intensity_button = ttk.Button(frame, text="Until Intensity is greater than")
    straight_color_is_button = ttk.Button(frame, text='Until Color is')
    straight_color_is_not_button = ttk.Button(frame, text='Until color is not')
    less_button = ttk.Button(frame, text="Less Than")
    greater_button = ttk.Button(frame, text="Greater Than")
    color_is_button = ttk.Button(frame, text="Color is")
    color_is_not_button = ttk.Button(frame, text='Color is not')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=0)
    intensity_label.grid(row=1, column=1)
    color_label.grid(row=1, column=2)

    straight_less_intensity_button.grid(row=2, column=0)
    straight_geater_intensity_button.grid(row=2, column=2)
    straight_color_is_button.grid(row=4, column=0)
    straight_color_is_not_button.grid(row=4, column=2)
    less_button.grid(row=3, column=0)
    greater_button.grid(row=3, column=2)
    color_is_button.grid(row=5, column=0)
    color_is_not_button.grid(row=5, column=2)


    # Set the button callbacks:
    straight_color_is_button["command"] = lambda: handle_color_is(
        color_entry, speed_entry, mqtt_sender)
    straight_color_is_not_button["command"] = lambda: handle_color_is_not(
        color_entry, speed_entry, mqtt_sender)
    straight_geater_intensity_button["command"] = lambda: handle_greater_intensity(
        intensity_entry, speed_entry, mqtt_sender)
    straight_less_intensity_button["command"] = lambda: handle_less_intensity(
        intensity_entry, speed_entry, mqtt_sender)

    return frame

def handle_color_is(color_entry, speed_entry, mqtt_sender):
    s = [color_entry.get(), speed_entry.get()]
    mqtt_sender.send_message('color_is', s)

def handle_color_is_not(color_entry, speed_entry, mqtt_sender):
    s = [color_entry.get(), speed_entry.get()]
    mqtt_sender.send_message('color_is_not', s)

def handle_greater_intensity(intensity_entry, speed_entry, mqtt_sender):
    s = [intensity_entry.get(), speed_entry.get()]
    mqtt_sender.send_message('greater_intensity', s)

def handle_less_instensity(intensity_entry, speed_entry, mqtt_sender):
    s = [intensity_entry.get(), speed_entry.get()]
    mqtt_sender.send_message('less_intensity', s)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()



