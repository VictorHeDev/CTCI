'''
Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the
heights of the two subtrees of any node never differ by more than one.

APPROACH:
- recurse through the entire tree and for each node compute the heights of
each subtree
- if the heights of subtrees are different by > 1 then return early
'''


def is_balanced(binary_tree):
    if not binary_tree:
        return (True, 0)
    left_balance, left_depth = is_balanced(binary_tree.left)
    if not left_balance:
        return (False, None)
    right_balance, right_depth = is_balanced(binary_tree.right)
    if not right_balance or abs(left_depth - right_depth) > 1:
        return (False, None)

    return (True, max(right_depth, left_depth) + 1)
