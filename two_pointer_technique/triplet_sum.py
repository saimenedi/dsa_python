# Let us understand with this example:
# arr[] = [1, 4, 45, 6, 10, 8], target = 13

# Sort the array: arr = [1, 4, 6, 8, 10, 45].
# Set i = 0, fix the first element as 1, so the remaining two elements must sum to 12.
# Initialize l = 1 (4) and r = 5 (45).
# 4 + 45 = 49, which is greater than 12, so move r left to reduce the sum.
# 4 + 10 = 14, which is still greater than 12, so move r left again.
# 4 + 8 = 12, which matches the required sum.
# The triplet (1, 4, 8) adds up to 13, so the function returns true.


def hasTripletSum(arr, target):
    n = len(arr)
    arr.sort()

    for i in range(n-2):
        l = i+1
        r = n-1

        requiredSum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                return True
            if arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1

        return False

if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    target = 13
    if hasTripletSum(arr, target):
        print("true")
    else:
        print("false")