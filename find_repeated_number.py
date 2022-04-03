#finding repeated number

def findRepeatedNumber():
    nums=[2,4,1,4] #only one number can repeat
    nums=set('2414')
    d=sorted(nums)
    
    a=nums.intersection(set(d))
    for i in sorted(set(nums)):
        print(i)
        if d==a:
  
            print(a)

                
print(findRepeatedNumber(d))      