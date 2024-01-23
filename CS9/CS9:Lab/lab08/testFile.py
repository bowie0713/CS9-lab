from Car import *
from CarInventory import *
from CarInventoryNode import *

def test_comparison():
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car8 = Car("Ford", "Power", 2021, 25000)
    car6 = Car("Honda", "Bowie", 2023, 15000)
    car7 = Car("Honda", "Bowie", 2023, 15000)

    assert (car6 == car7) == True
    assert (car6 == car7) != False
    assert (car1 > car2) == False
    assert (car1 < car2) == True
    assert (car3 > car4) == True
    assert (car3 < car4) == False
    assert (car5 > car8) == True
    assert (car8 > car5) == False
    assert str(car1) == "Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000"
    assert str(car5) == "Make: FORD, Model: RANGER, Year: 2021, Price: $25000"
def test_node():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    assert str(carNode) == "Make: DODGE, Model: DART, Year: 2015, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n"
    carNode2 = CarInventoryNode(car3)
    assert str(carNode2) == "Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n"
    carNode2.cars.append(car4)
    assert str(carNode2) == "Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\nMake: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n"
    carNode3 = CarInventoryNode(car5)
    assert str(carNode3) == "Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n"
def test_CarInventory():
    bst = CarInventory()
    car1 = Car("Toyota", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model100", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car11 = Car("Ford", "Power", 2021, 25000)
    car6 = Car("Honda", "Bowie", 2023, 15000)
    car7 = Car("Honda", "Bowie", 2023, 15000)
    car8 = Car("Honda", "Hi", 2000, 10000)
    car9 = Car("hoNda", "Antique", 1900, 100000)
    car10 = Car("BMW", "720", 2015, 15000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car11)
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car3)
    assert bst.doesCarExist(car7) == False
    bst.addCar(car6)
    bst.addCar(car7)
    assert bst.doesCarExist(car7) == True
    bst.addCar(car8)
    bst.addCar(car9)
    bst.addCar(car10)
    assert bst.inOrder() == \
"""\
Make: BMW, Model: 720, Year: 2015, Price: $15000
Make: FORD, Model: POWER, Year: 2021, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: HONDA, Model: ANTIQUE, Year: 1900, Price: $100000
Make: HONDA, Model: BOWIE, Year: 2023, Price: $15000
Make: HONDA, Model: BOWIE, Year: 2023, Price: $15000
Make: HONDA, Model: HI, Year: 2000, Price: $10000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL100, Year: 2018, Price: $50000
Make: TOYOTA, Model: LEAF, Year: 2018, Price: $18000
"""
    assert bst.preOrder() == \
"""\
Make: TOYOTA, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL100, Year: 2018, Price: $50000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: FORD, Model: POWER, Year: 2021, Price: $25000
Make: BMW, Model: 720, Year: 2015, Price: $15000
Make: HONDA, Model: BOWIE, Year: 2023, Price: $15000
Make: HONDA, Model: BOWIE, Year: 2023, Price: $15000
Make: HONDA, Model: ANTIQUE, Year: 1900, Price: $100000
Make: HONDA, Model: HI, Year: 2000, Price: $10000
"""
    #print(bst.postOrder())
    assert bst.postOrder() == \
"""\
Make: BMW, Model: 720, Year: 2015, Price: $15000
Make: FORD, Model: POWER, Year: 2021, Price: $25000
Make: HONDA, Model: ANTIQUE, Year: 1900, Price: $100000
Make: HONDA, Model: HI, Year: 2000, Price: $10000
Make: HONDA, Model: BOWIE, Year: 2023, Price: $15000
Make: HONDA, Model: BOWIE, Year: 2023, Price: $15000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL100, Year: 2018, Price: $50000
Make: TOYOTA, Model: LEAF, Year: 2018, Price: $18000
"""
    assert bst.getBestCar("Toyota", "Leaf") == car1
    assert bst.getBestCar("Honda", "Bowie") == car6
    assert bst.getTotalInventoryPrice() == 338000
    car12 = Car("Honda", "Bowie", 2020, 15000)
    car13 = Car("Honda", "Bowie", 2023, 50000)
    bst.addCar(car12)
    bst.addCar(car13)
    assert bst.getBestCar("A", "B") == None
    assert bst.getBestCar("Honda", "bOWIE") == car13
    assert bst.getBestCar("Ford", "ranger") == car5
    assert bst.getWorstCar("Ford", "ranger") == car5
    assert bst.getWorstCar("A", "C") == None
    assert bst.getWorstCar("honda", "bowie") == car12
    assert bst.getWorstCar("Toyota", "Leaf") == car1
    assert bst.getTotalInventoryPrice() == 403000
     
test_CarInventory()




