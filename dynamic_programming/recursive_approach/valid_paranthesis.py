def countValid(open, close):

    if close < open:
        return 0

    if open == 0:
        return 1

    return countValid(open - 1, close) + countValid(open, close - 1)

def findWays(n):

    if n % 2 == 1:
        return 0
    return countValid(n // 2, n // 2)

if __name__ == "__main__":
    n = 4
    res = findWays(n)
    print(res)