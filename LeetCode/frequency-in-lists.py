# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:

# False

def check_same_frequency(list1, list2):
    if len(list1) != len(list2):
        return False
        
    dict1 = {}
    dict2 = {}
    
    for item in list1:
        if not item in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1
            
    for item in list2:
        if not item in dict2:
            dict2[item] = 1
        else:
            dict2[item] += 1
            
    for key in dict2:
        if not key in dict1:
            return False
        if key in dict1 and dict1[key] != dict2[key]:
            return False
            
    return True
