# 2145. Count the Hidden Sequences
# Topics: Array, Prefix Sum
# https://leetcode.com/problems/count-the-hidden-sequences/


from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Time: O(N)
        # Space: O(1)
        sum = 0
        min_dif = 0
        max_dif = 0
        for difference in differences:
            sum += difference
            min_dif = min(min_dif, sum)
            max_dif = max(max_dif, sum)

        return max((upper - lower) - (max_dif - min_dif) + 1, 0)