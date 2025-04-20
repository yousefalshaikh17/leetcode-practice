# 771. Jewels and Stones
# Topics: Hash Table, String
# https://leetcode.com/problems/jewels-and-stones/


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_set = set(jewels)
    
        jewels_count = 0

        for stone_char in stones:
            if stone_char in jewels_set:
                jewels_count += 1
        return jewels_count