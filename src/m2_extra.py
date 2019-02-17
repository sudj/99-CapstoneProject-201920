import time
import rosebot

def pick_up_water(self):
    print('Test')
    while True:
        self.robot.drive_system.go(50, 50)
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.9:
            self.robot.drive_system.go_straight_for_seconds(0, 0)
            self.robot.arm_and_claw.raise_arm()
            break

def alarm_sound(self):
    for k in range (5):
        self.robot.sound_system.tone_maker.play_tone(400, 1000)
        self.robot.sound_system.tone_maker.play_tone(1400, 1000)

def find_fire(self):
    self.robot.drive_system.go(50,-50)
    time.sleep(.2)
    self.robot.drive_system.go(0,0)
    self.robot.drive_system.go_straight_until_color_is('red',50)

def put_fire_out(self):
    self.robot.arm_and_claw.calibrate_arm()