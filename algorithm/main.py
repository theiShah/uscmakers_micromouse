from search import search
from robot_wrapper import Robot

robot = None

def init():
    robot_wrap = Robot(robot)

    maze = search(robot_wrap)

def periodic():
    pass
