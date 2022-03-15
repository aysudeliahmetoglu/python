import math #import the module
print(dir (math))  #to see the functions inside the module

print(help(math))  #for function usage details

print(math.factorial(3)) 

print(math.floor(5.6)) #Converting to integers less than x

print(math.ceil(6.5))  #Converting to smallest integers greater than x


import math as maths  #identification by different name

print(maths.factorial(5))

from math import *  #to include all functions
print(factorial(5))
print(floor(5,6))

from math import factorial,ceil  #to include only the functions we want
                                  #If functions other than these are used, it will give an error.

print(floor(5.1)) #it will give an error.

print(maths.factorial(5))

 #The last function we defined works. If we added the last module, 
 # #the module works. If we defined the last function, the function works.
from math import*
def factorial(number):
    print("my function is working.")
    factorial=1
    if (number==0 or number==1):
         return 1
    else:
        while (number >=1):
            factorial*=number    
            number -=1
        return factorial
print(factorial(5))

