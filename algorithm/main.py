from search import search
from robot_wrapper import Robot
import matplotlib.pyplot as plt
import networkx.drawing as nd
from dijkstras import dijkstra

robot = None

def init():
    robot_wrap = Robot(robot)

    maze = search(robot_wrap)

    path = dijkstra(maze.graph, (0,0), (8,8))

    print(path)

    maze.draw_graph()


#run dijkstra's, find best path, run through that path
def periodic():
    pass
