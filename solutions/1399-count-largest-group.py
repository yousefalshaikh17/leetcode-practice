# 1399. Count Largest Group
# Topics: Hash Table, Math
# https://leetcode.com/problems/count-largest-group/


from typing import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        digit_sum_map = Counter()
        largest_count = 0
        num_largest_groups = 0
        
        for i in range(1, n + 1):
            digit_sum = sum_digits(i)
            digit_sum_map[digit_sum] += 1

            if largest_count == digit_sum_map[digit_sum]:
                num_largest_groups += 1
            elif largest_count < digit_sum_map[digit_sum]:
                largest_count = digit_sum_map[digit_sum]
                num_largest_groups = 1

        return num_largest_groups