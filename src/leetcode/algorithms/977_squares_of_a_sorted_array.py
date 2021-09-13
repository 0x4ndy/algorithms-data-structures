"""
https://leetcode.com/problems/squares-of-a-sorted-array/ 
"""

from typing import List


class Solution:
    def sorted_squares1(self, nums: List[int]) -> List[int]:
        return sorted(n*n for n in nums)

    def sorted_squares2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left, right = 0, n-1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[n-1] = nums[right]*nums[right]
                right -= 1
            else:
                result[n-1] = nums[left]*nums[left]
                left += 1
            n -= 1
        return result
