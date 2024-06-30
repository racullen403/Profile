"""
We want to return a string that follows a zigzag pattern based on how many
rows we choose.

    example: "PAYPALISHIRING"

        P A Y P A L I S H I R I N G  -> "PAYPALISHIRING" 1 row

        P Y A I H R N   -> "PYAIHRNAPLSIIG" 2 rows
        A P L S I I G

        P   A   H   N   -> "PAHNAPLSIIGYIR" 3 rows
        A P L S I I G
        Y   I   R

        P     I     N   -> "PINALSIGYAHRPI" 4 rows
        A   L S   I G
        Y A   H R
        P     I

The solution is as follows:
    - Use a pointer to tell us what row we are currently at, starting at row 0,
    and add the character into a list/string .
    - Use another pointer to tell us the direction of the next row, +-1
    - Everytime we get to the first or last row, swap the direction
    - Simply iterate through the characters  until they have all been added
    to their corresponding row. Then join all the rows into one string
"""


def zigzag_pattern(s, nrows):
    if nrows <= 0:
        return
    if nrows == 1:
        return s
    rows = [""]*nrows
    direction = 1
    row = 0
    for i in range(len(s)):
        rows[row] += s[i]
        if row == 0:
            direction = 1
        elif row == nrows-1:
            direction = -1
        row += direction
    return "".join(rows)



