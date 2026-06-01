#Python program to print the Missing number from 1 to n

#defining a function
def missingNum(arr):
    #asssigning length  + 1
    n = len(arr) + 1

    for i in range(1, n+1):
        found = False
        for j in range(n-1):
            if arr[j] == i:
                found = True
                break

        if not found:
            return i
    return -1

if __name__ == "__main__":
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))