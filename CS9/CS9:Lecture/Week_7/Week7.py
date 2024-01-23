'''Divide and Conquer Algorithms
* Subdivide a larger problem into smaller problems
* Solve each smaller part
* Combine solutions of smaller sub problems back into 
the larger problems
'''

'''Mergesort
* Idea: Break a list into sublists where the size == 1
    * Sublist with 1 element is considered sorted
    * Merge each small sorted sublist together to form a larger sorted list
    * Continue to merge sublists back into the original list.
'''
def mergeSort(alist): # this methoe takes up extra memory
    if len(alist) > 1:
        mid = len(alist) // 2

        #uses additional space to create left/right halves
        lefthalf = alist[:mid] 
        righthalf = alist[mid:]

        #recusively sortts the lefthalf, then righthalf
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # merge two sorted sublists (left/right half) into aList
        i = 0 # index for lefthalf
        j = 0 # index for righthalf
        k = 0 # index for alist

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        # put the remaining lefthalf elements (if any) into aList
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        # put the remaining righthalf elements (if any) into aList
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


# Tests!
def test_mergeSort():
    numList1 = [9,8,7,6,5,4,3,2,1]
    numList2 = [1,2,3,4,5,6,7,8,9]
    numList3 = []
    numList4 = [1,9,2,8,3,7,4,6,5]
    numList5 = [5,6,4,7,3,8,2,9,1]
    mergeSort(numList1)
    mergeSort(numList2)
    mergeSort(numList3)
    mergeSort(numList4)
    mergeSort(numList5)

    assert numList1 == [1,2,3,4,5,6,7,8,9]
    assert numList2 == [1,2,3,4,5,6,7,8,9]
    assert numList3 == []
    assert numList4 == [1,2,3,4,5,6,7,8,9]
    assert numList5 == [1,2,3,4,5,6,7,8,9]

'''Analysis:
* Mergesort breaks the list into two EQUAL parts recursively
* Merge Sort breaks the list into two equal parts per recursive iteration
* Note that the height (number of levels) of the tree is log n (for 8 nodes, we have a height of 3).
* For each level, the merge step needs to compare n elements
    * So if there are log n levels and we need to do n comparisons to merge the elements for each level, then we have: O(n log n) running time
* One disadvantage of Merge Sort is it requires O(n) additional space when creating the left and right sublists
    * Can be problematic if the list we are trying to sort is extremely large
'''

'''QuickSort
* Another divide-and-conquer algorithm
* Has running times of O(n log(n))in a typical cas, but we'll see 
how this can also lead to O(n^2) in a worst-case scenario
* Idea
    * Can sort a list by subdivising the list based on a PIVOT value
        * Place elements < pivot to the left-side of the list
        * Place elements > pivot to the right-side of the list
        * Recurse for each left/right portion of the list
        * When sub list sizes == 1, then the entire list is sorted. 
How do we partition the list into left/right sub lists?
* Choose pivot (since elements are random, choose 1st element [0] in the list).
* Find an element in the left side (using leftmark index starting at 
the beginning of the list just past the pivot that will move from 
left to right) that's out-of-place (> pivot)
* Find an element in the right side (using rightmark index starting at
the end of the list moving from right to left) that's out-of-place (< pivot)
* Swap out-of-place elements with each other 
    * We're just putting them in the correct side of thelist
* Continue doing this until the rightmark index < leftmark index
    * Swap the pivot element with rightmark 
        * We're just putting the pivot element in the correct place!
'''
# partition function that will organize left sub list 
# < pivot, and right sub list > pivot (returns index of where pivot is placed)
def partition(aList, first, last):
    pivotvalue = aList[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # move leftmark until we find a left element that's greater than the pivot value
        # Find value that's out of place
        while leftmark <= rightmark and aList[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # move rightmark until we find a right element < pivotvalue
        while rightmark >= leftmark and aList[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        # check if we are done swapping left/right elements into correct side
        if rightmark < leftmark:
            done = True # will break the outer while loop
        else: #swap left and right elements into correct side of the list
            temp = aList[leftmark]
            aList[leftmark] = aList[rightmark]
            aList[rightmark] = temp
    # put the pivot value into the correct place
    temp = aList[first]
    aList[first] = aList[rightmark]
    aList[rightmark] = temp

    return rightmark

    

# Helper Function so we can pass in the first/last index of the lists
def quickSortHelper(aList, first, last):
    if first < last:

        # will define the index of the left / right sub lists
        splitpoint = partition(aList, first, last)

        # recursively sort the left/right sub lists
        quickSortHelper(aList, first, splitpoint-1)
        quickSortHelper(aList, splitpoint+1, last)

def quickSort(aList):
    quickSortHelper(aList, 0, len(aList)-1)

def test_quickSort():
    numList1 = [9,8,7,6,5,4,3,2,1]
    numList2 = [1,2,3,4,5,6,7,8,9]
    numList3 = []
    numList4 = [1,9,2,8,3,7,4,6,5]
    numList5 = [5,6,4,7,3,8,2,9,1]
    quickSort(numList1)
    quickSort(numList2)
    quickSort(numList3)
    quickSort(numList4)
    quickSort(numList5)

    assert numList1 == [1,2,3,4,5,6,7,8,9]
    assert numList2 == [1,2,3,4,5,6,7,8,9]
    assert numList3 == []
    assert numList4 == [1,2,3,4,5,6,7,8,9]
    assert numList5 == [1,2,3,4,5,6,7,8,9]







