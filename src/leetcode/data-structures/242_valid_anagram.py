"""
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hms = dict()
        hmt = dict()
        for i in range(0, len(s)):
            c = hms.get(s[i], 0)
            hms[s[i]] = c + 1
            c = hmt.get(t[i], 0)
            hmt[t[i]] = c + 1

        for k, v in hms.items():
            if (not k in hmt.keys() or v != hmt[k]):
                return False

        return True
