#return -used to return value-

def addition(a,b,c,):
    print("sum = ",a+b+c)

def multiplyByTwo(a):
    print("result = ",a*2)


# sum=addition(a, b, c)  -not valued-
# multiplyByTwo(sum)   

def addition(a,b,c):
    return a+b+c
def multiplyByTwo(a):
    return a*2

sum = addition(3,4,5)
print(multiplyByTwo(sum))     


def multiplyByThree(a):
    print("1st function worked")
    return a*3
def addUptoFive(a):
    print("2nd function worked")
    return a+5
def divideByFour(a):
    print("3rd function worked")
    return a/5    

print(multiplyByThree(addUptoFive(divideByFour(5))))

#Functions that do not return any value where they work in the function are called void