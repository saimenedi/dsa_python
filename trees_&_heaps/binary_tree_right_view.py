class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def recRightView(root, level, maxLevel, result):
    if root is None:
        return

    if level > maxLevel[0]:
        result.append(root.data)
        maxLevel[0] = level

    recRightView(root.right, level+1, maxLevel, result)
    recRightView(root.left, level+1, maxLevel, result)


def rightView(root):
    result = []
    maxLevel = [-1]

    recRightView(root, 0, maxLevel, result)

    return result


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    result = rightView(root)

    for val in result:
        print(val, end=" ")
    print()
