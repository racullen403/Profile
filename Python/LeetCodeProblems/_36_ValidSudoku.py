"""
Given an incomplete Sudoku board, we must determine if it is valid.

    - The board will be a list of the 9 lists, where each nested list represents a row given by its index, and will
    contain 9 items for each of the 9 cells in the row.
    - Rows, columns and 3x3 boxes must not contain repeat digits from 1-9.
    - The absence of a digit is represented by "."


Solution:

    - Consider a row of the board, we know it can only contain digits 1-9 once to be valid, we can represent the digits
    currently in this row using a list of length 9, where index+1 tells us if that digit is in the row or not:

        e.g     [False, False, True, True, False, False, False, False, False]

                This would tell us only index 2 and 3 are in the row, which means digits "3" and "4"

    We would then represent every row like this in a list, where index of the row points to the respective row.

    - In a similar way we do this with the columns and the 3x3 boxes, this gives us an O(1) lookup for each cell,
    allowing us to see if the digit is a duplicate or not in constant time, instead of comparing to every term in
    the row, O(n).

    (Note, we could also implement a set, {} for each row, col, box, it has O(1) lookup and .remove() runs in O(1)
    time. This would also reduce the space needed as it is unlikely we would apply this to a completed board)

    - Now we simply iterate through every cell in the board, work out what row/col/box it is, and check if that digit
    exists or not, then update the row/col/box lookups, if we make it through every cell, then the board is valid.

"""


def is_sudoku_board_valid(board):
    digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    rows = [[False]*9 for _ in range(9)]
    cols = [[False] * 9 for _ in range(9)]
    boxes = [[False] * 9 for _ in range(9)]
    for i in range(81):
        r = i // 9
        c = i % 9
        b = 3*(r//3) + (c//3)
        if board[r][c] != ".":
            num = digits[board[r][c]] - 1
            if rows[r][num] is True or cols[c][num] is True or boxes[b][num] is True:
                return False
            rows[r][num] = True
            cols[c][num] = True
            boxes[b][num] = True
    return True


def is_sudoku_valid_sets(board):
    digits = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8}
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(81):
        r = i // 9
        c = i % 9
        b = 3*(r//3) + (c // 3)
        if board[r][c] != ".":
            num = digits[board[r][c]]
            if num in rows[r] or num in cols[c] or num in boxes[b]:
                return False
            rows[r].add(num)
            cols[c].add(num)
            boxes[b].add(num)
    return True


