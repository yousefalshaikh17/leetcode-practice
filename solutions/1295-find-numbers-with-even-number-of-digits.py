# 1295. Find Numbers with Even Number of Digits
# Topics: Array, Math
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


from typing import List


class Solution:
    def has_even_digits(self, num: int) -> bool:
        # Time: O(log M)
        # Space: O(1)
        num_digits = 0
        while num:
            num_digits += 1
            num //= 10
        return num_digits & 1 == 0

    def findNumbers(self, nums: List[int]) -> int:
        # Time: O(N log M)
        # Space: O(1)
        num_even = 0

        for num in nums:
            if self.has_even_digits(num):
                num_even += 1
        return num_even
    

# Alternate slower solution
class Solution:
    def has_even_digits(self, num: int) -> bool:
        # Time: O(M)
        # Space: O(1)
        return len(str(num)) % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        # Time: O(N * M)
        # Space: O(1)
        num_even = 0

        for num in nums:
            if self.has_even_digits(num):
                num_even += 1
        return num_even