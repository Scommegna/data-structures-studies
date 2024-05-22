"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

class Solution:
    def split_string(self, string, length):
        return [string[i:i+length] for i in range(0, len(string), length)]

    def strStr(self, haystack: str, needle: str) -> int:
        new_haystack = self.split_string(haystack, len(needle))

        for i in range(len(new_haystack)):
            if new_haystack[i] == needle:
                return i

        return -1