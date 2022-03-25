import random
wait_time=random.randint(1,60)
print(wait_time)

#mutable -list
#inmutable -tuple cannot be change under any circumstance.Tuple use as a constant list.
#dictionary - an unordered data structure (unordered and mutable). A dictonary stores key /values pairs.
temps=[32.0,212.0,0.0,81.6,95,4]
words=['hello','python']
print(words)
car_details=['opel','corsa','black','1.6','10200']
everything=[temps,words,car_details]
print(everything)
odds_and_ends=[[1,3,5,7],['a','b','c',],['one','two','three']]  #lists inside of a list
print(odds_and_ends)

vowels=['a','e','i','o','u']
word="Milliways"
for letter in word:
    if letter in vowels:
        print(letter)

found=[]
print(len(found))
found.append('a')
found.append('e')
found.append('i')
found.append('o')

if 'u' not in found:
    found.append('u')
print(found)  


vowels=['a','e','i','o','u']
word=input("Provide a word to search for vowels")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in word:
    print(vowels)            


  




