#user login program with loops
sys_username="aysud"
sys_password="12345"
right_of_entry=3
while True:
    username=input("please enter your username:")
    password=input("please enter your password:")
    if(sys_username==username and sys_password!=password):
        print("your password is uncorrect!")
        right_of_entry -=1
    elif((sys_username!=username and sys_password==password)):
        print("your username is uncorrect!")
        right_of_entry -=1
    elif((sys_username!=username and sys_password!=password)):
        print("your username and password are  uncorrect!")
        right_of_entry -=1  
    else:
        print("successfully logged into the system.") 
        break
    if(right_of_entry==0):
        print("you cannot login")     
        break
     
