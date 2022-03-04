'''
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based
on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the 2nd linked list,
the they are intersecting.
'''


def if_intersect_brute(head1, head2):
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


'''
SOLUTION 1
- run through each LL to get the lengths and the tails
- compare the tails. If they are different, return immediately bc no intersection
- set 2 pointers to the start of each LL
- on the longer LL, advance the pointer by different lengths
- traverse on each LL until the pointers are the same
'''


def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) > len(list2) else list1

    difference = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(difference):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    # can return either shorter_node or longer_node
    return longer_node
