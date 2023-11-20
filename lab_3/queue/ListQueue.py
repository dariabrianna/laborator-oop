from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
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


class ListQueue(Queue):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if len(self.items) < 5:
            self.items.append(item)
        else:
            print("Queue is full. Cannot enqueue item:", item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == 5

    def get_size(self):
        return len(self.items)
