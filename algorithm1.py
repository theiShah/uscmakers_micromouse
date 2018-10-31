
robot = None

def init():
    pass

def periodic():
    if not robot.get_front():
        robot.move_forward()
    elif not robot.get_left():
        robot.turn_left()
        robot.move_forward()
    elif not robot.get_right():
        robot.turn_right()
        robot.move_forward()
    else:
        robot.turn_left()
