"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT
allocate another 2D matrix and do the rotation.


Solution:

    - This is very basic if you understand matrices, a 90' rotation clockwise can be achieved by doing a reflection
    along the vertical, and then a reflection along the upward diagonal


     [ (0,0), (0,1), (0,2) ]  Vertical Reflection ->   [ (0,2), (0,1), (0,0) ]
     [ (1,0), (1,1), (1,2) ]                           [ (1,2), (1,1), (1,1) ]
     [ (2,0), (2,1), (2,2) ]                           [ (2,2), (2,1), (2,0) ]

     Diagonal Reflection ->  [ (2,0), (1,1), (0,0) ]    == 90' CW Rotation
                             [ (2,1), (1,1), (0,1) ]
                             [ (2,2), (1,2), (0,2) ]

    - Note: We can also achieve this by first doing a horizontal reflection, and then a reflection on the downward
    diagonal (Transpose: interchanging rows into columns), we will do this as the matrix is made up of nest lists for
    rows, and it is faster to simply swap rows than swap all the elements in the rows.

"""


def rotate_image(matrix):
    # Horizontal reflection
    top, bot = 0, len(matrix)-1
    while top < bot:
        matrix[top], matrix[bot] = matrix[bot], matrix[top]
        top += 1
        bot -= 1

    # Downward Diagonal reflection, (i, j) swaps with (j, i)
    for r in range(len(matrix)):
        for c in range(r):  # We only swap cells (r, c) where r > c, this ensures we don't undo swaps
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]



