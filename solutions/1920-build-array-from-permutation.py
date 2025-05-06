# 1920. Build Array from Permutation
# Topics: Array, Simulation
# https://leetcode.com/problems/build-array-from-permutation/


from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(1)
        return [nums[nums[i]] for i in range(len(nums))]