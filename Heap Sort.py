import numpy as np
from matplotlib import pyplot as plt
import time


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    sizes = np.array([i*10000 for i in range(1, 11)])

    total_time = time.time()
    time_taken = list()

    print("**** Heap Sort ****")
    for i in range(1, 11):
        array = np.random.randint(i * 10000, size=i * 10000)

        start = time.time()
        heapSort(array)
        end = time.time()

        time_taken.append(end-start)
        sec = "{:.4f}".format(end-start)

        print(f"\nLength of Array : {i*10000}")
        print(f"Time Taken to Sort : {sec}s")

    plt.plot(sizes, time_taken, label='Heap Sort')

    total = "{:.4f}".format(time.time()-total_time)
    print(f"\nOverall Time by Heap Sort : {total}s")

    plt.legend()
    plt.show()
