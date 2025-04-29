# 2962. Count Subarrays Where Max Element Appears at Least K Times
# Topics: Array, Sliding Window
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/


from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        num_subarrays = 0

        max_element = max(nums)
        num_window_max_elements = 0

        # Variable sliding window
        left = 0
        for right in range(len(nums)):
            if nums[right] == max_element:
                num_window_max_elements += 1
                
            while num_window_max_elements == k:
                if nums[left] == max_element:
                    num_window_max_elements -= 1
                left += 1

            num_subarrays += left

        return num_subarrays