from search import search
from robot_wrapper import Robot

robot = None

def init():
    robot_wrap = Robot(robot)

    search(robot_wrap)

def periodic():
    pass
