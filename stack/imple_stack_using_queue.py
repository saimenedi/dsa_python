class myQueue:
  def __init__(self):
    self.s1 = []
    self.s2 = []

  def enqueue(self, x):
    while self.s1:
      self.s2.append(self.s1.pop())

    self.s1.append(x)

    while self.s2:
      self.s1.append(self.s2.pop())


  def dequeue(self):
    if not self.s1:
      return 
    self.s1.pop()

  def front(self):
    if not self.s1:
      return -1
    return self.s1[-1]

  def size(self):
    return len(self.s1)

if __name__ == "__main__":
  q = myQueue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  
  print("Front:", q.front())  
  print("Size:", q.size())    
  
  q.dequeue()        
  print("Front:", q.front())  
  print("Size:", q.size()) 