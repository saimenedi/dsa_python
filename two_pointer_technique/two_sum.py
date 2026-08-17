# Step-by-step algorithm:

# We need to initialize two pointers as left and right with position at the beginning and at the end of the array respectively.
# Need to calculate the sum of the elements in the array at these two positions of the pointers.
# If the sum equals to target value, return the 1-indexed positions of the two elements.
# If the sum comes out to be less than the target, move the left pointer to the right to the increase the sum.
# If the sum is greater than the target, move the right pointer to the left to decrease the sum.
# Repeat the following steps till both the pointers meet.


from typing import List

def twoSum(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return [left+1, right+1]

        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    result = twoSum(arr, target)
    for num in result:
        print(arr[num], end=' ')
    print()