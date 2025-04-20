# 13. Roman to Integer
# Topics: Hash Table, Math, String
# https://leetcode.com/problems/roman-to-integer/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        i = 0
        while i < len(s):
            if (i+1 < len(s) and key[s[i+1]] > key[s[i]] ):
                num += key[s[i+1]] - key[s[i]]
                i += 2
            else:
                num += key[s[i]]
                i += 1
                    
        return num