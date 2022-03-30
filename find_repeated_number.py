#finding repeated number

def findRepeatedNumber():
    nums=[2,4,1,4] #only one number can repeat
    x=len(nums)
    counter=1
    for i in range(x):
        j=i+1
        for j in range(j,x):
            if(nums[i]==nums[j]):
                counter+=1
            if(counter >1):
                return nums[i]
                
print(findRepeatedNumber())      