#default value assignment
def sayHi(name="no name"):
    print("hi!",name)

sayHi()    

def showInformation(name,surname,no):
    print("name: ",name ,"surname: ",surname ,"school number: ",no)

showInformation("aysu", "deliahmetoglu","10910010")

def showInformation(name="No information ",surname="No information", no="No information"): 
    print("name: ",name ,"surname: ",surname ,"school number: ",no)

showInformation() #print default value (no information)
showInformation(no="12345")
showInformation("aysu","deliahmetoglu")

#flexible number of values
def addition(*a):
     print(a)
addition(1,2,3,4,5,6)    #tupple 

def addition(*a):
    sum=0
    for i in a:
        sum +=i
    print(sum)    

addition(1,2,3,4,5,6,7,8,9)