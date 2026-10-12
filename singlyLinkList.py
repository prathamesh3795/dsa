# singly linear linked list
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next): #this means temp.next is not null 
                temp = temp.next  # traverse list until the value is null,if not go to the next node
            temp.next=new_node # append new node

    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1: # inserting at first position
            new_node.next = self.head
            self.head = new_node

        else:
            p = 1
            while(p!=pos-1):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node
    

    def print(self):
        # sum = 0 #sum of even/odd values
        temp = self.head
        # while temp: #checks if temp has some data 
        #     if temp.data>0:
        #         sum+= temp.data
        #     temp=temp.next
        # print(sum)
        while temp.next:
            print(temp.data)
            temp=temp.next
        if temp:
            print(temp.data)

#for delete last
    def del_node(self,val):
        temp=self.head
        if temp.data==val:
            self.head=self.head.next
            return
        while(temp):
            if temp.data==val:
                break
            else:
                prev=temp
                temp=temp.next
        if temp==None:
            print("Value is not there in the last")
            return
        prev.next=temp.next
        temp=None


    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev
        return prev
    

list =LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(50)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(40))
list.insert(Node(100),1)
list.print()
list.insert(Node(66),4)
list.print()
list.insert(Node(80),7)
list.del_node(1)
list.print()

# printing alternate node

# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def append(self,new_node):
#         if(self.head==None):
#            self.head=new_node
#         else:
#             temp=self.head
#             while(temp.next):
#                 temp=temp.next
#             temp.next=new_node #appending new node
#     def display(self):
#         temp=self.head
#         while temp.next:
#             print(temp.data)
#             temp=temp.next.next
#         if temp:
#             print(temp.data)
# l1=LinkedList()
# n1=Node(10)
# n2=Node(-20)       
# n3=Node(30)
# n4=Node(50)
# l1.append(n1)
# l1.append(n2)
# l1.append(n3)
# l1.append(n4)
# l1.append(Node(-40))
# l1.display()