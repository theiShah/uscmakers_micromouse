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

    def _init_(self, row, column, top=None, left=None, bottom=None, right=None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.row = row
        self.column = column


class Maze:

    def _init_(self, size):
        self.size = size

    def processFile(self) :
        f = open("input.txt","r")
        print (f.read())

    def createSquare(self, type, row, column) :
        format = dictionary[type]
        top, left, bottom, right = 0,0,0,0
        if (format.contains("top")) :
            top = 1
        if (format.contains("left")) :
            left = 1
        if (format.contains("bottom")) :
            bottom = 1
        if (format.contains("right")) :
            right = 1
        return Square(row, column, top, left, bottom, right)

# public static void main (int argc, const char* argv[]) {}
maze = Maze()
maze.processFile()
















# qwertyuiop
