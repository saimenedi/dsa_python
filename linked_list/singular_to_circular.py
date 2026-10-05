class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def circular(curr, head):
  if curr.next == None:
    curr.next = head
    return 

  circular(curr.next, head)

def printList(head):
  curr = head

  while True:
    print(curr.data, end=' ')
    curr = curr.next
    if curr == head:
      break

  print()


if __name__ == "__main__":
  head = Node(10)
  head.next = Node(12)
  head.next.next = Node(14)
  head.next.next.next = Node(16)

  circular(head, head)

  printList(head)