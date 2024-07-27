"""
Medium: Given a 2D grid where grid[i][j] is the height of land. Return a list of coords [[i,j]] that if water were to flow from, 
it could reach both the Top/Left (Pacific) side and Bottom/Right side (Atlantic). 

Sol:
    - Feels like we do a DFS from a given cell and see if we can reach both sides by traversing throguh the heights.
    - We can only go to the next cell if it is same or lower height.
    - We must retain the lowest height for exploring.
    
    - Simply do a DFS from the Top/Left sides and add all reachable cells into a set Pacific, then again for Right/Bottom sides and add to set 
    Atlantic.
    - Note that a cell will reach pacific if its height is greater than or equal to the cell that already reachs the pacific.
    - If we find a cell that is in both sets, then we know it can reach both oceans.

"""
import heapq

def waterFlow(heights):
    rows = len(heights)
    cols = len(heights[0])
    pacific = set()
    atlantic = set()
    
    def backtrack(i, j, visited, prevH):
        if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or heights[i][j] < prevH:
            return 
        visited.add((i, j))
        backtrack(i + 1, j, visited, heights[i][j])
        backtrack(i - 1, j, visited, heights[i][j])
        backtrack(i, j + 1, visited, heights[i][j])
        backtrack(i, j - 1, visited, heights[i][j])

    for r in range(rows):
        backtrack(r, 0, pacific, heights[r][0])
        backtrack(r, cols - 1, atlantic, heights[r][cols - 1])

    for c in range(cols):
        backtrack(0, c, pacific, heights[0][c])
        backtrack(rows - 1, c, atlantic, heights[rows - 1][c])

    res = []
    for i in range(rows):
        for j in range(cols):
            if (i, j) in pacific and (i, j) in atlantic:
                res.append([i, j])

    return res
    
