
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

    def add_square(self, square, x, y):
        self.squares[(x, y)] = square

    def link_squares(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                current_square = self.squares[(i, j)]
                if current_square.neighbors.top:
                    current_square.neighbors.top = self.squares[(i-1, j)]
                if current_square.neighbors.left:
                    current_square.neighbors.left = self.squares[(i, j-1)]
                if current_square.neighbors.bottom:
                    current_square.neighbors.bottom = self.squares[(i+1, j)]
                if current_square.neighbors.right:
                    current_square.neighbors.right = self.squares[(i, j+1)]
