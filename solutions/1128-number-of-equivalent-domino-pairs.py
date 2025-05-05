# 1128. Number of Equivalent Domino Pairs
# Topics: Array, Hash Table, Counting
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/


from typing import Counter, List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Time: O(N)
        # Space: O(N)

        # Counts all occurences regardless of the order
        counter = Counter(tuple(sorted(el)) for el in dominoes)

        num_equiv_pairs = 0
        for count in counter.values():
            if count > 1:
                num_equiv_pairs += count * (count - 1) // 2

        return num_equiv_pairs
