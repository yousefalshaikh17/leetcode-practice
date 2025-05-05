# 790. Domino and Tromino Tiling
# Topics: Dynamic Programming
# https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    def numTilings(self, n: int) -> int:
        # Time: O(N)
        # Space: O(N)
        
        dominoes_possible = [1, 1, 2, 5]

        if n < len(dominoes_possible):
            return dominoes_possible[n]

        dominoes_possible += ([0] * (n - 3))
        mod = int(1e9 + 7)

        for i in range(4, n + 1):
            dominoes_possible[i] = (2 * dominoes_possible[i - 1] + dominoes_possible[i - 3]) % mod

        return dominoes_possible[n]