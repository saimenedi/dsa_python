class Node:
  def __init__(self, x):
    self.data = x
    self.left = None
    self.right = None

def ifNodeExists(root, key):
  if root is None:
    return False

  if root.data == key:
    return True

  res1 = ifNodeExists(root.left, key)

  if res1:
    return True

  res2 = ifNodeExists(root.right, key)

  return res2

if __name__ == "__main__":
  root = Node(0)
  root.left = Node(1)
  root.left.left = Node(3)
  root.left.left.left = Node(7)
  root.left.right = Node(4)
  root.left.right.left = Node(8)
  root.left.right.right = Node(9)
  root.right = Node(2)
  root.right.left = Node(5)
  root.right.right = Node(6)

  key = 4

  if ifNodeExists(root, key):
    print("True")
  else:
    print("False")