def intersect(a, b):
    sa = set(a)

    res = []

    for elem in b:
        if elem in sa:
            res.append(elem)

            sa.remove(elem)

    return res

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = intersect(a, b)
    print(res)
    print(" ".join(map(str, res)))