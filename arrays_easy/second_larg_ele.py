#Python program to find the 2nd Largest element in a list.

#Initializing a list of integers to a variable numbers.
numbers = [10, 20, 20, 4, 25, 45, 54, 99]

# The list is converted to set by using set() to eliminate the duplicates
#Again it is type casted to list by using list().
unique_numbers = list(set(numbers))

# sorting the original list.
unique_numbers.sort()

#After sorting the list assigning the second 
#largest element to a varaiablle second_largest.
second_largest = unique_numbers[-2]

#Displaying the result 
print("Second Largest Number is:", second_largest)