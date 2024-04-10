"""
Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.

The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.



Input:

A list of integers nums .

An integer val representing the value to be removed from the list.



Output:

An integer representing the new length of the modified list after removing all occurrences of val.



Constraints:

Do not use any built-in list methods, except for pop() to remove elements.

It is okay to have extra space at the end of the modified list after removing elements.
"""

def remove_element(nums, val):
    counter = 0
    
    while counter < len(nums):
        if nums[counter] == val:
            nums.pop(counter)
        else:
            counter += 1
    
    return len(nums)
