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

class Trie():

    def __init__(self):
        self.child = {}
        self.wordCount = 0

    def add(self, word):
        temp = self
        for c in word:
            if c not in temp.child:
                temp.child[c] = Trie() 
            temp = temp.child[c]
        temp.wordCount += 1

    def remove(self, word):
        def backtrack(i, trie):
            if i == len(word) and trie.wordCount > 0:
                trie.wordCount -= 1
                if trie.child == {}:
                    return True
                return False 
            elif i < len(word) and word[i] in trie.child and backtrack(i+1, trie.child[word[i]]):
                if trie.wordCount == 0 and trie.child == {}:
                    print("  popping", word[i])
                    trie.child.pop(word[i])
                    return True
                return False
            return False

        backtrack(0, self)

    def show(self):
        res = [] 
        def backtrack(trie, path):
            if trie.wordCount > 0:
                res.append(path)
            elif not trie.child:
                return
            for child in trie.child:
                backtrack(trie.child[child], path + child)
        backtrack(self, "")
        print("Words in Trie:", res)
        return res


def findWords(board, words):
    t = Trie()
    for word in words:
        t.add(word)
    t.show()
    res = set()
    rows = len(board)
    cols = len(board[0])
    visited = set()

    def backtrack(r, c, trie, path):
        if trie.wordCount > 0:
            print("  Found result:", path)
            res.add(path)
            print(" Output:", res)
            t.remove(path)
            t.show()
        if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] not in trie.child:
            print("  Path ends:", path, (r, c))
            return
        ch = board[r][c]
        node = trie.child[ch]
        visited.add((r, c))
        backtrack(r + 1, c, node, path + ch)
        backtrack(r - 1, c, node, path + ch)
        backtrack(r, c + 1, node, path + ch)
        backtrack(r, c - 1, node, path + ch)
        visited.remove((r, c))
        return
    
    for i in range(rows):
        for j in range(cols):
            backtrack(i, j, t, "")

    print(res)
    return res



def test():
    t = Trie()
    t.show()
    print("  Adding worm")
    t.add("worm")
    t.show()
    print("  Adding work")
    t.add("work")
    t.show()
    print("  Adding word")
    t.add("word")
    t.show()
    print("  Adding wo")
    t.add("wo")
    t.show()
    print("  Adding warm")
    t.add("warm")
    t.show()
    print("  Adding walk")
    t.add("walk")
    t.show()
    print("  Removing wo")
    t.remove("wo")
    t.show()
    print("  Removing word")
    t.remove("word")
    t.show()
    print("  Removing work")
    t.remove("work")
    t.show()
    print("  Removing walk")
    t.remove("walk")
    t.show()
    print("  Removing worm")
    t.remove("worm")
    t.show()
    print("  Removing warm")
    t.remove("warm")
    t.show()
    

def test2():
    board = [["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]]
    words = ["bat","cat","back","backend","stack"]
    findWords(board, words)

