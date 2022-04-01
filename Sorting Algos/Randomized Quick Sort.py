import random
import numpy as np
import matplotlib.pyplot as plt
import time


def randomized_quick_sort(arr, low, high):
    if(low < high):
        pivotindex = random_partition_index(arr, low, high)
        randomized_quick_sort(arr, low, pivotindex-1)
        randomized_quick_sort(arr, pivotindex + 1, high)


# Here we are generating a Random Pivot and swapping the first element with pivot
def random_partition_index(arr, low, high):
    pivot_index = random.randrange(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    return partition(arr, low, high)


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
    time_taken = list()

    for i in range(1, 11):
        array = np.random.randint(i * 1000, size=i * 1000)

        start = time.time()

        randomized_quick_sort(array, 0, i*1000-1)

        end = time.time()
        time_taken.append(end-start)

        sec = "{:.4f}".format(end-start)

        print(f"Size of Array : {i * 1000}")
        print(f"Time Taken to Sort : {sec}s\n")

    total_sec = "{:.4f}".format(time.time()-initial_time)
    print(f"Total Time Of Randomized Quick Sort : {total_sec}s\n")
    plt.plot(markings, time_taken, label="Randomized Quick Sort",
             marker=".", color="black")

    plt.legend()
    plt.grid(True)
    plt.show()
