class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)



class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data=data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1


    def pop(self):
        if self.top is None:
            return None
        top = self.top
        data = top.data
        self.size -= 1
        if top.next is None:
            self.top = None
            return data
        else:
            self.top = top.next
            return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.size == 0


    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(str(current))
            current = current.next
        return str(result)



# Create a stack and add data
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Stack after pushes:")
print(stack)  # Output: 40 <- 30 <- 20 <- 10 <- Top

# Pop items from the stack
print("\nPop operations:")
print(f"Popped: {stack.pop()}")  # Output: 40
print(f"Popped: {stack.pop()}")  # Output: 30

print("\nStack after pops:")
print(stack)  # Output: 20 <- 10 <- Top

# Push another item
stack.push(50)
print("\nStack after another push:")
print(stack)  # Output: 50 <- 20 <- 10 <- Top

# Peek the top of the stack
print(f"\nTop item: {stack.peek()}")  # Output: 50

# Check if the stack is empty
print(f"\nIs stack empty? {stack.is_empty()}")  # Output: False

# Get the size of the stack
print(f"Stack size: {stack.size}")  # Output: 3

