def findEquilibrium(arr):
    for i in range(len(arr)):
        leftSum = sum(arr[:i])

        rightSum = sum(arr[i+1:])

        if leftSum == rightSum:
            return i
    return -1

if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print(findEquilibrium(arr))