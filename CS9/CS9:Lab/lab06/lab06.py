from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        #uses additional space to create left/right halves
        lefthalf = apartmentList[:mid] 
        righthalf = apartmentList[mid:]
        #recusively sortts the lefthalf, then righthalf
        mergesort(lefthalf)
        mergesort(righthalf)
        # merge two sorted sublists (left/right half) into aList
        i = 0 # index for lefthalf
        j = 0 # index for righthalf
        k = 0 # index for alist

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].__lt__(righthalf[j]):
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1
        # put the remaining lefthalf elements (if any) into aList
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        # put the remaining righthalf elements (if any) into aList
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1
def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList)-1):
        if apartmentList[i].__lt__(apartmentList[i+1]) == False:
            return False
    return True
def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()
def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()
def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    str = ""
    for i in apartmentList:
        if i.getRent() <= budget:
            str = str + i.getApartmentDetails() + "\n"
    return str.strip()


'''a0 = Apartment(1115, 215, "bad")
a1 = Apartment(950, 215, "average")
a2 = Apartment(950, 215, "excellent")
a3 = Apartment(950, 190, "excellent")
a4 = Apartment(900, 190, "excellent")
a5 = Apartment(500, 250, "bad")
apartmentList = [a0, a1, a2, a3, a4, a5]


print('apartmentList is NOT SORTED:')
for apartment in apartmentList: 
    print(apartment.getApartmentDetails())
mergesort(apartmentList)
print('apartmentList is SORTED:')
for apartment in apartmentList: 
    print(apartment.getApartmentDetails())'''





