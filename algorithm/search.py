from stack import Stack
from robot import Robot, Direction

class Move():

	def __init__(self, direction, previous_direction):
		self.direction = direction
		self.previous_direction = previous_direction

def get_relative_move(relative_direction, current_direction):

	retval = current_direction + relative_direction
	retval %= 4

	return retval

def add_moves(robot, stack, current_direction):

	backwards = get_relative_move(Direction.down, current_direction)
	valid_moves = False

	if robot.get_front():
		direction = get_relative_move(Direction.up, current_direction)
		move = Move(direction, backwards)
		stack.add(move)
		valid_moves = True
	if robot.get_left():
		direction = get_relative_move(Direction.left, current_direction)
		move = Move(direction, backwards)
		stack.add(move)
		valid_moves = True
	if robot.get_right():
		direction = get_relative_move(Direction.right, current_direction)
		move = Move(direction, backwards)
		stack.add(move)
		valid_moves = True

	return valid_moves