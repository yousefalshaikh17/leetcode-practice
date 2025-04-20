# 392. Is Subsequence
# Topics: Two Pointers, String, Dynamic Programming
# https://leetcode.com/problems/is-subsequence/


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True 
        if len(s) > len(t):
            return False
        
        cursor = 0

        for c in t:
            if c == s[cursor]:
                cursor += 1
                if cursor == len(s):
                    return True
        return False