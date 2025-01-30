class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node
    def __str__(self):
        """Return a string representation of the node."""
        return f"Node(data={self.data})"

class DoublyLinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head is self.tail:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.tail = new_node.next
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1


    def dequeue(self):
        if self.tail is None:
            return None

        data = self.tail.data
        if self.tail is self.head:
            self.tail = None
            self.head = None
            self.size -= 1
            return data

        prev = self.tail.prev
        prev.next = None
        self.tail = prev
        self.size -= 1
        return data

    def is_empty(self):
        return self.head is None

    def __str__(self):
        """Returns a string representation of the queue."""
        if self.is_empty():
            return "[]"

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next  # Move to the next node from head to tail

        return "[" + ", ".join(elements) + "]"


queue = DoublyLinkedListQueue()

queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue)
print(f'head {queue.head}')
print(f'tail {queue.tail}')

print(queue.dequeue())

print(queue)
print(f'head {queue.head}')
print(f'tail {queue.tail}')

print(f'dequeue {queue.dequeue()}')
print(f'dequeue {queue.dequeue()}')
print(f'dequeue {queue.dequeue()}')


print(queue)
print(f'head {queue.head}')
print(f'tail {queue.tail}')
queue.enqueue(10)

print(queue)
print(f'head {queue.head}')
print(f'tail {queue.tail}')