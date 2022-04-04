d=dict()  #an empty dictionary
d={'first':1,'second':2,'third':3}
print(d)
s=set() #an empty set
s=(1,2,3)
print(s)
t=tuple() #an empty tuple
t=(1,2,3)
print(t)
# def search4vowels(word:str)->set : #word argument is expected string and function returns set
#     vowels=set('aeiou')
#     return vowels.intersection(set(word))
# help(search4vowels('word')) 
#Help on set object:
# class set(object)
#  |  set() -> new empty set object
#  |  set(iterable) -> new set object
#  |  
#  |  Build an unordered collection of unique elements.
def search4vowels(phrase:str)->set :
    return set('aeiou').intersection(set(phrase))
def search4letters(phrase:str,letters:str='aeiou')->set :
    return set(letters).intersection(set(phrase))  #create set object from "letters"
search4vowels('deneme')
search4letters('deneme', 'aeiou')
