import time
import rosebot


class Cat(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot

    def intro(self):
        print('Congradulations on getting your very own cat-robot. This robot wcan act like a cat and has several functions it can perform. You can feed it pla with it and then finally put it to sleep' )


    def play_till(self, play_entry):
        for k in range(play_entry):
            self.robot.drive_system.spin_counterclockwise_until_beacon_heading_is_nonpositive(80)
            inch = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            self.robot.drive_system.go_straight_for_inches_using_encoder(inch, 50)




class Grab(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot

    def beep_grab(self):
        # starting_distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        self.robot.drive_system.go(20, 20)
        if self.robot.sensor_system.ir_proximity_sensor.get_distance() > 0:
            while True:
                distance_away = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
                if distance_away <= 1:
                    self.robot.drive_system.stop()
                    break
                if distance_away > 0:
                    self.robot.sound_system.beeper.beep()
                    time.sleep(abs(distance_away / 20))
            self.robot.arm_and_claw.raise_arm()









###gui delegate