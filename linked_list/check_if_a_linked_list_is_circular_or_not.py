class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_circular(head):
    if not head:
        return True

    slow = head
    fast = head.next
    while slow and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("Yes" if is_circular(head) else 'No')

    head.next.next.next.next = head

    print("Yes" if is_circular(head) else "No")