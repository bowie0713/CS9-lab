from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(Pizza):
    def __init__(self, time):
        self.time = time
        self.pizzas = []
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = time
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        str = ""
        count = 0
        for i in self.pizzas:
            str = str + i.getPizzaDetails()
            str = str + "\n"+"----"+"\n"
            count = count + i.getPrice()
        
        return "******\nOrder Time: {}\n{}TOTAL ORDER PRICE: ${:.2f}\n******\n".format(self.time, str, count)
cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)
#print(order.getOrderDescription())