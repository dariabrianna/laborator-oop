from ListStack import ListStack

if __name__ == "__main__":
    # Create a ListStack
    my_list_stack = ListStack()

    # Push some elements
    my_list_stack.push("apple")
    my_list_stack.push("banana")
    my_list_stack.push("cherry")

    # Display the top element
    print("Top element:", my_list_stack.peek())

    # Pop elements
    print("Popped element:", my_list_stack.pop())
    print("Popped element:", my_list_stack.pop())

    # Check if the stack is empty
    print("Is the stack empty?", my_list_stack.is_empty())

    # Display the size of the stack
    print("Size of the stack:", my_list_stack.get_size())
