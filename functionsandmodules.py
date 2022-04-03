def search4vowels():
    vowels=set('aeiou')
    word=input("please enter word for vowels: ")
    found=vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
search4vowels() 

def search4vowels(word):
    vowels=set('aeiou')
    return vowels.intersection(set(word))
    
search4vowels('word')
 
