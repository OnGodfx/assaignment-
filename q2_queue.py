# Q2. Queue implementation (enqueue, dequeue, is empty, is full, peek)


class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full, cannot add", item)
            return
        rear = (self.front + self.count) % self.size
        self.queue[rear] = item
        self.count += 1
        print(item, "added to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]


q = Queue(3)

print("Is empty:", q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print("Is full:", q.is_full())
print("Front element:", q.peek())
print("Removed:", q.dequeue())
print("Removed:", q.dequeue())
print("Front element:", q.peek())
print("Removed:", q.dequeue())
q.dequeue()
print("Is empty:", q.is_empty())
