
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data


# Main program
s = Stack()
q = Queue()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Original Stack:")
s.display()

# Transfer stack elements to queue
while s.top is not None:
    q.enqueue(s.pop())

# Transfer queue elements back to stack
while q.front is not None:
    s.push(q.dequeue())

print("Reversed Stack:")
s.display()
