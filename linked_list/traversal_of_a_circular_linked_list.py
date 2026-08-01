class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def printList(head):

    if head is None:
        return

    curr = head

    while True:
        print(curr.data, end=" ")
        curr = curr.next

        if curr == head:
            print()
            break

if __name__ == '__main__':
    head = Node(11)
    head.next = Node(2)
    head.next.next = Node(56)
    head.next.next.next = Node(12)

    head.next.next.next.next = head

    printList(head)