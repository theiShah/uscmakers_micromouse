from Tkinter import *

class Square:

    def __init__(self, row, column, top=None, left=None, bottom=None, right=None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.row = row
        self.column = column

class Maze:

    wall_length = 50
    line_width = 4

    dictionary = {
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
        f = open(file,"r")
        self.size = int(f.readline())

        for i in range(1, self.size+1):
            line = f.readline()
            self.squares.append([])
            squares = line.split()
            for j in range(0, len(squares)):
                self.squares[i-1].append(self.create_square(squares[j], i-1, j))

        f.close()


    def create_square(self, square_type, row, column):
        format_string = self.dictionary[int(square_type)]
        #print("Creating square: " + format_string)
        top, left, bottom, right = None, None, None, None
        if "top" in format_string:
            top = 1
        if "left" in format_string:
            left = 1
        if "bottom" in format_string:
            bottom = 1
        if "right" in format_string:
            right = 1

        #print(" {} \n{} {}\n {} ".format(top, left, right, bottom))
        return Square(row, column, top, left, bottom, right)

    def print_maze(self):

        offset = self.line_width - self.line_width%2
        outer_dimension = self.wall_length*self.size + offset + 1

        master = Tk()
        w = Canvas(master, width=outer_dimension, height=outer_dimension)
        w.pack()

        for i in self.squares:
            for square in i:
                x_start, y_start = square.column*self.wall_length + offset, square.row*self.wall_length + offset
                if square.top != None:
                    w.create_line(x_start, y_start, x_start + self.wall_length, y_start, width=self.line_width)
                if square.bottom != None:
                    w.create_line(x_start, y_start + self.wall_length, x_start + self.wall_length, y_start + self.wall_length, width=self.line_width)
                if square.left != None:
                    w.create_line(x_start, y_start, x_start, y_start + self.wall_length, width=self.line_width)
                if square.right != None:
                    w.create_line(x_start + self.wall_length, y_start, x_start + self.wall_length, y_start + self.wall_length, width=self.line_width)

        mainloop()


def main():

    maze = Maze()
    maze.process_file("input.txt")
    maze.print_maze()


main()
