"""
Medium: Given a 2D board of X and O's, a region of O's will be surround if it is closed off by X's. Convert
all regions surrounded to X's.

Sol:
    - We do a DFS when we find an O.
    - If we reach a boarded then the region is not surrounded.
    - When leaving the DFS, if we reached a boarder, do nothing, if we never reached a border, then convert all the O's to X's

    - Better method, we start at the boarder cells and do a DFS, every "O" be find, replace with "#"
    - Then iterate through all the cells, and convert remaining "O" to "X" as they will be whats surrounded.
    - Finally iterate through again and convert our boarder "#" back to "O".

"""

def solve(board):
    rows = len(board)
    cols = len(board[0])

    def backtrack(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != "O":
            return
        board[i][j] = "#"
        backtrack(i + 1, j)
        backtrack(i - 1, j)
        backtrack(i, j + 1)
        backtrack(i, j - 1)
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O" and (i in [0, rows - 1] or j in [0, cols - 1]):
                backtrack(i, j)
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O":
                board[i][j] = "X"

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "#":
                board[i][j] = "O"

    return board


def test():
    board = [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","O","O","X"],
             ["X","X","X","O"]]
    print(solve(board))


test()