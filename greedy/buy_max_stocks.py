def buyMaximumProducts(n, k, price):
    arr  = []

    for i in range(n):
        arr.append([i+1, price[i]])

    arr.sort(key = lambda x: x[1])

    total_purchase = 0
    for i in range(n):
        P = min(arr[i][0], k//arr[i][1])
        total_purchase += P
        k -= (P* arr[i][1])

    return total_purchase


price = [10, 7, 19]
n = len(price)
k = 45

print(buyMaximumProducts(n, k, price))