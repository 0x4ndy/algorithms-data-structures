"""
https://leetcode.com/problems/rotate-array/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n

        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
