"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        reversed_string = ""

        for word in s.split():
            w = list(word)
            w.reverse()
            reversed_string += "".join(w) + " "

        return reversed_string[:-1]
