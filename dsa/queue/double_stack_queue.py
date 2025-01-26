class DoubleStackQueue:
    '''

    '''

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def push(self, x: int) -> None:
        self.inbound_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        if self.outbound_stack:
            return self.outbound_stack[-1]
        else:
            return self.inbound_stack[0]

    def empty(self) -> bool:
        return not self.inbound_stack and not self.outbound_stack

    def __str__(self):
        """Return a string representation of the queue."""

        if not self.inbound_stack and not self.outbound_stack:
            return "[]"  # Empty queue

        # Logic to handle display when elements are in stack2 but not stack1
        if not self.inbound_stack and self.outbound_stack:
            elements = [str(x) for x in reversed(self.outbound_stack)]
            return "[" + ", ".join(elements) + "]"

        elements = [str(x) for x in self.inbound_stack]  # normal case
        return "[" + ", ".join(elements) + "]"


queue = DoubleStackQueue()

queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

print(queue)
queue.pop()
queue.pop()
queue.pop()
print(f'stack1 {queue.inbound_stack}')
print(f'stack2 {queue.outbound_stack}')
print(f'queue: ${queue}')
queue.push(2)
queue.push(4)
print(f'queue: ${queue}')
print(f'peek: {queue.peek()}')

queue.pop()
queue.pop()
queue.pop()
queue.pop()
print(f'queue: ${queue}')
print(f'peek: {queue.peek()}')
