"""
A Trie Data Structure is a tree-like structure used for storing a dynamic set of strings. Commonly used for efficient retrieval and storage of keys in large datasets.
It typically supports operations like insert, search, delete for keys.

Each node in the Trie (excluding root), represents a character or part of a string. The root represents an empty string. The path from root to a node represents 
the prefix of a string stored in the Trie.


Insert:
    We can implement insert very easily, either represent the children as, key: Trie pairs, or as an array [None]*26 for each character, and insert the relavent 
    trie in the correct position. Then add to wordCount.

Search:
    Very similar to insert, we just traverse the Trie and search each key, wither word wont exist (because no character at Trie), all characters exist but wordCount is 
    0 indicating the word exists as a prefix to another word but is not itself present in the Trie, or finally we find the word and wordCount > 0.

Delete:
    For deletion we essentially search the word, there will be a few cases to consider.
        - The word has no prefix that is also a word, ie, only the final key has wordCount>0, we delete whole branch (Word has no common prefix)
        - The word has a prefix word, ie, some key not at the end of the word has wordCount>0, we only delete keys this point. (Word containts common prefix)
        - The word is itself a prefix for another word, ie the final key contains another Trie in the children nodes. (Word is a prefix)

Use Cases:
    - Tries are used for things like autocompletion, spell checkers, prefix matching, dictionaries.

Advantages are:
    - Search words in O(l) time, l is length of word.
    - Easy to find prefixes which can be useful in some cases.
    - Allows for order iteration (only when we do not use a dictionary/map like below).

Disadvantages:
    - Common implementations are very sparse, meaning lots of wasted memory.
    - O(l) searching is a lot slower than efficient hashmaps that are O(1).

Notes:
    - Usually implemented with an array on constant size as using a dictionary/hashmap object usually in itself takes up more memory and computation to find the key: value.
    - More Efficient implementation is to simply have a child and sibling pointer, as at most when searching for a key, you will only have to search a couple of siblings, 
    this tends to have no impact on performance, but drastically decreases memory usage. 
    - You could even store key counts and order siblings by most counts to increase average search time.
"""

class TrieNode():

    def __init__(self):
        self.child = {}         
        self.wordCount = 0


class MyTrie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        i = 0
        temp = self.root
        while i < len(s):
            if s[i] not in temp.child:
                temp.child[s[i]] = TrieNode()
            temp = temp.child[s[i]]
            i += 1
        temp.wordCount += 1


    # Implementation using array
    # def insert2(self, s):
    #     i = 0
    #     temp = self.root
    #     while i < len(s):
    #         k = ord(s.lower()) - ord("a")
    #         if temp.child[k] is None:
    #             temp.child[k] = TrieNode(val=s.lower())
    #         temp = temp.child[k]
    #         i += 1
    #     temp.wordCount += 1

    def delete(self, word):
        stack = [self.root] 
        temp = self.root
        i = 0
        while i < len(word) - 1:
            if word[i] not in temp.child:
                print("Could not find word:", word)
                return
            stack.append(temp.child[word[i]])
            temp = temp.child[word[i]]
            i += 1
        while stack:
            parent = stack.pop()
            key = parent.child[word[i]]
            if i == len(word) - 1:
                if key.wordCount == 0:
                    print("Word {} only exists as a prefix to another word, is not actually contained".format(word))
                    return
                elif len(key.child) > 0:
                    print("Word {} exists and is a common prefix, reduce count by 1".format(word))
                    key.wordCount -= 1
                    return 
                else:
                    print("Deleting", word[i])
                    key.wordCount -= 1
                    parent.child.pop(word[i])
            elif key.wordCount > 0:
                print("Word contains prefix, ending delete")
                return
            elif len(key.child) > 0:
                print("Word {} contains a common prefix".format(word))
                return 
            else:
                print("Deleting", word[i])
                parent.child.pop(word[i])
            i -= 1


    def search(self, s):
        i = 0
        temp = self.root
        while i < len(s):
            if s[i] not in temp.child:
                return False
            temp = temp.child[s[i]]
            i += 1
        return temp.wordCount > 0
    

    def show_words(self):
        res = [] 
        word = []

        def backtrack(node):
            if node.wordCount > 0:
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
    print("Delete wo:")
    t.delete("wo")
    print("All words in Trie t:", t.show_words())
    print("Delete worm:")
    t.delete("worm")
    print("All words in Trie t:", t.show_words())
    



test()