"""
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.
"""

def item_in_common(list1, list2):
    aux_dict = {}
    
    for i in list1:
        aux_dict[i] = True
        
    for j in list2:
        if j in aux_dict:
            return True
            
    return False