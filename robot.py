
class Direction():
    up = 0
    left = 1 
    down = 2
    right = 3

class Robot:

    def __init__(self):
        pass

    def __pointing_up(self):
        return self.current_angle > 45 and self.current_angle < 135

    def __pointing_left(self):
        return self.current_angle > 135 and self.current_angle < 225

    def __pointing_down(self):
        return self.current_angle > 225 and self.current_angle < 315

    def __pointing_right(self):
        return self.current_angle > 315 or self.current_angle < 45

    def move_forward(self):
        pass

    def turn_right(self):
        pass

    def turn_left(self):
        pass

    def get_front(self):
        pass

    def get_left(self):
        pass

    def get_right(self):
        pass
