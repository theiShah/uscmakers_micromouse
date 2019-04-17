from search import search
from robot_wrapper import Robot
import matplotlib.pyplot as plt
import networkx.drawing as nd
from dijkstras import dijkstra
from path_following import follow_path
import config

def init(robot):
	robot_wrap = Robot(robot)

	maze = search(robot_wrap)
	#maze.draw_graph()

	path = dijkstra(maze.graph, (robot_wrap.x, robot_wrap.y), (0,0))

	follow_path(robot_wrap, path)

	path = dijkstra(maze.graph, (0,0), (8,7))
	# for node in path:
	# 	print(node)

	config.sim_speed = 0.75  

	follow_path(robot_wrap, path)