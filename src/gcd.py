"""
This is an example implementation of Greatest Common Divisor using Euclid's algorithm.
"""


def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a


def test():
    print(gcd(60, 96))
    print(gcd(20, 8))


if __name__ == "__main__":
    test()
