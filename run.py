import time, sys, importlib
import config


def main():

    # if len(sys.argv) != 2:
    #     print("This program must have 1 argument!")
    #     sys.exit()

    if config.simulated:
        import tkinter as tk
        from sim.Maze import Maze
        from sim.Robot import RobotSim
        maze = Maze()
        maze.process_file(config.input_file)
        gui = tk.Tk()
        canvas = maze.draw_maze(gui)
        robot = RobotSim(maze, gui, canvas)
    else:
        from drivers.Robot import Robot
        robot = Robot()


    # algorithm_file = sys.argv[1]

    # if algorithm_file[0] != '.' and algorithm_file[0] != '/':
    #     algorithm_file = './' + algorithm_file

    algorithm_file = config.algorithm

    filename_index = algorithm_file.rfind('/')
    file_directories = algorithm_file[:filename_index]
    file_name = algorithm_file[filename_index + 1:]
    sys.path.append(file_directories)

    algorithm = importlib.import_module(file_name.replace(".py", ""))

    start_time = time.time()
    algorithm.init(robot)
    if config.use_periodic:
        while not robot.current_square.end:
            algorithm.periodic()
            wait_time_start = time.time()
            while time.time() - wait_time_start < config.periodic_wait * config.sim_speed:
                pass
    end_time = time.time()

    print("Succeeded in {} seconds!".format(end_time-start_time))

    if config.simulated:
        try:
            tk.mainloop()
        except AttributeError:
            pass

if __name__ == "__main__":
    main()
