"""
Medium: Implement a data structure that supports adding new words and searching existing words. Note that searching words can contain a '.' that 
represents any letter.

Sol:
    - This is literally a Trie implementation.
    - The only extra step is when searching for "." we must loop through all the children.
"""

class WordDictionary():

    def __init__(self):
        self.child = [None]*26
        self.wordCount = 0

    def addWord(self, word):
        temp = self 
        for c in word:
            i = ord(c.lower()) - ord("a")
            if not temp.child[i]:
                temp.child[i] = WordDictionary()
            temp = temp.child[i]
        temp.wordCount += 1

    def search(self, word):

        def backtrack(i, node):
            temp = node 
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in temp.child:
                        if child and backtrack(j + 1, child):
                            return True
                    return False
                else:
                    ind = ord(word[j].lower()) - ord("a")
                    if not temp.child[ind]:
                        return False
                    temp = temp.child[ind]
            return temp.wordCount > 0
                

            # if i == len(word) and node.wordCount > 0:
            #     return True
            # elif i == len(word):
            #     return False
            # elif word[i] == ".":
            #     for child in node.child:
            #         if child and backtrack(i + 1, child):
            #             return True
            #     return False
            # else:
            #     ind = ord(word[i].lower()) - ord("a")
            #     if not node.child[ind]:
            #         return False
            #     return backtrack(i + 1, node.child[ind])
        
        return backtrack(0, self)

