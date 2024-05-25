"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

class Solution:
    def binary_search(self, arr, low, high, value):
        if high >= low:
            
            mid = (high + low) // 2

            if arr[mid] == value:
                return mid

            elif arr[mid] > value:
                return self.binary_search(arr, low, mid - 1, value)
            
            else:
                return self.binary_search(arr, mid + 1, high, value)
        else:
            return low
        


    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)