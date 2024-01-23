class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        if name == None:
            self.name = name
        elif type(name) == str:
            self.name = name.upper()
        if species == None:
            self.species = species
        elif type(species) == str:
             self.species = species.upper()
        self.weight = weight
        self.age = age
    
    def setSpecies(self, species): 
        self.species = species.upper()
    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return("Species: {}, Name: {}, Age: {}, Weight: {}" \
                .format(self.species, self.name, self.age, self.weight))

#a = Animal("dog", weight=12.2, age=2, name = "Ruffles")
#print(a.toString())

