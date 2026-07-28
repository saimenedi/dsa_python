# Add Two Numbers represented as Linked List using Recursion
import sys

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def reverse(head):
    prev = None
    curr = head
    next = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def trimLeadingZeroes(head):
    while head and head.data == 0:
        head = head.next
    return head

def addListRec(num1, num2, carry):
    if num1 is None and num2 is None and carry[0] == 0:
        return None

    sum = carry[0]

    if num1 is not None:
        sum += num1.data
        num1 = num1.next

    if num2 is not None:
        sum += num2.data
        num2 = num2.next

    carry[0] = sum // 10
    result = Node(sum % 10)

    result.next = addListRec(num1, num2, carry)

    return result


def addTwoLists(num1, num2):
    num1 = trimLeadingZeroes(num1)
    num2 = trimLeadingZeroes(num2)

    num1 = reverse(num1)
    num2 = reverse(num2)

    carry = [0]
    result = addListRec(num1, num2, carry)

    if carry[0] != 0:
        newNode = Node(carry[0])
        newNode.next = result
        result = newNode

    return reverse(result)

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
    print()


if __name__ == "__main__":

    num1 = Node(1)
    num1.next = Node(2)
    num1.next.next = Node(3)

    num2 = Node(9)
    num2.next = Node(9)
    num2.next.next = Node(9)

    sumList = addTwoLists(num1, num2)
    printList(sumList)