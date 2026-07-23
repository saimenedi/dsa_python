def findWays(n):
    if n % 2 == 1:
        return 0

    pairs = n // 2

    dp  = [[0] * (pairs + 1) for _ in range(pairs+1)]

    for close in range(pairs+1):
        dp[0][close] = 1

    for open in range(1, pairs+1):
        for close in range(open, pairs+1):
            dp[open][close] = dp[open-1][close] + dp[open][close-1]

    return dp[pairs][pairs]

if __name__ == "__main__":
    n = 6
    res = findWays(n)
    print(res)