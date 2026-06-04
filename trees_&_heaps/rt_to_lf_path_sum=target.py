# Root to leaf path sum equal to a given number

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    if root is None:
        return False

    subSum = sum - root.data

    if subSum == 0 and root.left is None and root.right is None:
        return True

    left = hasPathSum(root.left, subSum) if root.left else False
    right = hasPathSum(root.right, subSum) if root.right else False

    return left or right


if __name__ == "__main__":
    sum = 21

    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    print(hasPathSum(root, sum))
