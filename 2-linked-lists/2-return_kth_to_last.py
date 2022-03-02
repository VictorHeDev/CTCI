'''
Implement an algorithm to find the kth to last element of a singly linked list
'''


def return_kth_to_last(head, k):
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    return slow
