# 2845. Count of Interesting Subarrays
# Topics: Array, Hash Table, Prefix Sum
# https://leetcode.com/problems/count-of-interesting-subarrays/


from typing import Counter, List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        num_interesting_subarrays = 0

        mod_frequency = Counter()
        mod_frequency[0] = 1 # Because we start with prefix sum = 0

        for num in nums:
            
            if num % modulo == k:
                prefix_count += 1
                prefix_count = prefix_count % modulo

            num_interesting_subarrays += mod_frequency[(prefix_count - k) % modulo]
            mod_frequency[prefix_count] += 1

        return num_interesting_subarrays