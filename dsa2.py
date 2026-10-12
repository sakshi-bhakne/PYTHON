class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # 2. Traverse and print node values
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # 3. Insert node at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node and print its value
    def middle(self):
        a = self.head
        b = self.head

        while b and b.next:
            a = a.next
            b = b.next.next

        if a:
            print("Middle node:", a.data)

    # 5. Delete node
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

    # 6. Reverse list
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
#find mid node
    # def reverse(self):
    #         self.head = prev
    def findmid_del(self):
            temp = temp1=self.head
            prev = None
            while temp1 and temp1.next:
                prev = temp
                temp = temp.next
                temp1=temp1.next.next
            print("middle node: ",temp.data)
            prev.next = temp.next
            temp = None
# 8. Print first and last node
def first_last(self):
    if self.head is None:
        print("Linked List is empty")
        return

    # First node
    print("First node:", self.head.data)

    # Find last node
    temp = self.head
    while temp.next:
        temp = temp.next

    print("Last node:", temp.data)
#del first and last node:
def delete_first(self):
    if self.head is None:
        print("Linked List is empty")
        return

    self.head = self.head.next
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
#delete alternate nodes:


def delete_alternate(self):
    prev  = self.head
    temp = self.head.next

    while prev and temp:
        prev.next = temp.next
        temp = None
        prev = prev.next
    if prev:
        temp=prev.next
# def print(self):
#     print(self)
#     print("list elements : ")


def concatenate(self):
    
   


mylist = LinkedList()

mylist.append(Node(10))
mylist.append(Node(20))
mylist.append(Node(30))
mylist.append(Node(40))
mylist.append(Node(50))

# First list: mylist
mylist = LinkedList()
mylist.append(Node(10))
mylist.append(Node(20))
mylist.append(Node(30))

# Second list: list2
list2 = LinkedList()
list2.append(Node(40))
list2.append(Node(50))
list2.append(Node(60))

# Concatenate list2 with mylist
mylist.concatenate(list2)

print("After concatenation:")
mylist.print()

print("Original List:")
mylist.print()

mylist.insert(Node(25), 3)
print("After Insertion:")
mylist.print()

mylist.middle()

mylist.del_node(25)
print("After Deletion:")
mylist.print()

mylist.reverse()
print("After Reversing:")
mylist.print()

print("Sum of Consecutive Nodes:")
mylist.pair_sum()

# mylist.delete_first()
# print("After deleting first node:")
# mylist.print()

# mylist.delete_last()
print("After deleting last node:")
mylist.print()

# mylist.delete_alternate()
print("After deleting alternate nodes:")
mylist.print()