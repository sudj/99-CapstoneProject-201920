import time
import rosebot

def led(rate_of_increase, initial, robot):
    print (rate_of_increase, initial)
    robot.drive_system.go(35, 35)
    d=initial
    while robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= 1:
        time.sleep(0.1)
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        robot.led_system.left_led.turn_on()
        time.sleep(d)
        robot.led_system.left_led.turn_off()
        time.sleep(d)
        robot.led_system.right_led.turn_on()
        time.sleep(d)
        robot.led_system.right_led.turn_off()
        time.sleep(d)
        robot.led_system.left_led.turn_on()
        time.sleep(d)
        robot.led_system.right_led.turn_on()
        time.sleep(d)
        robot.led_system.left_led.turn_off()
        time.sleep(d)
        robot.led_system.right_led.turn_off()
        time.sleep(d)
        d =d - rate
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()