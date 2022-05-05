# Prime numbers are numbers that are only divisible by 1 and itself.
def isItPrime(number):
    if (number > 1):
        for i in range(2, number):
            if not number % i:
                return False          
        return True
    return False

while True:
    # number = "2"
    number=input("please enter number: ")
    if(number == "q"):
        break
    number = int(number)
    if(isItPrime(number)):
        print("this number is prime")
        continue
    print("this number is not prime")

