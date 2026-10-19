class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at a specific position (0-based)
    def insert(self, pos, data):
        new_node = Node(data)

        if pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


    # Print the list
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def count_occurrence(self, key):
        if self.head is None:
            print("List is empty")
            return

        count = 0
        temp = self.head

    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return

        first = self.head
        last = self.head

        while last.next:
            last = last.next

        # Swap data
        first.data, last.data = last.data, first.data

# Main program
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

print("Original list:")
dll.print_list()

dll.insert(1, 15)

print("After insertion:")
dll.print_list()

print("Display backword:")
dll.display_backward()