# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets

def contains_duplicate(nums):
    aux_set = set(nums)
    
    if len(nums) != len(aux_set):
        return True
    
    return False
