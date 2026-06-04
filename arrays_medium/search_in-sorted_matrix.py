def search(arr, x):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo+hi) // 2

        if x == arr[mid]:
            return True
        if x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    lo = 0
    hi = n-1
    row = -1

    while lo <= hi:
        mid = (lo+hi) // 2

        if x == mat[mid][0]:
            return True

        if x > mat[mid][0]:
            row = mid
            lo = mid + 1

        else:
            hi = mid - 1

    if row == -1:
        return False

    return search(mat[row], x)


if __name__ == "__main__":
    mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    x = 14

    if searchMatrix(mat, x):
        print("true")
    else:
        print("false")
