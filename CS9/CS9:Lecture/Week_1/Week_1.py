x = []
x.append(1) #add items in list
x.append("one")
print(x)
x = [1,2,2,3,3,3]
x.count(2)
print(x.count(1))

x[3]
x[3] = "3"
x[-1]# counts backward, return last element

3 in x # return boolean value, check if it's inside the collection/list x
x = [1,2,2,3,3,3]
x.insert(2, 2.5) # insert at index 2, shift other things to the right
print(x)

x.pop()#by default, index = -1, so will remove the last element of the list
print(x)

x.pop(2)
print(x) # removes element at index 2
print() # print does not return value, so returns None

''' List Slicing'''
# [i:j] syntax starts (includes) element at index i up to (not including) 
# element at index j. N0te, i and j are ints. 

x = [1,2,3,4,5]
print(x[1:4]) # [1,4)
print(x[:3]) # index 0 - 2, exclude 3

''' Strings represent a collection of characters 
But in python, characters aren't a specific type. It's basically
a string with one value
Strings are very similar to lists (not exactly)'''

x = "CS9"
print(type(x))
print(x[2])

# String collection does not support item assignment. Strings are immutable, 
# can't be changed. 

'''Lists in python are mutable, strings are immutable'''

x = x.replace("9","1") # (old value, replace/new value)
print(x) # string needs to assign, or else won't actually change it

x.split("S") # gives you a list that separates by "S" -> replace "S" with comma 
print(x)
y = "CSS1"
print(y.split("S")) #['C', '', '1']

# Function Definition

''' When immutable types are passed into a function, a Copy
of what variable is made within the function
When Mutable types are passed into a function, the actual parameter 
variable is used within the function '''
def changeListParameter (x):
    x[0] = "!" # list can just change cuz it's mutable
    return x
a = ["C","S","9"]
print(changeListParameter(a))
print(a)

#mutable - modify original, so actual thing change

def changeStringParameter(x):
    x = x.replace("C","!") # string needs to assign cuz it's immutable
    return x
b = "CS9"

print(changeStringParameter(b)) # function return the new copy
print(b) #return the same cuz a COPY was modfied, not the actual thing 

for x in range(4): # [0->3] Four unique times 
    print(x, "hello!" * x)
 # range (x,y) returns a collection of numbers starting at x 
 # up to (but not included) y 
 # range(x,y,z) returns a collection of numbers starting at x up to 
 # (but not including) y, with a step z

for x in range(3,8,2): 
    print(x)

'''Sets a collectino of items with:
    * no duplicates
    * Order and position does not matter'''
s2 = set([2,4,4,6])
print(s2)

print(3 in s2)
print(4 in s2)
print(3 not in s2)

'''Dictionaries * key maps to a value
* keys must be UNIQUE'''

D = {}
print(D)
print(len(D))
D = {'Jane':18, 'Jen':19, 'Joe':20, 'John': 21}
print(D)
print(len(D))

print("Jane's age is", D['Jane']) # can extract dictionary element using bracket
D["Jerry"] = 30 #insert value into dictionary
print(D)

D['Joe'] = 30 # modified dictionary
print(30)


