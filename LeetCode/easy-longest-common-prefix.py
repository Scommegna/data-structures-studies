"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_word = 0
        stack = []
        pref = ""

        for word in strs:
            if len_word == 0:
                len_word = len(word)
            
            if len(word) < len_word:
                len_word = len(word)

        
        for i in range(len_word):
            stack.append(strs[0][i])

            for j in range(len(strs)):
                if strs[j][i] != stack[0]:
                    stack.pop()
                    return
            
            if len(stack) == 0:
                return ""
            
            pref += stack.pop()

        return pref