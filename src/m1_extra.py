import time
import rosebot
import mqtt_remote_method_calls as com

class Cat(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot

    def play_till(self, play_entry):
        for k in range(play_entry // 32):
            self.robot.drive_system.spin_counterclockwise_until_sees_object(60, 150)
            self.robot.drive_system.go(40, -40)
            time.sleep(1.5)
            self.robot.drive_system.stop()
            inch = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            time.sleep(1)
            print('distance is', inch)
            self.robot.drive_system.go_straight_for_inches_using_encoder((inch - 1), 50)
            time.sleep(1)
            self.robot.arm_and_claw.raise_arm()
            time.sleep(0.5)
            self.robot.sound_system.speech_maker.speak('My Ball! Meow')
            for j in range(3):
                self.robot.drive_system.go(-50, 50)
                time.sleep(1)
                self.robot.drive_system.go(50, -50)
                time.sleep(1)
                self.robot.drive_system.stop()
            time.sleep(5)
            self.robot.arm_and_claw.lower_arm()
            self.robot.sound_system.speech_maker.speak('Ok you can throw to ball now')
            time.sleep(10)

    def nap(self):
        self.robot.sound_system.speech_maker.speak('Time to sleep')


    def cry(self):
        for k in range(5):
            self.robot.sound_system.speech_maker.speak('meow').wait()

    def eat(self):
        self.robot.drive_system.go(100, 80)
        while True:
            if self.robot.sensor_system.color_sensor.get_color_as_name() is 'Blue':
                break
        self.robot.drive_system.stop()
        self.robot.sound_system.speech_maker.speak('yum yum yum')







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