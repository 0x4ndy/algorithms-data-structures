"""
https://leetcode.com/problems/search-insert-position/
"""

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            idx = (left + right) // 2
            if target == nums[idx]:
                return idx
            elif target > nums[idx]:
                left = idx + 1
            elif target < nums[idx]:
                right = idx - 1

        return left
