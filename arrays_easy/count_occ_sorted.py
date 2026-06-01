#Count number of occurrences (or frequency) in a sorted array
def countFreq(arr, target):
    res = 0
    for i in range(len(arr)):
        if arr[i] == target:
            res += 1

    return res

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2

    print(countFreq(arr, target))