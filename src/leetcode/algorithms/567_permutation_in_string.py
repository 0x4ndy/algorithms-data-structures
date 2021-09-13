"""
https://leetcode.com/problems/permutation-in-string/
"""

from typing import List


class Solution:
    """
    Solution using an array as a sliding window over s2.
    Complexity:
    n = len(s1)
    m = len(s2)
    O(n + (m - n) * 26)
    """

    def check_inclusion(self, s1: str, s2: str) -> bool:
        # s1 can't be longer than s2
        if len(s1) > len(s2):
            return False

        a1, a2 = [0] * 26, [0] * 26

        # first sliding window for s2
        for i in range(len(s1)):
            # ascii of s1/2 - 'a' to get the index and increase the occurence
            a1[ord(s1[i]) - ord('a')] += 1
            a2[ord(s2[i]) - ord('a')] += 1

        # move the sliding window
        for i in range(0, len(s2) - len(s1)):
            # check if a1 and a2 match
            if self.equals(a1, a2):
                return True

            # moving the window to the right
            # decreasing the count of this letter
            a2[ord(s2[i]) - ord('a')] -= 1
            # increasing the count of this letter
            a2[ord(s2[i + len(s1)]) - ord('a')] += 1

        return self.equals(a1, a2)

    def equals(self, a1: List[int], a2: List[int]) -> bool:
        for i in range(len(a1)):
            if a1[i] != a2[i]:
                return False

        return True
