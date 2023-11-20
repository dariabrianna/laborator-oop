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


class ArrayQueue(Queue):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
            self.size += 1
        else:
            print("Queue is full. Cannot enqueue item:", item)

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return removed_item

    def peek(self):
        if not self.is_empty():
            return self.items[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_size(self):
        return self.size
