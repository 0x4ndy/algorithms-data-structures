"""
https://leetcode.com/problems/maximum-subarray/
"""

import math
from typing import List


class Solution:
    # Solution 1 (Optimized Brute Force)
    def max_sub_array1(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray
    # Solution 2 (Dynamic programming - Kadane's Algorithm)

    def max_sub_array2(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]

        for n in nums[1:]:
            current_subarray = max(n, current_subarray + n)
            max_subarray = max(current_subarray, max_subarray)

        return max_subarray

    # Solution 3 (Divide and Conquer)
    def max_sub_array3(self, nums: List[int]) -> int:
        def find_best_subarray(nums, left, right):
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            left_half = find_best_subarray(nums, left, mid - 1)
            right_half = find_best_subarray(nums, mid + 1, right)

            return max(best_combined_sum, left_half, right_half)

        return find_best_subarray(nums, 0, len(nums) - 1)
