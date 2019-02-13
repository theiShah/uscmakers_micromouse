import tkinter as tk
import config

class Neighbors:

    def __init__(self, top=None, left=None, bottom=None, right=None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

class Square:

    def __init__(self, x_start, y_start, x_end, y_end, neighbors, start=False, end=False):
        self.neighbors = neighbors
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.start = start
        self.end = end

        self.x_mid = x_start + (x_end-x_start)/2
        self.y_mid = y_start + (y_end-y_start)/2

    def draw(self, canvas, line_width):
        if self.start:
            canvas.create_rectangle(self.x_start, self.y_start, self.x_end, self.y_end, fill="red", outline="red")
        if self.end:
            canvas.create_rectangle(self.x_start, self.y_start, self.x_end, self.y_end, fill="green", outline="green")

        if self.neighbors.top == None:
            canvas.create_line(self.x_start, self.y_start, self.x_end, self.y_start, width=line_width)
        if self.neighbors.bottom == None:
            canvas.create_line(self.x_start, self.y_end, self.x_end, self.y_end, width=line_width)
        if self.neighbors.left == None:
            canvas.create_line(self.x_start, self.y_start, self.x_start, self.y_end, width=line_width)
        if self.neighbors.right == None:
            canvas.create_line(self.x_end, self.y_start, self.x_end, self.y_end, width=line_width)

class Maze:

    wall_length = config.wall_length
    line_width = config.wall_thickness
    start_square = None

    file_symbols = {
        0 : "",
        1 : "top",
        2 : "left",
        3 : "bottom",
        4 : "right",
        5 : "top-left",
        6 : "left-bottom",
        7 : "bottom-right",
        8 : "top-right",
        9 : "top-left-bottom",
        10 : "left-bottom-right",
        11 : "top-bottom-right",
        12 : "top-left-right",
        13 : "top-bottom",
        14 : "left-right",
        15 : "top-left-bottom-right"
    }

    def __init__(self):
        self.squares = []

    def process_file(self, file):
        self.squares = []
        f = open(file,"r")
        self.start_angle = int(f.readline())
        self.size = int(f.readline())

        for i in range(1, self.size+1):
            line = f.readline()
            self.squares.append([])
            squares = line.split()
            for j in range(0, len(squares)):
                new_square = self.create_square(squares[j], i-1, j)
                self.squares[i-1].append(new_square)
                if new_square.start:
                    self.start_square = new_square
        f.close()
        self.link_squares()

    def create_square(self, square_type, row, column):

        start, end = False, False
        if "S" in square_type:
            square_type = square_type.replace("S", "")
            start = True
        if "E" in square_type:
            square_type = square_type.replace("E", "")
            end = True

        format_string = self.file_symbols[int(square_type)]
        #print("Creating square: " + format_string)
        neighbors = Neighbors()
        if "top" not in format_string:
            neighbors.top = 1
        if "left" not in format_string:
            neighbors.left = 1
        if "bottom" not in format_string:
            neighbors.bottom = 1
        if "right" not in format_string:
            neighbors.right = 1

        offset = self.line_width - self.line_width%2
        outer_dimension = self.wall_length*self.size + offset + 1

        x_start = column*self.wall_length + offset
        y_start = row*self.wall_length + offset
        x_end = x_start + self.wall_length
        y_end = y_start + self.wall_length

        return Square(x_start, y_start, x_end, y_end, neighbors, start, end)

    def link_squares(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                current_square = self.squares[i][j]
                if current_square.neighbors.top:
                    current_square.neighbors.top = self.squares[i-1][j]
                if current_square.neighbors.left:
                    current_square.neighbors.left = self.squares[i][j-1]
                if current_square.neighbors.bottom:
                    current_square.neighbors.bottom = self.squares[i+1][j]
                if current_square.neighbors.right:
                    current_square.neighbors.right = self.squares[i][j+1]

    def draw_maze(self, gui):

        offset = self.line_width - self.line_width%2
        outer_dimension = self.wall_length*self.size + offset + 1

        canvas = tk.Canvas(gui, width=outer_dimension, height=outer_dimension)
        canvas.pack()

        for i in self.squares:
            for square in i:
                square.draw(canvas, self.line_width)

        gui.update()
        return canvas


def main():

    maze = Maze()
    maze.process_file("input.txt")
    maze.draw_maze()
    tk.mainloop()

if __name__ == "__main__":
    main()
