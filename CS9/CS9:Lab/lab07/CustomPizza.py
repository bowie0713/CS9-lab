from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        if size == "S":
            super().__init__(size)
            super().setPrice(8.00)
        elif size == "M":
            super().__init__(size)
            super().setPrice(10.00)
        elif size == "L":
            super().__init__(size)
            super().setPrice(12.00)
        self.topping = []
    def addTopping(self, topping):
        self.topping.append(topping)
        if super().getSize() == "L":
                x = super().getPrice()
                super().setPrice(x + 1.00)
        elif super().getSize() == "M":
                x = super().getPrice()
                super().setPrice(x + 0.75)
        elif super().getSize() == "S":
                x = super().getPrice()
                super().setPrice(x + 0.50)
    def getPizzaDetails(self):
        str = ""
        for i in self.topping:
            str += "\n\t+ " + i 
        return "CUSTOM PIZZA\n\
Size: {}\n\
Toppings:{}\n\
Price: ${:.2f}\n".format(super().getSize(), str, super().getPrice())

cp1 = CustomPizza("S")
#print(cp1.getPizzaDetails())

cp2 = CustomPizza("L")
cp2.addTopping("extra cheese")
cp2.addTopping("sausage")
#print(cp2.getPizzaDetails())




