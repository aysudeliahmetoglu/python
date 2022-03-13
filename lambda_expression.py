#remember list comprehension

list1=[1,2,3,4,5]
list2=[i*2 for i in list1]
print(list2)

def multiplybyTwo(x):
    return x * 2 
print(multiplybyTwo(2))

multiplybyTwo = lambda x : x * 2   #so the function is defined in one line.
print(multiplybyTwo(3))

def addition(x,y,z):
    return x+ y + z
print(addition(3, 4, 5))

addition = lambda x,y,z : x + y + z
print(addition(3,2,4,))

def turnItOver(s):
    return s [::-1]
print(turnItOver("Python Programming"))

turnItOver = lambda s : s [::-1]      
print(turnItOver("System Programming"))


def oddOrEvenNumber(number):
    return number % 2 == 0  # if number is even return true , if number is odd return false.

    
print(oddOrEvenNumber(13))   

oddOrEvenNumber = lambda number : number % 2 == 0
print(oddOrEvenNumber(123))