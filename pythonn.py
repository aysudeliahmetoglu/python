vowels=set('aeiou')
print(vowels)
word='hello'
u=vowels.union(set(word))
print(u)
list_u=sorted(list(u))
print(list_u)
x=vowels.difference(set(word))
print(x)
y=vowels.intersection(set(word))
print(y)

vowels=set('aeiou')
word=input("please enter a word to search for vowels: ")
found=vowels.intersection(set(word))
for vowel  in found:
    print(vowel)
