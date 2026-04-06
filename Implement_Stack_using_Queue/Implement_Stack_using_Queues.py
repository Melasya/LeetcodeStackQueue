class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self):
        value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        return value

    def peek(self):
        return self.front_node.value

    def is_empty(self):
        return self.front_node is None


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
