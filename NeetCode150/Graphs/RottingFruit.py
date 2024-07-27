"""
Medium: Given a 2D matrix, grid, containing the following:
    - 0 empty
    - 1 fresh fruit
    - 2 rotten fruit
    Every tick of time, a fresh fruit adjacent to a rotten fruit, vertically or horizontally, will become rotten itself.
    Return the minimum time until there are 0 fresh fruit remaining, return -1 if not possible.

Sol:
    - We for a multipoint BFS from the rotten fruit, step by step rotting all the fruit we can, if we reach a point where the queue is 
    empty then we are done.
    - We hold the fresh fruit in a separated set and pop out when it rots, this will allow us to check if there is any fresh fruit left at the end.
    - Alternatively, just count the fruit, and if none zero at end then we know fruit is left over.

"""

def orangesRotting(grid):
    q = []
    rows = len(grid)
    cols = len(grid[0])
    fruit = 0
    visited = set()
    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell == 1:
                fruit.add((i, j))
            elif cell == 2:
                q.append((i, j))
                visited.add((i, j))
                fruit.add((i, j))
    
    if not fruit:
        return 0 
    
    print("\n  Queue:", q)
    print("  Visited:", visited)
    print("  Fruit:", fruit)

    def queueFruit(i, j, queue):
        if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == 0:
            return 
        queue.append((i, j))
        visited.add((i, j))
    
    t = 0
    while q:
        new_q = [] 
        print("\n  Queue:", q)
        for i, j in q:
            print(f"\n  Rotting fruit: {(i, j)} at time {t}")

            fruit.remove((i, j))
            print("  Visited:", visited)
            print("  Fruit:", fruit)
            queueFruit(i + 1, j, new_q)
            queueFruit(i - 1, j, new_q)
            queueFruit(i, j + 1, new_q)
            queueFruit(i, j - 1, new_q)
        q = new_q 
        t += 1
    
    if len(fruit) > 0:
        return - 1
    return t - 1


def fruitRotting(grid):
    q = [] 
    rows = len(grid)
    cols = len(grid[0])
    fresh = 0 
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                q.append((i, j))

    def queueAdd(i, j, queue):
        nonlocal fresh
        if i in range(rows) and j in range(cols) and grid[i][j] == 1:
            queue.append((i, j))
            grid[i][j] = 2
            fresh -= 1

    t = 0 
    while fresh > 0 and q:
        new_q = []
        for i, j in q:
            queueAdd(i + 1, j, new_q)
            queueAdd(i - 1, j, new_q)
            queueAdd(i, j + 1, new_q)
            queueAdd(i, j - 1, new_q)
        t += 1
        q = new_q
    
    if fresh == 0:
        return t 
    return -1
    


def test():
    grid = [[1,1,0],
            [0,1,1],
            [0,1,2]
            ]
    grid2 = [[0]]
    print(orangesRotting(grid2))


test()