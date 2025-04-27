# 3392. Count Subarrays of Length Three With a Condition
# Topics: Array
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/


from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        num_sub_arrays = 0

        # No point in starting from index 0.
        # Instead we start at index 2 and look at the 2 previous values.
        for i in range(2, len(nums)):
            # Evaluate sum of first and third numbers
            if (nums[i-2] + nums[i]) * 2 == nums[i-1]:
                num_sub_arrays += 1

        return num_sub_arrays
