# Flatten a multilevel linked list using level order traversal
class Node:
    def __init__(self, new_value):
        self.data = new_value
        self.next = None
        self.child = None

def flatten_list(head):

    if head is None:
        return

    tail = head
    while tail.next is not None:
        tail = tail.next

    curr = head
    while curr != None:

        if curr.child is not None:
            tail.next = curr.child

            tmp = curr.child

            while tmp.next is not None:
                tmp = tmp.next
            tail = tmp

            curr.child = None
        curr = curr.next

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    head.child = Node(4)
    head.child.next = Node(5)
    head.next.next.child = Node(6)
    head.child.child = Node(7)

    flatten_list(head)
    print_list(head)