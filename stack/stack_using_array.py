class myStack:

    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0] * self.capacity
        self.top = -1

    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        val = self.arr[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return -1
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1


if __name__ == "__main__":
    st = myStack(4)
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    print("Popped:", st.pop())

    print("Top element:", st.peek())

    print("Is stack empty: ", "Yes" if st.isEmpty() else "No")

    print("Is stackfull: ", "Yes" if st.isFull() else "No")
