"""
Hard: Given a 2D board of characters, and a list of strings, words, return all words that are present in the grid (formed
by horizontal and vertical movements).

Sol:
    - We create a Trie for the list of words.
    - We then iterate through all the (r, c) pairs of the board, exploring in all directions.
    - In doing this, we can compare/search for the current word created in the exploration (the path), by looking in our Trie. If its not there, then continue on,
    if it does exist, add it to the output and remove from the Trie.
    - This is essentially 2D backtracking while using a Trie.
"""

