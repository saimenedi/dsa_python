class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def count_nodes(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    print("Count of nodes is", count_nodes(head))
