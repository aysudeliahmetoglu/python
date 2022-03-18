#Write a program that finds that water is in solid liquid gas state according to its temperature and writes it to the screen.

temperature_degree=int(input("please enter temperature degree "))
if(temperature_degree>0 and temperature_degree<100):
    print("liquid state")
elif(temperature_degree>=100):
    print("gas state")
else:
    print("solid")    