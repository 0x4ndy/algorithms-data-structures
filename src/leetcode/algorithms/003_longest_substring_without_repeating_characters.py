"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        a = []
        max_count = 0
        for c in s:
            if c in a:
                count = len(a)
                max_count = count if count > max_count else max_count
                idx = a.index(c)
                a = a[idx+1:] if idx < len(a) else []

            a.append(c)

        count = len(a)
        max_count = count if count > max_count else max_count
        return max_count
