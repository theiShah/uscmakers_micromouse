import math, time
import config

def bound_angle(angle):
    angle %= 360
    if angle < 0:
        angle += 360
    return angle

class RobotGraphic:

    def __init__(self, x, y, angle, length, gui, canvas):

        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.canvas = canvas
        self.gui = gui

        self.update_points()
        self.polygon = self.canvas.create_polygon(self.point1[0], self.point1[1], self.point2[0], self.point2[1], self.point3[0], self.point3[1], fill="yellow", outline="black")
        self.gui.update()

    def update_points(self):
        angle_offset = 30
        self.angle = bound_angle(self.angle)
        angle = math.radians(self.angle)
        self.point1 = [self.x + self.length/3 * math.cos(angle), self.y - self.length/3 * math.sin(angle)]
        angle = math.radians(self.angle + 180 + angle_offset)
        self.point2 = [self.x + self.length/4 * math.cos(angle), self.y - self.length/4 * math.sin(angle)]
        angle = math.radians(self.angle + 180 - angle_offset)
        self.point3 = [self.x + self.length/4 * math.cos(angle), self.y - self.length/4 * math.sin(angle)]

    def go_to_angle(self, angle):
        self.angle = angle

        self.update_points()
        self.canvas.coords(self.polygon, self.point1[0], self.point1[1], self.point2[0], self.point2[1], self.point3[0], self.point3[1])

    def rotate_to_angle(self, angle):
        angle = bound_angle(angle)
        start_angle = self.angle
        angle_delta = abs(angle-start_angle)
        direction = (angle-start_angle) / angle_delta
        if angle_delta > 180:
            direction *= -1
            angle_delta -= 180

        for i in range(0, angle_delta)[::2]:
            self.go_to_angle(start_angle + direction * i)
            self.gui.update()
            time.sleep(.001 * config.turn_rate * config.sim_speed)
        self.go_to_angle(angle)
        self.gui.update()

    def go_to_point(self, x, y):
        self.x = x
        self.y = y

        self.update_points()
        self.canvas.coords(self.polygon, self.point1[0], self.point1[1], self.point2[0], self.point2[1], self.point3[0], self.point3[1])

    def move_to_point(self, x, y):
        x_start = self.x
        y_start = self.y
        x_delta = x-x_start
        y_delta = y-y_start
        h = math.sqrt(x_delta**2 + y_delta**2)
        x_step = x_delta/h
        y_step = y_delta/h

        for i in range(0, int(h))[::2]:
            self.go_to_point(x_start + x_step * i, y_start + y_step * i)
            self.gui.update()
            time.sleep(.001 * config.move_rate * config.sim_speed)
        self.go_to_point(x, y)
        self.gui.update()

class RobotSim:

    def __init__(self, maze, gui, canvas):
        self.current_square = maze.start_square
        self.current_angle = maze.start_angle
        self.robot_graphic = RobotGraphic(self.current_square.x_mid, self.current_square.y_mid, self.current_angle, maze.wall_length, gui, canvas)

    def __pointing_up(self):
        return self.current_angle > 45 and self.current_angle < 135

    def __pointing_left(self):
        return self.current_angle > 135 and self.current_angle < 225

    def __pointing_down(self):
        return self.current_angle > 225 and self.current_angle < 315

    def __pointing_right(self):
        return self.current_angle > 315 or self.current_angle < 45

    def move_forward(self):
        if self.__pointing_up() and self.current_square.neighbors.top:
            self.current_square = self.current_square.neighbors.top
        elif self.__pointing_left() and self.current_square.neighbors.left:
            self.current_square = self.current_square.neighbors.left
        elif self.__pointing_down() and self.current_square.neighbors.bottom:
            self.current_square = self.current_square.neighbors.bottom
        elif self.__pointing_right() and self.current_square.neighbors.right:
            self.current_square = self.current_square.neighbors.right
        else:
            raise RuntimeError("Drove into a wall!!")

        self.robot_graphic.move_to_point(self.current_square.x_mid, self.current_square.y_mid)
        time.sleep(config.move_wait * config.sim_speed)

    def turn_right(self):
        self.current_angle = bound_angle(self.current_angle - 90)
        self.robot_graphic.rotate_to_angle(self.current_angle)
        time.sleep(config.turn_wait * config.sim_speed)

    def turn_left(self):
        self.current_angle = bound_angle(self.current_angle + 90)
        self.robot_graphic.rotate_to_angle(self.current_angle)
        time.sleep(config.turn_wait * config.sim_speed)

    def get_front(self):
        if self.__pointing_up():
            return self.current_square.neighbors.top == None
        elif self.__pointing_left():
            return self.current_square.neighbors.left == None
        elif self.__pointing_down():
            return self.current_square.neighbors.bottom == None
        elif self.__pointing_right():
            return self.current_square.neighbors.right == None
        else:
            raise RuntimeError("Pointing in an awkward direction, current angle is {}.".format(self.current_angle))

    def get_left(self):
        if self.__pointing_up():
            return self.current_square.neighbors.left == None
        elif self.__pointing_left():
            return self.current_square.neighbors.bottom == None
        elif self.__pointing_down():
            return self.current_square.neighbors.right == None
        elif self.__pointing_right():
            return self.current_square.neighbors.top == None
        else:
            raise RuntimeError("Pointing in an awkward direction, current angle is {}.".format(self.current_angle))

    def get_right(self):
        if self.__pointing_up():
            return self.current_square.neighbors.right == None
        elif self.__pointing_left():
            return self.current_square.neighbors.top == None
        elif self.__pointing_down():
            return self.current_square.neighbors.left == None
        elif self.__pointing_right():
            return self.current_square.neighbors.bottom == None
        else:
            raise RuntimeError("Pointing in an awkward direction, current angle is {}.".format(self.current_angle))
