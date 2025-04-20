# 1. Two Sum
# Topics: Array, Hash Table
# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = dict()
        for i, num in enumerate(nums):
            hm[num] = i
        
        for i,num in enumerate(nums):
            other_num = target-num
            if (other_num in hm) and hm[other_num] != i:
                return [i, hm[other_num]]