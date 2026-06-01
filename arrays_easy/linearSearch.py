#Python program to perform ilnear search in a list of item

#defininng a function to perform the task
def linSearch(arr, x):
    #Length of the list
    n = len(arr)
    #for(i=0;i<n;i++)
    for i in range(n):
        #if the value of x is equal to the list 
        # Return that index to the caller
        if arr[i] == x:
            return i
    #else return non negative index 
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    x = 6
    
    result = linSearch(arr, x)

    if (result == -1):
        print("Element is not present in array")
    else:
        print(f"{x} is persent at index", result)
