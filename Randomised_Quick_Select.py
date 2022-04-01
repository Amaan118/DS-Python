import random


def randomized_selection(arr, start, end, k):
    if start == end:
        return arr[start]

    if start < end:
        mid = random_partition_index(arr, start, end)
        position = end - mid + 1
        if position == k:
            return arr[mid]
        elif k > position:
            # s 0 e 5 k 4
            return randomized_selection(arr, start, mid-1, k)
        else:
            return randomized_selection(arr, mid+1, end, position-k)


def random_partition_index(arr, low, high):
    pivot_index = random.randint(low, high)
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


def findKthLargest(nums, k):
    return randomized_selection(nums, 0, len(nums)-1, k)


if __name__ == '__main__':
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(arr, k))
    arr.sort()
    print(arr)

    # Incomplete
