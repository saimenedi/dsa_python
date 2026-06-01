#Python program to find Union of two sorted arrays

#defining a function to perform the task
def findUnion(a, b):
    #Creating an empty list
    res = []

    #for(i=0;i<len(a);i++)
    for i in range(len(a)):
        #if a[i] value is not in res[] then
        #we are appending the value to res
        if a[i] not in res:
            res.append(a[i])
    #for(i=0;i<len(b);i++)
    for i in range(len(b)):
        #if b[i] value is not there in res then
        #append the value to res
        if b[i] not in res:
            res.append(b[i])
    #Sort the res list
    res.sort()
    #return the list to the caller
    return res

if __name__ == "__main__":
    a = [1, 1, 2, 2, 3, 4,]
    b = [2, 2, 3, 5]
    #calling the function and assigning it to a variable
    res = findUnion(a, b)

    for i in res:
        print(i, end=" ")