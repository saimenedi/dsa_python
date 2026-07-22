def countWaysRec(n, dp):
    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]

    dp[n] = countWaysRec(n-1, dp) + countWaysRec(n-2, dp)
    return dp[n]

def countWays(n):

    dp = [-1]*(n+1)
    return countWaysRec(n, dp)

if __name__ == "__main__":
    n = 4
    print(countWays(n))

