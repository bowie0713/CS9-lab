from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits
    def getInfo(self):
        str = ""
        for i in self.fruits:
            str = str + i + "/"
        str = str.strip("/")
        return "{} Juice, ".format(str) + super().getInfo()

'''juice = FruitJuice(16, 4.5, ["Guava", "Apple"])
print(juice.getInfo())'''