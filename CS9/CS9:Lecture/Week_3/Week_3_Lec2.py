'''class A(Exception):
    pass
class B(A):
    pass
class C(Exception):
    pass
try:
    x = int(input("Enter a positive number"))
    if x <0:
        raise B()
except C:
    print("Caught C")
except A:
    print("Caught A")
except B:
    print("Caught B")

print("Resuming execution")'''

'''Asymptotic Behavior
* We want to analyze appromixately how fast an algorithm runs when the size of 
the input apporaches infinite'''

'''Order of magnitude function (Big-O)
* We want to assume the WORST-CASE scenario when analyzing our algorithms.
    * Calculate the time function(T(n) number of steps an algorithm takes)
    We can express Big-O by 
        * Dropping all lower order terms, constants, and coefficients'''
# Big-O notation don't care about coefficients, theoretically
# just care about magnitudes!!!

import time 
def f1(n):
    l = []
    for i in range(n):
        l.insert(0, 1)  
    return   
def f2(n):
    l = []
    for i in range(n):
        l.append(i)
    return 
print("starting f1")
start = time.time()#bench marking start time
f1(200000)
end = time.time()#bench marking end time
print("time elasped ", end - start, " seconds")

print("starting f2")
start = time.time()
f2(200000)
end = time.time()
print("time elasped ", end - start, " seconds")

'''Common Big-O notation
* O(1)
* O(log(n))
* O(n
* O(n^2)
* O(n^3)
* O(2^n)'''

