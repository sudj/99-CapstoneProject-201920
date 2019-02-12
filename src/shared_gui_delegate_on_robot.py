"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Christina Rogers, Jason Ims, Dan Su.
  Winter term, 2018-2019.
"""

class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot
        self.quit = False

    def forward(self, leftSpeed, rightSpeed):
        self.robot.drive_system.go(int(leftSpeed), int(rightSpeed))

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm(self, position):
        self.robot.arm_and_claw.move_arm_to_position(position)
        print(position)

    def go_seconds(self, speed, seconds):
        self.robot.drive_system.go_straight_for_seconds(seconds, speed)

    def go_inches_encoder(self, speed, inches):
        print('start')
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, speed)
        print('end')

    def go_inches_time(self, speed, inches):
        print('start')
        self.robot.drive_system.go_straight_for_inches_using_time(inches, speed)
        print('end')

    def beep(self, times):
        print('I will beep', times, 'times')
        for k in range(times):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, duration, frequency):
        print('I will play a tone at Frequency', frequency, 'for duration', duration)
        self.robot.sound_system.tone_maker.play_tone(frequency, duration*1000)

    def phrase(self, phrase):
        print('I will speak the phrase', phrase)
        self.robot.sound_system.speech_maker.speak(phrase)

    def is_quit(self):
        self.quit = True


    def ir_sensor(self,distance):
        print(self.robot.sensor_system.ir_proximity_sensor.get_distance())
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < distance:
            self.robot.drive_system.go_straight_for_seconds(0, 0)

