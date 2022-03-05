#break -it just ends the loop it's in.-
i=0
while(i<10):
    if(i ==5):
        break
    print("i:",i) #0,1,2,3,4
    i+=1
list1=[1,2,3,4,5]
for i in list1:
    if(i==3):
        break
    print("i:",i)

while True: #If no termination statement is used anywhere, the loop continues.
    name=input("please enter name:(press 'q' to exit)")
    if(name=="q"):
        print("exiting the program")
        break
    print("your name is",name)
#continue -when we use this anywhere in the loop, it doesn't do
#  the remaining work and returns to the beginning of the loop-
list2=[0,1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if(i==3 or i==5): #The values ​​3 and 5 will not be printed
        continue
    print(i)
#endless loop
# i=0
# while(i<10):
#     if(i==2):   if we use i+=1 loop is not infinite
#      continue
#     print(i) 
#     i+=1   