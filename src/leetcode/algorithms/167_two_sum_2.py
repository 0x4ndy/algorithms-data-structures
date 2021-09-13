"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(0, len(numbers)):
            x = target - numbers[i]
            if x in m.keys():
                return [min([i+1, m[x]+1]), max([i+1, m[x]+1])]
            else:
                m[numbers[i]] = i

        return []
