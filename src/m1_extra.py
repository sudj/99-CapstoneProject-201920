import time
import rosebot


class Cat(object):
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