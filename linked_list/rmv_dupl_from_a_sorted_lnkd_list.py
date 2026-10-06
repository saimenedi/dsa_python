class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

def removeDuplicates(head):
  st = set()

  temp = head
  new_head = None
  tail = None

  while temp:
    if temp.data not in st:
      new_node = Node(temp.data)

      if new_head is None:
        new_head = new_node
        tail = new_head
      else:
        tail.next = new_node
        tail = new_node
      st.add(temp.data)

    temp = temp.next
  return new_head

def printList(node):
  while node:
    print(node.data, end=' ')
    node = node.next
  print()

if __name__ == "__main__":
  head = Node(11)
  head.next = Node(11)
  head.next.next = Node(11)
  head.next.next.next = Node(13)
  head.next.next.next.next = Node(13)
  head.next.next.next.next.next = Node(20)

  printList(head)

  head = removeDuplicates(head)

  printList(head)