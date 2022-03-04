'''
Describe how you would use a single array to implement three stacks
'''


'''
SOLUTION 1: Fixed Division
- divide the array into 3 equal parts and allow the individual stack to grow in that limited space.
- for example, set num_stacks = 3, stack_size = 6
'''


class MultiStack:
    def __init__(self, stack_size, num_stacks):
        self.stack_size = stack_size
        self.num_stacks = num_stacks
        self.array = [0] * (stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    def push(self, value, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_full(stack_num):
            return f"Push failed: stack #{stack_num} is full"
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            return f"Cannot pop from empty stack #{stack_num}"
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        return value

    def peek(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            return f"Cannot peek at empty stack #{stack_num}"
        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def _assert_valid_stack_num(self, stack_num):
        if stack_num >= self.num_stacks:
            return f"Stack #{stack_num} does not exist"
