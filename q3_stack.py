# Q3. Stack implementation (push, pop, is empty, is full, size, peek)


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def size(self):
        return len(self.stack)

    def push(self, item):
        if self.is_full():
            print("Stack is full, cannot push", item)
            return
        self.stack.append(item)
        print(item, "pushed")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]


s = Stack(3)

print("Is empty:", s.is_empty())
s.push(5)
s.push(15)
s.push(25)
s.push(35)
print("Is full:", s.is_full())
print("Size:", s.size())
print("Top element:", s.peek())
print("Popped:", s.pop())
print("Size:", s.size())
print("Popped:", s.pop())
print("Popped:", s.pop())
s.pop()
print("Is empty:", s.is_empty())
