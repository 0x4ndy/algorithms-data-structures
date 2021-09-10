# Given a large collection of numbers, find 5 biggest numbers in it.

import sys

from typing import List


def max_sorted(l: List[int], n: int) -> List[int]:
    l.sort()
    return l[-n:]


def max_unsorted(l: List[int], n: int) -> List[int]:

    if len(l) < n:
        return l

    result = [-sys.maxsize]

    for n in l:
        if len(result) >= n:
            if n > result[0]:
                result[0] = n
                result.sort()
        else:
            result.append(n)

    return result


def test():
    l = [6, 0, -3, 1.25, 10, 6]
    print(l)
    print(max_sorted(l, 5))
    print(max_unsorted(l, 5))


if __name__ == "__main__":
    test()
