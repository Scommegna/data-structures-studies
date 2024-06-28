"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        aux_dict_s = {}
        aux_dict_t = {}
    
        for letter in s:
            if not letter in aux_dict_s.keys():
                aux_dict_s[letter] = 1
            else:
                aux_dict_s[letter] += 1
        
        for letter in t:
            if not letter in aux_dict_t.keys():
                aux_dict_t[letter] = 1
            else:
                aux_dict_t[letter] += 1
            
        for letter in t:
            if not letter in aux_dict_s.keys():
                return False
            elif aux_dict_s[letter] != aux_dict_t[letter]:
                return False
        
        return True