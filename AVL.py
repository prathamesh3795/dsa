
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    # Right Rotation
    def right_rotate(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

    # Left Rotation
    def left_rotate(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    # Insert Node
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and data < root.left.data:
            return self.right_rotate(root)

        # RR Case
        if b < -1 and data > root.right.data:
            return self.left_rotate(root)

        # LR Case
        if b > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if b < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Main Program
tree = AVL()
root = None

values = [10, 20, 30, 40, 50, 25]

for i in values:
    root = tree.insert(root, i)

print("Inorder Traversal:")
tree.inorder(root)

print("\nPreorder Traversal:")
tree.preorder(root)

print("\nPostorder Traversal:")
tree.postorder(root)
