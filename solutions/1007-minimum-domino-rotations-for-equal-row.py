# 1007. Minimum Domino Rotations For Equal Row
# Topics: Array, Greedy
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Time: O(N)
        # Space: O(1)

        minimum_rotations = len(tops) + 1

        # Check for each possible domino value
        for i in range(1, 7):
            top_count = 0
            bottom_count = 0

            for j in range(len(tops)):
                if tops[j] == bottoms[j] == i:
                    continue

                if tops[j] == i:
                    top_count += 1
                elif bottoms[j] == i:
                    bottom_count += 1
                else:
                    break
            else:
                minimum_rotations = min(minimum_rotations, top_count, bottom_count)
                if minimum_rotations == 0: # We already found the minimum
                    break

        return minimum_rotations if minimum_rotations <= len(tops) else -1