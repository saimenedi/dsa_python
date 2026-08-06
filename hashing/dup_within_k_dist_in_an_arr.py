def checkDuplicatesWithinK(arr, n, k):
    myset= set()

    for i in range(n):
        if arr[i] in myset:
            return True

        myset.add(arr[i])

        if (i >= k):
            myset.remove(arr[i-k])

    return False

if __name__ == "__main__":
    arr = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr)
    if (checkDuplicatesWithinK(arr, n, 3)):
        print("Yes")
    else:
        print("No")
