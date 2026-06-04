class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def insertAtEnd(head, x)
  newNode = Node(x)

   if head is None:
        return newNode

    last = head

    while last.next is not None:
        last = head.next

    last.next = newNode

    return head


def printList(node):
    while node is not None:
        print(node.data, end="")
        if node.next is not None:
            print('->', end="")
        node = node.next
        print()


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = insertAtEnd(head, 6)

    printList(head)
