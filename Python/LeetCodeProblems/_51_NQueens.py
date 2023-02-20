"""
Given an integer n, return all distinct n x n chess boards that can hold n queens such that no 2 queens can attack
each other.

    Solution:
        - There are 3 conditions that must be met,

            - Two Queens cannot be in the same row
            - Two Queens cannot be in the same column
            - Two queens cannot lie on the same diagonal

            i.e.    if (r1, c1) and (r2, c2) are the coordinates of 2 queens then,

                        r1 != r2

                        c1 != c2

                        r1 - c1 != r2 - c2  and r1 + c1 != r2 + c2  (this comes from + or - 1 gradient)

        - We can solve this using dfs and a backtracking algorithm, we simply iterate through the columns and rows
        and try insert a Queen, if it fails the conditions, we remove it and move on, if we hit a dead end we can fall
        back to a previous recursion call and continue the iteration from there.

        -

"""
import copy


def n_queens(n):
    board = [["."] * n for _ in range(n)]
    solutions = []

    def dfs_solve(xy_sum, xy_diff, cols, r=0):
        if r == n:
            solutions.append(copy.deepcopy(board))
            return
        for c in range(n):
            if cols[c] is True:
                continue
            s = r + c
            d = r - c
            if s not in xy_sum and d not in xy_diff:
                cols[c] = True
                xy_sum.add(s)
                xy_diff.add(d)
                board[r][c] = "Q"
                dfs_solve(xy_sum, xy_diff, cols, r+1)
                board[r][c] = "."
                cols[c] = False
                xy_sum.remove(s)
                xy_diff.remove(d)

    cols = [False] * n
    dfs_solve(set(), set(), cols)

    for i in range(len(solutions)):
        print("Solution", i+1, ":")
        for r in solutions[i]:
            for c in r:
                print("", c, end="  ")
            print()

