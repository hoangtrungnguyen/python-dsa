class Node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def delete(self, data):
        """
        1. find node
            if find None return empty
        2. found node:
            2.1 if found node is head:
                new_head = node.next
                new_head.prev = None
            2.2 at the middle
                current.prev.next = current.next
                current.next.prev = current.prev
            2.3 at the tail
                current.prev.next = None
                tail = current.prev
        :param data:
        :return:
        """
        current = self.head
        prev = None
        found = None
        while current:
            if current.data == data:
                found = current
                prev = current.prev
                break
            current = current.next

        if found is None:
            return

        if found == self.head:
            new_head = found.next
            if new_head:
                new_head.prev = None
                self.head = new_head
            else:
                self.head = None
                self.tail = None
        elif found == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = found.next
            found.next.prev = prev


    def __str__(self):
        """Returns a string representation of the list showing pointers."""
        result = []
        current = self.head
        while current:
            prev_data = current.prev.data if current.prev else "None"
            next_data = current.next.data if current.next else "None"
            result.append(f"[Prev: {prev_data}, Data: {current.data}, Next: {next_data}]\n")
            current = current.next
        if result is None or len(result) == 0:
            return "The list is empty."
        return " <-> ".join(result)  # Visualize the list as a linked chain




# Create and populate the DoublyLinkedList
dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.append("D")

dll.delete("D")
dll.delete("A")
dll.delete("B")
# dll.delete("C")

# Print the DoublyLinkedList
print(dll)