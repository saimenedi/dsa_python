class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def getMiddle(head):

    slowptr = head
    fastptr = head

    while fastptr is not None and fastptr.next is not None:
        fastptr = fastptr.next.next
        slowptr = slowptr.next

    return slowptr.data


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(getMiddle(head))
