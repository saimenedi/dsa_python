def nthfibonacciUtil(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = nthfibonacciUtil(n-1, dp) + nthfibonacciUtil(n-2, dp)

    return dp[n]


def nthFibonacci(n):

    dp = [-1]*(n+1)

    return nthfibonacciUtil(n, dp)


if __name__ == "__main__":
    n = 5
    result = nthFibonacci(n)
    print(result)
