class DoubleStackQueue:
    '''

    '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if self.stack2:
            self.stack2.append(x)
        else:
            for i in range(len(self.stack1) - 1, -1, -1):
                self.stack2.append(self.stack1[i])
            self.stack1 = []
            self.stack2.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if self.stack1:
            return self.stack1.pop()
        else:
            for i in range(len(self.stack2) - 1, -1, -1):
                self.stack1.append(self.stack2[i])
            self.stack2 = []
            return self.stack1.pop()


    def peek(self) -> int:
        if self.empty():
            return -1
        if self.stack1:
            return self.stack1[len(self.stack1) - 1]
        else:
            for i in range(len(self.stack2) - 1, -1, -1):
                self.stack1.append(self.stack2[i])
            self.stack2 = []
            return self.stack1[len(self.stack1) - 1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


    def __str__(self):
        """Return a string representation of the queue."""

        if not self.stack1 and not self.stack2:
            return "[]"  # Empty queue

        # Logic to handle display when elements are in stack2 but not stack1
        if not self.stack1 and self.stack2:
            elements = [str(x) for x in reversed(self.stack2)]
            return "[" + ", ".join(elements) + "]"

        elements = [str(x) for x in self.stack1]  # normal case
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
print(f'stack1 {queue.stack1}')
print(f'stack2 {queue.stack2}')
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



