from LinkedQueue import LinkedQueue

if __name__ == "__main__":
    # Create an ArrayQueue with a capacity of 3
    my_array_queue = LinkedQueue()

    # Enqueue some elements
    my_array_queue.enqueue("apple")
    my_array_queue.enqueue("banana")
    my_array_queue.enqueue("cherry")

    # Display the front element
    print("Front element:", my_array_queue.peek()) # Apple

    # Dequeue elements
    print("Dequeued element:", my_array_queue.dequeue())
    print("Front element:", my_array_queue.peek()) # banana


    print("Dequeued element:", my_array_queue.dequeue())

    # Check if the queue is empty
    print("Is the queue empty?", my_array_queue.is_empty()) # Not empty

    # Display the size of the queue
    # print("Size of the queue:", my_array_queue.get_size()) # Empty
