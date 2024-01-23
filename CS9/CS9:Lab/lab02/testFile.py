from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

b1 = Beverage(16, 20.0)
b2 = Beverage(13, 5.5)
b3 = Beverage(20, 18.324)
b4 = Beverage(17, 17.698)
def testBev():
    assert b1.getInfo() == "16 oz, $20.00"
    assert b2.getInfo() == "13 oz, $5.50"
    assert b3.getInfo() == "20 oz, $18.32"
    assert b4.getInfo() == "17 oz, $17.70"
    b1.updateOunces(15)
    b1.updatePrice(6.2)
    assert b1.getOunces() == 15
    assert b1.getPrice() == 6.2


c1 = Coffee(16, 20.0, "Espresso")
c2 = Coffee(13, 5.5, "American")
c3 = Coffee(20, 18.324, "Capuccino")

def testCofeeConstructor():
    assert c1.ounces == 16
    assert c1.price == 20.00
    assert c1.style == "Espresso"
    assert c2.ounces == 13
    assert c2.price == 5.50
    assert c2.style == "American"
    assert c3.ounces == 20
    assert c3.price == 18.324
    assert c3.style == "Capuccino"

def test_CoffeeInfo():
    assert c1.getInfo() == "Espresso Coffee, 16 oz, $20.00"
    assert c2.getInfo() == "American Coffee, 13 oz, $5.50"
    assert c3.getInfo() == "Capuccino Coffee, 20 oz, $18.32"

f1 = FruitJuice(16, 20.0, ["Apple", "Guava"])
f2 = FruitJuice(13, 5.5,["Banana", "Mango", "Pineapple"])
f3 = FruitJuice(20, 18.324, [])
def test_FruitJuiceCOnstructor():
    assert f1.ounces == 16
    assert f1.price == 20.00
    assert f1.fruits == ["Apple", "Guava"]
    assert f2.ounces == 13
    assert f2.price == 5.50
    assert f2.fruits == ["Banana", "Mango", "Pineapple"]
    assert f3.ounces == 20
    assert f3.price == 18.324
    assert f3.fruits == []
def test_FruitJuiceInfo():
    assert f1.getInfo() == "Apple/Guava Juice, 16 oz, $20.00"
    assert f2.getInfo() == "Banana/Mango/Pineapple Juice, 13 oz, $5.50"
    assert f3.getInfo() == " Juice, 20 oz, $18.32"
d1 = DrinkOrder()
def test_DrinkOrderConstructor():
    assert d1.drinks == [] 
def test_DrinkOrdergetTotal():
    d1.addBeverage(c1)
    d1.addBeverage(f1)
    assert d1.getTotalOrder() == "Order Items:\n* Espresso Coffee, 16 oz, $20.00\n* Apple/Guava Juice, 16 oz, $20.00\nTotal Price: $40.00"
        











    