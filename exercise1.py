#Write a program that finds the larger of two numbers given different from each other.

number1=int(input("please enter number1:"))
number2=int(input("please enter number2:"))

if(number1>number2):
    print("number1 is greater than number2",number1)
elif(number1==number2): 
    print("two numbers are equal")
else:
    print("number2 is greater than number1",number2)       