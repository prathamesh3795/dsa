
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def create(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Traverse linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Head)")

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Delete a node
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        while True:
            if temp.data == data:
                if prev is None:
                    if temp.next == self.head:
                        self.head = None
                    else:
                        last = self.head
                        while last.next != self.head:
                            last = last.next

                        self.head = self.head.next
                        last.next = self.head
                else:
                    prev.next = temp.next

                print("Node deleted")
                return

            prev = temp
            temp = temp.next

            if temp == self.head:
                break

        print("Node not found")

    # Search a node
    def search(self, data):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            if temp.data == data:
                print("Node found")
                return

            temp = temp.next
            if temp == self.head:
                break

        print("Node not found")


# Main program
cll = CircularLinkedList()

cll.create(10)
cll.create(20)
cll.create(30)

print("Circular Linked List:")
cll.display()

cll.insert_beginning(5)
print("After insertion:")
cll.display()

cll.delete(20)
print("After deletion:")
cll.display()

cll.search(30)
