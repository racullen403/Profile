"""
Given a valid Sudoku, we must create an algorithm that will return a completed board if possible.


Solution:

    - The method is very similar to validating the Sudoku board, in _36_ValidSudoku, we apply the same technique for
    O(1) lookup times of the rows, cols, and boxes. The only addition is we apply a backtracking technique using
    Breadth First Search.

    BFS: For each cell, 1-81, we try to insert digits 1-9 (keeping track of what digits are in the board using our
    sets), once we add a digit, we update the sets and move to the next cell. If we reach a cell where no digit
    can be inserted, we know the path we are on is wrong and must "backtrack" to the previous cell, we then simply
    continue with the next possible digit in our current cell and continue as before.

    - We continue until the board is full

    - Note, we must preprocess the input board and add all the initial digits into the sets.

"""


def solve_sudoku(board):
    digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Preprocess
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                num = digits[board[r][c]]
                b = 3*(r//3) + (c//3)
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

    # Recursive Solver, ends when index is 81 (larger than last cell in Sudoku)
    def bfs_solver(i):
        if i == 81:
            return True
        r = i // 9
        c = i % 9
        b = 3*(r//3) + (c//3)
        if board[r][c] == ".":
            for d in range(1, 10):
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)
                    board[r][c] = str(d)
                    if bfs_solver(i+1) is True:
                        return True
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
                    board[r][c] = "."
            return False
        return bfs_solver(i+1)

    # Solve
    bfs_solver(0)

    return board

