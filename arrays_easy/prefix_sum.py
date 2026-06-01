def prefSum(arr):
    n = len(arr)

    prefixSum = [0]*n

    prefixSum[0] = arr[0]

    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1]+arr[i]
    return prefixSum

if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefixSum = prefSum(arr)

    for i in prefixSum:
        print(i, end = " ")