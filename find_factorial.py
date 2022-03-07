#Find Factorial
print("""***************

Factorial Finder Program

Press 'q' to exit.

*******************
""")
while True:
    number = input("Please enter number:")
    if(number == "q"):
        print("The program is terminated.")
        break
    else:
        number=int(number)
        Factorial=1
        for i in range(2,number+1):
            Factorial *=i
        print("Factorial : ",Factorial)