"""
https://leetcode.com/problems/ransom-note/
"""


class Solution:

    def can_construct1(self, ransomNote: str, magazine: str) -> bool:
        # O(m * n)
        for c in ransomNote:
            if c in magazine:
                idx = magazine.index(c)
                magazine = magazine[:idx] + magazine[idx+1:]
            else:
                return False

        return True

    def can_construct2(self, ransomNote: str, magazine: str) -> bool:
        # Two hash maps
        hmr = dict()
        hmm = dict()

        for c in ransomNote:
            count = hmr.get(c, 0)
            hmr[c] = count + 1

        for c in magazine:
            count = hmm.get(c, 0)
            hmm[c] = count + 1

        for k, v in hmr.items():
            if (not k in hmm.keys() or v > hmm[k]):
                return False

        return True

    def can_construct3(self, ransomNote: str, magazine: str) -> bool:
        # One hash map
        hm = dict()

        for c in magazine:
            count = hm.get(c, 0)
            hm[c] = count + 1

        for c in ransomNote:
            if not c in hm.keys():
                return False
            else:
                count = hm[c]
                if count == 0:
                    return False
                hm[c] = count - 1

        return True
