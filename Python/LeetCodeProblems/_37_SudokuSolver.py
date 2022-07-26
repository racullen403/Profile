"""
Given some Sudoku Board, we want to create an algorithm that will solve it if it is solvable.

Assume boards are of form [ [],[],...] where each sub list is a row.
"""

""" 
    First attempt was very brute force, checking whole board each time and the entire row/col/cell each time for 
    validity
"""


class SudokuBad:

    def __init__(self, board=None):
        self.board = board
        self.sol = board

    def is_board_valid(self, board):
        for i in range(9):
            if not self.is_row_valid(board, i):
                return False
            if not self.is_column_valid(board, i):
                return False
            if not self.is_cell_valid(board, i + 1):
                return False
        return True

    def solve_sudoku(self):
        if self.is_board_complete(self.sol) is True:
            return True
        r, c = self.find_empty_cell(self.sol)
        for i in range(1, 10):
            self.sol[r][c] = str(i)
            if self.is_board_valid(self.sol):
                if self.solve_sudoku() is True:
                    return True
            self.sol[r][c] = "."
        return False

    def is_board_complete(self, board):
        if not self.is_board_valid(board):
            return False
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    return False
        return True

    def find_empty_cell(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    return r, c

    def is_pos_valid(self, board, pos):
        row = (pos - 1) // 9
        col = (pos - 1) % 9
        cell = (row * 3) + (col + 1)
        if self.is_row_valid(board, row) and self.is_column_valid(board, col) and self.is_cell_valid(board, cell):
            return True
        return False

    def is_row_valid(self, board, row):
        items = set()
        for col in range(9):
            if board[row][col] == ".":
                continue
            elif board[row][col] in items:
                return False
            items.add(board[row][col])
        return True

    def is_column_valid(self, board, col):
        items = set()
        for row in range(9):
            if board[row][col] == ".":
                continue
            elif board[row][col] in items:
                return False
            items.add(board[row][col])
        return True

    def is_cell_valid(self, board, cell):
        row = (cell - 1) // 3
        col = (cell - 1) % 3
        items = set()
        for r in range(3 * row, 3 * row + 3):
            for c in range(3 * col, 3 * col + 3):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in items:
                    return False
                items.add(board[r][c])
        return True

    def show(self, board):
        for r in range(9):
            if r % 3 == 0:
                print(" -" * 12)
            print("|", end=" ")
            for c in range(9):
                print(board[r][c], end=" ")
                if c in [2, 5]:
                    print("|", end=" ")
            print("|")
        print(" -" * 12)


""" 
Second Attempt: much more efficient, we use a mapping for the rows cols and cells in the form of nested lists, the index 
of the list is the corresponding row/col/cell and the index of the item in the list refers to whether the number is in 
that row/col/cell already using True of it is and False if its not present 
"""
import copy


class Sudoku:

    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.sol = board

    def solve_sudoku(self):
        row = [[False] * 9 for i in range(9)]
        col = [[False] * 9 for i in range(9)]
        cell = [[False] * 9 for i in range(9)]
        visit = []
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != ".":
                    num = int(self.board[r][c]) - 1
                    row[r][num] = True
                    col[c][num] = True
                    cell[(r // 3) * 3 + c // 3][num] = True
                else:
                    visit.append((r, c))
        self.backtrack_solve(row, col, cell, visit)

    def backtrack_solve(self, row, col, cell, visit):
        if len(visit) == 0:
            return True
        r, c = visit.pop()
        for num in range(1, 10):
            ind = num - 1
            if not row[r][ind] and not col[c][ind] and not cell[(r // 3) * 3 + c // 3][ind]:
                self.sol[r][c] = str(num)
                row[r][ind] = True
                col[c][ind] = True
                cell[(r // 3) * 3 + c // 3][ind] = True
                if self.backtrack_solve(row, col, cell, visit):
                    return True
                self.sol[r][c] = "."
                row[r][ind] = False
                col[c][ind] = False
                cell[(r // 3) * 3 + c // 3][ind] = False
        visit.append((r, c))

    def show(self, board=None):
        if board is None:
            board = self.sol
        for r in range(9):
            if r % 3 == 0:
                print(" -" * 12)
            print("|", end=" ")
            for c in range(9):
                print(board[r][c], end=" ")
                if c in [2, 5]:
                    print("|", end=" ")
            print("|")
        print(" -" * 12)


# board1 = [["5","3",".",".","7",".",".",".","."],
#           ["6",".",".","1","9","5",".",".","."],
#           [".","9","8",".",".",".",".","6","."],
#           ["8",".",".",".","6",".",".",".","3"],
#           ["4",".",".","8",".","3",".",".","1"],
#           ["7",".",".",".","2",".",".",".","6"],
#           [".","6",".",".",".",".","2","8","."],
#           [".",".",".","4","1","9",".",".","5"],
#           [".",".",".",".","8",".",".","7","9"]]
#
# i = Sudoku(board1)
# i.solve_sudoku()
# i.show(i.board)
# i.show(i.sol)
