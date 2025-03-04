from picarx import PicarX  # Assuming this is your car control library

class CarController:
    def __init__(self):
        self.car = PicarX()

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

class Forward:
    def __init__(self, controller: CarController):
        self.controller = controller

    def execute(self):
        self.controller.move_forward()

class Backward:
    def __init__(self, controller: CarController):
        self.controller = controller

    def execute(self):
        self.controller.move_backward()

class TurnLeft:
    def __init__(self, controller: CarController):
        self.controller = controller

    def execute(self):
        self.controller.turn_left()

class TurnRight:
    def __init__(self, controller: CarController):
        self.controller = controller

    def execute(self):
        self.controller.turn_right()

def main():
    car_controller = CarController()

    # Example usage
    forward_action = Forward(car_controller)
    backward_action = Backward(car_controller)
    turn_left_action = TurnLeft(car_controller)
    turn_right_action = TurnRight(car_controller)

    # Simulate actions (you can replace this with a UI, joystick input, or another control mechanism)
    forward_action.execute()
    turn_left_action.execute()
    car_controller.stop()

if __name__ == "__main__":
    main()
