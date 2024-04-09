"""
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
"""

def has_unique_chars(string):
    aux_set = set({})
    
    for char in string:
        aux_set.add(char)
        
    if len(aux_set) != len(string):
        return False
    
    return True