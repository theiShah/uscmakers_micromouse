from search import search
from robot_wrapper import Robot
import matplotlib.pyplot as plt
import networkx.drawing as nd

robot = None

def init():
    robot_wrap = Robot(robot)

    maze = search(robot_wrap)

    maze.draw_graph()


def periodic():
    pass
