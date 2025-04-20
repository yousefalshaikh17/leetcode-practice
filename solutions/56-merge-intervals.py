# 56. Merge Intervals
# Topics: Array, Sorting
# https://leetcode.com/problems/merge-intervals/


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []

        if len(intervals) > 0:
            intervals.sort(key=lambda interval: interval[0])

            for i, interval in enumerate(intervals):
                if not new_intervals or new_intervals[-1][1] < interval[0]:
                    new_intervals.append(interval)
                else:
                    new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])

        return new_intervals