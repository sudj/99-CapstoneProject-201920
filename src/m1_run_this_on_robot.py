"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Daniel Su.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    robot = rosebot.RoseBot()
    test_drive(robot)
    real_thing(robot)





def real_thing(robot):
    delagate_receiver = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delagate_receiver)
    mqtt_receiver.connect_to_pc()


    while True:
        time.sleep(0.01)
        if delagate_receiver.is_quit:
            break

def test_drive(robot):
    robot.drive_system.go(100, -100)
    time.sleep(10)
    print('Go method finished')
    robot.drive_system.stop()
    print('stop method finished')
    robot.drive_system.go_straight_for_seconds(3, 100)
    time.sleep(10)
    print('go straight for seconds method finished')
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_time(3, 50)
    time.sleep(10)
    print('go straight for inches using time finished')
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(10, 100)
    print('go straight for inches using encoder finished')




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()