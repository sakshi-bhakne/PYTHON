# class node:
#     def __init__(self, data):
#        self.data = data 
#        self.next = None
# n1 = node(10)
# n2 = node(20)
# n3 = node(30)
# print(n1.data)
# print(n1.next)

# n1.next = n2
# n2.next = n3
# head = n1

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedlist:
    def __init__(self):
        self.head = None
    def insert_end(self,data):
        new_node = node(data)
        if self.head is None:
           self.head = new_node
           return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            temp.next = new_node

