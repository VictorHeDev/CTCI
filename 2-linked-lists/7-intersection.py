'''
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based
on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the 2nd linked list,
the they are intersecting.
'''

def if_intersect(head1, head2):
    curr1 = head1
    curr2 = head2
    tracker = set()

    while curr1 is not None:
        tracker.add(curr1)
        curr1 = curr1.next

    while curr2 is not None:
        if curr2 in tracker:
            return True

    return False

