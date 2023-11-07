class ArrayStack(Stack):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.items[self.top] = item
        else:
            print("Stack is full. Cannot push item:", item)

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

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1
