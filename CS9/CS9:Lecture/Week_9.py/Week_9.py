''' Review From Week 8 Lecture 2
Binary Search Tree (BST)
* Binary SEARCH Trees are binary trees that have the following property
    * Values that are less than the parent are found in the left subtree
    * Values that are greater than the parent are found in the right subtree
    * This is known as the BST PROPERTY
* Binary Search Trees are also one way to implement a MAP Abstract Data Type. 
    * Think of unique keys defining where in the BST structure a node 
    gets inserted. 
    * And each node has a corresponding value
'''
''' BST Deletion
We can break up deletion in three cases:

Case 1: The node to be deleted is a leaf node (no children)
Case 2: The node to be deleted has one child
Case 3: The node to be deleted has both children. 
'''

class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild # Considers None as a False Value
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    def findSuccessor(self):
        succ = None
        # Check if node has a right subtree...
        if self.hasRightChild():
            # traverse through left children(min)
            succ = self.rightChild.findMin()
        return succ
    def spliceOut(self):
        # Case 1: 
        # If node to be removed is a leaf, set parent's left 
        # or right child reference to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        # Case 2:
        # Not a leaf node. Should only have a right child for BST maintenance
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    def findMin(self):
        # Try to walk down as left as possible until it can't anymore
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


