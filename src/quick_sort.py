"""
This is an example implementation of Quick Sort algorithm.
"""


def quick_sort(dataset, first, last):
    if first < last:
        pivotIdx = partition(dataset, first, last)

        quick_sort(dataset, first, pivotIdx-1)
        quick_sort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    pivotvalue = datavalues[first]

    lower = first + 1
    upper = last

    done = False
    while not done:
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        if upper < lower:
            done = True
        else:
            tmp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = tmp

    tmp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = tmp

    return upper


def test():
    items = [3, 6, 1, 9, 20, 12, 43, 1, 2, 4, 8, 5]
    print("Items: ", items)
    quick_sort(items, 0, len(items) - 1)
    print("Result: ", items)


if __name__ == "__main__":
    test()
