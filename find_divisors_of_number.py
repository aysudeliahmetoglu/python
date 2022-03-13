#find the divisors of a number

# number=int(input("please enter number"))
def findDivisors(number):
    list1=[]
    for i in range(1,number):
        if(number % i == 0):
            list1.append(i)
    return list1
# print(findDivisors(number))            
while True:
    number=input("please enter number: ")
    if(number == "q"):
        break
    else:
        number = int (number)
        print("divisors: ",findDivisors(number))