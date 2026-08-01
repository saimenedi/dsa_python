class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count(head, key):
    curr = head
    count = 0
    while curr is not None:
        if curr.data == key:
            count += 1
        curr = curr.next
    return count

head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

key = 2
print(count(head, key))