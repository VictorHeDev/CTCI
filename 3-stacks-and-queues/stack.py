class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)
