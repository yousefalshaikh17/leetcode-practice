# 167. Two Sum II - Input Array Is Sorted
# Topics: Array, Two Pointers, Binary Search
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0, len(numbers)-1
        while L < R:
            num_sum = numbers[L] + numbers[R]
            if num_sum > target:
                R -= 1
            elif num_sum < target:
                L += 1
            else:
                return [L+1,R+1]