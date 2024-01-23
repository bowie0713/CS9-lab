from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getBestApartment
from lab06 import getWorstApartment
from lab06 import getAffordableApartments

def test_lessthan():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(500, 250, "bad")
    assert a1 < a0 == True
    assert a0 < a1 == False
    assert a2 < a3 == True
    assert a3 < a2 == False
    assert (a1 == a2) == True
    assert (a1 == a3) == False
    assert a1 > a0 == True
    assert a0 > a1 == False
    assert a2 > a3 == False
    assert a3 > a2 == True

def test_method1():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert apartmentList[1].getApartmentDetails() == "(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"
    assert ensureSortedAscending(apartmentList) == False
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"
    assert getAffordableApartments(apartmentList, 950) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent\n(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent\n(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"
    #print(getAffordableApartments(apartmentList, 950))
def test_method2():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    assert apartmentList[3].getApartmentDetails() == "(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: excellent"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    assert getAffordableApartments(apartmentList, 1000) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\n(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent\n(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average\n(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: excellent"
    #print(getAffordableApartments(apartmentList, 1000))
