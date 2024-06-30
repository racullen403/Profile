"""
We will use a backtracking algorithm (DFS), this simply reverts to a previous step if it is determined
that the current solution cannot be completed.

Solving  A Sudoku:

    - Find an empty cell
    - Try place digit 1-9
    - Check if this is valid in current cell based on current state of the board
    - If valid, recursively attempt to fill the board as previously
    - If not valid, reset the cell and go back to previous space
    - When board is full, we have a solution

"""
from random import shuffle


class SudokuSolver:

    def __init__(self, board=None):
        if board is None:
            self.board = [[0 for i in range(9)] for j in range(9)]
        else:
            if len(board) != 9:
                print("Input 9x9 Please")
                return
            for row in board:
                if len(row) != 9:
                    print("Input 9x9 Please")
                    return
                for num in row:
                    if num not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
                        print("Invalid Entries")
                        return
            self.board = board
        print("\nInitial Board")
        self.print_board()
        self.create_solution_board(self.board)
        print("\nSolution Board")
        self.print_board()

    def find_empty(self, board):
        """Finds the next empty square and returns it, returns None if complete"""
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return

    def is_valid_row(self, num, row, board):
        """Return True if num is in a valid position in the row"""
        for col in range(9):
            if board[row][col] == num:
                return False
        return True

    def is_valid_col(self, num, col, board):
        """Return True if num is in a valid position in the column"""
        for row in range(9):
            if board[row][col] == num:
                return False
        return True

    def is_valid_box(self, num, row, col, board):
        """Returns True if num is in a valid position in the sub-square"""
        sub_row = row // 3
        sub_col = col // 3
        for r in range(3*sub_row, 3*sub_row + 3):
            for c in range(3*sub_col, 3*sub_col + 3):
                if board[r][c] == num:
                    return False
        return True

    def is_valid_location(self, num, row, col, board):
        """Returns True if num is in a valid location in the Sudoku"""
        if self.is_valid_row(num, row, board) is False:
            return False
        elif self.is_valid_col(num, col, board) is False:
            return False
        elif self.is_valid_box(num, row, col, board) is False:
            return False
        return True

    def create_solution_board(self, board):
        """Uses backtracking to create a completed Sudoku from an input board"""
        # Base Case
        empty_cell = self.find_empty(board)
        if empty_cell is None:
            return True
        else:
            row, col = empty_cell
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num_list)
        for num in num_list:
            if self.is_valid_location(num, row, col, board) is True:
                board[row][col] = num
                if self.create_solution_board(board) is True:
                    return True
                board[row][col] = 0
        return False

    def print_board(self, title=None):
        if title:
            print(title)
        for row in range(9):
            if row % 3 == 0:
                print(" ------- ------- -------")
            for col in range(9):
                if col % 3 == 0:
                    print("|", end=" ")
                print(self.board[row][col], end=" ")
            print("|")
        print(" ------- ------- -------")


sudoku1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

print("\n----puzzle1----")
puzzle1 = SudokuSolver()

print("\n----puzzle2----")
puzzle2 = SudokuSolver(board=sudoku1)

