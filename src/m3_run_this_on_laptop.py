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
import time


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
    teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, camera_frame, led_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, camera_frame, led_frame)

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
    camera_frame = shared_gui.camera_frame(main_frame, mqtt_sender)
    led_frame = shared_gui.led_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, camera_frame, led_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, beep_frame, camera_frame, led_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=0, column=1)
    beep_frame.grid(row=1, column=1)
    camera_frame.grid(row=2, column=1)
    led_frame.grid(row=0, column=2)


# def led(rate_of_increase, initial, robot):
#     print (rate_of_increase, initial)
#     robot.drive_system.go(25, 25)
#     initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
#     rate=initial
#     while True:
#         led_rotation(rate, robot)
#         distance_traveled = initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
#         # if distance_traveled > 1:
#         #     rate = rate - distance_traveled/initial_distance * rate_of_increase
#         print('distance')
#         if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2.0:
#             robot.drive_system.stop()
#             print('stop')
#             robot.arm_and_claw.raise_arm()
#             break

def led_rotation(rate, robot):
    robot.led_system.left_led.turn_on()
    time.sleep(rate)
    robot.led_system.left_led.turn_off()
    time.sleep(rate)
    robot.led_system.right_led.turn_on()
    time.sleep(rate)
    robot.led_system.right_led.turn_off()
    time.sleep(rate)
    robot.led_system.left_led.turn_on()
    time.sleep(rate)
    robot.led_system.right_led.turn_on()
    time.sleep(rate)
    robot.led_system.left_led.turn_off()
    time.sleep(rate)
    robot.led_system.right_led.turn_off()
    time.sleep(rate)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()