
class Direction():
    up = 0
    left = 1 
    down = 2
    right = 3


class Robot:

    def __init__(self, robot):
        self.direction = Direction.up
        self.x = 0
        self.y = 0
        self.robot = robot

    def move_forward(self):
        start_x = self.x
        start_y = self.y
        self.x = start_x + (self.direction % 2) * (self.direction - 2)
        self.y = start_y + ((self.direction % 2)-1) * (self.direction - 1)
        print('Moving from ({}, {}) to ({}, {}) in direction {}'.format(start_x, start_y, self.x, self.y, self.direction))
        self.robot.move_forward()

    def turn_right(self):
        self.direction = (self.direction + 3) % 4
        print('Turning right to direction {}'.format(self.direction))
        self.robot.turn_right()

    def turn_left(self):
        self.direction = (self.direction + 1) % 4
        print('Turning left to direction {}'.format(self.direction))
        self.robot.turn_left()

    def get_front(self):
        return self.robot.get_front()

    def get_left(self):
        return self.robot.get_left()

    def get_right(self):
        return self.robot.get_right()

    def get_direction(self):
        return self.direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def rotate_to_direction(self, direction):

        difference = (direction - self.get_direction())
        if abs(difference) == 3:
            difference = difference/3 * -1
        
        for i in range(abs(difference)):
            if difference > 0:
                self.turn_left()
            else:
                self.turn_right()


