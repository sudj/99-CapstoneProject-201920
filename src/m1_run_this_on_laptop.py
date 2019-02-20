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
import time
from tkinter import messagebox


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
    delagate = Delegate_on_laptop()
    mqtt_receiver = com.MqttClient(delagate)
    mqtt_receiver.connect_to_ev3()


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
    intro_frame, function_frame = get_shared_frames(main_frame, mqtt_sender)



    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(intro_frame, function_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    intro_frame = title_screen(main_frame, mqtt_sender)
    function_frame = function_window(main_frame, mqtt_sender)

    return intro_frame, function_frame


def grid_frames(intro_frame, function_frame):
    intro_frame.grid(row=0, column=0)
    function_frame.grid(row=1, column=0)

def function_window(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=1)
    frame.grid()

    eat_lable = ttk.Label(frame, text='Eating (Happiness)', font=('Arial Bold', 10))
    eat_entry = ttk.Entry(frame, width=8)
    eat_button = ttk.Button(frame, text='Start')
    eat_progress = ttk.Progressbar(frame, orient='horizontal', length=287, mode='determinate')

    eat_lable.grid(row=2, column=0)
    eat_entry.grid(row=2, column=1)
    eat_button.grid(row=2, column=2)
    eat_progress.grid(row=3, column=0, pady=10)

    eat_button['command'] = lambda: handle_eat(mqtt_sender, eat_entry, eat_progress)




    play_lable = ttk.Label(frame, text='Play with Yarn (Happiness)', font=('Arial Bold', 10))
    play_entry = ttk.Entry(frame, width=8)
    play_button = ttk.Button(frame, text='Start')
    play_progress = ttk.Progressbar(frame, orient='horizontal', length=287, mode='determinate')


    play_lable.grid(row=0, column=0)
    play_entry.grid(row=0, column=1)
    play_button.grid(row=0, column=2)
    play_progress.grid(row=1, column=0, pady=10)

    play_button['command'] = lambda: handle_play(mqtt_sender, play_entry, play_progress)



    sleep_button = ttk.Button(frame, text='Go to Sleep')

    sleep_button.grid(row=4, column=0)

    sleep_button['command'] = lambda: handle_sleep(mqtt_sender, play_progress, eat_progress)

    return frame

def title_screen(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=1, relief='ridge')
    frame.grid()

    intro_button = ttk.Button(frame, text='Intro')
    title_lable = ttk.Label(frame, text='Cat Remote', font=('Arial Bold', 50))

    title_lable.grid(row=0, column=1)
    intro_button.grid(row=2, column=0)

    intro_button['command'] = lambda: handle_intro()

    return frame

def handle_intro():
    messagebox.showinfo('Introduction', 'Congratulations on getting your very own cat-robot. This robot wcan act like a cat and has several functions it can perform. You can feed it pla with it and then finally put it to sleep')

def handle_play(mqtt_sender, play_entry, play_progress):
    mqtt_sender.send_message('m1_play', [play_entry.get()])
    play_progress['maximum'] = 100
    a = 0
    b = int(play_entry.get())
    for k in range(a, b):
        time.sleep(0.05)
        play_progress['value'] = k
        play_progress.update()

def handle_eat(mqtt_sender, eat_entry, eat_progress):
    mqtt_sender.send_message('m1_eat')
    eat_progress['maximum'] = 100
    a = 0
    b = int(eat_entry.get())
    for k in range(a, b):
        time.sleep(0.05)
        eat_progress['value'] = k
        eat_progress.update()

def handle_sleep(mqtt_sender, play_progress, eat_progress):
    if (play_progress['value'] and eat_progress['value']) >= 99:
        mqtt_sender.send_message('m1_nap')
        time.sleep(3)
        play_progress['value'] = 0
        play_progress.update()
        time.sleep(0.05)
        eat_progress['value'] = 0
        eat_progress.update()
        messagebox.showinfo('Good Morning', 'Robo-Cat just woke up and it looks like it is ready to start its day')


    else:
        mqtt_sender.send_message('m1_cry')
        messagebox.showinfo('Error', 'You need to play or feed your cat!')








def m1_play(self, play_entry):
    self.cat.play_till(int(play_entry.get()))

def m1_cry(self):
    self.cat.cry()

def m1_nap(self):
    self.cet.nap()

class Delegate_on_laptop(object):
    def eating_time(self):
        print('This food looks yummy!')






# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()



