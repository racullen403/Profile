def isValidSudoku(board):
    # Medium: We store 3 arrays for row/cols/squares, each array 
    # of length 9 to store True/False if the digits exists in 
    # respective row/col/square

    row = [ [False]*9 for _ in range(9)]
    col = [ [False]*9 for _ in range(9)]
    sqr = [ [False]*9 for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue 
            num = int(num) - 1
            blk = (c // 3) + (( r // 3) * 3)
            if (row[r][num] == True or col[c][num] == True or 
                sqr[blk][num] == True):
                return False
            row[r][num] = True 
            col[c][num] = True 
            sqr[blk][num] = True 
    return True



