"""
This is an example implementation of Bubble Sort algorithm.
"""


def bubbleSort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                tmp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = tmp


def test():
    list1 = [3, 6, 1, 9, 20, 12, 43, 1, 2, 4, 8, 5]
    print("List: ", list1)
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    test()
