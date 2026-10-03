class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None

def levelOrderRec(root, level, res):
  if root is None:
    return

  if len(res) <= level:
    res.append([])

  res[level].append(root.data)

  levelOrderRec(root.left, level+1, res)
  levelOrderRec(root.right, level+1, res)

def levelOrder(root):
  res = []
  levelOrderRec(root, 0, res)
  return res

if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.right = Node(6)

  res = levelOrder(root)

  for level in res:
    print(' '.join(map(str, level)))