"""
This is an example implementation of Priority Queue data structure.
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """ 
        Element is a tuple (priority, item), hence using [1] to return the actual item.
        """
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


def test():
    pq = PriorityQueue()

    pq.put("third", 3)
    pq.put("second", 2)
    pq.put("first", 1)
    print(pq)

    element = pq.get()
    print(element)

    assert element == "first"


if __name__ == "__main__":
    test()
