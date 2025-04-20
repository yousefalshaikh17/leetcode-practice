# 383. Ransom Note
# Topics: Hash Table, String, Counting
# https://leetcode.com/problems/ransom-note/


from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letter_count_map = Counter(magazine)
        
        for c in ransomNote:
            if letter_count_map[c] > 0:
                letter_count_map[c] -= 1
            else:
                return False
        return True