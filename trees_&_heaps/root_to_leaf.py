class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def collectPaths(node, path, paths):
    if node is None:
        return

    path.append(node.data)

    if node.left is None and node.right is None:
        paths.append(list(path))
    else:
        collectPaths(node.left, path, paths)
        collectPaths(node.right, path, paths)

    path.pop()


def Paths(root):
    paths = []
    path = []
    collectPaths(root, path, paths)
    return paths


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    res = Paths(root)

    for row in res:
        for val in row:
            print(val, end=" ")
        print()
