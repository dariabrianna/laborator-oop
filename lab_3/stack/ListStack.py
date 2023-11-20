from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


class ListStack(Stack):
    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) < 5:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == 5

    def get_size(self):
        return len(self.items)
