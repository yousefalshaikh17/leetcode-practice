# 242. Valid Anagram
# Topics: Hash Table, String, Sorting
# https://leetcode.com/problems/valid-anagram/


from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)