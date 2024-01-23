from Car import Car
class CarInventoryNode(Car):
    def __init__(self, car, right = None, left = None, parent = None):
        self.cars = [car]
        self.make = car.make
        self.model = car.model
        self.parent = left
        self.right = right
        self.left = parent
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right
    def __str__(self):
        a = ""
        for i in self.cars:
            a += str(i) + "\n"
        return a

'''car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
print(carNode)'''

