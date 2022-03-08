'''
Implement a function to check if a binary tree is a binary search tree

APPROACH 1:
- leverage in-order traversal and copy the elements into an array
- check to see if the array is sorted
- this approach takes up extra memory, but it works for brute force
- does not work if there are any dups in the bst

APPROACH 2:
- leverage definition of a bst
- must satisfy the condition left.data <= current.data < right.data for
each node
- more precise definition--all left nodes must be <= current node, current node must be < all right nodes
- we cn pass down the min and max values, and as we iterate through the tee we can verify against progressively narrower ranges
- when we branch left, the max gets updated, when we branch right, the min gets updated. If anything fails then we stop and return false
'''


def validate_tree(binary_tree):
    return validate_tree_node(binary_tree, -float('inf'), float('inf'))


def validate_tree_node(node, left_bound, right_bound):
    if not node:
        return True

    return node.data >= left_bound and node.data <= right_bound and validate_tree_node(node.left, left_bound, node.data) and validate_tree_node(node.right, node.data, right_bound)


# solution
def check_bst(tree):
    return _check_best(tree.root)


def _check_bst(node, min=None, max=None):
    if node is None:
        return True

    if (min is not None and node.data <= min) or (max is not None and node.data > max):
        return False
    if not _check_best(node.left, min, node.data) or not _check_bst(node.right, node.data, max):
        return False
    return True
