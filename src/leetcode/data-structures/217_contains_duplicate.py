"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List


class Solution:
    # Approach 1 (Naive Linear Search)
    def contains_duplicate1(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False

    # Approach 2 (Sorting)
    def contains_duplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    # Approach 3 (Hash Table or Set)
    def contains_duplicate3(self, nums: List[int]) -> bool:
        d_nums = set()
        for n in nums:
            if n in d_nums:
                return True
            d_nums.add(n)
        return False
