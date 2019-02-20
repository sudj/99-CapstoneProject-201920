import time
import rosebot

def led(initial_rate, rate_of_increase, robot):
    robot.drive_system.go(50, 50)
    robot.drive_system.left_motor.reset_position()
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    initial_time = time.time()
    rate = initial_rate
    delta = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / (
                (robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - 0.01) / rate_of_increase)
    while True:
        if robot.drive_system.left_motor.get_position() - initial_distance >= delta:
            if time.time() - initial_time >= rate:
                initial_distance = robot.drive_system.left_motor.get_position()
                initial_time, rate = led_rotation(rate, rate_of_increase, robot)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

def led_rotation(rate, rate_of_increase,robot):
    robot.led_system.left_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()  # the time from last beep is reset:
    return time.time(), rate - rate_of_increase