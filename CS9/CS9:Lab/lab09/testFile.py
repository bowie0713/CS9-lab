from CarInventory import *
from CarInventoryNode import *
def __eq__(self, rhs):
    return self == rhs
def test_successor():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    car6 = Car("No", "Hi", 2025, 50000)
    car7 = Car("Oi", "Nah", 2000, 30000)
    car8 = Car("BMW", "X5", 2020, 58000)
    car9 = Car("Car", "ai", 2000, 10000)
    car10 = Car("X", "what", 2013, 20000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    bst.addCar(car7)
    bst.addCar(car8)
    bst.addCar(car10)

    assert bst.getSuccessor("X", "what") == None
    assert str(bst.getSuccessor("BMW", "X5")) == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    assert str(bst.getSuccessor("No", "Hi")) == "Make: OI, Model: NAH, Year: 2000, Price: $30000\n"
    assert str(bst.getSuccessor("Audi", "A3")) == "Make: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\n"
test_successor()
def test_remove0():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    car6 = Car("No", "Hi", 2025, 50000)
    car7 = Car("Oi", "Nah", 2000, 30000)
    car8 = Car("BMW", "X5", 2020, 58000)
    car9 = Car("Car", "ai", 2000, 10000)
    car10 = Car("X", "what", 2013, 20000)

    cara = Car("Ax", "what", 2021, 24000)
    carb = Car("Bx", "sup", 2020, 30000)
    carc = Car("Cx", "ai", 2005, 15000)

    bst.addCar(cara)
    bst.addCar(carb)
    bst.addCar(carc)
    #print(bst.inOrder())
    assert bst.inOrder() == "Make: AX, Model: WHAT, Year: 2021, Price: $24000\nMake: BX, Model: SUP, Year: 2020, Price: $30000\nMake: CX, Model: AI, Year: 2005, Price: $15000\n"
    bst.removeCar("Cx", "ai", 2005, 15000)
    assert bst.inOrder() == "Make: AX, Model: WHAT, Year: 2021, Price: $24000\nMake: BX, Model: SUP, Year: 2020, Price: $30000\n"
    bst2 = CarInventory()
    bst2.addCar(car1)
    bst2.addCar(car9)
    bst2.addCar(car10)
    bst2.addCar(car7)
    assert bst2.inOrder() == "Make: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst2.removeCar("Oi", "Nah", 2000, 30000)
    assert bst2.inOrder() == "Make: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst2.removeCar("Car", "ai", 2000, 10000)
    assert bst2.inOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    #print(bst2.inOrder()) 
    #bst2.removeCar(car)
def test_remove1():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    car6 = Car("No", "Hi", 2025, 50000)
    car7 = Car("Oi", "Nah", 2000, 30000)
    car8 = Car("BMW", "X5", 2020, 58000)
    car9 = Car("Car", "ai", 2000, 10000)
    car10 = Car("X", "what", 2013, 20000)
    car11 = Car("D", "does", 1994, 26000)
    
    bst.addCar(car1)
    bst.addCar(car11)
    bst.addCar(car9)
    bst.addCar(car4)
    bst.addCar(car8)
    bst.addCar(car5)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: D, Model: DOES, Year: 1994, Price: $26000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: D, Model: DOES, Year: 1994, Price: $26000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    #print(bst.inOrder())
    bst.removeCar("Car", "ai", 2000, 10000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: D, Model: DOES, Year: 1994, Price: $26000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    bst.removeCar("Mazda", "CX-5", 2022, 25000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: D, Model: DOES, Year: 1994, Price: $26000\n"

    bst2 = CarInventory()
    bst2.addCar(car1)
    bst2.addCar(car6)
    bst2.addCar(car7)
    bst2.addCar(car10)
    assert bst2.inOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst2.removeCar("Mazda", "CX-5", 2022, 25000)
    assert bst2.inOrder() ==  "Make: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst2.removeCar("Oi", "Nah", 2000, 30000)
    assert bst2.inOrder() == "Make: NO, Model: HI, Year: 2025, Price: $50000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst2.removeCar("No", "Hi", 2025, 50000)
    bst2.removeCar("X", "what", 2013, 20000)
    bst2.inOrder() == ""

    bst3 = CarInventory()
    bst3.addCar(car1)
    bst3.addCar(car10)
    bst3.addCar(car7)
    bst3.addCar(car6)
    bst3.addCar(car2)
    assert bst3.inOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst3.removeCar("X", "what", 2013, 20000)
    assert bst3.inOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
def test_remove2():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    car6 = Car("No", "Hi", 2025, 50000)
    car7 = Car("Oi", "Nah", 2000, 30000)
    car8 = Car("BMW", "X5", 2020, 58000)
    car9 = Car("Car", "ai", 2000, 10000)
    car10 = Car("X", "what", 2013, 20000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    bst.addCar(car7)
    bst.addCar(car8)
    bst.addCar(car10)
    bst.addCar(car9)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst.removeCar("Tesla", "Model3", 2018, 50000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    #print(bst.inOrder())
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"
    bst.removeCar("Mazda", "CX-5", 2022, 25000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: CAR, Model: AI, Year: 2000, Price: $10000\nMake: NO, Model: HI, Year: 2025, Price: $50000\nMake: OI, Model: NAH, Year: 2000, Price: $30000\nMake: X, Model: WHAT, Year: 2013, Price: $20000\n"



