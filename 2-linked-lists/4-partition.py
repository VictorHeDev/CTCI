'''
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x. If x is
contained within the list, the values of x only need to be after the
elements less than x. The partition element x can reappear anywhere in the
"right partition"; it does not need to appear between the left and
right partitions.

EXAMPLE
INPUT:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
OUTPUT: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

APPROACH:
- instead of shifting and swapping elements, we can actually create 2
different LL and combine them at the end
- one LL will include elements less than the partition
- the other LL will include elements greater or equal to than the partition
'''


def partition(ll, target):
    current = ll.head = ll.tail

    while current:
        next_node = current.next
        current.next = None

        if current.value < target:
            # insert node at head
            current.next = ll.head
            ll.head = current
        else:
            # insert node at tail
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # error checking in case all nodes are less than target
    if ll.tail.next is not None:
        ll.tail.next = None
