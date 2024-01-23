'''Recursion
* Is when a function contains a call to itself
* Recursive solutions are useful when the result is dependent 
on the result of SUB-PARTS of the problem
* We're mostly familiar with writing code in an iterative fashion, 
    * And we can write an iterative solution for a recursive algorithm
    and vice versa
    
The Three Laws of Recursion
1. A recursive algorithm must have a BASE CASE
2. A recursive algorithm must change its state and move toward the base case
3. A recursive algorithm must call itself, recursively

Example: Factorial
* N! == N * (N-1) * (N-2) * 3 * 2 * 1
* 0! == 1
* N! = N * (N-1)! '''

def factorial(n):
    if n ==0: #Base Case!!!
        return 1
    return n * factorial(n-1)
def double(n):
    return 2*n
def triple(n):
    return n + double(n)

# Another Example:

# Fibonacci 
'''
f(n) = f(n-1) + f(n-2)
f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 3, f(5) = 5, ...'''

def fib(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    return fib(n-1) * fib(n-2)
    
print(factorial(3))
print(triple(5))

'''List vs Dictoinaries'''
DICT = {}
infile = open("wordlist.txt", 'r') #read the file and put in into my computer
for x in infile: # goes through each line in the file
    DICT[x.strip()] = 0 #Create an entry in dictionary with value 0

print(len(DICT)) # how many words are in DICT
infile.close()

WORDLIST = []
for y in DICT: #put the dictionary key into wordlist
    WORDLIST.append(y)

print(len(WORDLIST))

# Algorithm 1 - Lists
from time import time

start = time()
infile = open("Peterpan.txt", 'r')
largeText = infile.read() #take entire file content as one large STRING, put it in largeText
infile.close()
counter = 0
words = largeText.split()
for x in words:
    x = x.strip("\"\'(){},.?!<>;-").lower()
    if x in WORDLIST:
        counter += 1
end = time()
print(counter)
print("Time elapsed with WORDLIST (seconds):", end - start)

# Algorithm 2 - Dictionaries
from time import time

start = time()
infile = open("Peterpan.txt", 'r')
largeText = infile.read() #take entire file content as one large STRING, put it in largeText
infile.close()
counter = 0
words = largeText.split()
for x in words:
    x = x.strip("\"\'(){},.?!<>;-").lower()
    if x in DICT:
        counter += 1
end = time()
print(counter)
print("Time elapsed with DICT (seconds):", end - start)

# Dictionary is a hash function - needs to take in a key
