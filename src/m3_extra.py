import time
import rosebot

def led(initial_rate, rate_of_increase, robot):
    # print (rate, intial_d)
    # robot.drive_system.go(35, 35)
    # case = 0
    # initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    # d=initial_distance
    # while True:
    #     time.sleep(d)
    #     led_rotation(case, robot)
    #     print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
    #     if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
    #         robot.drive_system.stop()
    #         robot.arm_and_claw.raise_arm()
    #         break
    #     case = case + 1
    #     if case > 7:
    #         case = 0
    #     d = d - (initial_distance- robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())/initial_distance * rate_of_increase
    #     if d<=0:
    #         d=0.1

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

# def led_rotation(case, robot):
def led_rotation(rate, rate_of_increase,robot):
#     print('led')
#     if (case == 0):
#         robot.led_system.left_led.turn_on()
#     elif (case == 1):
#         robot.led_system.left_led.turn_off()
#     elif (case == 2):
#         robot.led_system.right_led.turn_on()
#     elif (case == 3):
#         robot.led_system.right_led.turn_off()
#     elif (case == 4):
#         robot.led_system.left_led.turn_on()
#     elif (case == 5):
#         robot.led_system.right_led.turn_on()
#     elif (case == 6):
#         robot.led_system.left_led.turn_off()
#     elif (case == 7):
#         robot.led_system.right_led.turn_off()
#     print('finish')
    robot.led_system.left_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()  # the time from last beep is reset:
    return time.time(), rate - rate_of_increase