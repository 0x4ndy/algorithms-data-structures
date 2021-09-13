"""
https://leetcode.com/problems/reshape-the-matrix/
"""

from typing import List


class Solution:
    def matrix_reshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        new_matrix = [[0] * c for _ in range(r)]
        row, col = 0, 0

        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                new_matrix[row][col] = mat[i][j]
                if col < c-1:
                    col += 1
                else:
                    row += 1
                    col = 0

        return new_matrix
