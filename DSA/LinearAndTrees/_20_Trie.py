"""
A Trie Data Structure is a tree-like structure used for storing a dynamic set of strings. Commonly used for efficient retrieval and storage of keys in large datasets.
It typically supports operations like insert, search, delete for keys.

Each node in the Trie (excluding root), represents a character or part of a string. The root represents an empty string. The path from root to a node represents 
the prefix of a string stored in the Trie.


Insert:
    We can implement insert very easily, either represent the children as key: Trie pairs or as an array [None]*26 for each character, and insert the relavent 
    trie in the correct position

Search:
    Very similar to insert, we just traverse the Trie and search each key, with word wont exist (because no characters at Trie), all characters exist but wordEnd is 
    False indicating the word exists as a prefix to another word but is not itself present in the Trie, or finally we find the word and wordEnd is True.

"""

class TrieNode():

    def __init__(self, val=""):
        self.key = val
        self.child = {}
        self.wordEnd = False


class MyTrie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        i = 0
        temp = self.root
        while i < len(s):
            if s[i] not in temp.child:
                temp.child[s[i]] = TrieNode(val=s[i])
            temp = temp.child[s[i]]
            i += 1
        temp.wordEnd = True


    # def insert2(self, s):
    #     i = 0
    #     temp = self.root
    #     while i < len(s):
    #         k = ord(s.lower()) - ord("a")
    #         if temp.child[k] is None:
    #             temp.child[k] = TrieNode(val=s.lower())
    #         temp = temp.child[k]
    #         i += 1
    #     temp.wordEnd = True


    def search(self, s):
        i = 0
        temp = self.root
        while i < len(s):
            if s[i] not in temp.child:
                return False
            temp = temp.child[s[i]]
            i += 1
        return temp.wordEnd
    

    def show_words(self):
        res = [] 
        word = []

        def backtrack(node):
            if node.wordEnd:
                res.append("".join(word.copy()))
            for ch in node.child:
                word.append(ch)
                backtrack(node.child[ch])
                word.pop()

        backtrack(self.root)
        return res
        
    


def test():
    t = MyTrie()
    print("MyTrie Created: t")
    t.insert("word")
    print("  insert word: word")
    print("  searching word:", t.search("word"))
    print("  searching wo:", t.search("wo"))
    t.insert("wo")
    print("  insert word: wo")
    print("  searching wo:", t.search("wo"))
    t.insert("worm")
    print("  insert word: worm")
    print("  searching worm:", t.search("worm"))
    print("All words in Trie t:", t.show_words())



test()