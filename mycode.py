
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List: Insert at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print node values
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert node at a specific position (1-based)
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        a = self.head
        b = self.head

        while b and b.next:
            a = a.next
            b = b.next.next

        if a:
            print("Middle node:", a.data)
        else:
            print("Linked List is empty")

    # 5. Delete a node by value
    def del_node(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None

        while temp:
            if temp.data == value:
                prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Value not found")

    # 6. Reverse the linked list
    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    # 7. Sum of every two consecutive node values
    def pair_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next

    # 8. Find and delete the middle node
    def findmid_del(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = fast = self.head
        prev = None

        while fast and fast.next:
            prev = temp
            temp = temp.next
            fast = fast.next.next

        print("Middle node deleted:", temp.data)

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

    # 9. Print first and last nodes
    def first_last(self):
        if self.head is None:
            print("Linked List is empty")
            return

        print("First node:", self.head.data)

        temp = self.head
        while temp.next:
            temp = temp.next

        print("Last node:", temp.data)

    # 10. Delete first node
    def delete_first(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # 11. Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # 12. Delete alternate nodes
    # Keeps positions 1, 3, 5, ...
    def delete_alternate(self):
        temp = self.head

        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next

    # 13. Concatenate two linked lists
    def concatenate(self, list2):
        if list2.head is None:
            return

        if self.head is None:
            self.head = list2.head
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = list2.head


# =====================================
# MAIN PROGRAM
# =====================================

# First linked list: mylist
mylist = LinkedList()

mylist.append(Node(10))
mylist.append(Node(20))
mylist.append(Node(30))
mylist.append(Node(40))
mylist.append(Node(50))

print("Original List:")
mylist.print()

# Insert at position 3
mylist.insert(Node(25), 3)
print("\nAfter Insertion:")
mylist.print()

# Find middle node
mylist.middle()

# Delete node with value 25
mylist.del_node(25)
print("\nAfter Deleting 25:")
mylist.print()

# Reverse list
mylist.reverse()
print("\nAfter Reversing:")
mylist.print()

# Sum of consecutive node pairs
print("\nSum of Consecutive Nodes:")
mylist.pair_sum()

# Print first and last nodes
print("\nFirst and Last Nodes:")
mylist.first_last()

# Delete first node
mylist.delete_first()
print("\nAfter Deleting First Node:")
mylist.print()

# Delete last node
mylist.delete_last()
print("\nAfter Deleting Last Node:")
mylist.print()

# Delete alternate nodes
mylist.delete_alternate()
print("\nAfter Deleting Alternate Nodes:")
mylist.print()

# Find and delete middle node
mylist.findmid_del()
print("\nAfter Deleting Middle Node:")
mylist.print()

# Create second linked list
list2 = LinkedList()
list2.append(Node(60))
list2.append(Node(70))
list2.append(Node(80))

print("\nSecond Linked List:")
list2.print()

# Concatenate second list with mylist
mylist.concatenate(list2)

print("\nAfter Concatenating Both Lists:")
mylist.print()
