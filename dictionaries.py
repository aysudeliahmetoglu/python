sözlük1={"bir":1,"iki":2,"üç":3,"dört":4}
#print(type(sözlük1))
#print(sözlük1["bir"])
sözlük1["beş"]=5 #adding new element
print(sözlük1)
sözlük2={"bir":[23,45],"iki":23}
print(sözlük2["bir"][1])
sözlük2["iki"]=21  #changing value 
print(sözlük2) 
a={"sayılar":{1,2,3,4},"meyveler":{"elma","armut","portakal"}}  #nested dictionaries
print(a)
print(sözlük1.keys())  #to print key values
print(sözlük1.values()) #to print values
print(sözlük1.items()) #to print  in tupples
