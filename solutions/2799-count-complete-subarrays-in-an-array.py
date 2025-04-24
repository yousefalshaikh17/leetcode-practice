# 2799. Count Complete Subarrays in an Array
# Topics: Array, Hash Table, Sliding Window
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/


from typing import Counter, List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        target_num_unique = len(set(nums))
        frequency_count = Counter()
        num_sub_arrays = 0

        # Variable sliding window
        left = 0
        for right in range(n):
            # Update frequency for number
            frequency_count[nums[right]] += 1

            while len(frequency_count) == target_num_unique:
                # All extended window sizes are complete
                num_sub_arrays += n - right

                # Decrement frequency to shift left pointer to the right
                frequency_count[nums[left]] -= 1
                if frequency_count[nums[left]] == 0:
                    frequency_count.pop(nums[left])
                
                # Shift left pointer by one
                left += 1

        return num_sub_arrays