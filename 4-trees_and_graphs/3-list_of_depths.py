'''
Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth. If you have a tree with depth D, you'll have D
linked lists.

APPROACH
- use bfs and keep track of the levels using a tuple
- create the linked list if the node being popped off is same level
'''


def list_of_depths(binary_tree):
    if not binary_tree:
        return []
    lists = []
    tail = None
    node = binary_tree
    queue = Queue()
    depth = -1
    node.depth = 0

    while node:
        if node.depth == depth:
            tail.next = ListNode(node.data)
            tail = tail.next
        else:
            depth = node.depth
            tail = ListNode(node.data)
            lists.append(tail)
        for child in (node.left, node.right):
            if child:
                child.depth = node.depth + 1
                queue.add(child)
        node = queue.remove()
    return lists


class TreeNode():
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data, self.left, self.right = data, left, right


class ListNode():
    def __init__(self, data=None, next=None) -> None:
        self.data, self.next = data, next

    def __str__(self) -> str:
        return str(self.data) + ', ' + str(self.next)


class Queue():
    def __init__(self) -> None:
        self.head, self.tail = None, None

    def add(self, item):
        if self.head:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next
        else:
            self.head = self.tail = ListNode(item)

    def remove(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        return item