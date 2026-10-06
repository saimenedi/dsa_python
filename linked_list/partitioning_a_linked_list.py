class Node:
  def __init__(self, val):
    self.data = val
    self.next = None

def partition(head, x):
  lessHead = Node(0)

  equalHead = Node(0)

  greaterHead = Node(0)

  less = lessHead
  equal = equalHead
  greater = greaterHead

  curr = head

  while curr is not None:
    if curr.data < x:
      less.next = curr
      less = less.next
    elif curr.data == x:
      equal.next = curr
      equal = equal.next
    else:
      greater.next = curr
      greater = greater.next
    curr = curr.next

  greater.next = None

  equal.next = greaterHead.next

  less.next = equalHead.next

  newHead = lessHead.next

  return newHead

def printList(head):
  curr = head
  while curr is not None:
    print(curr.data, end=' ')
    curr = curr.next

  print()

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(4)
  head.next.next = Node(3)
  head.next.next.next = Node(2)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(2)

  x = 3
  head = partition(head, x)
  printList(head)