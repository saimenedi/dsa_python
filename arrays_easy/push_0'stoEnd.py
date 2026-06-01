#Python Program to Push zeroes to the end

#defining a function to do the task
def pushZerosToEnd(arr):
    #length of the array
    n = len(arr)
    #creates an empty list of the size n and
    #initializes 0 to every index
    temp = [0]*n

    j = 0
    #for(i=0;i<n;i++)
    for i in range(n):
        #checing the current i value is equal to zero or not!
        #if it's not equal to zero then copy the element to the empty list
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1
    #Fill remaining positions in temp with zero
    while j < n:
        temp[j] = 0
        j += 1
    #Copy elemnts from temp to arr
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    #for every number in the list of array
    for num in arr:
        print(num, end = " ") 