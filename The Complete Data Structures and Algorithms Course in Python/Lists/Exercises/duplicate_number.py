"""
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]

"""

def remove_duplicates(arr):
    new_set = set()
    
    for num in arr:
        new_set.add(num)
        
    arr = []
        
    for num in new_set:
        arr.append(num)
        
    return arr

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))


"""
Alternative answer:

def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]
"""