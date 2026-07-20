#Maximize sum of consecutive differences in a circular array

def maxSum(arr, n):
    sum = 0
    arr.sort()

    for i in range(0, int(n/2)):
        sum -= (2 * arr[i])
        sum += (2 * arr[n - i- 1])

    return sum

arr = [4, 2, 1, 8]
n = len(arr)
print(n)
print(maxSum(arr, n))