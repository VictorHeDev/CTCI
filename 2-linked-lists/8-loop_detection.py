'''
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
'''


'''
APPROACH
- detect if linked list has a loop
  - use fast runner / slow runner approach
- when do fast and slow collide?
  - last and slow are LOOP_SIZE - k nodes from each other
- head of the LL is also k nodes from front of the loop
- if we keep a pointer where it is and another at the head of the LL
  - they will meet at the start of loop
'''


def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            break

    # if there is no cycle
    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast
