def findMaxSum(arr):
    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    secondLast, last = 0, arr[0]

    for i in range(1, n):
        res = max(arr[i] + secondLast, last)
        secondLast = last
        last = res

    return res

if __name__ == "__main__":
    arr = [6, 7, 1, 3, 8, 2, 4]
    print(findMaxSum(arr))