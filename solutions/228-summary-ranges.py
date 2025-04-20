# 228. Summary Ranges
# Topics: Array
# https://leetcode.com/problems/summary-ranges/


from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        if len(nums) > 0:
            range_start_index = 0
            range_last_index = range_start_index
            for i, num in enumerate(nums):
                if num - 1 == nums[range_last_index] or num == nums[range_last_index]:
                        range_last_index = i
                else:
                    if range_last_index == range_start_index:
                        # Range is only one value
                        ranges.append(str(nums[range_start_index]))
                    else:
                        ranges.append(f'{nums[range_start_index]}->{nums[range_last_index]}')
                    range_start_index = i
                    range_last_index = i
            if range_last_index == range_start_index:
                # Range is only one value
                ranges.append(str(nums[range_start_index]))
            else:
                ranges.append(f'{nums[range_start_index]}->{nums[range_last_index]}')

        return ranges