from Animal import Animal
class AnimalShelter(Animal):
    def __init__(self):
        self.shelter = {}
    def addAnimal(self, animal):
        if self.shelter.get(animal.species) == None:
            self.shelter[animal.species] = [animal]
            #print("Hello")
        elif self.shelter.get(animal.species) != None:
            self.shelter[animal.species].append(animal)
            #print("Hello")
    def removeAnimal(self, animal):
        if self.shelter.get(animal.species) != None:
            for i in self.shelter.values():
                for j in i:
                    if animal.name == j.name and animal.age == j.age and animal.weight == j.weight and animal.species == j.species:
                        self.shelter[animal.species].remove(animal)
                        #print("Hello")
    def removeSpecies(self, species):
        if self.shelter.get(species.upper()) != None:
                if species.upper() in self.shelter.keys():
                        self.shelter.pop(species.upper())
                #for item in self.shelter.values():
                    #or j in item:
                        #if self.shelter.age in j.age and self.shelter.name in item.name and self.shelter.weight in item.weight: 
    def getAnimalsBySpecies(self, species):
        str1 = ""
        if self.shelter.get(species.upper()) != None:
                if species.upper() in self.shelter.keys():
                    for item in self.shelter[species.upper()]:
                        str1 = str1 + item.toString() + "\n"    
                    return str1.strip()      
        else:
            return ""
    def doesAnimalExist(self, animal):
        if self.shelter.get(animal.species) != None:
            for i in self.shelter.values():
                for j in i: #runs through the objects in the list
                    #print("hello")
                    if animal.age == j.age and animal.weight == j.weight and animal.name == j.name and animal.species == j.species:
                        return True #print("True")
        return False
            
    '''def printing(self):
        for species in self.shelter:
            print("Species",species.upper())
            for animal in self.shelter[species]:
                print(animal.toString())
            print('---')'''
        
'''a = Animal(species = "dog", weight=12.2, age=2, name = "Ruffles")
b = Animal(species = "dog", weight = 10, age = 3, name = "Rab")
c = Animal(species = "DOG", weight = 11, age = 4, name = "Bowie")
box = AnimalShelter()
box.addAnimal(a)
box.addAnimal(b)
box.addAnimal(c)
box.removeAnimal(a)
#box.doesAnimalExist(b)
#print(box.getAnimalsBySpecies("dog"))
box.printing()
#box.printing()
#print(box.addAnimal(a))
#box.removeAnimal(a)
box.doesAnimalExist(a)
#box.removeSpecies(a)'''


