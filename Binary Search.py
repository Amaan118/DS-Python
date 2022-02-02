import time

def binary_search(arr, num):
    high = len(arr) - 1
    low = 0
    iter = 0
    while low <= high:
        iter += 1
        mid = (high + low)//2
        if arr[mid] == num:
            return mid,iter
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def linear_search(arr, num):
    for ind, val in enumerate(arr):
        if val == num:
            return ind
    return -1


arr = [i for i in range(1000000)]

t1 = time.time()
print(linear_search(arr, 500000))
print(time.time() - t1)

t2 = time.time()
print("Index of Element : ", binary_search(arr, 500000)[0], "\nIterations : ", binary_search(arr, 500000)[1] )
print(time.time() - t2)