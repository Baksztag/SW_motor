import threading
from motor.Motor import Motor
from motor.MotorControl import MotorControl

LEFT_MOTOR_NAME = 'LEFT_MOTOR'
RIGHT_MOTOR_NAME = 'RIGHT_MOTOR'
LEFT_MOTOR_PINS = [17, 22, 23, 24]
RIGHT_MOTOR_PINS = [5, 6, 12, 13]


class VehicleDrive(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__left_motor_control = MotorControl(direction=-1, speed=0.0)
        self.__right_motor_control = MotorControl(speed=0.0)
        self.__left_motor = Motor(1, LEFT_MOTOR_NAME, LEFT_MOTOR_PINS, self.__left_motor_control)
        self.__right_motor = Motor(2, RIGHT_MOTOR_NAME, RIGHT_MOTOR_PINS, self.__right_motor_control)

    def run(self):
        self.__left_motor.start()
        self.__right_motor.start()

        self.__left_motor.join()
        self.__right_motor.join()

    def start_vehicle(self):
        self.__left_motor_control.run_motor()
        self.__right_motor_control.run_motor()

    def stop_vehicle(self):
        self.__left_motor_control.stop_motor()
        self.__right_motor_control.stop_motor()

    def go_forward(self, speed, ratio):
        if self.__left_motor_control.direction != -1:
            self.__left_motor_control.switch_direction()
        if self.__right_motor_control.direction != 1:
            self.__right_motor_control.switch_direction()

        if ratio >= 100:
            new_speed = (speed - 100) / 100 
            new_ratio = (200 - ratio) / 100
            print(new_ratio)
            self.__right_motor_control.change_speed(new_speed * abs(new_ratio))
            self.__left_motor_control.change_speed(new_speed)
        else:
            new_speed = (speed - 100) / 100
            new_ratio = (100 - ratio) / 100
            self.__left_motor_control.change_speed(new_speed * abs(new_ratio))
            self.__right_motor_control.change_speed(new_speed)

    def go_backwards(self, speed, ratio):
        new_speed = (100 - speed) / 100
        if self.__left_motor_control.direction != 1:
            self.__left_motor_control.switch_direction()
        if self.__right_motor_control.direction != -1:
            self.__right_motor_control.switch_direction()
        if ratio >= 100:
            new_ratio = (200 - ratio) / 100
            self.__right_motor_control.change_speed(new_speed * abs(new_ratio))
            self.__left_motor_control.change_speed(new_speed)
        else:
            new_ratio = (100 - ratio) / 100
            self.__left_motor_control.change_speed(new_speed * abs(new_ratio))
            self.__right_motor_control.change_speed(new_speed)

    # def turn_left(self, ratio):
        # current_speed = self.__left_motor_control.speed \
        #     if self.__left_motor_control.speed >= self.__right_motor_control.speed \
        #     else self.__right_motor_control.speed
        # self.__left_motor_control.speed = current_speed
        # self.__right_motor_control.speed = (1 - ratio) * current_speed
        # if self.__left_motor_control.direction != 1:
        #     self.__left_motor_control.switch_direction()
        # if self.__right_motor_control.direction != 1:
        #     self.__right_motor_control.switch_direction()

    # def turn_right(self, ratio):
        # current_speed = self.__left_motor_control.speed \
        #     if self.__left_motor_control.speed >= self.__right_motor_control.speed \
        #     else self.__right_motor_control.speed
        # self.__left_motor_control.speed = (1 - ratio) * current_speed
        # self.__right_motor_control.speed = current_speed
        # if self.__left_motor_control.direction != -1:
        #     self.__left_motor_control.switch_direction()
        # if self.__right_motor_control.direction != -1:
        #     self.__right_motor_control.switch_direction()

