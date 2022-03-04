#in operator Checks if an element is in another list, tuple, string
print(5 in [1,2,3,4]) #false (searching in list)
print("he"in "hello world") #true (searching in string)
print(4 in (1,2,3,4,5)) #true (searching in tupple)

#for loop -For loop loops through lists, tuples, strings-
list=[1,2,3,4,5]
for element in list:
    print(element)

sum=0
list=[1,2,3,4,5,6,7,8,9]
for element in list:
    sum=sum+element
    print("sum:{} element:{}".format(sum,element))
print(sum)
#printing even numbers to the screen
list=[1,2,23,45,67,87,44,22,26]
for element in list:
    if element % 2==0:
     print(element)    

s="I am learning Python" 
for char in s:
    print(char)
    

s="I am learning Python" 
for char in s:
    print(char*3)

#using dictionary with for loop
dictionary1={"one":1,"two":2,"three":3}
for element in dictionary1.keys():
    print(element)
for element in dictionary1.values():
    print(element)
for element in dictionary1.items():
    print(element)
