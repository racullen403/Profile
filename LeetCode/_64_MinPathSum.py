"""
Given an N x M grid of non-negative numbers, find the shortest path, you can only move down or right.

Solution:
    - We can solve this dynamically.
    - We accumulate the first row and column path lengths

        e.g         [1, 3, 1]  becomes      [1, 4, 5]
                    [1, 5, 1]               [2, 5, 1]
                    [4, 2, 1]               [6, 2, 1]

    - Next we move along each row, and find the minimum of cell + cell above, or cell + cell left, this is because the
    above and left cells to this cell will already have the shortest path distance found, hence we either move down or
    right to reach this current cell.

                    [1, 4, 5]   cell[1][1] becomes min of 4+5 or 2+5, so 7      [1, 4, 5]
                    [2, 5, 1]                                                   [2, 7, 1]
                    [6, 2, 1]                                                   [6, 2, 1]

    - We continue like this until we reach the final cell which will contain the answer.

"""


def min_grid_path(grid):

    for c in range(1, len(grid[0])):
        grid[0][c] += grid[0][c-1]
    for r in range(1, len(grid)):
        grid[r][0] += grid[r-1][0]

    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            grid[r][c] += min(grid[r-1][c], grid[r][c-1])

    return grid[-1][-1]


def example():

    my_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    print("My Grid:")
    for row in my_grid:
        print(row)

    print("Shortest Path:", min_grid_path(my_grid))

    print("Final Grid:")
    for row in my_grid:
        print(row)


example()