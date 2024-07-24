"""
Medium: Implement a prefix tree (trie) that can insert a word, search for a word, and tell you if a prefix exists.

Sol:
    - Very basic prefix tree implementation, we will use [None]*26 to represent the 26 lower case letters.
"""
class PrefixTree:

    def __init__(self):
        self.child = [None]*26
        self.wordCount = 0
        

    def insert(self, word: str) -> None:
        temp = self
        for c in word:
            index = ord(c.lower()) - ord("a")
            if not temp.child[index]:
                temp.child[index] = PrefixTree()
            temp = temp.child[index]
        temp.wordCount += 1


    def search(self, word: str) -> bool:
        temp = self
        for c in word:
            index = ord(c.lower()) - ord("a")
            if not temp.child[index]:
                return False
            temp = temp.child[index]
        return temp.wordCount > 0
        

    def startsWith(self, prefix: str) -> bool:
        temp = self
        for c in prefix:
            index = ord(c.lower()) - ord("a")
            if not temp.child[index]:
                return False
            temp = temp.child[index]
        return True
