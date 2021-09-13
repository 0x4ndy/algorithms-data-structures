"""
https://leetcode.com/problems/first-bad-version/
"""


def first_bad_version(v: int) -> bool:
    """
    The implementation of this function is provided within Leetcode
    """

    return False


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n

        while left <= right:
            v = left + (right - left) // 2
            if first_bad_version(v):
                right = v
            else:
                left = v + 1

        return right
