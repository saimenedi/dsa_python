def fourSum(arr, target):
    res = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        curr = [arr[i], arr[j], arr[k], arr[l]]

                        curr.sort()

                        if curr not in res:
                            res.append(curr)

    return res

if __name__ == "__main__":
    arr = [10, 2, 3, 4, 5, 7, 8]
    target = 23
    ans = fourSum(arr, target)
    for v in ans:
        print(" ".join(map(str, v)))