# 11. Container With Most Water
# Topics: Array, Two Pointers, Greedy
# https://leetcode.com/problems/container-with-most-water/


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        max_height = max(height)
        L,R = 0, len(height)-1
        while L < R:
            min_height = min(height[L], height[R])
            container_length = R - L
            area = container_length * min_height
            max_area = max(area, max_area)

            if height[L] > height[R]:
                R -= 1
            else:
                L += 1

            if max_area > (R-L) * max_height:
                break
        return max_area