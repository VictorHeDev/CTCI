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
'''


def validate_tree(binary_tree):
    return validate_tree_node(binary_tree, -float('inf'), float('inf'))


def validate_tree_node(node, left_bound, right_bound):
    if not node:
        return True

    return node.data >= left_bound and node.data <= right_bound and validate_tree_node(node.left, left_bound, node.data) and validate_tree_node(node.right, node.data, right_bound)
