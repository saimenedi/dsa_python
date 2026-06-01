# Statement: Print all elements of an array


#Initialized a list of elements.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Assigned length of the list "arr" to a variable "size".
size = len(arr)

#printing the statement.
print("The elements present in the array are: ")
#Iterating the list using for loop with range function.
for i in range(0, size):
    #prints the elements of the array on the console.
    print(arr[i])
