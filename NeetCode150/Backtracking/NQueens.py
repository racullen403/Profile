"""
Hard: Return all possible N-Queens layouts. This is when given positive number N, we place N Queens on an N x N chess board.

Sol:
    - Back tracking algorithm with some additional logic to create board and let us know what places a queen can go in.

    - Only tricky part is in the way we find the valid rows, cols and diagonals.
    - We can easily do this brute force like my first implementation.
    - Alternatively, we can carry through sets for the rows, cols, posDiagonals and negDiagonals that contain a Q already, this is because the 
    diagonals can be uniquely identified as (r-c) for the Negative gradiant and (r + c) in the positive gradient.
"""

def solveNQueens(n):
    if n == 0:
        return []
    
    board = [["." for _ in range(n)] for _ in range(n)]
    print(board)

    res = []

    def backtrack(r, path):
        print("r", r)
        if r == n:
            print(path)
            res.append(["".join(x.copy()) for x in path])
            return
        for i in range(n):
            if isValidPosition(r, i, path):
                path[r][i] = "Q"
                print("board", path)
                backtrack(r + 1, path)
                path[r][i] = "."

    def isValidPosition(r, c, board):
        for i in range(n):
            if board[r][i] == "Q" or board[i][c] == "Q":
                return False
         
        i, j = r, c 
        while 0 <= i < n and 0 <= j < n:
            if board[i][j] == "Q":
                return False
            i += 1
            j += 1

        i, j = r, c 
        while 0 <= i < n and 0 <= j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        i, j = r, c 
        while 0 <= i < n and 0 <= j < n:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1

        i, j = r, c 
        while 0 <= i < n and 0 <= j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        return True

    
    
    backtrack(0, board)

    return res


def solveNQueens2(n):
    if n == 0:
        return []
    res =[] 
    board = [["."]*n for _ in range(n)]
    cols = set()
    posD = set()
    negD = set()

    def backtrack(r):
        if r == n:
            new_board = ["".join(x.copy()) for x in board]
            res.append(new_board)
            return
        for c in range(n):
            if c in cols or (r - c) in negD or (r + c) in posD:
                continue
            board[r][c] = "Q"
            cols.add(c)
            posD.add(r + c)
            negD.add(r - c)
            backtrack(r + 1)
            board[r][c] = "."
            cols.remove(c)
            posD.remove(r + c)
            negD.remove(r - c)

    backtrack(0)
    return res


def test():
    print(solveNQueens2(4))
