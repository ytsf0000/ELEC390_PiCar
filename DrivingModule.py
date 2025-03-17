class CarController:
    def __init__(self,car):
        self.car = car

    def move_forward(self, speed=30):
        self.car.forward(speed)

    def move_backward(self, speed=30):
        self.car.backward(speed)

    def turn_left(self, speed=30, angle=-30):
        self.car.set_dir_servo_angle(angle)
        self.car.forward(speed)

    def turn_right(self, speed=30, angle=30):
        self.car.set_dir_servo_angle(angle)
        self.car.forward(speed)

    def stop(self):
        self.car.stop()

