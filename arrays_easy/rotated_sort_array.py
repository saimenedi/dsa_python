#Search in a Sorted and Rotated Array
def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        
    return -1

if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    index = search(arr, key)
    print(index)