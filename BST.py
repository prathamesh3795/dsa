
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


# Main program
b = BST()

b.root = b.insert(b.root, 50)
b.root = b.insert(b.root, 30)
b.root = b.insert(b.root, 70)
b.root = b.insert(b.root, 20)
b.root = b.insert(b.root, 40)
b.root = b.insert(b.root, 60)
b.root = b.insert(b.root, 80)

print("Inorder Traversal:")
b.inorder(b.root)

key = 40

if b.search(b.root, key):
    print("\nElement Found")
else:
    print("\nElement Not Found")
