def subCount(arr, k):
    n = len(arr)
    res = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = (sum+arr[j]) % k
            if sum == 0:
                res += 1

    return res


if __name__ == "__main__":
    arr = [4, 5, 0, -2, -3, 1]
    k = 5
    print(subCount(arr, k))
