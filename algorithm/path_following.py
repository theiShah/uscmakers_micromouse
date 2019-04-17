
from robot_wrapper import Direction

def follow_path(robot, path):

	if len(path) <= 1:
		return

	for i in range(len(path) - 1):
		start_node = path[i]
		next_node = path[i+1]

		direction = -1
		if next_node[0] - start_node[0] < 0:
			direction = Direction.left
		elif next_node[0] - start_node[0] > 0:
			direction = Direction.right
		elif next_node[1] - start_node[1] < 0:
			direction = Direction.down
		elif next_node[1] - start_node[1] > 0:
			direction = Direction.up	

		robot.rotate_to_direction(direction)
		robot.move_forward()


