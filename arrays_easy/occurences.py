#count te number of Oocurences

def countFreq(arr, target):
    res = 0
    #for(i=0;i<n;i++)
    for i in range(len(arr)):
        #if list element is equal to target 
        #increment the res counter
        #and break
        if arr[i] == target:
            res += 1
    #return res to the caller
    return res

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    print(countFreq(arr, target))