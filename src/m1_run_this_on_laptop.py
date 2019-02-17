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
    intro_frame, play_frame, eat_frame, sleep_frame = get_shared_frames(main_frame, mqtt_sender)



    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(intro_frame, play_frame, eat_frame, sleep_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    intro_frame = title_screen(main_frame, mqtt_sender)
    play_frame = play_window(main_frame, mqtt_sender)
    eat_frame = eat_window(main_frame, mqtt_sender)
    sleep_frame =  sleep_window(main_frame, mqtt_sender)

    return intro_frame, play_frame, eat_frame, sleep_frame


def grid_frames(intro_frame, play_frame, eat_frame, sleep_frame):
    intro_frame.grid(row=0, column=0)
    play_frame.grid(row=1, column=0)
    eat_frame.grid(row=2, column=0)
    sleep_frame.grid(row=3, column=0)

def sleep_window(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=1)
    frame.grid()

    sleep_button = ttk.Button(frame, text='Go to Sleep')

    sleep_button.grid(row=0, column=0)

    return frame

def eat_window(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=1)
    frame.grid()

    eat_lable = ttk.Label(frame, text='Eating (time)', font=('Arial Bold', 10))
    eat_entry = ttk.Entry(frame, width=8)
    eat_button = ttk.Button(frame, text='Start')
    eat_progress = ttk.Progressbar(frame, orient='horizontal', length=287, mode='determinate')

    eat_lable.grid(row=0, column=0)
    eat_entry.grid(row=0, column=1)
    eat_button.grid(row=0, column=2)
    eat_progress.grid(row=1, column=0, pady=10)

    return frame

def play_window(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=1)
    frame.grid()

    play_lable = ttk.Label(frame, text='Play with Yarn (time)', font=('Arial Bold', 10))
    play_entry = ttk.Entry(frame, width=8)
    play_button = ttk.Button(frame, text='Start')
    play_progress = ttk.Progressbar(frame, orient='horizontal', length=287, mode='determinate')

    play_lable.grid(row=0, column=0)
    play_entry.grid(row=0, column=1)
    play_button.grid(row=0, column=2)
    play_progress.grid(row=1, column=0, pady=10)

    play_button['command'] = lambda: handle_play(mqtt_sender, play_entry)

    return frame

def title_screen(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=1, relief='ridge')
    frame.grid()

    intro_button = ttk.Button(frame, text='Intro')
    title_lable = ttk.Label(frame, text='Cat Remote', font=('Arial Bold', 50))

    title_lable.grid(row=0, column=1)
    intro_button.grid(row=2, column=0)

    # intro_button['command'] = lambda: handle_intro(mqtt_sender)

    return frame

def handle_intro(mqtt_sender):
    mqtt_sender.send_message('m1_intro')

def handle_play(mqtt_sender, play_entry):
    mqtt_sender.send_message('m1_play', [play_entry.get()])







def m1_intro(self):
    self.cat.intro()

def m1_play(self, play_entry):
    self.cat.play_till(int(play_entry))




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()



