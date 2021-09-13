"""
https://leetcode.com/problems/search-a-2d-matrix/
"""


from typing import List


class Solution:
    def search_matrix1(self, matrix: List[List[int]], target: int) -> bool:
        # Finding the row
        for row in matrix:
            if target < row[0]:
                return False
            if target == row[0]:
                return True
            elif target == row[-1]:
                return True
            elif target < row[-1]:
                if target in row:
                    return True

        return False

    def search_matrix2(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            idx = (left + right) // 2
            v = matrix[idx // n][idx % n]
            if v == target:
                return True
            else:
                if target < v:
                    right = idx - 1
                else:
                    left = idx + 1

        return False
