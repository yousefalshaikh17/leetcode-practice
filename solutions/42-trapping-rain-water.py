# 42. Trapping Rain Water
# Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
# https://leetcode.com/problems/trapping-rain-water/


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        L = R = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        # Initialize values for maximum heights
        for i in range(n):
            j = -i - 1
            max_left[i] = L
            max_right[j] = R
            L = max(L, height[i])
            R = max(R, height[j])

        # Calculate height of water
        total = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            total += max(0, pot - height[i]) # Height is to account for raised floors.

        return total