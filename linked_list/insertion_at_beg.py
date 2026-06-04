class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def insertAtFront(head, x):
    newNode = Node(x)
    newNode.next = head
    return newNode


def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    x = 1
    head = insertAtFront(head, x)

    printList(head)
