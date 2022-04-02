#tuples are immutable
vowels=['a','e','i','o','u']  #list
print(type(vowels))
vowels2=('a','e','o','i','u') #tuple
print(type(vowels2))
vowels[2]='I'
print(vowels)
vowels2[2]='I'
print(vowels2) #TypeError:'tuple' object does not support item assignment

t=('Python')  #single object
print(type(t))  #string

t2=('Python',) #single object with comma
print(type(t2)) #tuple