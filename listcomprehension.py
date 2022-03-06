list=[1,2,3,4]
(list.append(5))   #added 5
print(list)

list3=[1,2,3,4,5]
list4=[i for i in list3]  #list comprehension
print(list4)

list2=[3,4,5]
list3=[i*3 for i in list2]
print(list3)

list=[(1,2),(3,4),(5,6)]
list1=[i*j for i,j in list]
print(list1)

s="Pyhton"
list=[i*3 for i in s]
print(list)

list=[[1,2,3,4],[5,6,7,8,9,10],[11,12,13,14,15]]
for i in list:
    for x in i:
        print(x)
