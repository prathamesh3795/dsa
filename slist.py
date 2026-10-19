
# Singly Linear Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append node)
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

        if temp is None:
            print("Linked List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert node at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        if self.head is None:
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # 5. Delete node by value
    def del_node(self, val):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        if temp.data == val:
            self.head = temp.next
            print("Node deleted:", val)
            return

        prev = None

        while temp and temp.data != val:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        print("Node deleted:", val)

    # 6. Reverse linked list
    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev
        print("Linked List reversed")

    # 7. Sum of every two consecutive node values
    def pair_sum(self):
        temp = self.head

        if temp is None or temp.next is None:
            print("At least two nodes are required")
            return

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next

    def findmid_del(self):
        temp=temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("Middle Node:",temp.data)
        prev.next=temp.next
        temp=None

    



# Main program

list = LinkedList()

# Create Linked List
n = int(input("Enter number of nodes: "))

for i in range(n):
    val = int(input("Enter node value: "))
    list.append(Node(val))

print("\n1. Traverse Linked List")
list.print()

# Insert node
pos = int(input("\nEnter position to insert: "))
val = int(input("Enter value to insert: "))
list.insert(Node(val), pos)
list.print()

# Find middle node
list.middle()

# Delete node
val = int(input("\nEnter value to delete: "))
list.del_node(val)
list.print()

# Reverse list
list.reverse()
list.print()

# Sum of consecutive nodes
print("\nSum of consecutive nodes:")
list.pair_sum()