# 977. Squares of a Sorted Array
# Topics: Array, Two Pointers, Sorting
# https://leetcode.com/problems/squares-of-a-sorted-array/


from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L,R = 0, len(nums)-1
        new_nums = []
        while L != R:
            if abs(nums[L]) < abs(nums[R]):
                new_nums.append(nums[R] ** 2)
                R -= 1
            else:
                new_nums.append(nums[L] ** 2)
                L += 1

        new_nums.append(nums[L] ** 2)

        return new_nums[::-1]