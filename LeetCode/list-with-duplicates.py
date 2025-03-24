# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]

def remove_duplicates(arr):
    aux_set = set(arr)
    
    new_list = list(aux_set)
    
    return new_list