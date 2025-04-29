# 2302. Count Subarrays With Score Less Than K
# Topics: Array, Binary Search, Sliding Window, Prefix Sum
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        num_subarrays = 0
        window_sum = 0
        left_index = 0

        # Variable sliding window
        for right_index in range(len(nums)):
            window_sum += nums[right_index]
            while left_index <= right_index and window_sum * (right_index - left_index + 1) >= k:
                window_sum -= nums[left_index]
                left_index += 1

            num_subarrays += right_index - left_index + 1

        return num_subarrays