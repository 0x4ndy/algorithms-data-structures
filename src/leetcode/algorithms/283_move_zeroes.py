"""
https://leetcode.com/problems/move-zeroes/
"""


from typing import List


class Solution:
    # Optimal - O(n)
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(0)
