# 54. Spiral Matrix
# Topics: Array, Matrix, Simulation
# https://leetcode.com/problems/spiral-matrix/


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])

        total_items = N * M

        def getItem(x,y):
            return matrix[y][x]

        x, y = 0,0

        flattened_spiral = []

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        LEFT_WALL = 0
        TOP_WALL = 0
        RIGHT_WALL = N
        BOTTOM_WALL = M

        current_direction_index = 0

        flattened_spiral.append(getItem(x,y))
        while len(flattened_spiral) != total_items:
            current_direction = directions[current_direction_index]
            new_x, new_y = x + current_direction[0], y + current_direction[1]
            if (new_x in range(LEFT_WALL,RIGHT_WALL)) and (new_y in range(TOP_WALL,BOTTOM_WALL)):
                x,y = new_x, new_y
                flattened_spiral.append(getItem(x,y))
            else:
                if current_direction_index == 0:
                    TOP_WALL += 1
                elif current_direction_index == 1:
                    RIGHT_WALL -= 1
                elif current_direction_index == 2:
                    BOTTOM_WALL -= 1
                elif current_direction_index == 3:
                    LEFT_WALL += 1
                current_direction_index = (current_direction_index+1) % 4
                
        return flattened_spiral
            