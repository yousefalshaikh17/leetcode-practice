# 1189. Maximum Number of Balloons
# Topics: Hash Table, String, Counting
# https://leetcode.com/problems/maximum-number-of-balloons/


from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target_text = "balloon"
        counter = Counter()

        for c in text:
            if c in target_text:
                counter[c] += 1
        
        if any(c not in counter for c in target_text):
            return 0
        else:
            return min(
                counter["b"],
                counter["a"],
                counter["l"] // 2,
                counter["o"] // 2,
                counter["n"]
            )