def rangeSum(arr, i, j):
    sum = 0

    for k in range(i, j+1):
        sum += arr[k]

    return sum

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(rangeSum(arr, 1, 3))
    print(rangeSum(arr, 2, 4))