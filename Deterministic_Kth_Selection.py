import random
from statistics import median
import numpy as np
import time
from matplotlib import pyplot as plt


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    # print(arr)
    return arr[len(arr)//2]


def partition(A, l, h):
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


def get_median(array, low, high, k):
    medians = list()

    for i in range(low, high+1, 5):
        medians.append(insertion_sort(array[i:min(i+5, high+1)]))

    return medians[len(medians)//2]


def Deterministic_Quick_Select(array, k, low, high):
    median = get_median(array, low, high, k)
    medInd = array.index(median)
    array[high], array[medInd] = array[medInd], array[high]

    pos = partition(array, low, high) - low + 1

    if pos == k:
        return array[k]
    elif pos > k:
        return Deterministic_Quick_Select(array, k, low, pos-1)
    else:
        return Deterministic_Quick_Select(array, k, pos+1, k-pos)
    exit()

    if end-start+1 <= 5:
        InsertionSort(A, start, 1, end)
        return A[start+i-1]
    else:
        k = (end-start+1)//5
        for j in range(0, k):
            InsertionSort(A, start+j, k, end)

        med_med = Deterministic_Quick_Select(
            A, (start + (2*k)), (start + (3*k)-1), k//2)
        A[i], A[med_med] = A[med_med], A[i]

        q = Partition(A, start, end)
        if i <= q-start+1:
            return Deterministic_Quick_Select(A, start, q, i)
        else:
            return Deterministic_Quick_Select(A, q+1, end, i-(q-start+1))


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26, 21, 95, 11]
    k = 2

    print(Deterministic_Quick_Select(arr, k, 0, len(arr)-1))
    exit()

    markings = [str(i)+'K' for i in range(1, 11)]

    plt.xlabel("Size of Array -->")
    plt.xlabel("Time taken in seconds -->")

    initial_time = time.time()
    time_taken = list()

    for i in range(1, 11):
        array = np.random.randint(i*1000, size=i*1000)

        k = random.randint(i, i*1000)

        start = time.time()

        ans = Selection(array, 0, i*1000-1, k)

        end = time.time()
        time_taken.append(end-start)

        sec = "{:.4f}".format(end-start)
        print(f"Size of Array : {i * 1000}")
        print(f"Time Taken to Find {k}th smallest : {sec}s")
        print(f"{k}th smallest in array was : {ans}\n")

    total_sec = "{:.4f}".format(time.time()-initial_time)
    print(f"Total Time Of Randomized Selection Algorithm : {total_sec}s\n")
    plt.plot(markings, time_taken, label="Deterministic Selection Algorithm",
             marker=".", color="black")

    plt.legend()
    plt.grid(True)
    plt.show()
