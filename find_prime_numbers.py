
def isItPrime(n: int) -> bool:
    """ """
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n/2)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True


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
