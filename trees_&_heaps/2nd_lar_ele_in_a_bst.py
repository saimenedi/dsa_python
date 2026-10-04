class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def reverseInorder(root, count, result):
  if root is None or count[0] >= 2:
    return 

  reverseInorder(root.right, count, result)

  count[0] += 1

  if count[0] == 2:
    result[0] = root.data
    return 

  reverseInorder(root.left, count, result)

def findSecondLargest(root):
  count = [0]
  result = [-1]

  reverseInorder(root, count, result)

  return result[0]

if __name__ == "__main__":
  root = Node(7)
  root.left = Node(4)
  root.right = Node(8)
  root.left.left = Node(3)
  root.left.right = Node(5)

  secondLargest = findSecondLargest(root)
  print(secondLargest)