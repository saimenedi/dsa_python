#Maximum equal sum of three stacks

def max_sum(s1, s2, s3):
    sum1 = sum(s1)
    sum2 = sum(s2)
    sum3 = sum(s3)

    top1 = top2 = top3 = 0

    while True:
        if top1 == len(s1) or top2 == len(s2) or top3 == len(s3):
            return 0
        
        if sum1 == sum2 == sum3:
            return sum1
        
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= s1[top1]
            top1 += 1

        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= s2[top2]
            top2 += 1
        else:
            sum3 -= s3[top3]
            top3 += 1

s1 = [3, 2, 1, 1, 1]
s2 = [4, 3, 2]
s3 = [1, 1, 4, 1]

print(max_sum(s1, s2, s3))
