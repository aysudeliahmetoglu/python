def search4vowels(phrase:str)->set:
    """Return  the set of vowels found in 'phrase' ."""
    return set('aeiou').intersection(set(phrase))

def search4letters(phrase:str,letters:str='aeiou')->set:   
    """Return a set of the 'letters ' found in 'phrase' """ 
    return set(letters).intersection(set(phrase))


