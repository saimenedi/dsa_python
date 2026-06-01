#Python program to left rotate array by K places

#function to rotate a n array left by k places
def rotateArr(arr, k):
    #length of the array

    n = len(arr)
    #Repeat the rotation k times
    #for(i=0;i<k;i++)
    for i in range(k):

        #assigning the value of arr[0] to first
        first = arr[0]

        #Left Rotate the array by one position
        for j in range(n-1):
        
            arr[j] = arr[j+1]
            #arr[0] = arr[0+1]
            #arr[0] = arr[1]
            #arr[0] = 2
            #.
            #.
            #.
        #last position is assigned to the first 
        arr[n-1] = first

# it is used to check whether a script is 
#being run directly or being imported as a module
if __name__ == "__main__":
    #Creating a list
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    #calling the function
    rotateArr(arr, k)
    #Iterating the array to display the result
    for i in range(len(arr)):
        print(arr[i], end=" ")