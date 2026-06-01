def sortSquare(arr, n):
    for i in range(n):
        arr[i] = arr[i]*arr[i]
    arr.sort()

arr = [-6, -3, -1, 2, 4, 5]
n = len(arr)

print("Before sort")
for i in range(n):
    print(arr[i], end=" ")
print("\n")
sortSquare(arr, n)
print("After sort")
for i in range(n):
    print(arr[i], end=" ")
print("\n")