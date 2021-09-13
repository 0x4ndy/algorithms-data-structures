"""
https://leetcode.com/problems/binary-search/
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            idx = left + (right - left) // 2
            if nums[idx] == target:
                return idx
            if nums[idx] < target:
                left = idx + 1
            else:
                right = idx - 1
        return -1
