class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def solution(values):
    # Q1. Create linked list
    head = None
    temp = None

    for val in values:
        new_node = Node(val)

        if head is None:
            head = new_node
            temp = new_node
        else:
            temp.next = new_node
            temp = new_node

    # Q2. Display linked list
    def display(head):
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    print("Original list:")
    display(head)

    # Q3. Insert a node at position 2
    new_node = Node(15)
    new_node.next = head.next
    head.next = new_node

    print("After insertion:")
    display(head)

    # Q4. Find middle node
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print("Middle node:", slow.data)

    # Q5. Delete node with value 30
    if head and head.data == 30:
        head = head.next
    else:
        temp = head
        while temp and temp.next:
            if temp.next.data == 30:
                temp.next = temp.next.next
                break
            temp = temp.next

    print("After deletion:")
    display(head)

    # Q6. Reverse linked list
    prev = None
    curr = head

    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode

    head = prev

    print("After reversing:")
    display(head)

    # Q7. Sum consecutive node values
    print("Consecutive pair sums:")
    temp = head

    while temp and temp.next:
        print(temp.data + temp.next.data, end=" ")
        temp = temp.next

    print()
    return head


# Run the solution
solution([10, 20, 30, 40, 50])