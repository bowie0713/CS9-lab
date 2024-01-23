'''Python Object:
- Objects are a way for programmers to define their own Python types 
and create abstractions of things with the programming language 
- Each object may have a certain state that gets modified 
througout program execution.
- Object Oriented programming is the way programs use and manipulate
objects to solve problems and model real-world properties
    - Object Oriented Programming is not REQUIRED
    - It's more of a way to organize, read, maintain, 
    and debug software in a manageable way  
'''

x = [1,2,3]
print(type(x))
x.count(3)# a method 
'''Define a student object: class Name'''

'''Complete Test
* Test every possible path through the code in every possible situation

def biggest(a,b,c,d):
    returns the largest int

Unit Testing
* Testing individual piees (units) of a program to ensure correct behavior

Test Driven Development 
1. Write test cases that describe what the intended behavior of a unit
of software should be 
2. Implement the details of the functionality
3. Repeat until tests pass. 
'''

try:
    for i in range(5):
        x = i / (i-5)
except:
    print("EXCEPTION CAUGHT")
print("RESUMING EXECUTION")

'''for x in "h00":
    print(x[0])
    print(None)
print("out of for loop")'''

x = "h00"
print(x[0])





    
