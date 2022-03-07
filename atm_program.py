#ATM PROGRAM 
print("""**********

welcome to atm machine.

Operations:
1.Balance Inquiry

2.Deposit money

3.Withdraw money
  
Press 'q' to exit the program.


**********
""")

balance = 1000
while True:

    operation = input("please enter operation:")

    if(operation == "q"):
        print("We are waiting for you again")
        break
    elif(operation == "1"):
        print("Your balance is {} TL.".format(balance))

    elif(operation == "2"):  
        amount = int(input("Enter the amount you want to deposit:"))
        balance += amount

    elif(operation == "3"):
        amount = int(input("Enter the amount you want to deposit:"))

        if(balance - amount < 0):
            print("You cannot withdraw money.")   
            continue 
        balance -= amount

    else:
        print("invalid operation. Please try again.")            