from Week_3 import Animal

class Cow(Animal): #contain everything from Animal class in Week_3 file
    def __init__(self, species=None, name=None, sound = None):
        # don't do self.species = species 
        #reuse parent class functionality
        super().__init__(species, name)
        self.sound = sound
    #Available method for Cow Class
    def setSound(self, sound):
        self.sound = sound
    def getSound(self): # can overide the method from the super/inherited class
        s = "Using Super class getSound method\n"
        s += super().getSound()
        #Animal.getSound(self)
        s += "Extending it with our functinoality\n"
        s += "{}!".format(self.sound)
        return s

c = Cow("Cow", "Betsy")
c.setSound("Moo")
print(c.getAttributes())
print(c.getSound())
#Inheritance Hierachy
'''a = Animal("Unicorm", "Lala")
print(a.getAttributes())
print(a.getSound())'''
c1 = Cow("Cow", "Betsy", "Moo")
print(c1.getAttributes())
print(c1.getSound())
