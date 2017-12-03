class MotorControl:
    def __init__(self, speed=0.0, direction=1):
        self.direction = direction
        self.speed = speed

    def switch_direction(self):
        self.direction = -1 * self.direction

    def change_speed(self, speed):
        if speed <= 0.01:
            self.speed = 0.0
        elif speed >= 1.0:
            self.speed = 1
        else:
            self.speed = speed
