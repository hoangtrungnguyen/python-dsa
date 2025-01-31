class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self):
        pass

    def remove(self):
        pass

    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current
