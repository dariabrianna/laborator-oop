from abc import ABC, abstractmethod
from collections import deque


class AbstractQueue(ABC):
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
    def size(self):
        pass


class SimpleListQueue(AbstractQueue):
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class DoubleStackQueue(AbstractQueue):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.is_empty():
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)


simple_list_queue = SimpleListQueue()

simple_list_queue.enqueue("apple")
simple_list_queue.enqueue("banana")
simple_list_queue.enqueue("cherry")

print("Is the SimpleListQueue empty?", simple_list_queue.is_empty())  # False
print("Front element of SimpleListQueue:", simple_list_queue.peek())  # "apple"

print("Dequeued element from SimpleListQueue:", simple_list_queue.dequeue())  # "apple"
print("Dequeued element from SimpleListQueue:", simple_list_queue.dequeue())  # "banana"
print("Dequeued element from SimpleListQueue:", simple_list_queue.dequeue())  # "cherry"

print("Is the SimpleListQueue empty?", simple_list_queue.is_empty())  # True


double_stack_queue = DoubleStackQueue()

double_stack_queue.enqueue("apple")
double_stack_queue.enqueue("banana")
double_stack_queue.enqueue("cherry")

print("Is the DoubleStackQueue empty?", double_stack_queue.is_empty())  # False
print("Front element of DoubleStackQueue:", double_stack_queue.peek())  # "apple"

print("Dequeued element from DoubleStackQueue:", double_stack_queue.dequeue())  # "apple"
print("Dequeued element from DoubleStackQueue:", double_stack_queue.dequeue())  # "banana"
print("Dequeued element from DoubleStackQueue:", double_stack_queue.dequeue())  # "cherry"

print("Is the DoubleStackQueue empty?", double_stack_queue.is_empty())  # True
