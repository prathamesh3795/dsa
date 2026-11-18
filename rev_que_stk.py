
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

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Main program
q = Queue()
s = Stack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print("Original Queue:")
q.display()

# Transfer queue elements to stack
while q.front is not None:
    s.push(q.dequeue())

# Transfer stack elements back to queue
while s.top is not None:
    q.enqueue(s.pop())

print("Reversed Queue:")
q.display()
