from Tkinter import *
master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

class Square:


    def __init__(self, row, column, top=None, bottom=None, left=None, right=None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.row = row
        self.column = column

    def print_square(self, x_start, y_start, length):

        if self.top != None:
            w.create_line(x_start, y_start, x_start + length, y_start)
        if self.bottom != None:
            w.create_line(x_start, y_start + length, x_start + length, y_start + length)
        if self.left != None:
            w.create_line(x_start, y_start, x_start, y_start + length)
        if self.right != None:
            w.create_line(x_start + length, y_start, x_start + length, y_start + length)



class Maze:

    def __init__(self, size):
        self.size = size


square = Square(0, 0, right=1)
square.print_square(10,10,20)

mainloop()
