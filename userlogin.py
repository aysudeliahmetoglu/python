print(""" **********

user login

********** """)

sys_username="\nusername_user"
sys_password=123456

username=input("please enter your username")
password=int(input("please enter your password"))

if(username==sys_username and password!=sys_password):
    print("password is uncorrect please check your password!")
elif(username!=sys_username and password==sys_password):
    print("username is uncorrect please check your username!")
elif(username!=sys_username and password!=sys_password):
    print("your username and password are uncorrect please try again !")
else:
    print("user login successful...")   