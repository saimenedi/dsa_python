#Maximize the number of segments of length x, y and z

def maxCutHelper(n, x, y, z, memo):

    if n == 0:
        return 0

    if n < 0:
        return -1

    if n in memo:
        return memo[n]

    cut1 = maxCutHelper(n-x, x, y, z, memo)
    cut2 = maxCutHelper(n-y, x, y, z, memo)
    cut3 = maxCutHelper(n-z, x, y, z, memo)

    maxCut = max(cut1, cut2, cut3)

    if maxCut == -1:
        memo[n] = -1
        return -1

    memo[n] = maxCut + 1
    return memo[n]

def maximizeCuts(n, x, y, z):
    memo = {}

    res = maxCutHelper(n, x, y, z, memo)

    if res == -1:
        return 0

    return res

if __name__ == "__main__":
    n = 11
    x = 2
    y = 3
    z = 5

    print(maximizeCuts(n, x, y, z))