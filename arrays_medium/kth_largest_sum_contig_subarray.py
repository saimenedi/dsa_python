def kthLargest(arr, k):
    n = len(arr)

    sums = []

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            sums.append(sum)

    sums.sort(reverse=True)

    return sums[k-1]

if __name__ == "__main__":
    arr = [20, -5, -1]
    k = 3
    print(kthLargest(arr, k))