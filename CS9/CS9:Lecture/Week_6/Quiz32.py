class Node:
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

class LinkedList:
    def __init__(self):
        self.head = None

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
            temp = temp.getNext()
        return count
    def countVowels(self):
        temp = self.head
        count = 0
        while temp != None:
            for i in temp.getData():
                if "A" in i.upper() or "E" in i.upper() or "I" in  i.upper() or "O" in  i.upper() or "U" in i.upper():
                    count = count +1
            temp = temp.getNext()
        return count
    def index(self, item):
        temp = self.head
        count = 0
        while temp != None:
            if temp.getData() == item:
                return count
            count = count + 1
            temp = temp.getNext()
        return 

    
def test_countVowels():
    ll = LinkedList()
    assert ll.countVowels() == 0
    ll.addToFront("xyz")
    assert ll.countVowels() == 0
    ll.addToFront("ABC")
    assert ll.countVowels() == 1
    ll.addToFront("def")
    assert ll.countVowels() == 2
    ll.addToFront("Audio")
    assert ll.countVowels() == 6
    ll.addToFront("CS9")
    assert ll.countVowels() == 6
