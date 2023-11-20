from ListQueue import ListQueue

if __name__ == "__main__":
    # Create a ListQueue
    my_list_queue = ListQueue()

    # Enqueue some elements
    my_list_queue.enqueue("apple")
    my_list_queue.enqueue("banana")
    my_list_queue.enqueue("cherry")

    # Display the front element
    print("Front element:", my_list_queue.peek())

    # Dequeue elements
    print("Dequeued element:", my_list_queue.dequeue())
    print("Dequeued element:", my_list_queue.dequeue())

    # Check if the queue is empty
    print("Is the queue empty?", my_list_queue.is_empty())

    # Display the size of the queue
    print("Size of the queue:", my_list_queue.get_size())
