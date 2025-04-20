# 682. Baseball Game
# Topics: Array, Stack, Simulation
# https://leetcode.com/problems/baseball-game/


from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for o in operations:
            if o == '+':
                record.append( record[-1] + record[-2] )
            elif o == 'D':
                record.append( record[-1] * 2 )
            elif o == 'C':
                record.pop(-1)
            else:
                record.append(int(o))
        
        return sum(record)