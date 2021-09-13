"""
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    # O(n^2)
    def two_sum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # O(n)
    def two_sum2(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in m.keys():
                return [i, m[x]]
            m[nums[i]] = i
        return None
