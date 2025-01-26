class ListQueue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            data = self.queue[0]
            self.queue = self.queue[1:len(self.queue)]
            self.size -= 1
            return data
        else:
            return None

    def __str__(self):
        return str(self.queue)


queue = ListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue)
print(queue.dequeue())
print(queue)
queue.enqueue(4)
print(
    queue
)
queue.enqueue(5)
print(
    queue
)

