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
    
    
    def getSuccessor(self, make, model):
        return self._getSuccessor(make, model, self.root)
    def _getSuccessor(self, make, model, currentNode):
        node = self._get1(make, model, currentNode)
        succ = None
        if node:
            if node.right:
                succ = node.right
                while succ.left:
                    succ = succ.getLeft()
            else:
                parent = node.parent
                while parent and (node.cars[0] > parent.cars[0]):
                    parent = parent.getParent()
                if parent:
                    succ = parent
        return succ
    def _get1(self, make, model, currentNode):
        if not currentNode:
            return None
        elif (currentNode.make == make.upper()) and (currentNode.model == model.upper()):
            return currentNode
        elif make.upper() < currentNode.make:
            return self._get1(make, model, currentNode.left)
        elif (make.upper() == currentNode.make) and  (model.upper() < currentNode.model):
                return self._get1(make, model, currentNode.left)
        else:
            return self._get1(make, model, currentNode.right)
    
    
    def removeCar(self, make, model, year, price):
        if self.root:
            node = self._get2(make, model, self.root)
            if node:
                if len(node.cars) > 1:
                    for i in node.cars:
                        if i.year == year and i.price == price:
                            #print('remove')
                            node.cars.remove(i)
                            return True     
                elif len(node.cars) == 1:
                    if node.cars[0].year == year and node.cars[0].price == price:
                        node.cars.remove(node.cars[0])
                        #print('last remove')
                        return self._removeCar(node)
                else:
                    return False
            return False
        else:
            return False
    def _get2(self, make, model, currentNode):
        if not currentNode:
            return None
        elif (currentNode.make == make.upper()) and (currentNode.model == model.upper()):
            return currentNode
        elif make.upper() < currentNode.make:
            return self._get2(make, model, currentNode.left)
        elif (make.upper() == currentNode.make) and  (model.upper() < currentNode.model):
                return self._get2(make, model, currentNode.left)
        else:
            return self._get2(make, model, currentNode.right)
    def _removeCar(self, currentNode):
        # Case 1: Node to remove is leaf
        #if not currentNode:
            #return False
        if (currentNode.left == None) and (currentNode.right == None):
            if not currentNode.parent:
                self.root = None
                return True
            if currentNode.parent.left:
                currentNode.parent.left = None
                #print("Hi")
                return True
            else:
                currentNode.parent.right = None
                #print("Hi")
                return True 
        # Case 3: Node to remove has both children
        elif currentNode.getLeft() != None and currentNode.getRight() != None:
            # Need to find the successor, remove successor, and replace
            # currentNode with successor's data / payload
            succ = currentNode.findSuccessor()
            currentNode.cars = succ.cars
            currentNode.model = succ.model
            currentNode.make = succ.make
            self.spliceOut(succ)
            
            
            #print(succ)
            
            return True

        # Case 2: Node to remove has one child
        else:
            # Node has leftChild
            if currentNode.left:
                if currentNode.parent == None:
                    currentNode.left.setParent(None)
                    self.root = currentNode.left
                    return True
                elif currentNode.parent.left:
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                    #print("ho")
                    return True
                elif currentNode.parent.right:
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                    #print("ho")
                    return True  
                
            # Node has rightChild
            else:
                if currentNode.parent == None:
                    currentNode.right.setParent(None)
                    self.root = currentNode.right
                    return True
                elif currentNode.parent.left:
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                    #print('ho')
                    return True
                elif currentNode.parent.right:
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                    #print('ho')
                    return True             
        return False
    def spliceOut(self, currentNode):
        # Case 1:
        # If node to be removed is a leaf, set parent's left or right
        # child references to None
        if (currentNode.left == None) and (currentNode.right == None):
            if currentNode.parent.left is currentNode:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None

        # Case 2:
        # Not a leaf node. Should only have a right child for BST
        # removal
        elif (currentNode.left) or (currentNode.right):
            if currentNode.left:
                if currentNode.parent.left is currentNode:
                    currentNode.parent.left = (currentNode.left)
                else:
                    currentNode.parent.right = currentNode.left
                currentNode.left.parent = (currentNode.parent)
            else:
                if currentNode.parent.left is currentNode:
                    currentNode.parent.left = (currentNode.right)
                else:
                    currentNode.parent.right = (currentNode.right)
                currentNode.right.parent = (currentNode.parent)
    
            
     
'''bst = CarInventory()

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
bst.addCar(car5)'''

bst = CarInventory()
bst2 = CarInventory()

car1 = Car("Mazda", "CX-5", 2022, 25000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("BMW", "X5", 2022, 60000)
car4 = Car("BMW", "X5", 2020, 58000)
car5 = Car("Audi", "A3", 2021, 25000)
car6 = Car("No", "Hi", 2025, 50000)
car7 = Car("Oi", "Nah", 2000, 30000)
car8 = Car("BMW", "X5", 2020, 58000)
car9 = Car("Car", "ai", 2000, 10000)
car10 = Car("X", "what", 2013, 20000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)
bst.addCar(car6)
bst.addCar(car7)
bst.addCar(car8)
bst.addCar(car10)

'''bst2.addCar(car1)
bst2.addCar(car3)
bst2.addCar(car5)
bst2.addCar(car9)'''
#print(bst.inOrder())
bst.removeCar("Tesla", "Model3", 2018, 50000)
#print(bst2.inOrder())
#bst2.removeCar("Mazda", "CX-5", 2022, 25000)
#print(bst.inOrder())




#print(bst.inOrder())

#print(bst.getSuccessor("Nissan", "Leaf"))

#print(bst.root.right)

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

'''
Body: 
    * Hook
    * Def of Constitution
    * State that most revoluion countries fail to set up a legal basis in a country
    * Argue that this is a thing because revolutionary countries lack the 
    legal system and are politically unstable, but also 
'''