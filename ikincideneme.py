#lists
list1=["python",234,"java",12367888]
print(len(list1)) # find length of list
#index
print(list1[0])
print(list1[2:])
list2=[1,2,3,4,5,6]
list3=[7,8,9,10,11]
liste4=list2+list3
print(list4*3)
#strings cannot be changed, but lists can.
list4[0]=45
print(list4) #the first element of list3 is 45 
list1.append(7) #add the element
print(list1)
list1.pop() #removes the last element
            
print(list1)
list1=[9,23,45,12,1,234]
list1.sort() #sort the elements of the list from smallest  to largest
print(list1)
list1.sort(reverse=True) #sort the elements of the list from largest  to smallest
print(list1)
#nested lists
list1=[[1,2],[3,5]]
print(list1[1][0])
#Tuples 
tuple1=(1,2,2,2,2,2,2,3,4,5,6,7)
print(tuple1[3])
print(tuple1.count(2)) #Shows how many times the value is used in tuple.
print(tuple1.index(1)) #show which index the item is in.


