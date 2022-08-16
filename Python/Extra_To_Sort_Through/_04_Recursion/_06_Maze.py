"""
We will now consider the problem of finding our way out of a maze

Let the maze be in square tiles for simplicity:

    maze = [    [ 1, 1, 1, 1, 1, 3, 1, 1],
                [ 1, 0, 0, 0, 0, 0, 0, 1],
                [ 1, 1, 1, 0, 1, 1, 0, 1],
                [ 1, 1, 1, 0, 1, 1, 1, 1],
                [ 1, 1, 1, 0, 1, 1, 1, 1],
                [ 1, 1, 0, 0, 0, 0, 1, 1],
                [ 1, 1, 0, 0, 2, 1, 1, 1],
                [ 1, 1, 1, 1, 1, 1, 1, 1]
            ]

            Here we say 1 represents the walls of  the maze, 0 is an open path, and let 2
            be the start and 3 be an exit.

    We need a systematic way to explore the maze and find a way out:

        - From our current position, try going North, then recursively try our procedure
        - If North was unsuccessful we will try going south and apply procedure
        - If not South, try west, and apply procedure again
        - If not west try east and apply procedure
        - If no direction works we failed to get out of the maze

        Note that in our procedure we go north, and if it fails we go south again, this will
        cause an infinite loop, to prevent this we must memorize the tiles we have been to,
        that way we can move to the next direction in the procedure.

        Our base cases:
            - Run into a wall
            - We move to a square already fully explored
            - We find the exit
            - We explore a tile unsuccessfully in all directions
"""


def find_start_position(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 2:
                return row, col


def search_maze(maze, row, col):
    tile = maze[row][col]
    # wall
    if tile == 1:
        return False
    # exploring
    if tile == ".":
        return False
    # exit
    if tile == 3:
        # path
        maze[row][col] = "o"
        return True
    maze[row][col] = "."
    found = search_maze(maze, row-1, col) or search_maze(maze, row+1, col) or \
            search_maze(maze, row, col-1) or search_maze(maze, row, col+1)
    if found:
        # path
        maze[row][col] = "o"
    else:
        # dead end
        maze[row][col] = "x"
    return found


def show_maze(maze):
    for row in range(len(maze)):
        print("")
        for col in range(len(maze[row])):
            print(maze[row][col], end=" ")

maze = [[1, 1, 1, 1, 1, 3, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 2, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
        ]

show_maze(maze)
search_maze(maze, find_start_position(maze)[0], find_start_position(maze)[1])
print("")
show_maze(maze)
