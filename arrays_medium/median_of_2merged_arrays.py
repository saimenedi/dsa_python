def medianOf2(a, b):
    c = a + b

    c.sort()

    len_c = len(c)

    if len_c % 2 == 0:
        return (c[len_c // 2] + c[len_c // 2-1]) / 2.0

    else:
        return c[len_c // 2]


if __name__ == "__main__":
    a = [-5, 3, 6, 12, 15]
    b = [-12, -10, -6, -3, 4, 10]
    print(medianOf2(a, b))
