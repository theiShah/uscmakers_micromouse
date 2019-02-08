
class Neighbors:

    def __init__(self, top=None, left=None, bottom=None, right=None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right


class Square:

    def __init__(self, x, y, neighbors, start=False, end=False):
        self.neighbors = neighbors
        self.x = x
        self.y = y
        self.start = start
        self.end = end

   
class Maze:

    def __init__(self):
        self.squares = {}
        self.max_x = 0
        self.max_y = 0

    def add_square(self, square, x, y):
        if self.max_y < y:
            self.max_y = y
        if self.max_x < x:
            self.max_x = x
        self.squares[(x, y)] = square

    def link_squares(self):
        for i in range(0, self.max_x):
            for j in range(0, self.max_y):
                current_square = self.squares[(i, j)]
                if current_square.neighbors.top:
                    current_square.neighbors.top = self.squares[(i, j+1)]
                if current_square.neighbors.left:
                    current_square.neighbors.left = self.squares[(i-1, j)]
                if current_square.neighbors.bottom:
                    current_square.neighbors.bottom = self.squares[(i, j-1)]
                if current_square.neighbors.right:
                    current_square.neighbors.right = self.squares[(i+1, j)]
