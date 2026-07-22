def lucas(n):
    a = 2
    b = 1

    if (n==0):
        return a
    
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
    return b

n = 9
print(lucas(n))