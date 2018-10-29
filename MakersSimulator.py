import Tkinter

class Square:

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

    def _init_(row, column, top=None, bottom=None, left=None, right=None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.row = row
        self.column = column


class Maze:

    def _init_(size):
        self.size = size
