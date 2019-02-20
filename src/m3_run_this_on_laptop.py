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


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


class m3_GUI(object):
    def __init__(self):
        self.mqtt_sender = com.MqttClient()
        self.mqtt_sender.connect_to_ev3()
        # Declaring variables
        self.time_initial = time.time()
        self.energy=100
        self.speed=0

        self.root = tkinter.Tk()
        self.root.title('CSSE120 Capstone Project')

        self.main_frame = ttk.Frame(self.root, padding=10, borderwidth=5, relief='groove')
        self.main_frame.grid()

        # Creates the title frame
        self.title_frame=ttk.Frame(self.main_frame, padding=10, borderwidth=5, relief="ridge")
        title_label = tkinter.Label(self.title_frame, text='ROBO-KART', font=("Cooper Black", 33), fg='goldenrod')
        title_label.grid()

        self.create_play_frame()

        # Grids title and play frame onto the main frame
        self.title_frame.grid(row=0, column=0)
        self.play_frame.grid(row=1, column=0)

        self.root.bind('<Up>', self.upKey)
        self.root.bind('<Down>', self.downKey)
        self.root.bind('<w>', self.forward)
        self.root.bind('<s>', self.backward)
        self.root.bind('<a>', self.left)
        self.root.bind('<d>', self.right)
        self.root.bind('<space>', self.stop)

    def create_play_frame(self):
        self.play_frame = ttk.Frame(self.main_frame, padding=10, borderwidth=5, relief="ridge")
        self.play_frame.grid()

        speed_label = ttk.Label(self.play_frame, text='Speed:', font=("Times New Roman", 15), padding=30)
        scale = tkinter.Scale(self.play_frame, orient='horizontal', from_=0, to=100, command=self.print_value)
        energy_label = tkinter.Label(self.play_frame, text='Energy Remaing:', font=("Times New Roman", 15))
        energy = ttk.Label(self.play_frame, text='100%', font=("Times New Roman", 15), padding=30)
        time_label = ttk.Label(self.play_frame, text='Time elapsed: ', font=("Times New Roman", 15), padding=30)
        time = ttk.Label(self.play_frame, text='0', font=("Times New Roman", 15), padding=30)

        speed_label.grid(row=0, column=0)
        scale.grid(row=0, column=1)
        energy_label.grid(row=1, column=0)
        energy.grid(row=1, column=1)
        time_label.grid(row=3, column=0)
        time.grid(row=3, column=1)

    def print_value(self, val):
        self.speed = int(val)
        print('speed:', val)

    def upKey(self, event):
        print('Up', self.speed)
        self.speed = int(self.speed) + 1
        if self.speed > 100:
            self.speed = 100
        self.play_frame.children['!scale'].set(self.speed)

    def downKey(self, event):
        print('Down')
        self.speed = int(self.speed) - 1
        if self.speed < 0:
            self.speed = 0
        self.play_frame.children['!scale'].set(self.speed)

    def forward(self, event):
        print('forward')
        self.mqtt_sender.send_message('forward', [int(self.speed), int(self.speed)])
        self.adjust_energy()

    def backward(self, event):
        print('backward')
        self.adjust_energy()

    def left(self, event):
        print('left')
        self.adjust_energy()
        self.mqtt_sender.send_message('forward', [int(self.speed)/2, int(self.speed)])

    def right(self, event):
        print('right')
        self.adjust_energy()

    def stop(self, event):
        print('stop', 'beep')
        self.mqtt_sender.send_message('forward', [0,0])

    def adjust_energy(self):
        self.energy =self.energy-(.001*int(self.speed))
        if self.energy<=0:
            self.energy=0
        self.play_frame.children['!label3'].config(text=str(int(self.energy))+'%')

    def adjust_time(self):
        self.play_frame.children['!label5'].config(text=str(int(time.time() - self.time_initial)))
        self.root.after(1000, lambda: self.adjust_time())

    def open(self):
        self.root.after(1000, lambda: self.adjust_time())
        self.root.mainloop()

GUI = m3_GUI()
GUI.open()