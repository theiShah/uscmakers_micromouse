from array import *

maze = [[square00, square01, square02], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
#maze is a 2D array of nodes
def mazeToGraph(maze):
    '''This function turns a 2D array containing the maze info
    into a graph data structure'''
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] is not None:
                
