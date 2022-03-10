'''
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.

SOLUTION 1: With Links to Parents
- if each node has a link to its parent, we could trace p and q's path up until they intersect.

SOLUTION 2: With Links to Parents
- trace p's path upward and check if any of the nodes cover q
- the first node that covers q must be the first common ancestor

SOLUTION 3: Without Links to Parents


'''

def first_common_ancestor(p, q):
    if not p or not q:
        return None
    depth_p = get_depth(p)
    depth_q = get_depth(q)
    delta = abs(depth_p - depth_q)
    if depth_p < depth_q:
        for _ in range(delta):
            q = q.parent
    elif depth_q < depth_p:
        for _ in range(delta):
            p = p.parent
    ancestor_p = p
    ancestor_q = q
    while ancestor_p != ancestor_q:
        ancestor_p = ancestor_p.parent
        ancestor_q = ancestor_q.parent
    return ancestor_p


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth
