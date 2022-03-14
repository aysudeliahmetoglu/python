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
