class node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node


    #Traverse and print the value

    def traverse(self):
        if not self.head:
            print("Empty List")
            return
        cur=self.head
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.next

        print("None")


    # Insert by specific position    

    def insert(self,prev,new):
        temp=self.head
        while temp:
            if temp.data == prev:
                break
            temp=temp.next

        if temp==None:
            print(f"Node with data{prev}Not found")
            return
        new_node=node(new)
        new_node.next=temp.next
        temp.next=new_node

    # Delete Negative Node

    def delete(self):
        cur=self.head
        while cur and cur.next:
            if cur.next.data<0:
                cur.next=cur.next.next
            else:
                cur=cur.next    

l1=linkedList()
l1.append(10)
l1.append(11)
l1.append(20)
l1.append(-10)

l1.traverse()

l1.insert(11,50)
print("After Insert New Node")
l1.traverse()

l1.delete()
print("After Delete Negative Node")
l1.traverse()