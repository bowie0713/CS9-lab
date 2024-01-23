'''Linear Data Structure
* Elements are next to each other in a linear way
'''
#from pythonds.basic import Stack
#pytests

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def test_insertIntoStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    assert s.size() == 2
    assert s.peek() == "Hi"
    assert s.isEmpty() == False

def test_deleteFromStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    x = s.pop()
    assert x == "Hi"
    assert s.peek() == "There"
    assert s.size() == 1
    y = s.pop()
    assert y == "There"
    assert s.size() == 0
    assert s.isEmpty() == True

'''Queue
* a linear data structure that has the First In, FIrst Out (FIFO) property
'''
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def test_insertIntoQueue():
    q = Queue()
    assert q.isEmpty() == True
    assert q.size() == 0
    q.enqueue("Customer 1")
    q.enqueue("Customer 2")
    assert q.isEmpty() == False
    assert q.size()

def test_removeFromQueue():
    q = Queue()
    q.enqueue("Customer 1")
    q.enqueue("Customer 2")
    assert q.dequeue() == "Customer 1"
    assert q.isEmpty() == False
    assert q.size() == 1
    assert q.dequeue() == "Customer 2"
    assert q.isEmpty() == True
    assert q.size() == 0


''' Deque "Deck"
* Linear Data Structure more flexible than a stack and a queue
    * "Double-ended Queue"
    * Allows us to insert and remove from both sides
'''
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def test_Deque():
    d = Deque()
    assert d.isEmpty() == True
    assert d.size() == 0
    d.addFront(10)
    d.addFront(20)
    d.addRear(30)
    d.addRear(40)
    assert d.isEmpty() == False
    assert d.size() == 4
    assert d.removeFront() == 20
    assert d.removeRear() == 40
    assert d.isEmpty() == False
    assert d.size() == 2
    assert d.removeRear() == 30
    assert d.removeRear() == 10
    assert d.isEmpty() == True
    assert d.size() == 0