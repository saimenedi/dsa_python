class Node:
  def __init__(self, x):
    self.data = x
    self.left = None
    self.right = None
def inorder(root, low, high, ans):
  if root is None:
    return

  inorder(root.left, low, high, ans)

  if low <= root.data <= high:
    ans.append(root.data)

  inorder(root.right, low, high, ans)

def nodesInRange(root, low, high):
  ans = []

  inorder(root, low, high, ans)
  return ans

if __name__ == "__main__":
  root = Node(22)
  root.left = Node(12)
  root.right = Node(30)
  root.left.left = Node(8)
  root.left.right = Node(20)  

  low, high = 10, 22

  ans = nodesInRange(root, low, high)

  print(' '.join(map(str, ans)))