
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


class BST:
    def __init__(self):
        self.root = None

    def level_order(self):
        if self.root is None:
            return

        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            current = q.dequeue()
            print(current.data, end=" ")

            if current.left:
                q.enqueue(current.left)

            if current.right:
                q.enqueue(current.right)


# Creating Tree
tree = BST()

tree.root = Node(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.left.left = Node(40)
tree.root.left.right = Node(50)
tree.root.right.left = Node(60)
tree.root.right.right = Node(70)

print("Level Order Traversal:")
tree.level_order()
