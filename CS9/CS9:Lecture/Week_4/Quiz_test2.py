class Person:
  def __init__(self, name = "", weight = 0):
     self.name = name
     self.weight = weight
  def setName(self, name):
     self.name = name
  def setWeight(self, weight):
     self.weight = weight
  def getInfo(self):
     return "Name: {}, Weight: {}".format(self.name, self.weight)
  
p1 = Person("Thor", 250)
p2 = Person()

assert p1.name == "Thor"
assert p1.weight == 250
assert p2.name == ""
assert p2.weight == 0
assert p1.getInfo() == "Name: Thor, Weight: 250"
assert p2.getInfo() == "Name: , Weight: 0"
p1.setName("Roar")
p1.setWeight(300)
assert p1.getInfo() == "Name: Roar, Weight: 300"

print(p1.getInfo())