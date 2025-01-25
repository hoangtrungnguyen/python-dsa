
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data= data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.tail = current.next
                self.size -= 1
            prev = current
            current = current.next

    def search(self, data):
        current = self.tail
        while current:
            if current.data == data:
                return True
        return False

    def clear(self):
        """Clear all nodes from the list."""
        self.tail = None
        self.head = None
        self.size = 0
