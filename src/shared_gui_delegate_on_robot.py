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

    def forward(self, leftSpeed, rightSpeed):
        self.robot.drive_system.go(int(leftSpeed), int(rightSpeed))

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm(self, position):
        print('y')
        # self.robot.arm_and_claw.move_arm_to_position(position)
        print(position)