"""
https://leetcode.com/problems/valid-sudoku/
"""


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = 9

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                v = board[i][j]

                if v == ".":
                    continue

                if v in rows[i]:
                    return False
                rows[i].add(v)

                if v in cols[j]:
                    return False
                cols[j].add(v)

                idx = (i // 3) * 3 + j // 3
                if v in boxes[idx]:
                    return False
                boxes[idx].add(v)

        return True
