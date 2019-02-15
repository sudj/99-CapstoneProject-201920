"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Christina Rogers.
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
    root.title('CSSE120 Capstone Project')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth = 5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, ir_frame, camera = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, ir_frame, camera)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    beep_frame = shared_gui.beep_frame(main_frame,mqtt_sender)
    ir = ir_frame(main_frame,mqtt_sender)
    camera = camera_frame(main_frame,mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, ir, camera


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, ir, camera):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=0, column=1)
    beep_frame.grid(row=1, column=1)
    ir.grid(row=3,column=0)
    camera.grid(row=2, column=1)

# Extra Frames
def ir_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='IR System')
    IR_mode_button = ttk.Button(frame, text='IR Mode')
    IR_entry = ttk.Entry(frame, width=20)
    IR_label = ttk.Label(frame, text='Distance to stop before object:')
    IR_grab = ttk.Button(frame, text='Use proximity to grab object')
    factor = ttk.Entry(frame, width=20)
    factor_label = ttk.Label(frame, text='Factor tone increases by')

    IR_mode_button['command'] = lambda: handle_send_ir_sensor(mqtt_sender,IR_entry)
    IR_grab['command'] = lambda: handle_send_grab(mqtt_sender,factor)

    factor_label.grid(row=5, column=0)
    factor.grid(row=5,column=1)
    frame_label.grid(row=0, column=0)
    IR_mode_button.grid(row=2, column=0)
    IR_entry.grid(row=1, column=1)
    IR_label.grid(row=1, column=0)
    IR_grab.grid(row=4, column=0)


    return frame


def camera_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    title = ttk.Label(frame, text='Camera system')
    info_button = ttk.Button(frame, text='Get info')
    speed_label = ttk.Label(frame, text='Speed: ')
    speed_entry = ttk.Entry(frame, width=8)
    area_label = ttk.Label(frame, text='Area: ')
    area_entry = ttk.Entry(frame, width=8)
    which = ttk.Label(frame, text='Direction:')
    clock = ttk.Button(frame, text='Clockwise')
    counter = ttk.Button(frame, text='Counter Clockwise')


    title.grid(row=0, column=1)
    info_button.grid(row=1, column=1)
    speed_label.grid(row=2, column=0)
    speed_entry.grid(row=2, column=1)
    area_label.grid(row=3, column=0)
    area_entry.grid(row=3, column=1)
    which.grid(row=4, column=0)
    clock.grid(row=4, column=1)
    counter.grid(row=4, column=2)

    info_button['command'] = lambda: handle_camera(mqtt_sender)
    clock['command'] = lambda : handle_clockwise(mqtt_sender, speed_entry, area_entry)
    counter['command'] = lambda : handle_counter(mqtt_sender, speed_entry, area_entry)

    return frame




def handle_circle_counter(mqtt_sender):
    mqtt_sender.send_message('counter')

def handle_circle_clockwise(mqtt_sender):
    mqtt_sender.send_message('clockwise')

def handle_send_ir_sensor(mqtt_sender,IR_entry):
    mqtt_sender.send_message('ir_test',[IR_entry.get()])

def handle_send_grab(mqtt_sender,factor):
    mqtt_sender.send_message('pick_up_with_prox',[factor.get()])

def handle_counter(mqtt_sender, speed_entry, area_entry):
    mqtt_sender.send_message('camera_counter_clockwise', [int(speed_entry.get()), int(area_entry.get())])

def handle_clockwise(mqtt_sender, speed_entry, area_entry):
    mqtt_sender.send_message('camera_clockwise', [int(speed_entry.get()), int(area_entry.get())])

def handle_camera(mqtt_sender):
    mqtt_sender.send_message('camera')
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()