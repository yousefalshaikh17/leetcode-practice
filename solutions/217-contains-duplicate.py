# 217. Contains Duplicate
# Topics: Array, Hash Table, Sorting
# https://leetcode.com/problems/contains-duplicate/


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(set(nums)) != len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False