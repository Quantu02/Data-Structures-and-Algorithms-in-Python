class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Example usage:
tree = BST()
root = None
root = tree.insert(root, 50)
tree.insert(root, 30)
tree.insert(root, 70)
tree.insert(root, 20)
tree.insert(root, 40)
tree.insert(root, 60)
tree.insert(root, 80)

print("Inorder Traversal:")
tree.inorder(root)
print("\nPreorder Traversal:")
tree.preorder(root)
print("\nPostorder Traversal:")
tree.postorder(root)

# Search
found = tree.search(root, 40)
print("\n\nFound" if found else "Not Found")

# Delete
root = tree.delete(root, 20)
print("\nAfter deletion (Inorder):")
tree.inorder(root)
