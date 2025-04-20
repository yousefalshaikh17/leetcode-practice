# 36. Valid Sudoku
# Topics: Array, Hash Table, Matrix
# https://leetcode.com/problems/valid-sudoku/


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate Rows
        for row in board:
            row_set = set()
            for item in row:
                if item != ".":
                    if item in row_set:
                        return False
                    row_set.add(item)

        # Validate Columns
        for i in range(9):
            column_set = set()
            for j in range(9):
                item = board[j][i]
                if item != ".":
                    if item in column_set:
                        return False
                    column_set.add(item)

        # Validate sub-boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                sub_box_set = set()
                for k in range(3):
                    for l in range(3):
                        item = board[i+k][j+l]
                        if item != ".":
                            if item in sub_box_set:
                                return False
                            sub_box_set.add(item)


        return True