# 2444. Count Subarrays With Fixed Bounds
# Topics: Array, Queue, Sliding Window, Monotonic Queue
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Time: O(n)
        # Space: O(1)
        num_sub_arrays = 0
        min_pos = -1
        max_pos = -1
        bad_pos = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_pos = i
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i

            num_sub_arrays += max(0, min(min_pos, max_pos) - bad_pos)

        return num_sub_arrays