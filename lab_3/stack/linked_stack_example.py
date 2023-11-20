from LinkedStack import LinkedStack

if __name__ == "__main__":
    # Create a LinkedStack with a capacity of 3
    my_linked_stack = LinkedStack(3)

    # Push some elements
    my_linked_stack.push("apple")
    my_linked_stack.push("banana")
    my_linked_stack.push("cherry")

    # Display the top element
    print("Top element:", my_linked_stack.peek())

    # Pop elements
    print("Popped element:", my_linked_stack.pop())
    print("Popped element:", my_linked_stack.pop())

    # Check if the stack is empty
    print("Is the stack empty?", my_linked_stack.is_empty())

    # Display the size of the stack
    print("Size of the stack:", my_linked_stack.get_size())
