import random
import numpy as np
import matplotlib.pyplot as plt
import time


def randomized_quick_sort(arr, low, high):
    if(low < high):
        pivotindex = random_partition_index(arr, low, high)
        randomized_quick_sort(arr, low, pivotindex-1)
        randomized_quick_sort(arr, pivotindex + 1, high)


def quick_sort(arr, l, h):
    if l < h:
        partitionIndex = deterministic_partition(arr, l, h)
        quick_sort(arr, l, partitionIndex-1)
        quick_sort(arr, partitionIndex+1, h)


# Here we are generating a Random Pivot and swapping the first element with pivot
def random_partition_index(arr, low, high):
    pivot_index = random.randrange(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    return partition(arr, low, high)


def deterministic_partition(arr, l, h):
    pivot = arr[h]
    i = l
    j = h-1
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] >= pivot and j > -1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[h] = arr[h], arr[i]
    return i


def partition(arr, low, high):
    pivot = low

    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]

    pivot = i - 1
    return pivot


if __name__ == "__main__":
    markings = [f"{i}K" for i in range(1, 11)]

    plt.xlabel("Size of Array --> ")
    plt.ylabel("Time taken in seconds --> ")

    initial_time = time.time()
    time_taken_rqs = list()
    time_taken_dqs = list()

    for i in range(1, 11):
        array = np.random.randint(i * 100, size=i * 100)
        array.sort()

        start = time.time()

        randomized_quick_sort(array, 0, i*100-1)

        end = time.time()
        time_taken_rqs.append(end-start)
        sec = "{:.4f}".format(end-start)

        print("\n*** Randomized Quick Sort ***")
        print(f"Size of Array : {i * 100}")
        print(f"Time Taken to Sort : {sec}s\n")

        start = time.time()

        quick_sort(array, 0, i*100-1)

        end = time.time()
        time_taken_dqs.append(end-start)

        sec = "{:.4f}".format(end-start)

        print("\n*** Deterministic Quick Sort ***")
        print(f"Size of Array : {i * 100}")
        print(f"Time Taken to Sort : {sec}s\n")

    plt.plot(markings, time_taken_rqs, label="Randomized Quick Sort",
             marker=".", color="black")

    plt.plot(markings, time_taken_dqs, label="Deterministic Quick Sort",
             marker=".", color="red")

    plt.legend()
    plt.grid(True)
    plt.show()
