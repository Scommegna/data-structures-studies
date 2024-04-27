"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:



Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.

"""

def longest_consecutive_sequence(nums):
    aux = set(nums)
    longest = 0
    
    for num in nums:
        if num - 1 not in aux:
            curr_num = num
            curr_seq = 1
            
        while curr_num + 1 in aux:
            curr_num += 1
            curr_seq += 1
            
        longest = max(longest, curr_seq)
        
    return longest
    
