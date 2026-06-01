#Python program to remove duplicates from an array

#function to remove duplicates 
def removeDuplicates(arr):
    n = len(arr)
    #if the len less than or equal to one 
    # return the length of the list
    if n <= 1:
        return n
    
    #assigning a value 1 to the varaiable index
    idx = 1

    #Iterating the list using range function
    for i in range(1, n):
        #checking the Unique condition
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx += 1
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    for i in range(newSize):
        print(arr[i], end=" ")