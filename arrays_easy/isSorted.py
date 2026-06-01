#Python program to check if the list is sorted or not

#Function to check if the list is sorted or not?
def isSorted(arr):
    # Length of the list 
    n = len(arr)
    #Iterating the list.
    for i in range(1, n):
        #Comparing the list elements with its previous ele..
        if (arr[i-1] > arr[i]):
            return False
    return True

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)

    if(isSorted):
        print("true")
    else:
        print("false")