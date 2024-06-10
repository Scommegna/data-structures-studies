"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return ""
        elif len(nums) == 1:
            return [str(nums[0])]

        output = []
        pointer = 1
        aux1 = 0
        aux2 = 0

        while pointer < len(nums):
            if nums[pointer] == nums[aux2] + 1:
                aux2 = pointer
            elif nums[pointer] != nums[aux2] + 1 and aux2 == aux1:
                output.append(str(nums[aux1]))
                aux1 = pointer
                aux2 = pointer
            else:
                output.append(str(nums[aux1]) + "->" + str(nums[aux2]))
                aux1 = pointer
                aux2 = pointer

            pointer += 1

        return output

