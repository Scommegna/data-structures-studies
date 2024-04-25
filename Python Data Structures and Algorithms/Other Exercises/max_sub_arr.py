"""
Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

Remember to also account for an array with 0 items.



Function Signature:

def max_subarray(nums):


Input:

A list of integers nums.



Output:

An integer representing the sum of the contiguous subarray with the largest sum.



Example:

max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output: 6
Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
"""

def max_subarray(nums):
    if len(nums) == 0:
        return 0
        
    subarrays = []
    max_sum = 0
    
    for item in nums:
        if item < max_sum:
            max_sum = item
    
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray = nums[i:j]
            subarrays.append(subarray)
            
    for item in subarrays:
        counter = 0
        for number in item:
            counter += number
            
        if counter > max_sum:
            max_sum = counter
            
    return max_sum
