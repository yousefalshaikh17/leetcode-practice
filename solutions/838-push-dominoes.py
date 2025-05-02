# 838. Push Dominoes
# Topics: Two Pointers, String, Dynamic Programming
# https://leetcode.com/problems/push-dominoes/


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Time: O(N)
        # Space: O(N)

        forces = []

        # Left -> Right
        force = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                force = len(dominoes)
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces.append(force)

        # Right -> Left
        force = 0
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == 'L':
                force = - len(dominoes)
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = min(force + 1, 0)
            forces[i] += force

        output = ['.' if force == 0 else 'R' if force > 0 else 'L' for force in forces]

        return ''.join(output)