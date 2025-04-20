# 14. Longest Common Prefix
# Topics: String, Trie
# https://leetcode.com/problems/longest-common-prefix/


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = strs[0]
        for s in strs:
            if len(s) < len(shortest_str):
                shortest_str = s
        
        shortest_prefix = shortest_str
        is_prefix = False
        while len(shortest_prefix) > 0 and not is_prefix:
            is_prefix = True
            for s in strs:
                if shortest_prefix not in s[:len(shortest_prefix)]:
                    shortest_prefix = shortest_prefix[:-1]
                    is_prefix = False
                    break

        return shortest_prefix