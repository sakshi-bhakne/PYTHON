class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete(self, value):
        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # def display(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data, end=" <-> ")
    #         temp = temp.next
    #     print("None")
    # def count_occurrence(self):
    #     count = 0
    #     temp = self.head

    # while temp:
    #     if temp.data == 10:
    #         count += 1
    #     temp = temp.next
    
    def swap_first_last(self):
       temp = node1 = self.head
       while(temp.next):
           temp = temp.next 

dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

dll.display()

dll.delete(20)

dll.display()