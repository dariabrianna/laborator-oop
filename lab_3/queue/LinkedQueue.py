from abc import ABC, abstractmethod

# Abstract Queue Interface
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


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue(AbstractQueue):
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = LinkedNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
            return removed_item
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count


# if __name__ == "__main__":
#     my_queue = LinkedQueue()

#     # Enqueue some elements
#     my_queue.enqueue("apple")
#     my_queue.enqueue("banana")
#     my_queue.enqueue("cherry")

#     # Display the front element
#     print("Front element:", my_queue.peek())

#     # Dequeue elements
#     print("Dequeued element:", my_queue.dequeue())
#     print("Dequeued element:", my_queue.dequeue())

#     # Check if the queue is empty
#     print("Is the queue empty?", my_queue.is_empty())

#     # Display the size of the queue
#     print("Size of the queue:", my_queue.size())
#     pass
