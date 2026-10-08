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
    def del_node(self,value):
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            return
        while(temp):
            if temp.data == value:
                break
            else:
                prev = temptemp = temp.next
        if temp == None:
            print("value is not there in the list")
            return
        prev.next = temp.next
        temp = None 
    def reverse(self):
        curr = self.head
        prev = None
        while(curr):
            nextnode = curr.next
            curr.next=prev
            prev = curr
            curr = nextnode
        self.head =  prev
    # def insert(self, new_node,pos):
    #     temp=self.head
        # if pos == 1:#inserting at first position.
        #     new_node.next = self.head
        #     self.head = new_node
        # else:
        #     p = 1
        #     while(p!=pos-1 and temp.next!=None):
        #         temp=temp.next
        #         p+=1
        #     new_node.next=temp.next
        #     temp.next=new_node
    #     #     return
    # def del_node(self,value):
    #     temp=self.head = self.head.next
    #     return
    def print(self):
        print("list elements: ")
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next
list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))
list.print()
# list.del_node(60)
list.reverse()
list.print()
# list.insert(Node(100),1)
# list.print()

# list.insert(Node(66),7)
# list.print()



        