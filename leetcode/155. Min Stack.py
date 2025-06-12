class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.stack_min = None


class MinStack:
    # each node saves a stack_min at the current time.
    # if the
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:
        new_node = Node(data=val)

        if self.head is None:
            new_node.stack_min = val
            self.head = new_node
            self.tail = new_node
        else:
            if val < self.head.stack_min:
                new_node.stack_min = val
            else:
                new_node.stack_min = self.head.stack_min
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self) -> None:
        if self.head is None:
            return None
        data = self.head.data

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return data
        else:
            self.head = self.head.next
            self.head.prev = None
            return data

    def top(self) -> int:
        if self.head is None:
            return None
        return self.head.data

    def getMin(self) -> int:
        if self.head is None:
            return None
        return self.head.stack_min

    def __str__(self):
        if self.head is None:
            return "MinStack[]"
        else:
            current = self.head
            elements = []
            while current:
                elements.append(str(current.data))
                current = current.next
            return f"MinStack[{', '.join(elements)}] (min={self.getMin()})"


#
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack)
# print(f'getMin(): {minStack.getMin()}'); # return -3
# minStack.pop()
# print(f'top: {minStack.top()}') #   // return 0
# print(f'getMin: {minStack.getMin()}') # return -2

# print(f'pop 2: {minStack.pop()}') # return 0
# print(f'getMin: {minStack.getMin()}') # return -2


# minStack2 = MinStack()
# minStack2.push(2147483646)
# minStack2.push(2147483646)
# minStack2.push(2147483647)
# print(f'minStack2: {minStack2}')
# print(f'top: {minStack2.top()}')
# print(f'getMin: {minStack2.getMin()}')
# print(f'minStack2.pop() {minStack2.pop()}')
# print(f'minStack2: {minStack2}')

#
commands = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
values = [[], [2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648], [],
          [], [], []]

minStack = None
results = []

for i in range(len(commands)):
    command = commands[i]
    value = values[i]

    if command == "MinStack":
        minStack = MinStack()
        results.append(None)
    elif command == "push":
        minStack.push(value[0])
        results.append(None)
    elif command == "pop":
        results.append(minStack.pop())
    elif command == "top":
        results.append(minStack.top())
    elif command == "getMin":
        results.append(minStack.getMin())

print(results)


# Optimized solution
class MinStack2:
    def __init__(self):
        self.stack = []  # Main stack to store values
        self.min_stack = []  # Auxiliary stack to store minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Only push to min_stack if it's empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:  # Check for empty stack
            return
        # If popped value is the current min, pop from min_stack as well
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
