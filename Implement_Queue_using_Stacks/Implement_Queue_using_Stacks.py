class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        value = self.top_node.value
        self.top_node = self.top_node.next
        return value

    def peek(self):
        return self.top_node.value

    def is_empty(self):
        return self.top_node is None


class MyQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def pop(self) -> int:
        while self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        while self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def empty(self) -> bool:
        return self.in_stack.is_empty() and self.out_stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty
