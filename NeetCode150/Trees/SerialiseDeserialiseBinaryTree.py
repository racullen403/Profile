"""
Hard: Given a binary tree, serialise is into a string to be sent, and deserialize that string back into the binary tree.

Sol:
    - We already now how to create a binary tree from the inorder and postorder traversal.
    - Hence we just need to serialise these into a string, and then deserialise that string and use the binary tree builder.

    - Above implementation works but is over the top.
    - All we need to do is a dfs and add the null nodes which tell us when at a leaf.

"""

class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 


class Codec():

    def inorder(self, root):        # Returns "in1#n2#n3#n4#..."
        s = ["i"]

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            s.append(str(node.val))
            s.append("#")
            dfs(node.right)
        
        dfs(root)

        return "".join(s)
    
    def preorder(self, root):       # Returns "pn1#n2#n3#n4#..."
        s = ["p"]

        def dfs(node):
            if not node:
                return
            s.append(str(node.val))
            s.append("#")
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return "".join(s)

    def serialize(self, root):
        inorder = self.inorder(root)
        preorder = self.preorder(root)
        return inorder + preorder           # Returns "in1#n2#n3#n4#...#pn1#n2#n3#n4#...#"
    
    def deserialize(self, data):
        inorder = []
        preorder = [] 
        i = 1
        while i < len(data):        # Breaks the strings n1, n2, n3 up until p and converts to int, then adds to list inorder
            if data[i] == "p":
                i += 1
                break
            j = i
            while j < len(data) and data[j] != "#":
                j += 1
            print(data[i:j])
            n = int(data[i: j])
            inorder.append(n)
            i = j + 1
        while i < len(data)-1:  # Breaks the strings n1, n2, n3 up until last # and converts to int, then adds to list preorder
            j = i
            while j < len(data) and data[j] != "#":
                j += 1
            n = int(data[i: j])
            preorder.append(n)
            i = j + 1
        return self.buildTree(preorder, inorder)   

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None 
        root = TreeNode(preorder[0])
        i = 0 
        while inorder[i] != preorder[0]:
            i += 1
        root.left = self.buildTree(preorder[1: i + 1], inorder[: i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
        
        
# Implementation above works but is over the top and not needed, better more efficient below

class Codec2():

    def serialise(self, root):
        res = [] 

        def dfs(node):          # preorder dfs and include the None values
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)    # serialise by making string and comma seaparated
    
    def deserialise(self, data):    # deserialise by splitting the string by comma into is integers (as stings)
        vals = data.split(",")
        self.i = 0

        def dfs():      # DFS again building the tree using the preorder traversal, this works as we have stored None values that left us break recursive call
            if vals[self.i] == "N":
                self.i += 1
                return None 
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        
