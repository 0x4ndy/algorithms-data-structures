"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


from typing import List


class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using hash map - in case the order is not important
        result = []

        a1 = nums1
        a2 = nums2
        if len(nums2) < len(nums1):
            a1 = nums2
            a2 = nums1

        hashmap = dict()
        for n in a1:
            hashmap[n] = hashmap.get(n, 0) + 1

        for n in a2:
            if n in hashmap.keys() and hashmap[n] > 0:
                result.append(n)
                hashmap[n] = hashmap[n] - 1

        return result

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using 2 pointers in case lists are sorted or the result has to be sorted
        nums1.sort()
        nums2.sort()

        result = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result
