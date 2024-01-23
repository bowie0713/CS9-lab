def biggestInt(a,b,c,d):
    biggest = 0
    if a >= b and a >= c and a >= d:
        biggest = a
    if b >=a and b>=c and b>=d:
        biggest = b
    if c >= a and c>=b and c>=d:
        biggest = c
    else:
        biggest = d
    return biggest
class Student1:
    def __init__(self, name=None, perm=None):
        self.name = name
        self.perm = perm
    def setName(self, name):
        self.name = name # give it a value 
    def setPerm(self, perm):
        self.perm = perm
    def printAttributes(self):
        print("Student name: {}, perm: {}" \
                .format(self.name, self.perm))
    def __eq__ (self, rhs):
        return self.perm == rhs.perm
    def __str__(self):
        return "Student name:{}, perm: {}".format(self.name, self.perm)
    "+"
    def __add__(self, rhs):
        '''Take two students and return a list containing these two students'''
        return [self, rhs] # bracket because it returns a list
    ">="
    def __ge__(self, rhs):
        '''Returns true if the student is greater than or equal 
        another student based on lexicographical order'''
        return self.name.upper() >= rhs.name.upper()
    #"<=" __le__
    #"<" __lt__
    #">" __gt__
    #... Overriding methods

s1 = Student1("Gaucho", 1234567)
s2 = Student1("Jane", 5555555)
print(s1)
print(s1+s2)

studentPair = s1 + s2
for s in studentPair:
    s.printAttributes()
x = s1>=s2
print(x)
x1 = s1 + 34.5
print(x1)
print(1+2)

'''Inheritance: It is a way of extending the functionality and properties
of an existing class
    * And allows us to add new features
    * And also allows us to replace existing features
'''
class Animal:
    '''Animal class type that contains attributes for all animals'''
    def __init__ (self, species = None, name = None):
        self.species = species
        self.name = name
    def setName(self, name):
        self.name = name
    def setSpecies(self, species):
        self.species = species
    def getAttributes(self):
        return "Species: {}, Name: {}".format(self.species, self.name)
    def getSound(self):
        return "I'm an animal! "
    


