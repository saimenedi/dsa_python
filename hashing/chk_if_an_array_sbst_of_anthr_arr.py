# Check if an array is subset of another array

def isSubset(a, b):
    hash_set = set(a)

    for num in b:
        if num not in hash_set:
            return False

    return True

if __name__ == "__main__":
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 7, 1]

    if isSubset(a, b):
        print("True")
    else:
        print("False")