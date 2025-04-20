# 48. Rotate Image
# Topics: Array, Math, Matrix
# https://leetcode.com/problems/rotate-image/


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):

            for y in range(len(matrix)):
                for x in range(y+1, len(matrix)):
                    matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
            
        def reverse(list):
            for i in range(len(list) // 2):
                list[i], list[-(i+1)] = list[-(i+1)], list[i]

        reverse(matrix)
        transpose(matrix)

        