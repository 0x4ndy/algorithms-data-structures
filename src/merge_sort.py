"""
This is an example implementation of Merge Sort algorithm.
"""


def merge_sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left = dataset[:mid]
        right = dataset[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                dataset[k] = left[i]
                i += 1
            else:
                dataset[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            dataset[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            dataset[k] = right[j]
            j += 1
            k += 1


def test():
    items = [3, 6, 1, 9, 20, 12, 43, 1, 2, 4, 8, 5]
    print("Items: ", items)
    merge_sort(items)
    print("Result: ", items)

if __name__ == "__main__":
    test()