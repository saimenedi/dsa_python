def subarraySum(arr, traget):
    res = []
    n = len(arr)

    for s in range(n):
        curr = 0

        for e in range(s, n):
            curr += arr[e]
            if curr == target:
                res.append(s+1)
                res.append(e+1)
                return res
            
    return [-1]
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    res = subarraySum(arr, target)

    for ele in res:
        print(ele, end = " ")