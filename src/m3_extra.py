import time
import rosebot

def led(rate_of_increase, initial, robot):
    print (rate_of_increase, initial)
    robot.drive_system.go(50, 50)
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    rate=initial
    while True:
        led_rotation(rate, robot)
        distance_traveled = initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if distance_traveled > 1:
            rate = rate - distance_traveled/initial_distance * rate_of_increase
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


def led_rotation(rate, robot):
    robot.led_system.left_led.turn_on()
    time.sleep(rate)
    robot.led_system.left_led.turn_off()
    time.sleep(rate)
    robot.led_system.right_led.turn_on()
    time.sleep(rate)
    robot.led_system.right_led.turn_off()
    time.sleep(rate)
    robot.led_system.left_led.turn_on()
    time.sleep(rate)
    robot.led_system.right_led.turn_on()
    time.sleep(rate)
    robot.led_system.left_led.turn_off()
    time.sleep(rate)
    robot.led_system.right_led.turn_off()
    time.sleep(rate)