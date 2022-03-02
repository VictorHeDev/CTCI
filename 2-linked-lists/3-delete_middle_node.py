'''
Implement an algorithm to delete a node in the middle (i.e. any node but the
first and last node, not necessarily the exact middle) of a singly linked
list, given only access to that node
'''

def delete_middle_node(head, target_node):
    prev = head
    curr = head.next

    while curr is not None:
        if curr == target_node:
            prev.next = curr.next

        prev = curr
        curr = curr.next


