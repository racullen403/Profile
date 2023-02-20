"""
Given a MxN maze and the entrance (i, j), we have to return the shortest distance out of the maze.

    Maze:
        - A list of M lists with each being length N
        - Walls denoted by "+", empty space denoted by "."

    Solution:
        - We explore the maze in a radial sense using a BFS, this means as soon as we find an exit, we will know it
        is the shortest path as we have explored the cells 1 step at a time.

"""


def maze_shortest_distance_exit(maze, entrance):
    to_visit = [(entrance[0], entrance[1], 0)]  # Queue [(i, j, steps)]

    def is_exit(i, j):  # Check if it is exit cell
        isentrance = (i == entrance[0]) and (j == entrance[1])
        isexit = (i == 0) or (i == len(maze)-1) or (j == 0) or (j == len(maze[0])-1)
        return isexit and not isentrance

    while to_visit:
        neighbours = []  # temp list to hold next queue
        for r, c, steps in to_visit:
            if is_exit(r, c):
                return steps
            else:
                for x, y in ([1, 0], [-1, 0], [0, 1], [0, -1]):  # New 4 potential directions to explore
                    i = r + x
                    j = c + y
                    if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == ".":  # Make sure new indices are inside the maze and the cell is valid
                        neighbours.append((i, j, steps+1))  # Add to queue
                        maze[i][j] = "+"  # Update maze so we don't explore this cell again
        to_visit = neighbours

    return -1
