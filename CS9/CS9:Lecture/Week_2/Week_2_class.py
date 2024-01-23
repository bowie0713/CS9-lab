'''Student class type that contains student values.'''
'''Contains traits'''
'''Lets' assume that all UCSB students have perm # and names'''
class Student:
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
         # backlash is just doing for formatting reason, line break character

s = Student()
s.setName("Bowie Chuang")
s.setPerm(7240096) # student type, doesn't have a state
s.printAttributes()

s2 = Student("Crhis Gaucho", 1111111)
s2.printAttributes()

s3 = Student("Chris Gaucho")
s3.printAttributes()

s4 = Student(perm = 1111111)
s4.printAttributes()

a = Student("Jane", 1234567)
b = Student("Joe", 7654321)
c = Student("Jill", 5555555)

studentList = [a,b,c]
for s in studentList:
    s.printAttributes()
x = Student("Jane", 1234567)
y = Student("Jane",1234567)
z = y # refer to same object memory



print(x==y)#Yield False
print(x) # objects have been stored in separate location
print(y) # compare memory addresses, they are two different memory addresses
print(z)
print(y == z)

'''Python allows us to check for equality using the == operator
for our objects
* By default, Python uses the memory address (not the values)
to determine if two objects are the same
* This is known as SHALLOW EQUALITY 
'''



a1 = Student("Jane", 1234567)
a2 = Student("Jane",1234567)
a3 = a2 # refer to same object memory

print(a1==a2)#Yield False, yield true when define __eq__ funciton in a class
'''print(x) # objects have been stored in separate location
print(y) # compare memory addresses, they are two different memory addresses
print(z)
print(y == z)'''

print("Start")
'''Python Errors
* Syntax error is something that's wrong with the python expressions
* Exceptions are errors that occur DURING program execution (runtime errors)'''
#print(Hello) 
#print('5' + 5)#can only concatenate str not int

'''Excetption handling
* The general rule of exception handling is:
    * if an exception was raised in a program and 
    nobody catches the exception error, then the program 
    will termiante
* But we can handle exception messages with a a general structure
referred to as try/except'''

'''while True:
    try: 
        x = int(input("Enter an int "))
        break
    except Exception:
        print("Input was not an int type")
    print("Let's try again")'''

'''The flow of execution is:
    * Everything within a try block is executed normally
    * if an exception occrus in the try block, execution halts and 
    an exception message is passed to a corresponding except block
    * The except block tries to catch a certain exception type
    (not that Exception catches ALL types of exceptions)
    * If there is a matching type, then the first-mathcing
    except block is executed. 
    * Once done, program execution resuems past the except block'''

'''while True:
    try: 
        x = int(input("Enter an int "))
        print(1/0)
        break
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception:
        print("Input was not an int type")
    print("Let's try again")'''


#ctrl + c breaks 

'''while True:
    try: 
        x = int(input("Enter an int "))
        print(1/0)
        break
    except ZeroDivisionError:
        print("Can't divide by zero")
    except NameError:
        print("Input was not an int type")
    print("Let's try again")

print(x)
print("Resuming execution")'''

l = [1,2,3]
#l[10] # list index out of range

'''Example 
Functions raising exceptions that are caught by the caller
'''

def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError() # this is an object, construct and raise it
    return numerator / denominator

'''try:
    print(divide(1,1))
    print(divide(1,0))
    print(divide(2,2))
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
print("Resuming execution")'''

try:
    print(divide(1,1))
    print(divide(1,0))
    print(divide(2,2))
except Exception:
    print("Caught Exception...")
except ZeroDivisionError:
    print("Error: Cannot divide by zero") # dead code, never be reach

print("Resuming execution")














