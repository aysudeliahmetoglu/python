first=[1,2,4,5,6]
print(first)
second=first
print(second)
second.append(7)
print(second)
print(first)  #if you change one list,the other changes too.
#to solve
third=second.copy()
print(third)
third.append(8)
print(third) 
print(first)   #the existing list is unchanged.
print(second)

saying="Hello world!"
list1=list(saying)
print(list1[-1])
print(list1[8])
print(list1[0:5:2])