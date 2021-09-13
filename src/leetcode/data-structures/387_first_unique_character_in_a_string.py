"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


class Solution:
    def first_uniq_char1(self, s: str) -> int:
        # Brute force
        tmp = []
        for i in range(0, len(s)):
            if s[i] in tmp:
                continue
            found: bool = False
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    found = True
                    continue

            if not found:
                return i
            tmp.append(s[i])

        return -1

    def first_uniq_char2(self, s: str) -> int:

        # hashmap = collections.Counter(s) - possible hashmap building
        hashmap = dict()
        for c in s:
            count = hashmap.get(c, 0)
            hashmap[c] = count + 1

        for idx, c in enumerate(s):
            if hashmap[c] == 1:
                return idx

        return -1
