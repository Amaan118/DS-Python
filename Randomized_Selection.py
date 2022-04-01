import random
import numpy as np
from matplotlib import pyplot as plt
import time


def randomized_selection(arr, start, end, k):
    if start == end:
        return arr[start]

    if k == 0:
        return "Can't be 0th smallest element"

    if start < end:
        mid = random_partition_index(arr, start, end)
        position = mid - start + 1
        if position == k:
            return arr[mid]
        elif k < position:
            return randomized_selection(arr, start, mid-1, k)
        else:
            return randomized_selection(arr, mid+1, end, k-position)


def random_partition_index(arr, low, high):
    pivot_index = random.randrange(low, high)
    pivot = arr[pivot_index]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    pivot_index = high
    j = low - 1

    for i in range(low, high):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[j+1], arr[pivot_index] = arr[pivot_index], arr[j+1]
    return j+1


if __name__ == '__main__':
    markings = [f"{i}K" for i in range(1, 11)]

    plt.xlabel("Size of Array --> ")
    plt.ylabel("Time taken in seconds --> ")

    initial_time = time.time()
    time_taken = list()

    for i in range(1, 11):
        array = np.random.randint(i * 1000, size=i * 1000)
        k = random.randrange(0, i*1000-1)

        start = time.time()

        ans = randomized_selection(array, 0, i*1000-1, k)

        end = time.time()
        time_taken.append(end-start)

        sec = "{:.4f}".format(end-start)

        print(f"Size of Array : {i * 1000}")
        print(f"Time Taken to Find {k}th smallest : {sec}s")
        print(f"{k}th smallest in array was : {ans}\n")

    total_sec = "{:.4f}".format(time.time()-initial_time)
    print(f"Total Time Of Randomized Selection Algorithm : {total_sec}s\n")
    plt.plot(markings, time_taken, label="Randomized Selection Algorithm",
             marker=".", color="black")

    plt.legend()
    plt.grid(True)
    plt.show()
