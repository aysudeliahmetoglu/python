#getting input from user
a=input("please enter number: ")
print(a)
b=int(input("please enter school number:"))# conversion data type.
print("school number is :",b)
isim=input("please enter your name:")
print("your name is ",isim)
# printing the sum of 3 numbers received from the user to the screen.
x=int(input("please enter first number: "))
y=int(input("please enter second number: "))
z=int(input("please enter third number: "))
print("sum of 3 numbers :" ,x+y+z)
#if string is entered instead of int as input, user should be warned.
try:
    a=int(input("a:"))
    
except ValueError:
    print("please enter the input in the correct format!")


