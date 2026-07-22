#Count ways to reach the nth stair using step 1, 2 or 3
def countWaysRecur(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if memo[n] != -1:
        return memo[n]

    memo[n] = countWaysRecur(n-1, memo) + countWaysRecur(n-2, memo) + countWaysRecur(n-3, memo)
    return memo[n]


def countWays(n):
    memo = [-1]*(n+1)
    return countWaysRecur(n, memo)

if __name__ == "__main__":
    n = 4
    print(countWays(n))