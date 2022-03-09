#type(),print(), etc. -built in function-
# our own custom made functions -user defined functions-

 #print(type(greet)) #it gives an error because we didnt defined its content.

def greet():
    print("say hi")
    print("How are you?")

print(type(greet))   
greet()    #call function

#parameters and arguments
def greet(name):
    print("your name is",name)

greet("aysu")

def addition(a,b,c):
    print("sum =", a+b+c)

addition(3,4,5)    

def factorial(number):
    factorial=1
    if(number == 0 or number ==1 ):
     print("factorial = ",factorial)
    else: 
        while(number >= 1):
            factorial *= number
            number -= 1

        print("factorial = ",factorial)
factorial(5)            
