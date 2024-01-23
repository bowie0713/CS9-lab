'''LinkedList
* Python lists are just one way to implement a List type structure
* The underlying structure of a Python List uses the concept of storing
information in CONTIGUOUS memory
* There is another way to implement a List type structure that performs 
better in certain operations (and worse in others)
    * This doesn't organize data in contiguous memory, so maintaining 
    the list structure doesn't need to shift elements around
* LINKED LISTS are a list structure that is not stored in contiguous memory
    * But the structure still provides relative positioning of the data in the list

LINKED LISTS 
* An object that changes and maintains the chain of nodes as a collection
* Contains a HEAD reference to the first node in the LINKED LIST
    * As long as we know where the first element is, we can "walk down"
    the Linked List and visit every node in the structure
    * Methods in the LinkedList class should maintain the 
    links between the nodes
'''

class Node: #PIECES of linked list structure
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext 
''' Linked List Big-O Algorithm
* insert to the front: O(1)
* find middle index: O(n)
'''
class LinkedList:
    def __init__(self):
        self.head = None # no first node (our first attribute)
        # can do self.count = 0 (increment every time we take a step)
    def isEmpty(self):
        return self.head == None
    def addToFront(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext() # move down the List
        return count
    def search(self, item): #O(n) operation
        temp = self.head #always start in the beginning
        found = False
        while temp != None and not found:
            if temp.getData() == item:
                found = True
            else:
                temp = temp.getNext()
        return found
    def remove(self, item):
        current = self.head
        
        if current == None: # empty list, nothing to do
            return 
        previous = None
        found = False
        while not found: # Find the element, and move current and previos
            if current == None:
                return 
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # Case 1
        if found == True and previous == None:
            self.head = current.getNext()
        # Case 2
        if found == True and previous != None:
            previous.setNext(current.getNext())
    '''Ordered Linked Lists
* Is similar to an Unordered Linked List except 
the nodes in the list are ordered with respect to each other
'''
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        #find the correct place in the list to add
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        # create Node with item to add
        temp = Node(item)

        # Case 1: Insert at the front of the list
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    def getList(self):
        current = self.head
        output = ""
        while current != None:
            output += str(current.getData()) + " "
            current = current.getNext()
        output = output[:len(output)-1] # remove end space
        return output
    
ll = LinkedList()
ll.addToFront(10)
ll.addToFront(20)

l = LinkedList()
l.add(10)
l.add(20)
print(l.getList())







