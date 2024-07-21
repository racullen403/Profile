"""
Medium: Given a 2-D grid of characters, board, and a string word, return True if word is present in the grid.
Word can only be formed from vertical and horizontal movements.

Sol:
    - Create backtracking algorithm that checks up to the length of word ahead, terminating any false cases early.
    - Simply need to ensure i, j are within board, and watch the letter we are looking for. If we find the last letter, return True.
    - If not True and not False, then check every direction again, increasing the letter we look for.
    - We need to track what coordinates we have been to inorder to ensure we dont use the same letters more than once, or we can pass a copy of the board and 
    change the letters to # as we pass them.
"""

def exists(board, word):

    def backtrack(i, j, count, visited):
        if i >= len(board[0]) or j >= len(board) or i < 0 or j < 0 or board[j][i] != word[count] or (i, j) in visited:   # Conditions that cause False
            return False
        elif count == len(word) - 1:    # If not False then we found the letter, if its the last, return True
            return True
        visited.add((i, j))
        n = count + 1   # Increase index of letter to search for and check every new direction
        return (backtrack(i + 1, j, n, visited) or backtrack(i - 1, j, n, visited)
                or backtrack(i, j + 1, n, visited) or backtrack(i, j - 1, n, visited))

    for i in range(len(board[0])):
        for j in range(len(board)):
            if backtrack(i, j, 0, set()):
                return True 

    return False    

def test():
    board = [["A","B","C","D"],
            ["S","A","A","T"],
            ["A","C","A","E"]
            ]
    print(exists(board, "CAT"))

test()
                    
