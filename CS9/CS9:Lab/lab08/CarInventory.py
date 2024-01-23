from Car import *
from CarInventoryNode import CarInventoryNode
class CarInventory(CarInventoryNode):
    def __init__(self):
        self.root = None
    def addCar(self, car):
        if self.root:
            self._add(car, self.root)
        else:
            self.root = CarInventoryNode(car)
        
    def _add(self, car, currentNode):
        if (car.make == currentNode.make) and (car.model == currentNode.model) :
            currentNode.cars.append(car)
            return
        if car < currentNode.cars[0]:
            if currentNode.left:
                self._add(car, currentNode.left)
            else:
                newNode = CarInventoryNode(car)
                currentNode.setLeft(newNode)
                newNode.setParent(currentNode)
        else:
            if currentNode.right:
                self._add(car, currentNode.right)
            else:
                newNode = CarInventoryNode(car)
                currentNode.setRight(newNode)
                newNode.setParent(currentNode)
    '''def get(self, key): # returns payload for key if it exists
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        else:
            return None'''
    '''def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)'''
    def doesCarExist(self, car):
        if self.root:
            res = self._get(car, self.root)
            if res:
                mylist = res.cars
                for i in mylist:
                    if car == i:
                        return True
            return False
        else:
            return False
    def _get(self, car, currentNode):
        if not currentNode:
            return None
        elif (car.make.upper() == currentNode.make.upper()) and (car.model.upper() == currentNode.model.upper()):
            return currentNode
        elif car.make.upper() < currentNode.make:
            return self._get(car, currentNode.left)
        elif (car.make.upper() == currentNode.make.upper()) and  (car.model.upper() < currentNode.model.upper()):
            return self._get(car, currentNode.left)
        else:
            return self._get(car, currentNode.right)

         
    def inOrder(self):
        # current = self.root # a root node
        # self.root.left # left node
        # self.root.right # right node
        return self._inOrder(self.root)
        
    def _inOrder(self, carnode): # recurisvely call itself to call a string
        ret = ""
        if carnode:
            ret += self._inOrder(carnode.left)
            ret += str(carnode)
            ret += self._inOrder(carnode.right)
        return ret
    def preOrder(self):
        return self._preOrder(self.root)
    def _preOrder(self, carnode):
        ret = ""
        if carnode:
            ret += str(carnode)
            ret += self._preOrder(carnode.left)
            ret += self._preOrder(carnode.right)
        return ret
        
    def postOrder(self):
        return self._postOrder(self.root)
    def _postOrder(self, carnode):
        ret = ""
        if carnode:
            ret += self._postOrder(carnode.left)
            ret += self._postOrder(carnode.right)
            ret += str(carnode)
        return ret
    def getBestCar(self, make, model):
        if self.root:
                res = self._getbest(make, model, self.root)
                if res:
                    max = res.cars[0]
                    for i in range (0, len(res.cars), 1):
                        if res.cars[i].year > max.year:
                            max = res.cars[i]
                        elif res.cars[i].year == max.year:
                            if res.cars[i].price > max.price:
                                max = res.cars[i]
                    return max
        else:
            return None
    def _getbest(self, make, model, currentNode):
        if not currentNode:
            return None
        elif (currentNode.make == make.upper()) and (currentNode.model == model.upper()):
            return currentNode
        elif make.upper() < currentNode.make:
            return self._getbest(make, model, currentNode.left)
        elif (make.upper() == currentNode.make) and  (model.upper() < currentNode.model):
                return self._getbest(make, model, currentNode.left)
        else:
            return self._getbest(make, model, currentNode.right)
    def getWorstCar(self, make, model):
        if self.root:
                res = self._getworst(make, model, self.root)
                if res:
                    min = res.cars[0]
                    for i in range (0, len(res.cars), 1):
                        if res.cars[i].year < min.year:
                            min = res.cars[i]
                        elif res.cars[i].year == min.year:
                            if res.cars[i].price < min.price:
                                min = res.cars[i]
                    return min
        else:
            return None
    def _getworst(self, make, model, currentNode):
        if not currentNode:
            return None
        elif (currentNode.make == make.upper()) and (currentNode.model == model.upper()):
            return currentNode
        elif make.upper() < currentNode.make:
            return self._getbest(make, model, currentNode.left)
        elif (make.upper() == currentNode.make) and  (model.upper() < currentNode.model):
                return self._getbest(make, model, currentNode.left)
        else:
            return self._getbest(make, model, currentNode.right)
    
    def getTotalInventoryPrice(self):
        return self._getTotal(self.root)
    def _getTotal(self, carnode):
        a = 0
        if carnode:
            for i in carnode.cars:
                a += i.price
            a += self._getTotal(carnode.left)
            a += self._getTotal(carnode.right)
        return a
    
            
        
        
bst = CarInventory()

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)
car6 = Car("Honda", "Bowie", 2023, 15000)
car7 = Car("Honda", "Bowie", 2023, 15000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)


# print(bst.inOrder())
# print(bst.getTotalInventoryPrice())
# print(bst.doesCarExist(car7))

#print(bst.getBestCar("Nissan", "Leaf"))

'''print(bst.getBestCar("Nissan", "Leaf"))
print(bst.getBestCar("Tesla", "Model3"))
print(bst.getBestCar("Mercedes", "Sprinter"))
print(bst.getBestCar("Honda", "Accord"))

print(bst.getWorstCar("Nissan", "Leaf"))
print(bst.getWorstCar("Mercedes", "Sprinter"))
print(bst.getBestCar("Honda", "Accord"))'''