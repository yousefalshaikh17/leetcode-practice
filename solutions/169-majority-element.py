# 169. Majority Element
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting
# https://leetcode.com/problems/majority-element/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_element = None
        current_count = 0

        for num in nums:
            if current_count == 0:
                current_element = num

            if num == current_element:
                current_count += 1
            else:
                current_count -= 1

        return current_element