'''
Write code to remove duplicates from an unsorted linked list
How would you solve this problem if a temporary buffer is not allowed?
'''


def remove_duplicates(head):
    prev = LinkedListNode(None)
    curr = head
    dups = set()

    while curr is not None:
        if curr.value in dups:
            prev.next = curr.next
        dups.add(curr.value)

        prev = curr
        curr = curr.next

    return head