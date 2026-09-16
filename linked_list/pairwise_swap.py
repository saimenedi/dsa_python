class Node:
  def __init__(self, val):
    self.data = val
    self.next = None


def pairwiseSwap(head):
  curr = head

  while curr is not None and curr.next is not None:
    curr.data, curr.next.data = curr.next.data, curr.data

    curr = curr.next.next
  return head

def printList(head):
  temp = head
  while temp is not None:
    print(temp.data, end="")
    if temp.next is not None:
      print(" -> ", end="")
    temp = temp.next
  print()

if __name__ == "__main__":
     # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    printList(head)

    pairwiseSwap(head)

    printList(head)