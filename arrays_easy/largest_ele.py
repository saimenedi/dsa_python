#Python program to print the largest element from a list

#Initialized a list 
arr = [10, 324, 45, 90, 1000]


#assigend the first element to the varaible res.
#Assumption arr[0] is the maximum element.
res = arr[0]


#Iterating the list using range function.
for i in range(0, len(arr)):

    #condition to check the largest element.
    if arr[i] > res:
        
        #Assigning the largest element to the res varaiable.
        res = arr[i]

#Displaying the result.
print("The largest element in the list is:",res)