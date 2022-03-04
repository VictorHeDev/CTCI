'''
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure (such as an array). The stack supports the
following operations: push, pop, peek, and isEmpty.
'''

'''
APPROACH
There are several ways we can approach this problem. If we are able to use unlimited stacks, we could implement a quicksort or merge sort solution. If we are only allowed to use two stacks in total, then we will simply hold the minimum item in a tmp variable, pop off stack2 and insert into stack1 and repeat until we can properly move the minimum item into the stack2
'''


class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def push(self, item):
        if self.is_empty() or item < self.peek():
            super().push(item)
        else:
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())
            super().push(item)
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())
