import Tkinter as tk
import time, sys, importlib
import config
from sim.Maze import Maze
from sim.Robot import RobotSim

def main():
    global robot

    if len(sys.argv) != 2:
        print("This program must have 1 argument!")
        sys.exit()

    gui = tk.Tk()
    maze = Maze()
    maze.process_file(config.input_file)
    canvas = maze.draw_maze(gui)
    robot = RobotSim(maze, gui, canvas)

    algorithm_file = sys.argv[1]

    if algorithm_file[0] != '.' and algorithm_file[0] != '/':
        algorithm_file = './' + algorithm_file

    filename_index = algorithm_file.rfind('/')
    file_directories = algorithm_file[:filename_index]
    file_name = algorithm_file[filename_index + 1:]
    sys.path.append(file_directories)

    algorithm = importlib.import_module(file_name.replace(".py", ""))
    algorithm.robot = robot

    start_time = time.time()
    algorithm.init()
    while not robot.current_square.end:
        algorithm.periodic()
        wait_time_start = time.time()
        while time.time() - wait_time_start < config.periodic_wait * config.sim_speed:
            pass
    end_time = time.time()

    print("Succeeded in {} seconds!".format((end_time-start_time)/config.sim_speed))
    tk.mainloop()

if __name__ == "__main__":
    main()
