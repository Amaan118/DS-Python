import numpy as np
import time
import os
import matplotlib.pyplot as plt


def bubble_sort(array):
    for passes in range(len(array)-1):  # Loop for Passes
        is_sorted = False
        for comparison in range(0, len(array)-passes-1):  # Loop for Comparison
            if array[comparison] > array[comparison+1]:
                array[comparison], array[comparison +
                                         1] = array[comparison+1], array[comparison]
            is_sorted = True

        if not is_sorted:
            return array


def selection_sort(array):
    for passes in range(len(array)-1):
        low = passes
        for comparison in range(passes+1, len(array)):
            if array[low] > array[comparison]:
                low = comparison
            array[passes], array[low] = array[low], array[passes]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quick_sort(array, low, high):  # Include High
    if low < high:
        parInd = partition(array, low, high)
        quick_sort(array, low, parInd-1)
        quick_sort(array, parInd+1, high)


def count_sort(array):
    max_val = max(array)
    m = max_val + 1
    count = [0] * m

    for a in array:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1


if __name__ == "__main__":
    sorts = [
        {
            'name': 'Bubble Sort',
            'algo': lambda array: bubble_sort(array)
        },
        {
            'name': 'Selection Sort',
            'algo': lambda array: selection_sort(array)
        },
        {
            'name': 'Merge Sort',
            'algo': lambda array: merge_sort(array)
        },
        {
            'name': 'Quick Sort',
            'algo': lambda array: quick_sort(array, 0, len(array)-1)
        },
        {
            'name': 'Count Sort',
            'algo': lambda array: count_sort(array)
        }
    ]

    markings = np.array([i*100 for i in range(1, 11)])
    linetypes = ['-', '-', '-.', ':', '--']
    j = 0

    plt.xlabel("Array Size ---->")
    plt.ylabel("Time Taken in seconds ---->")
    for sort in sorts:
        print('----------------------------------------------------------------')
        print(f"***** {sort['name']} ***** \n")
        time_taken = list()
        total_time = time.time()
        for i in range(1, 11):
            array = np.random.randint(i * 100, size=i * 100)
            start = time.time()
            sort['algo'](array)
            end = time.time()

            time_taken.append(end-start)
            sort_time = "{:.4f}".format(end-start)

            print(f"Length of Array : {i * 100}")
            print(f"Time Taken : {sort_time}s\n")

        total = "{:.4f}".format(time.time()-total_time)

        print(f"Overall Time by {sort['name']} : {total}s")
        print('----------------------------------------------------------------\n\n')

        plt.plot(markings, time_taken,
                 linestyle=linetypes[j], label=sort["name"])
        j += 1

plt.legend()
plt.grid()
plt.show()
