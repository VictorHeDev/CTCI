'''
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height

APPROACH
- we want to match the number of nodes in the left subtree to the number of
nodes in the right subtree as much as possible
- we want the root to be the middle element of the array

create_minimal_bst method:
1. insert into the tree the middle element of the array
2. insert (into the left subtree) the left subarray elements
3. insert (into the right subtree) the right subtree elements
4. recurse
'''


def minimal_height_bst(sorted_array):
    if len(sorted_array) == 0:
        return None
    if len(sorted_array) == 1:
        return BSTNode(sorted_array[0])
    mid = len(sorted_array) // 2
    left = minimal_height_bst(sorted_array[:mid])
    right = minimal_height_bst(sorted_array[mid + 1:])
    return BSTNode(sorted_array[mid], left, right)


class BSTNode():
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data, self.left, self.right = data, left, right


# ALT
def create_minimal_bst(sorted_array):
    return _create_minimal_bst(sorted_array, 0, len(sorted_array) - 1)


def _create_minimal_bst(array, start, end):
    if end < start:
        return None

    mid = (start + end) // 2
    node = BSTNode(array[mid])
    node.left = _create_minimal_bst(array, start, mid - 1)
    node.right = _create_minimal_bst(array, mid + 1, end)
    return node
