#Longest Subarray With Sum K

def longestSubarray(arr, k):
    res = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]

            if sum == k:
                subLen = j - i + 1
                res = max(res, subLen)
        return res
    
if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, -10]
    k = 15
    print(longestSubarray(arr, k))