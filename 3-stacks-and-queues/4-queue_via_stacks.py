'''
Implement a MyQueue class which implements a queue using two stacks.

APPROACH
- we need to modify peek() and pop() to go in reverse order
- perform the operation and then push everything back to 2nd stack
- we can implement a "lazy" approach where we let the elements in s2 sit until we MUST reverse the elements
'''


class MyQueue:
    def __init__(self) -> None:
        self.new_stack = Stack()
        self.old_stack = Stack()

    def _shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    def add(self, value):
        return self.new_stack.push(value)

    def peek(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.peek()

    def remove(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.pop()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.new_stack) + len(self.old_stack)
