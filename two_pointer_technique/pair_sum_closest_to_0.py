# Steps to implement the above idea:

# Sort the array in ascending order.
# Initialize two pointers: one at the start and one at the end.
# Initialize variables to store the closest sum and its absolute difference.
# Iterate while left pointer is less than right pointer.
# Update the closest sum if the current sum is closer to zero.
# Move the left pointer right if the sum is negative; else, move the right pointer left.


from typing import List

def closestToZero(arr: List[int]):
    arr.sort()

    i = 0
    j = len(arr) - 1

    sum  = arr[i] + arr[j]

    diff = abs(sum)

    while i < j:

        if arr[i] + arr[j] == 0:
            return 0

        if abs(arr[i] + arr[j]) < abs(diff):
            diff = abs(arr[i]+arr[j])
            sum = arr[i] + arr[j]
        elif abs(arr[i] + arr[j] == abs(diff)):

            sum = max(sum, arr[i] + arr[j])

        if arr[i] + arr[j] > 0:
            j -= 1
        else:
            i += 1
    return sum


arr = [0, -8, -6, 3]
print(closestToZero(arr))

