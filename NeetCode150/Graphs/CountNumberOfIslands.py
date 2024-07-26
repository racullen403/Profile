"""
Medium: Given a 2D grid of "1" and "0", an island is a vertical and horizontal collection of "1"s, everywhere else is water. Ie no diagonal connections.
Given the grid, return how many islands it contains.

Sol1:
    - Explore each cell of the grid fully using a DFS, if we finda "1" add it to a set of already visited cells (i, j).
    - Once we have fully explored a cell, we can add 1 to the counter if we found an island.
    - Note that when an island is found, all coordinates (i, j) == "1" will be added to visited, that way we know if we find a new island.

"""

def numIslands(grid):
    count = [0]
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def explore(i, j, r, c):
        if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == "0":
            return
        # We found a new valid island (i, j)
        visited.add((i, j))
        explore(i + 1, j, r, c)
        explore(i, j + 1, r, c)
        explore(i - 1, j, r, c)
        explore(i, j - 1, r, c)
    
        if (i, j) == (r, c):                # When done exploring the island, add one to counter
            count[0] += 1

    for i in range(rows):
        for j in range(cols):
            explore(i, j, i, j)

    return count[0]


def numIslands2(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def explore(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == "0":
            return
        visited.add((i, j))
        explore(i + 1, j)
        explore(i - 1, j)
        explore(i, j + 1)
        explore(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                count += 1
                explore(i, j)

    return count