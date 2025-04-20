# 128. Longest Consecutive Sequence
# Topics: Array, Hash Table, Union Find
# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums) # (n)
        
        best_length = 0

        for num in num_set: # (n)
            if num - 1 in num_set:
                continue
            next_num = num
            length = 0
            while next_num in num_set:
                length += 1
                next_num += 1

            best_length = max(best_length, length)
        return best_length