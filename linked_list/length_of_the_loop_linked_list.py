class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

def lengthOfLoop(head):
  visited = set()
  current = head 
  count = 0

  while current is not None:
    if current in visited:
      startOfLoop = current
      while True:
        count += 1
        current = current.next
        if current == startOfLoop:
          break
      return count 

    visited.add(current)

    current = current.next

  return 0

if __name__ == "__main__":
  head = Node(25)
  head.next = Node(14)
  head.next.next = Node(19)
  head.next.next.next = Node(33)
  head.next.next.next.next = Node(10)
  
  head.next.next.next.next.next = head.next.next

  print(lengthOfLoop(head))