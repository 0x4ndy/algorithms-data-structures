"""
https://leetcode.com/problems/reverse-string/
"""


from typing import List


class Solution:

    def reverse_string1(self, s):
        # Life is short, use Python
        s.reverse()

    def reverse_string2(self, s: List[str]) -> None:
        # Manual swap
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            tmp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = tmp
