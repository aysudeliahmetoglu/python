#and operator  -all conditions must be true for the general condition to be true-
print(1<2 and "murat" == "murat") #true
pprint(1>2 and "murat" == "murat") #false
print(1<2 and "car"<"desk" and 23.41>12.5) #true
#or operator   -not all conditions need to be true for the general condition to be true-
print(1<2 or "murat"!="murat") #true
print(11<2 or "car"<"desk" or 23.41>12.5) #true
#not operator
print(2==2) #true
print(not 2==2)#false