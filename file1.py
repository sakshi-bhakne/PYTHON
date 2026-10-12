
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 2. Display all nodes
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Find the length
    def length(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    # 4. Search for a value
    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next

        return False

    # 5. Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 6. Insert at a position (positions start at 0)
    def insert_at(self, position, data):
        if position < 0 or position > self.length():
            print("Invalid position")
            return

        if position == 0:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(position - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # 7. Delete the first matching value
    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    # 8. Reverse the list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 9. Find the middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if slow is not None:
            return slow.data
        return None


# Main program
ll = SinglyLinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.display()
print("Length:", ll.length())
print("Search 20:", ll.search(20))

ll.insert_beginning(5)
ll.display()

ll.insert_at(2, 15)
ll.display()

ll.delete(20)
ll.display()

print("Middle:", ll.middle())

ll.reverse()
ll.display()
