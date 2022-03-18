#If the number that the user enters from the keyboard is in the range of 0-100, it is not valid, the algorithm that writes valid.

number=int(input("please enter number: "))

if(number >=0 or number==100):

    print("Number is in the valid range.")
    
else:
    print("The number you entered is not in the valid range.")    