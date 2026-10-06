class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

def removeDuplicates(head):
  if not head:
    return None

  seen = set()
  curr = head
  prev = None

  while curr is not None:

    if curr.data in seen:
      prev.next = curr.next
      curr = prev.next
    else:
      seen.add(curr.data)
      prev = curr
    curr = prev.next if prev else None
  return head

def printList(head):
  while head is not None:
    print(head.data, end='')
    if head.next is not None:
      print(' -> ', end='')
    head = head.next
  print()

if __name__ == "__main__":
  head = Node(5)
  head.next = Node(2)
  head.next.next = Node(2)
  head.next.next.next = Node(4) 

  head = removeDuplicates(head)
  printList(head)