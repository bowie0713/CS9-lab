from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = []
    def addBeverage(self, beverage):
        self.drinks.append(beverage)
    def getTotalOrder(self):
        str = "Order Items:" + "\n"
        x = 0
        for i in self.drinks:
            if isinstance(i, Coffee) == True:
                str = str + "* " + i.getInfo() + "\n"
                x = x + i.getPrice()
            elif isinstance(i, FruitJuice) == True:
                str = str + "* " + i.getInfo() + "\n"
                x = x + i.getPrice()
        str = str + "Total Price: ${:.2f}".format(x)
        return str

'''c1 = Coffee(8, 3.0, "Espresso")
juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
order = DrinkOrder()
order.addBeverage(c1)
order.addBeverage(juice)
print(order.getTotalOrder())'''
'''order = DrinkOrder()
print(order.getTotalOrder())'''
               
    
    