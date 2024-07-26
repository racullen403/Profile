"""
Medium: Given an m x n grid with values as follows
    - -1 Water
    - 0 Treasure
    - inf | 2^31 - 1  | 2147483647, land

    we want to fill the land cells with the disctance to the nearest treasure chest.


Sol:
    - Initial thoughts, traverse the grid each time we find a treasue chest, carrying the distance travelled from said chest.
    - If we do this in a dfs, then each time we find a piece of land, we replace its value with the smaller value.
    - We can improve efficiency by stopping early if we reach a cell that has a chest closer to it than the path travelled.

    - The better way to accomplish this is to do a BFS from all the Treasure Chests at the same time, queuing the neighbouring cells and increasing distance
"""
# Complicated DFS
def islandsAndTreasure(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited  = set()

    def backtrack(i, j, d):
        if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == - 1 or grid[i][j] < d:
            return 
        
        if grid[i][j] > 0:
            grid[i][j] = min(grid[i][j], d)
        
        visited.add((i, j))
        backtrack(i + 1, j, d + 1)
        backtrack(i - 1, j, d + 1)
        backtrack(i, j + 1, d + 1)
        backtrack(i, j - 1, d + 1)
        visited.remove((i, j))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                backtrack(r, c, 0)

    return grid


# Better way using BFS and queues.
def islandsAndTreasure2(grid):
    q = []
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                q.append((i, j))
                visited.add((i, j))
    
    def q_add(i, j, queue):
        if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited or grid[i][j] == -1:
            return
        queue.append((i, j))
        visited.add((i, j))

    d = 0
    while q:
        new_q = []
        for r, c in q:
            grid[r][c] = d
            q_add(r + 1, c, new_q)
            q_add(r - 1, c, new_q)
            q_add(r, c + 1, new_q)
            q_add(r, c - 1, new_q)
        q = new_q
        d += 1
    return grid


def test():
    grid = [[2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
            ]
    print(islandsAndTreasure2(grid))


test()
    