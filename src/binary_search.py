"""
This is an example implementation of Binary Search algorithm.
"""


def binary_search(item, item_list):
    list_size = len(item_list) - 1

    lower_idx = 0
    upper_idx = list_size

    while lower_idx <= upper_idx:
        mid_idx = (lower_idx + upper_idx) // 2

        if item_list[mid_idx] == item:
            return mid_idx

        if item > item_list[mid_idx]:
            lower_idx = mid_idx + 1
        else:
            upper_idx = mid_idx - 1

    if lower_idx > upper_idx:
        return None


def test():
    items = [1, 1, 2, 3, 4, 5, 6, 8, 9, 12, 20, 43]
    print("List: {}".format(items))
    print("Value {} is at index: {}".format(9, binary_search(9, items)))


if __name__ == "__main__":
    test()
