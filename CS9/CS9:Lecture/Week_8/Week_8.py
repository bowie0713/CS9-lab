'''Priority Queues
* Recall in a Queue structure, we can insert items from the back of the queue and 
remove items at the front of the queue. 
    * The order of elements in the queue were dictated by 
    when items were inserted into the queue. 
* Priority Queues are similar to Queues EXCEPT
    * We can insert items into the priority queue where an item has some
    value representing a priority, and items are ordered in the priority
    queue with respect to their priority value. 
'''

'''Heaps
* A heap is a COMPLETE binary tree
    * A BINARY TREE is a tree where a node has AT MOST two children.
    * A BALANCED binary tree: the left and right subtrees of EVERY node
    differ in height by no more than 1. 
    * A COMPLETE binary tree: Every level of the tree, except the deepest
    levevl, must contain as many nodes as possible. The deepest level must have 
    all nodes to the left as possible. 
'''

'''MaxHeap
* Complete tree where the value (priority) of a node is never less 
than the value of its children. 
'''

'''MinHeap
* The same as MaxHeap EXCEPT
    * The value (priority) of a node is never greater than the value 
    of its children. 
'''

'''Since binary heaps have the complete property, 
representing this with a Python list can be done. (need to be COMPLETE BINARY TREE)
    * Easier to represent the heap where the 0th [0]
    element in the list is meaningless
    * The root of the binary heap is at index 1 [1]
'''

'''
* A node's index with respect to its parent and children 
    * A node's parent index: node_index // 2
    * A node's left child index: 2 * node_index
    * A node's right child index: 2 * node_index + 1
'''

'''Insertion into a binary MaxHeap
* Insert the element in the first available location 
    * Note: this will be at the end of the list
* While the element's parent is less than the element
    * Swap the element with its parent
'''

'''Remove root element of a binary MaxHeap
* Since heaps are used to implement priority queues, 
removing the root element is a commonly used operation.
    * Copy the root element into a variable. 
    * Assign the last_element in the Python list to 
    the root position (new_root)
    * While new_root is less than one of its children 
        * Swap the largest child with the new_root
    * Return the original root element
'''
# Height: log(n)
# Insert: O(log(n))
# Remove: O(log(n))

# MinHeap
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self, i): # i is the index value we just insert
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                # swap 
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2
    def percDown(self, i):
        # we have at least a left child to check
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) # return index of min child
            if self.heapList[i] > self.heapList[mc]:
                # swap
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self, i):
        if (i * 2 + 1) > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def insert(self, k):
        self.heapList.append(k) # add to the last of the list
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
# pytest
def test_BinHeap():
	bh = BinHeap()
	bh.insert(5)
	bh.insert(7)
	bh.insert(3)
	bh.insert(11)
	assert bh.delMin() == 3
	assert bh.delMin() == 5
	assert bh.delMin() == 7
	assert bh.delMin() == 11

bh = BinHeap()
bh.insert(40)
bh.insert(20)
bh.insert(30)
bh.insert(50)
bh.insert(10)
bh.delMin()
print(bh.heapList)


