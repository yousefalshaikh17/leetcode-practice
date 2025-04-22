# 2338. Count the Number of Ideal Arrays
# Topics: Math, Dynamic Programming, Combinatorics, Number Theory
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/


from functools import cache


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        
        comb = [[0] * 16 for _ in range(n)]
        for i in range(n):
            for j in range(min(16, i + 1)):
                if j == 0:
                    comb[i][j] = 1
                else:
                    comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD

        @cache 
        def dfs(i: int, count: int) -> int:
            result = comb[n - 1][count - 1]
            if count < n:
                multiplier = 2
                while i * multiplier <= maxValue:
                    result = (result + dfs(i * multiplier, count + 1)) % MOD
                    multiplier += 1
            return result

        total = 0
        for i in range(1, maxValue + 1):
            total = (total + dfs(i, 1)) % MOD
        
        return total