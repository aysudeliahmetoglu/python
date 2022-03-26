nums=[1,2,3,4,5,6]
nums.extend([3,4])
print(nums)
nums.insert(3,7)
print(nums)
nums.insert(2,"two-and-half")
print(nums)
# print(help(list.append))   #To get information about the use of the method

phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)
# list1=[]
# plist.pop()
# print(plist)
# plist.insert(0,"on tap")
# list1.append('o')
# list1.append('n')
# list1.append('t')
# list1.append('a')
# list1.append('p')
# print(plist)
for letter in plist:
    if letter == "Don'panic!":
        plist.remove(letter)
print(plist)     
print(plist)

# for letter  in list1:
#     plist
   
        



# new_phrase=''.join(plist)
# print(plist)
# print(new_phrase)
