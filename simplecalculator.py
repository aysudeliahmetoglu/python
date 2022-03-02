print("""**************
Calculator

Operations:
1.Addition
2.Subtraction
3.Multiplication
4.Division

***************""")
number1=int(input("please enter a number1:"))
number2=int(input("please enter a number2:"))
operation=int(input("please enter operation:"))

if(operation == 1):
    print("The sum of the two numbers is",number1+number2)
elif(operation ==2):
    print("result of subtraction is",number1-number2)
elif(operation ==3 ):
    print("product of two numbers is ",number1*number2)
elif(operation==4):
    print("division of two numbers is ",number1/number2)
else:
    print("please enter the correct operation")    




