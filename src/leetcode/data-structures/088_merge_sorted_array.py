"""
https://leetcode.com/problems/merge-sorted-array/
"""


from typing import List


class Solution:
    # First solution using search insert position
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for n in nums2:
            left, right = 0, m - 1
            while left <= right:
                idx = (left + right) // 2
                if n == nums1[idx]:
                    left = idx
                    break
                elif n > nums1[idx]:
                    left = idx + 1
                elif n < nums1[idx]:
                    right = idx - 1

            nums1.insert(left, n)
            nums1.pop(-1)
            m += 1

    # Approach 3 : Three Pointers (Start From the End) - https://leetcode.com/problems/merge-sorted-array/solution/ 
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
