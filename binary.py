
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DSA:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right

    # Inorder: Left, Root, Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder: Root, Left, Right
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder: Left, Right, Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


d = DSA()

d.insert(50)
d.insert(30)
d.insert(70)
d.insert(20)
d.insert(40)
d.insert(60)
d.insert(80)

print("Inorder Traversal:")
d.inorder(d.root)

print("\nPreorder Traversal:")
d.preorder(d.root)

print("\nPostorder Traversal:")
d.postorder(d.root)
