class Beverage:
    def __init__(self, ounces, price):
        self.ounces = ounces
        self.price = price
    def updateOunces(self, newOunces):
        self.ounces = newOunces
    def updatePrice(self, newPrice):
        self.price = newPrice
    def getOunces(self):
        return self.ounces
    def getPrice(self):
        return self.price
    def getInfo(self):
        return "{} oz, ${:.2f}".format(self.ounces, self.price)
        #return self.ounces + " oz, $" + "{:.2f}".format(self.price)

'''b4 = Beverage(17, 17.698)
print(b4.getInfo())'''