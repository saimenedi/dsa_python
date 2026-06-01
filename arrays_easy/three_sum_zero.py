def findTriplets(arr):
    res = []
    n = len(arr)

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    res.append([i, j, k])

    return res

arr = [0, -1, 2, -3, 1]
res = findTriplets(arr)
for triplet in res:
    print(triplet[0], triplet[1], triplet[2])