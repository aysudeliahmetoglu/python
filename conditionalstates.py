#if-else
age=int(input("please enter your age"))

if(age < 18):
    print("you cannot enter this place!")
else:
    print("welcome this place!") 

number=int(input("please enter number"))

if(number <0):
    print("this number is negative")
else:
    print("number can be 0 or positive")    
#if-elif-else
operation=input("please choose operation:")
if operation=="1":
    print("operation 1 selected")
elif operation=="2":
    print("operation 2 selected")
elif operation =="3":
    print("operation 3 selected")
elif operation=="4":                     # #elif block is not used alone
    print("operation 4 selected")
else:                                   #else block is not used alone
    print("invalid operation")

#grade evaluation system
note=int(input("please enter note:"))
if(note>=90):
    print("AA")
elif(note >=85):
    print("BA")
elif(note >=80):
    print("BB")
elif(note >=75):
    print("CB")
elif(note >=70):
    print("CC")  
elif(note >=65):
    print("DC")
elif(note>=60 ):
    print("DD")
else:
    print("FF")        

