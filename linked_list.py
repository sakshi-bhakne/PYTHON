#singly linear linked list 
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node ):
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node 
    def insert(self, new_node,pos):
        temp=self.head
        if pos == 1:#inserting at first position.
            temp = self.head
            while(temp.next!=self.head):#find last node
                temp=temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next=self.head
        else:
            p = 1
            while(p!=pos-1 and temp.next!=None):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            return
    def print(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next
    def delete(self,value):
        temp = None
        prev = None
        if temp.data==value:
            while(temp.next!=self.head):
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
        else:
            while(temp.data!=value and temp):
                prev=temp
                temp=temp.next
                if temp==None:
                   self.head
                   print("value is not present in the list")
                   return
                prev.next=temp.next
                temp = None
    def print(self):
        print()
        print("list elements: ")
        temp = self.head
        while(True):
            print(temp.data,end="")
            temp=temp.next
list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))
# list.insert(Node(100),1)
list.insert(Node(38),7)
list.print()
# list.insert(Node(66),7)
list.print()



        