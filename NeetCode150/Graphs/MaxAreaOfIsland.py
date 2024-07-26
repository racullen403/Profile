"""
Medium: Given a grid of "1" and "0", where the horizonatal and vertical connections of "1" represents land. Return the are of the largest island.

Sol:
    - Simply DFS the islands, adding them to a visited, return the size of island for comparing to max value.
"""

def maxAreaOfIsland(grid):
    max_area = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def backtrack(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == 0:
            return 0
        visited.add((i, j))
        return 1 + backtrack(i + 1, j) + backtrack(i - 1, j) + backtrack(i, j + 1) + backtrack(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                max_area = max(max_area, backtrack(i, j))

    return max_area


def test():
    grid = [[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
    print(maxAreaOfIsland(grid))

test()