def findDuplicates(arr):
  s = set()
  for x in arr:
    if x in s: 
      return x
    s.add(x)
  return -1

if __name__ == "__main__":
  arr = [1, 3, 2, 3, 4]
  print(findDuplicates(arr))