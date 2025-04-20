# 2239. Find Closest Number to Zero
# Topics: Array
# https://leetcode.com/problems/find-closest-number-to-zero/


class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = nums[0]
        for num in nums:
            if abs(num) < abs(best):
                best = num

        if best < 0 and abs(best) in nums:
            return abs(best)
        return best

        