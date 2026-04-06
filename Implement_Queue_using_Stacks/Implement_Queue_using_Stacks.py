"""
Queue through stacks
"""
class Node:
    """
    Linked list node
    """
    def __init__(self, value):
        """initializes a node"""
        self.value = value
        self.next = None

class Stack:
    """
    Linked stack (LIFO)
    """
    def __init__(self):
        self.top_node = None

    def push(self, value):
        """
        Push a value on top of the stack
        """
        new_node = Node(value)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        """
        Remove and return the top value
        """
        value = self.top_node.value
        self.top_node = self.top_node.next
        return value

    def peek(self):
        """
        Return the top value
        """
        return self.top_node.value

    def is_empty(self):
        """
        Return True if the stack is empty
        """
        return self.top_node is None


class MyQueue:
    """FIFO queue using two stacks"""
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        """
        Add an element to the back of the queue
        """
        self.in_stack.push(x)

    def pop(self) -> int:
        """
        Remove and return the front element
        """
        while self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Return the front element
        """
        while self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def empty(self) -> bool:
        """
        Return True if the queue is empty
        """
        return self.in_stack.is_empty() and self.out_stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty
