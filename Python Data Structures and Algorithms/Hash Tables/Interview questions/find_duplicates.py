"""
Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


Input:

A list of integers nums.


Output:

A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].
"""

def find_duplicates(nums):
    aux_list = []
    aux_dict = {}
    
    for i in nums:
        aux_dict[i] = aux_dict.get(i, 0) + 1;
        
    for num, count in aux_dict.items():
        if count > 1:
            aux_list.append(num)
        
        
            
    return aux_list
    