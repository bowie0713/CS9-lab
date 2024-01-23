from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        if size == "S":
            super().__init__(size)
            super().setPrice(12.00)
        elif size == "M":
            super().__init__(size)
            super().setPrice(14.00)
        elif size == "L":
            super().__init__(size)
            super().setPrice(16.00)
        self.name = name
    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\n\
Size: {}\n\
Name: {}\n\
Price: ${:.2f}\n".format(super().getSize(), self.name, super().getPrice())

sp1 = SpecialtyPizza("S", "Carne-more")
#print(sp1.getPizzaDetails())

