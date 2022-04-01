def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r-l+1:
        n = r-l+1
        median = list()

        i = 0
        while(i < n // 5):
            median.append(findMedian(arr, l+i*5, 5))

        if(i*5) < n:
            median.append(findMedian(arr, l+i*5, 5))

        if i == 1:
            medOfMed = median[i-1]
        else:
            medOfMed = kthSmallest(median, 0, i-1, i//2)

        pos = partition(arr, l, r, medOfMed)

        if pos-l == k-1:
            return arr[pos]
        elif pos-l > k-1:
            return kthSmallest(arr, l, pos-1, k)
        return kthSmallest(arr, pos+1, r, k-pos+l-1)

    return 999999999999


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            swap(arr, r, i)
            break

    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i


def findMedian(arr, l, n):
    print('h')
    lis = []
    for i in range(l, l + n):
        lis.append(arr[i])

    # Sort the array
    lis.sort()

    # Return the middle element
    return lis[n // 2]


# Driver Code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is", kthSmallest(arr, 0, n - 1, k))
