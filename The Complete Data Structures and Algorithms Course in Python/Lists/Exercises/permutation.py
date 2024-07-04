"""
Given two strings, create a method to decide if one is a permutation of the other
"""

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    
    if list1 == list2:
        return True
    
    return False
