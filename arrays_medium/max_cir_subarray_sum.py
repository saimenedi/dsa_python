def maxCircularSum(arr):
    n = len(arr)
    res = arr[0]

    for i in range(n):
        currSum = 0

        for j in range(n):
            idx = (i+j) % n
            currSum += arr[idx]
            res = max(res, currSum)

    return res

if __name__=="__main__":
    arr = [8, -8, 9, -9, 10, -11, 12]
    print(maxCircularSum(arr))   