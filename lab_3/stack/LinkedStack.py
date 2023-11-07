class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack(Stack):
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.size = 0

    def push(self, item):
        if not self.is_full():
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node
            self.size += 1
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            self.size -= 1
            return popped_item

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size == self.capacity

    def size(self):
        return self.size
