"""
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(string):
    aux_dict = {}
    aux_char = None
    
    for i in string:
        aux_dict[i] = aux_dict.get(i, 0) + 1
        
    for key, val in aux_dict.items():
        if val == 1:
            aux_char = key
            break
        
    return aux_char
        

