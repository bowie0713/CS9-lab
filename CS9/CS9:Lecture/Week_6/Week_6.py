from LinkedList import LinkedList, Node

def test_NodeCreation():
    n = Node(20)
    assert n.getData() == 20
    assert n.getNext() == None
def test_NodeSetData():
    n = Node(20)
    n.setData(200)
    assert n.getData() == 200
def test_NodeSetNext():
    n = Node(20)
    n2 = Node(10)
    n.setNext(n2)
    assert n.getNext() == n2
    assert n.getNext().getData() == 10
def test_createList():
    ll = LinkedList()
    assert ll.isEmpty() == True
def test_addNodesToList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    assert ll.isEmpty() == False
    assert ll.length() == 3
    assert ll.search(10) == True
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9")   == False 
def test_addNodesToList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    ll.addToFront("CS9")
    assert ll.length() == 4
    assert ll.search(10) == True
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9")  == True 
    ll.remove(10)
    assert ll.search(10) == False
    assert ll.length() == 3
    assert ll.search(False) == True
    ll.remove(False) 
    assert ll.search(False) == False
    assert ll.length() == 2
    assert ll.search("CS9") == True
    ll.remove("CS9")
    assert ll.search("CS9") == False
def test_InsertIntoOrderedLinkedList():
    ll = LinkedList()
    ll.add(35)
    ll.add(50)
    ll.add(10)
    ll.add(40)
    ll.add(20)
    ll.add(30)
    assert ll.getList() == "10 20 30 35 40 50"
    ll.add(5)
    assert ll.getList() == "5 10 20 30 35 40 50"
    ll.add(60)
    assert ll.getList() == "5 10 20 30 35 40 50 60"

'''Quadratic Sorting Algorithms 
* We've discussed searching throught a list
    * Linear Search - start at the beginning and check every element in the list
        * Does not need to be sorted
    * Binary Search - check the middle, then check left or right sub lists
        * This does need to be sorted
'''
''' Bubble Sort:
* Idea: it will make several passes through the list and swap adjacent elements
to ensure the largest element ends up at the end of the list
(assuming we're sorting in ascending order).
'''

def bubbleSort(aList):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                #swap
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
                print(i)
                print(passnum)
                print(aList)
list4 = [1, 10, 3, 7, 9, 5]
bubbleSort(list4)

def test_bubbleSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    bubbleSort(list1)
    assert list1 == [1,2,3,4,5,6]
    bubbleSort(list2)
    assert list2 == [2,2,2,2,2,2]
    bubbleSort(list3)
    assert list3 == []
    bubbleSort(list4)
    assert list4 == [1,3,5,6,7]

'''Selection Sorts
* Idea: Similar to Bubble sort, we make passes through the list 
and find the largest element. We then swap the largest element 
in the correct place. (One swap per iteration)
'''
def SelectionSort(aList):
    for fillslot in range(len(aList)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location
        # swap largest element in correct place
        temp = aList[fillslot]
        aList[fillslot] = aList[positionOfMax]
        aList[positionOfMax] = temp
def test_SelectioSsort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    SelectionSort(list1)
    assert list1 == [1,2,3,4,5,6]
    SelectionSort(list2)
    assert list2 == [2,2,2,2,2,2]
    SelectionSort(list3)
    assert list3 == []
    SelectionSort(list4)
    assert list4 == [1,3,5,6,7]
'''Insert Sort 
Idea: We want to work left-to-right and insert unsorted elements into
the sorted right portion of the list.'''

def InsertionSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        position  = index
        # shift elements to make room for insertion
        while position > 0 and aList[position-1] > currentValue:
            aList[position] = aList[position-1]
            position = position-1
        # insert element in appropriate place
        aList[position] = currentValue
        

def test_InsertionSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    InsertionSort(list1)
    assert list1 == [1,2,3,4,5,6]
    InsertionSort(list2)
    assert list2 == [2,2,2,2,2,2]
    InsertionSort(list3)
    assert list3 == []
    InsertionSort(list4)
    assert list4 == [1,3,5,6,7]
