'''
Implement an algorithm to find the kth to last element of a singly linked list
'''


def return_kth_to_last_iter(head, k):
    slow = head
    fast = head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow


def return_kth_to_last_recursive(head, k):
    curr = head
    counter = 0

    def helper(node, k):
        nonlocal counter
        if not node:
            return None
        helper_node = helper(node.next, k)
        counter += 1

        if counter == k:
            return node
        return helper_node

    return helper(curr, k)
