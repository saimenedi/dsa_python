def countNum(arr):
  s = set()
  maxm = float('-inf')
  minm = float('inf')

  for num in arr:
    s.add(num)

    if num < minm:
      minm = num
    if num > maxm:
      maxm = num
  return (maxm - minm + 1) - len(s)

if __name__ == "__main__":
  arr = [3, 5, 8, 6]
  print(countNum(arr))