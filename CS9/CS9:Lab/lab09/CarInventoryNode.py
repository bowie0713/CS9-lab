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
    def findSuccessor(self):
        succ = None
        if self.right:
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.parent.left == self:
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    self.parent.right = self
        return succ

    # Find minimum value in a subtree by walking down the left children
    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current
    '''def spliceOut(self):
        if (self.left == None) and (self.right == None):
            #print('hi')
            if self.parent.left == self:
                #print('halo')
                self.parent.left = None
            else:
                #print("hola")
                self.parent.right = None

        # Case 2:
        # Not a leaf node. Should only have a right child for BST
        # removal
        elif (self.left) or (self.right):
            if self.left:
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent'''
'''car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
print(carNode)'''

