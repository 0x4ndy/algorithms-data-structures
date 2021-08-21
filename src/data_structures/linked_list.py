"""
This is an example implementation of Linked List.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def deleteAt(self, idx):
        if idx > self.count - 1:
            return

        if idx == 0:
            self.head = self.head.get_next()
        else:
            tmpIdx = 0
            node = self.head
            while (tmpIdx < idx - 1):
                node = node.get_next()
                tmpIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


def test():
    itemList = LinkedList()
    itemList.insert(38)
    itemList.insert(49)
    itemList.insert(13)
    itemList.insert(15)
    itemList.dump_list()

    print("Item count: ", itemList.get_count())
    print("Finding item: ", itemList.find(13))
    print("Finding item: ", itemList.find(78))

    itemList.deleteAt(3)
    print("Item count: ", itemList.get_count())
    print("Finding item: ", itemList.find(38))
    itemList.dump_list()


# Run the test function if executed as standalone
if __name__ == "__main__":
    test()
