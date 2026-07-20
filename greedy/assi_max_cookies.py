#Given two arrays, greed[] and cookie[] such that greed[i] denotes the minimum cookie 
# size wanted by ith child and cookie[i] denotes the size of ith cookie, we have to find the maximum number of children that can be satisfied by assigning them cookies, with each child getting at most 1 cookie.


def maxChildren(greed, cookie):
    greed.sort()
    cookie.sort()

    i = 0
    j = 0
    cnt = 0

    while i < len(greed) and j < len(cookie):

        if greed[i] <= cookie[j]:
            cnt += 1
            i += 1
            j += 1

        else:
            j += 1

    return cnt

if __name__ == "__main__":
    greed = [1, 10, 3]
    cookie = [1, 2, 3]

    print(maxChildren(greed, cookie))
