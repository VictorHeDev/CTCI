'''
Write an algorithm to find the "next" node (i.e., in-order successor) of
a given node in a binary search tree. You may assume that each node has
a link to its parent.
'''


def successor(node):
    if not node:
        return None

    child = node.right
    if child:
        while child.left:
            child = child.left
    if child:
        return child
    parent = node.parent
    child = node
    if parent and parent.left == child:
        return parent
    if parent and parent.right == child:
        while parent and parent.left != child:
            child = parent
            parent = child.parent
        return parent


class Node():
    def __init__(self, data, left=None, right=None) -> None:
        self.data, self.left, self,right = data, left, right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


# ALT SOLUTION
def in_order_successor(input_node):
    if input_node is None:
        return None

    if input_node.right:
        current = input_node.right
        while current.left:
            current = current.left
        return current

    ancestor = input_node.parent
    child = input_node
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor
