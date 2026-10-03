class Node:
  def __init__(self, x):
    self.data = x
    self.left = None
    self.right = None


def find_parent(root, target, parent):
  if root is None:
    return -1

  if root.data == target:
    return parent

  left_search = find_parent(root.left, target, root.data)

  if left_search != -1:
    return left_search

  return find_parent(root.right, target, root.data)

if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)

  target = 3
  parent = find_parent(root, target, -1)

  print(parent)