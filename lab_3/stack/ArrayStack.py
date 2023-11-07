class ArrayStack(Stack):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top < self.capacity - 1:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if not self.is_empty():
            popped_item = self.items[self.top]
            self.top -= 1
            return popped_item

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1
