#Prime numbers are numbers that are only divisible by 1 and itself.

# print(*range(2,number))


def isItPrime(number):
    if (number == 1 ):
     return False
    elif (number == 2):
        return True
    else:
       for i in  range(2,number):
            if (number % i == 0):
               return False
            
            return True


while True:
    number=input("please enter number: ")
    if(number == "q"):
        break
    else:
        number = int(number)    
        if(isItPrime(number)):
            print("this number is prime")
        else:
            print("this number is not prime")    