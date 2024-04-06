"""

Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.



Input:

A list of integers nums .

A target integer target.



Output:

A list of two integer representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
"""

def two_sum(nums, target):
    my_dict = {}
    
    for index, value in enumerate(nums):
        complement = target - value
        
        if complement in my_dict:
            return [my_dict[complement], index]
        
        my_dict[value] = index
        
    return []