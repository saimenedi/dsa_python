def cntSubarrays(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        currSum = 0

        for j in range(i, n):
            currSum += arr[j]

            if currSum == k:
                count += 1

    return count

if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(cntSubarrays(arr, k))