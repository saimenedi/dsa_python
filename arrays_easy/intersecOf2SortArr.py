def intersection(a, b):
    res = []
    m = len(a)
    n = len(b)

    for i in range(m):
        if i > 0 and a[i-1] == a[i]:
            continue
        
        for j in range(n):
            if a[i] == b[j]:
                res.append(a[i])
                break

    return res

a = [1, 1, 2, 2, 2, 4]
b = [2, 2, 4, 4]

res = intersection(a, b)
print(res)