# insert perform much worse than append

'''def f1(n): #O(n^2)
    l = []
    for i in range(n):
        l.insert(0,i)

def f2(n): #O(n)
    l=[]
    for i in range(n):
        l.append(i)'''


'''Python lists (under the hood) 
* Python Lists store items in CONTIGUOUS memory (one item is right next to the other)
* f(1) - insert function: The more element you have, the more movements(shift to the right) 
python lists need to do
* f(2) - append function: We are just adding something to the very end of python lists
No shifting are needed
'''

'''Binary Search Algorithm
* A useful and performant algorithms to earch for an item in a collection
IF THE ITEMS ARE IN SORTED ORDER
* Eliminating half the search space FOR EACH iteration 
is logarithmic (Olog(n))
    * Note that the base 2 isn't traditionally denoted unless the base is 
    something other than 2. 
'''

# Binary Search pytest

#1. Iterative approach
def binarySearch(intList, item):
    first = 0
    last = len(intList) -1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if intList[mid] == item:
            found = True
        else:
            if item < intList(mid):
                last = mid -1
            else:
                first = mid + 1
    return found

'''
#2. Recursive Approach
def binarySearch(intList, item):
    if len(intList) == 0: #base case
        return False
    mid = len(intList) // 2
    if intList[mid] == item:
        return True
    elif item < intList[mid]:
        return binarySearch(intList[:mid], item)
    else:
        return binarySearch(intList[mid+1:], item)
'''


def test_binarySearchNormal():
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 5) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], -1) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 11) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 1) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 10) == True

def test_binarySearchDuplicates():
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 0) == True
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 2) == False
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 4) == True

def test_binarySearchEmptyList():
    assert binarySearch([], 0) == False

def test_binarySearchSameValues():
    assert binarySearch([5,5,5,5,5,5,5,5], 5) == True
    assert binarySearch([5,5,5,5,5,5,5,5], 0) == False

# https://docs.google.com/presentation/d/1z-Ee46QQPVEHhZ-GuG61exLPUUeNDLjJevRPZl5aUXM/edit#slide=id.g23a97783dd0_0_222

def computePower(base, power):
    if power == 0:
        return 1
    return base * computePower(base, power-1)


assert computePower(3,3) == 27
assert computePower(3,0) == 1
assert computePower(-2,3) == -8
assert computePower(0,3) == 0

print(computePower(0,3))


