from Week_9 import TreeNode
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1
    # helper method to recursively walk down the tree
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = \
                TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = \
                TreeNode(key, val, parent = currentNode)
    def get(self, key): # returns payload for key if it exists
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        else:
            return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
    def delete(self, key):
        if self.size >1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove) # modify tree
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size -1
        else:
            raise KeyError('Error, key not in tree')
    def remove(self, currentNode):
        # Case 1: Node to remove is leaf
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # Case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            # Need to find the successor, remove successor, and replace 
            # current Node with successor's data / paylod
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # Case 2: Node to remove has one child
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.leftChild.key, 
                                                currentNode.leftChild.payload, 
                                                currentNode.leftChild.leftChild, 
                                                currentNode.leftChild.rightChild)
            # Node has rightChild
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.rightChild.key, 
                                                currentNode.rightChild.payload, 
                                                currentNode.rightChild.leftChild, 
                                                currentNode.rightChild.rightChild)
    def countPayload(self, num):
        return self._countPayload(num, self.root)
    def _countPayload(self, num, node):
        count = 0
        if node == None:
            return 0
        if node != None:
            temp = []
            temp.append(self._countPayload(num, node.leftChild))
            temp.append(node.payload)
            temp.append(self._countPayload(num, node.rightChild))
            print(temp)
            for i in temp:
                if i == num:
                    count += 1
            return count
    

    def inOrder(self, node):
        ret = ""
        if node != None:
            ret += self.inOrder(node.leftChild)
            ret += str(node.key) + " "
            ret += self.inOrder(node.rightChild)
        return ret
    

BST = BinarySearchTree()
assert BST.countPayload(10) == 0
BST.put("F", 10)
print(BST.countPayload(10) == 1)
print(BST.countPayload(20) == 0)
BST.put("B", 5)
BST.put("G", 15)
BST.put("A", 20)
BST.put("J", 10)
BST.put("M", 10)
print(BST.countPayload(30) == 0)
print(BST.countPayload(10) == 3)
print(BST.countPayload(20) == 1)
# pytest for put
'''def test_insertRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    assert BST.root.key == 10
    assert BST.root.payload == "ten"
    assert BST.root.hasLeftChild() == None
    assert BST.root.hasRightChild() == None

def test_insertNode():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(20, "twenty")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    assert BST.root.key == 10
    assert BST.root.leftChild.key == 5
    assert BST.root.rightChild.key == 20
    assert BST.root.rightChild.leftChild.key == 15
# pytests for deletion
def test_deleteSingleRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    assert BST.root.key == 10

def test_deleteRootOneChild():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(5, "five")
    assert BST.inOrder(BST.root) == "5 10 "
    BST.delete(10)
    assert BST.inOrder(BST.root) == "5 "
    assert BST.root.key == 5
def test_deleteLeaf():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(2, "two")
    assert BST.inOrder(BST.root) == "2 5 10 15 "
    BST.delete(15)
    assert BST.inOrder(BST.root) == "2 5 10 "
    BST.delete(2)
    assert BST.inOrder(BST.root) == "5 10 "
def test_deleteNodeOneChild():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(2, "two")
    assert BST.root.leftChild.key == 5
    BST.delete(5)
    assert BST.inOrder(BST.root) == "2 10 15 "
    assert BST.root.leftChild.key == 2
    assert BST.root.leftChild.parent.key == 10

def test_deleteRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    assert BST.inOrder(BST.root) == "3 5 7 10 12 15 17 "
    BST.delete(10)
    assert BST.inOrder(BST.root) == "3 5 7 12 15 17 "
def test_DeletenodeWithTwoChildren():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    BST.delete(15)
    assert BST.inOrder(BST.root) == "3 5 7 10 12 17 "
    BST.delete(5)
    assert BST.inOrder(BST.root) == "3 7 10 12 17 "
'''






