"""
Red-Black Tree:

    This is a self-balancing Binary Search Tree like the AVL tree, except instead of using height of Nodes to balance
    it, we are using the colour of the node to ensure the "black depth" of every leaf from any given node, is always
    the same. This ensures that we achieve an O(logn) insert/delete time, even if the tree is not of "perfect" balance.

    Now, because we are storing colour instead of height, we still end up with the same memory footprint as a BST.


    Rules:
        - Every Node has a colour, red or black.
        - Root node is always black.
        - There are never 2 adjacent red nodes (children of red node are always black).
        - Every path from a given node to all its descendant leaf nodes, will have the same number of black nodes.
        - All leaf nodes are black.


    Every Red-Black Tree with n nodes will have a height h <= 2*Log(n+1)  (base 2)
        - If we say k is the minimum number of nodes to get from root to leaf, then n >= 2^k - 1 so

            k <= log(n+1)

        - We know that every path from root to a leaf node has the same number of black nodes, so in theory, we could
        have a root to leaf path that contains k black nodes, worst case being log(n+1).

        - Knowing all leaf nodes are black, and no 2 adjacent nodes can be red, there is the potential for a path that
        contains the log(n+1) black nodes and a red node at either side of every black, we claim the height is there
        for:
                                        h <= 2 * Log(n+1)

        - So we know worst case, our search will still be O(logn) time, instead of O(n) like an ordinary  BST.


    INSERTION:

        Upon insertion of a new node, it is common for the Red-Black property to be broken, the complex part is now
        restoring this, in which there are a number of potential cases, and we must use recolouring and or rotation
        to fix it.

            We insert the new Node as we would with a BST insert, and label it red (if black, then we would violate
            the black depth property), the main loop then returns up the tree (using parent pointer) and ensures the
            Red-Black property.

            BLACK PARENT NODE
            - Let the current node be x, if the parent of x is Black, then we have not altered the Red-Black property
            and can leave it.

            RED PARENT NODE
            - When the parent of x is red, we now need to restore the RB property (double red can't exist), mark the
            uncle of x as y:

                Case 1: y is red

                                (B)          or         (B)
                               /  \                    /   \
                             (R)   (R) y              (R)   (R) y
                             /                         \
                            (R) x                       (R) x

                    Note that the grandparent of x will always be black. In both the cases above, we correct the RB
                    property by changing the colour of x's parent, grandparent and uncle.

                                (R)         or          (R)
                               /  \                    /   \
                             (B)   (B)               (B)   (B)
                             /                         \
                            (R)                         (R)

                    The black height is unchanged at the grandparent since the black has been moved down into its
                    children, and it changed to red.

                    Finally, let x now point to is grandparent which is red, and check for Red-Black property. In this
                    way we can continue back up the tree. Not that Case 1 can propagate the whole way back up the tree
                    meaning there could potentially be O(logn) recolours.


                - Case 2: uncle y is black

                                (B)         or           (B)
                               /  \                     /   \
                             (R)   (B) y              (R)   (B) y
                             /                          \
                            (R)  x                      (R) x

                    Let the left be case 2.A and the right be case 2.B

                    For case 2.A, we change the colour of the parent and grandparent of x, and then perform a right
                    rotation on the grandparent

                        Case 2.A

                                (B)         ->           (R)        ->        (B)
                               /  \                     /   \                /   \
                             (R)   (B) y              (B)   (B) y        x (R)   (R)
                             /                        /                            \
                            (R)  x                  (R) x                          (B) y

                            The black height has been conserved and the adjacent reds removed. We have corrected the
                            RB property and are done.


                    For case 2.B, we must first perform a left rotation on the parent of x, if we then set x to point
                    to the left child of x after the rotation, we have Case 2.A and can solve as before.

                        Case 2.B

                             (B)      ->           (B)         ->          (B)
                            /   \                 /  \                    /   \
                          (R)   (B) y         x (R)   (B) y             (R)    (B) y
                            \                  /                        /
                             (R) x           (R)                      (R) x Case 2.A



                After the Case 2.A rotation, we just need to check if the parent of x is the new root node, if so,
                set it to black. The RB properties should now be restored. This means there will be at most, 2 rotations
                after an insert.

                Once we know these cases we can simply apply the same logic for if x's parent is the right child of x's
                grandparent, this just requires us to do the opposite rotations.

                Note:
                    - We can name the 4 potential cases based on the location of the 2 adjacent red nodes from the
                    grandparent.

                     LL               LR              RR                 RL
                     (B)             (B)             (B)                 (B)
                    /   \           /   \           /   \               /   \
                  (R)    (B)       (R)   (B)       (B)   (R)           (B)  (R)
                  /                 \                      \                 /
                 (R)                (R)                     (R)            (R)



    DELETION:
        Deletion occurs just like in a BST, we only remove a node from the leaf position, or from an internal node that
        has only 1 child. We then must correct an RB property that has been broken.

        Let x be the deleted node

            X is RED
                In this case, no property of the RB tree is violated, we are done.

            X is Black
                This is more complicated and there are a number of situations to deal with.

                Let z be the successor of x


                Z is RED
                    We can simply recolour z as black and are done.

                Z is Black
                    In this instance, we say z is a "double black", and our goal is to do rotations and recolours
                    to remove this extra black from z.

                    Let the sibling of z be sib


                    CASE 1:
                        sib is red (parent has to be black)

                        We recolour sib to black, and the parent node to red, then do a rotation on the parent

                          (B)                ->       (R)       ->              (B) sib
                         /  \                        /  \                       / \
                    z (BB)   (R) sib             z (BB) (B) sib               (R)  (B)
                             / \                        / \                   / \
                          (B)  (B)                    (B)  (B)            z (BB) (B)

                        We now need to recheck for Cases 2-4


                    CASE 2:
                        sib is black with 2 black children (parent can be black or red)

                        We recolour sib to red, this forces the "double black" at z to move up to the parent. If the
                        parent is red, we change it to black and are done. If it was black, we now label it as z and
                        check for Case 1-4 again. This case can repeat O(logn) times.


                    CASE 3:
                        sib is black, with one black child to the right (parent can be black or red)

                        Recolour sib to red and the left child to black,then a rotation at sib.

                          ( )                ->       ( )       ->               ( )
                         /  \                        /  \                       /  \
                    z (BB)   (B) sib             z (BB) (R) sib             z (BB)  (B)
                             / \                        / \                          \
                          (R)  (B)                    (B)  (B)                       (R) sib
                                                                                       \
                                                                                        (B)

                        New sib is now black with red right child, Case 4


                    CASE 4:
                        sib is black, with red right child (left child and parent could be red or black
                        and both different)

                        We recolour sib to the colour of its parent, recolour the parent to black, and recolour the
                        red right child to black, then perform a rotation on the parent.

                             (B)           ->       (B)             ->         (B) sib
                            /  \                   /   \                      /   \
                       z (BB)   (B) sib        z (BB)   (B) sib            (B)     (B)
                                / \                     /  \               /  \
                              ()   (R)                 ()   (B)        z (BB)  ()

                                                or


                             (R)           ->       (B)             ->         (R) sib
                            /  \                   /   \                      /   \
                       z (BB)   (B) sib        z (BB)   (R) sib            (B)     (B)
                                / \                     /  \               /  \
                              ()   (R)                 ()   (B)        z (BB)  ()


                        In both cases, we have added extra black into the left side without effect the black depth
                        property of any other node. The "double black" has been removed, we are done.

                Work flow:

                    Case 1 ->   Case 2 with red parent  ->  DONE

                                Case 3  -> Case 4 -> DONE

                                Case 4  -> DONE

                We see at worst there will only be 3 node rotations and log(n) recolours.


Advantages of RB Tree:
    - The worst case scenarios for operations are all log(n), with insertion have a most 2 rotations and deletion
    have 3. This is very useful as rotations are costly.
    - This greatly benefits use cases with a lot of inserts and deletes.

Disadvantages:
    - RB Trees do not focus on perfect balance, one side could have twice the height of another. This could mean our
    searches are as efficient as a more balanced tree.

"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.red = True


class RBT:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            self.root.red = False
        else:
            x = self.root
            inserted = False
            while not inserted:  # Loop to insert val and leave x pointing to it
                if val <= x.val:
                    if not x.left:
                        x.left = Node(val)
                        x.left.parent = x
                        inserted = True
                    x = x.left
                else:
                    if not x.right:
                        x.right = Node(val)
                        x.right.parent = x
                        inserted = True
                    x = x.right
            rb = False
            while not rb:  # Loop to ensure the RB properties
                if not x.parent:  # Reached root
                    x.red = False
                    rb = True
                elif not x.parent.red:  # Black Parent Node
                    rb = True
                else:  # Red Parent Node
                    if x.parent.parent.left == x.parent:  # Find type and uncle
                        uncle = x.parent.parent.right
                        if x.parent.left == x:
                            typ = "LL"
                        else:
                            typ = "LR"
                    else:
                        uncle = x.parent.parent.left
                        if x.parent.left == x:
                            typ = "RL"
                        else:
                            typ = "RR"
                    if uncle and uncle.red:  # Case when Uncle is Red, recolour and check again at grandparent
                        x.parent.red = False
                        x.parent.parent.red = True
                        if uncle:
                            uncle.red = False
                        x = x.parent.parent
                    else:  # Case when Uncle is Black or Leaf
                        if typ == "LL":
                            x.parent.red = False
                            x.parent.parent.red = True
                            self.right_rotate(x.parent.parent)  # Method takes care of pointers
                            rb = True
                        elif typ == "RR":
                            x.parent.red = False
                            x.parent.parent.red = True
                            self.left_rotate(x.parent.parent)
                            rb = True
                        elif typ == "LR":
                            self.left_rotate(x.parent)
                            x = x.left
                        elif typ == "RL":
                            self.right_rotate(x.parent)
                            x = x.right
            self.root.red = False

    def delete_node(self, val):
        if not self.root:
            return
        x = self.root
        deleted = False
        while not deleted:  # Delete val and keep pointers to x and z
            if not x:  # val doesn't exist
                return
            elif val < x.val:
                x = x.left
            elif val > x.val:
                x = x.right
            else:  # found val
                if x.right and x.left:  # Replace with inorder value and continue
                    temp = self.inorder_successor(x.right)
                    x.val = temp.val
                    x = x.right
                    val = temp.val
                else:  # Find successor z and remove x
                    z = x.right
                    if x.left:
                        z = x.left
                    if not x.parent:  # x was root node
                        self.root = z
                    elif x == x.parent.left:  # x is left child
                        x.parent.left = z
                    else:  # x is right child
                        x.parent.right = z
                    if z:
                        z.parent = x.parent
                    if x.red or (z and z.red):  # RB property is not altered
                        return
                    deleted = True
        p = x.parent
        restored = False
        while not restored:  # Restore the RB properties
            if z:
                p = z.parent
            if z == self.root:  # We push the double black out of the tree
                z.red = False
                restored = True
            else:  # z is double black
                if z == p.left:  # z is left child
                    sib = p.right
                    if sib and sib.red:  # Case 1
                        sib.parent.red = True
                        sib.red = False
                        self.left_rotate(sib.parent)
                    elif sib and sib.right and sib.right.red:  # Case 4
                        sib.red = sib.parent.red
                        sib.right.red = False
                        sib.parent.red = False
                        self.left_rotate(sib.parent)
                        restored = True
                    elif sib and sib.left and sib.left.red:  # Case 3
                        sib.red = True
                        sib.left.red = False
                        self.right_rotate(sib)
                    else:  # Case 2
                        sib.red = True
                        if sib.parent.red:
                            sib.parent.red = False
                            restored = True
                        else:  # Special Case where double black moves up
                            z = p
                else:  # z is right child
                    sib = p.left
                    if sib and sib.red:  # Case 1
                        sib.red = False
                        sib.parent.red = True
                        self.right_rotate(sib.parent)
                    elif sib and sib.left and sib.left.red:  # Case 4
                        sib.red = sib.parent.red
                        sib.parent.red = False
                        sib.left.red = False
                        self.right_rotate(sib.parent)
                        restored = True
                    elif sib and sib.right and sib.right.red:  # Case 3
                        sib.red = True
                        sib.right.red = False
                        self.left_rotate(sib)
                    else:  # Case 2
                        sib.red = True
                        if sib.parent.red:
                            sib.parent.red = False
                            restored = True
                        else:
                            z = sib.parent

    def inorder_successor(self, node):
        while node.left:
            node = node.left
        return node

    def left_rotate(self, node):
        root = node.parent
        b = node.right
        b1 = b.left
        b.left = node
        node.parent = b
        node.right = b1
        if b1:
            b1.parent = node
        b.parent = root
        if not root:
            self.root = b
        elif root.left == Node:
            root.left = b
        else:
            root.right = b

    def right_rotate(self, node):
        root = node.parent
        b = node.left
        b2 = b.right
        b.right = node
        node.parent = b
        node.left = b2
        if b2:
            b2.parent = node
        b.parent = root
        if not root:
            self.root = b
        elif root.left == node:
            root.left = b
        else:
            root.right = b

    def show(self):
        def show_r(node, count=-1, left=True):
            if not self.root or not node:
                return
            if node == self.root:
                print("Root:", end="")
            elif left:
                print("    " + "|    " * count + "|--> L:", end="")
            else:
                print("    " + "|    " * count + "|--> R:", end="")
            col = "B"
            if node.red:
                col = "R"
            print("({},{})".format(node.val, col))
            show_r(node.left, count + 1, True)
            show_r(node.right, count + 1, False)
            return
        show_r(self.root, -1, True)


# Example of insertion
def example1():
    rbt = RBT()
    for i in range(10, 0, -1):
        print("\n----- Insert:{} -----".format(i))
        rbt.insert(i)
        print("\nShow:\n")
        rbt.show()


# Example of deletion:
def example2():
    rbt = RBT()
    for i in range(1, 20):
        rbt.insert(i)
    print("\n----- Initial Tree -----")
    rbt.show()
    d = 13
    print("\n----- Delete {} -----".format(d))
    rbt.delete_node(d)
    rbt.show()
