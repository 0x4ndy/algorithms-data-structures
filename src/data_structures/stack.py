"""
This is an example implementation of Stack data structure.
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str_(self):
        return str(self.items)


def test():
    pass


# Run the test function if executed as standalone
if __name__ == "__main__":
    test()
