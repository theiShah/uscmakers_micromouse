import Tkinter as tk
import time, sys, importlib
import config
from sim.Maze import Maze
from sim.RobotSim import RobotSim

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
    algorithm = importlib.import_module(algorithm_file.replace(".py", ""))
    algorithm.robot = robot

    start_time = time.time()
    algorithm.init()
    while not robot.current_square.end:
        algorithm.periodic()
        time.sleep(config.periodic_wait * config.sim_speed)
    end_time = time.time()

    print("Succeeded in {} seconds!".format((end_time-start_time)/config.sim_speed))
    tk.mainloop()

if __name__ == "__main__":
    main()
