#local and global variables
#local variables are used in a certain place and then they disappear.
#Global variables are used everywhere in the program from the moment they are defined.

def function():
    a=10         # a is a local variable
    print(a)

function()
# print(a)     # a is not defined 


b=5             #b is a global variable
def function():
    print(b)
function()

def function():
    print(s)
#function()
#s="Python"    # -s is not defined-  
               # throws an error because the value is assigned after the function is called

c=10    #global variable
def function():
    c=2   #local variable
    print(c)     
function()     #print c=2  
print(c)       #print c=10

d=5
def function():
    global d
    d=3       #3 is assigned to the value of the global variable
    print(3)  
function()
print(d)     

if True:
    e=5  #global variable It doesn't have to be defined at the top to be global. 
         # It can also be defined in any if block or while block.
    print(e)  #e=5
print(e)      #e=5
