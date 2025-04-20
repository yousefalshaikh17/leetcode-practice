# 781. Rabbits in Forest
# Topics: Array, Hash Table, Math, Greedy
# https://leetcode.com/problems/rabbits-in-forest/


import math
from typing import Counter, List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers_count = Counter(answers)
        min_rabbits = 0

        for other_rabbit_count, occurences in answers_count.items():
            similar_rabbits = other_rabbit_count + 1
            group_count = math.ceil(occurences / similar_rabbits)
            min_rabbits += group_count * similar_rabbits
        
        return min_rabbits