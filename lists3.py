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

for letter in plist[0:4]:
    plist.pop()
plist.pop(0)
plist.remove("'")    
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))
    
new_phrase=''.join(plist)
print(plist)
print(new_phrase)
