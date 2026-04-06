"""
LIFO stack implemented using two FIFO queues
"""
class Node:
    """
    Linked list node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
    Linked queue (FIFO)
    """
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, value):
        """
        Add an element to the back of the queue
        """
        new_node = Node(value)
        if self.is_empty():
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self):
        """
        Remove and return the front element
        """
        value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        return value

    def peek(self):
        """
        Return the front element
        """
        return self.front_node.value

    def is_empty(self):
        """
        Return True if the queue is empty
        """
        return self.front_node is None


class MyStack:
    """
    LIFO stack using two queues
    """
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Push an element on top of the stack
        """
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Remove and return the top element
        """
        return self.q1.dequeue()

    def top(self) -> int:
        """
        Return the top element
        """
        return self.q1.peek()

    def empty(self) -> bool:
        """
        Return True if the stack is empty
        """
        return self.q1.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
