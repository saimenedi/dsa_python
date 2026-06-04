class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def searchKey(head, key):

    if head is None:
        return False

    if head.data == key:
        return True

    return searchKey(head.next, key)


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    key = 5

    if searchKey(head, key):
        print("true")

    else:
        print("false")
