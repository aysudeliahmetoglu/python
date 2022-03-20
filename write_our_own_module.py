#write our own module

programming_languages=["Python","C","Java","C#"]
def addition(number1,number2,number3):
    """
    This function return sum of three number

    """
    sum=number1+number2+number3
    
    return sum
    

def calculateMean(list1):
    
    """
    This function returns the arithmetic mean of the elements in the list

    """
    
    sum=0
    for i in list1:
        print(list1[i-1])
        sum=sum+list1[i-1]
    return sum/len(list1)
    
   


    

    
        
