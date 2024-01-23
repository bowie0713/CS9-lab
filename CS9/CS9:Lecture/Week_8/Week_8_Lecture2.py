''' Binary Tree Implementation
* So far, we've talked about binary trees on a conceptual level when 
analyzing sorting algorithms 
* We've even talked about Binary Heaps that can be 
conceptualized as a COMPLETE binary tree
* Nodes and References Implementation
    * Similar to our Linked List representation, we can expand upon this 
    concept using nodes and references to construct our tree
    * Each node can be represented as an object
        * and each Node will have references to other nodes in the tree
'''
class BinaryTreeNode:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, newNode):
        # Case 1: Node does not have a left child
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a left child
            t = BinaryTreeNode(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self, newNode):
        # Case 1: NOde does not have a right child
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a right child
            t = BinaryTreeNode(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootValue(self, obj):
        self.key = obj
    def getRootValue(self):
        return self.key 

def test_createNode():
    node = BinaryTreeNode("A")
    assert node.getRootValue()
    assert node.getLeftChild() == None
    assert node.getRightChild() == None
def test_leftNode():
    node = BinaryTreeNode("A")
    node.insertLeft("B")
    assert node.getLeftChild().getRootValue() == "B"
    assert node.getRootValue() == "A"
    assert node.getRightChild() == None
    assert node.getLeftChild().getLeftChild() == None
    assert node.getLeftChild().getRightChild() == None
def test_insertLeft():
    node = BinaryTreeNode("A")
    node.insertLeft("B")
    node.insertLeft("C")
    node.insertLeft("D")

    temp = node
    s = ""

    while temp != None:
        s = s + temp.getRootValue()
        temp = temp.getLeftChild()
    assert s == "ADCB"
'''Tree Traversals
* Sometimes, we would want to visit all nodes in a tree
* We can do this in various ways, and the order of visiting the nodes may vary. 
* There are three common recursive ways to traverse nodes in a tree:
    * preorder: visit the node first, then recursively go down 
    the left subtree, then recursively go down the right subtree
    * inorder: recursively go down the left subtree, visit the node, 
    then recursively go down the right subtree. 
    * postorder: recursively go down the left subtree, then recursively go down 
    the right subtree, then we visit the node. 
'''

def preorder(tree):
    ret = ""
    if tree != None:
        ret += tree.getRootValue()
        ret += preorder(tree.getLeftChild())
        ret += preorder(tree.getRightChild())
    return ret
def inorder(tree):
    ret = ""
    if tree != None:
        ret += inorder(tree.getLeftChild())
        ret += tree.getRootValue()
        ret += inorder(tree.getRightChild())
    return ret
def postorder(tree):
    ret = ""
    if tree != None:
        ret += postorder(tree.getLeftChild())
        ret += postorder(tree.getRightChild())
        ret += tree.getRootValue()
    return ret
def test_preorder():
    # Create tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.insertRight("C")
    root.getRightChild().insertLeft("E")
    root.getRightChild().insertRight("F")
    assert preorder(root) == "ABDCEF"
def test_ineorder():
    # Create tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.insertRight("C")
    root.getRightChild().insertLeft("E")
    root.getRightChild().insertRight("F")
    assert inorder(root) == "DBAECF"
def test_postorder():
    # Create tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.insertRight("C")
    root.getRightChild().insertLeft("E")
    root.getRightChild().insertRight("F")
    assert postorder(root) == "DBEFCA"

''' Binary Search Tree (BST)
* Binary SEARCH Trees are binary trees that have the following property
    * Values that are less than the parent are found in the left subtree
    * Values that are greater than the parent are found in the right subtree
    * This is known as the BST PROPERTY
* Binary Search Trees are also one way to implement a MAP Abstract Data Type. 
    * Think of unique keys defining where in the BST structure a node 
    gets inserted. 
    * And each node has a corresponding value
    * Similar to how Python Dictionaries work on a high-level 
    (but the underlying implementation between a Python Dictionary 
    and BST are different (each with pros / cons))
'''



