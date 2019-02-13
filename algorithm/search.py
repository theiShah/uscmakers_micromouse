from stack import Stack
from robot_wrapper import Robot, Direction
from maze import Maze, Neighbors, Square

class Move:

	def __init__(self, current_x, current_y, direction):
		self.x = current_x + (direction % 2) * (direction - 2)
		self.y = current_y + ((direction % 2)-1) * (direction - 1)
		self.parent_x = current_x
		self.parent_y = current_y
		self.direction = direction

def get_relative_move(relative_direction, current_direction):

	retval = current_direction + relative_direction
	retval %= 4

	return retval

def create_current_square(robot):

	current_direction = robot.get_direction()

	front, left, right = not robot.get_front(), not robot.get_left(), not robot.get_right()

	if current_direction == Direction.up:
		neighbors = Neighbors(front, left, True, right)
	elif current_direction == Direction.left:
		neighbors = Neighbors(right, front, left, True)
	elif current_direction == Direction.down:
		neighbors = Neighbors(True, right, front, left)
	elif current_direction == Direction.right:
		neighbors = Neighbors(left, True, right, front)

	return Square(robot.x, robot.y, neighbors)

def add_move(move, stack, maze):

	if (move.x, move.y) in maze.squares:
		return False
	else:
		#print('Adding move from ({}, {}) to ({}, {})'.format(move.parent_x, move.parent_y, move.x, move.y))
		stack.add(move)
		return True

def add_moves(robot, stack, maze):

	current_direction = robot.get_direction()
	x = robot.get_x()
	y = robot.get_y()
	valid_moves = False

	if not robot.get_front():
		direction = get_relative_move(Direction.up, current_direction)
		#print('Front open at ({}, {}) in direction {}'.format(x, y, direction))
		move = Move(x, y, direction)
		add_move(move, stack, maze)
		valid_moves = True
	if not robot.get_left():
		direction = get_relative_move(Direction.left, current_direction)
		#print('Left open at ({}, {}) in direction {}'.format(x, y, direction))
		move = Move(x, y, direction)
		add_move(move, stack, maze)
		valid_moves = True
	if not robot.get_right():
		direction = get_relative_move(Direction.right, current_direction)
		#print('Right open at ({}, {}) in direction {}'.format(x, y, direction))
		move = Move(x, y, direction)
		add_move(move, stack, maze)
		valid_moves = True

	return valid_moves

def move_valid_from_square(move, square):
	return square.x == move.parent_x and square.y == move.parent_y

def search(robot):

	maze = Maze()
	to_be_explored = Stack()
	backtrace_directions = Stack()

	current_square = create_current_square(robot)
	current_square.neighbors.bottom = False
	add_moves(robot, to_be_explored, maze)
	maze.add_square(current_square, robot.x, robot.y)

	while to_be_explored.size() > 0:

		current_move = to_be_explored.pop()

		if (current_move.x, current_move.y) in maze.squares:
			continue

		while not move_valid_from_square(current_move, current_square):
			back_move = backtrace_directions.pop()
			robot.rotate_to_direction(get_relative_move(Direction.down, back_move.direction))
			robot.move_forward()
			current_square = create_current_square(robot)
		
		robot.rotate_to_direction(current_move.direction)
		robot.move_forward()
		backtrace_directions.add(current_move)

		current_square = create_current_square(robot)
		add_moves(robot, to_be_explored, maze)
		maze.add_square(current_square, robot.x, robot.y)

	maze.link_squares()

	return maze
		


