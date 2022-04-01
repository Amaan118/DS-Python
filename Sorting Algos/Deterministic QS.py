from matplotlib import pyplot as plt
import time
import numpy as np


def partition(arr, l, h):
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


def quick(arr, l, h):
    if l < h:
        partitionIndex = partition(arr, l, h)
        quick(arr, l, partitionIndex-1)
        quick(arr, partitionIndex+1, h)


if __name__ == "__main__":
    markings = np.array([f"{i*10}K" for i in range(1, 11)])

    plt.xlabel("Size of Array --> ")
    plt.ylabel("Time taken in seconds --> ")

    print("*** Deterministic Quick Sort : \n It is a Quick Sort where pivot is taken as last elemtn of array and based on that partition is done.***\n")

    initial = time.time()
    time_taken = list()

    for i in range(1, 11):
        arr = np.random.randint(i * 100, size=i * 100)
        arr.sort()

        start = time.time()
        quick(arr, 0, i*100-1)
        end = time.time()
        time_taken.append(end-start)

        sec = "{:.4f}".format(end-start)

        print(f"Size of Array : {i * 100}")
        print(f"Time Taken to Sort : {sec}s\n")

    total_sec = "{:.4f}".format(time.time()-initial)
    print(f"Total Time Of Deterministic Quick Sort : {total_sec}s\n")
    plt.plot(markings, time_taken, label="Deterministic Quick Sort",
             marker=".", color="black")

    plt.legend()
    plt.grid(True)
    plt.show()
