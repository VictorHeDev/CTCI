'''
Write code to remove duplicates from an unsorted linked list
How would you solve this problem if a temporary buffer is not allowed?
'''

'''
APPROACH
- in order to remove duplicates from a LL, we need to be able to track dups
- a hash table will work here (to keep track)
- iterate through the linked list and add each ele to a hash table
- when we find a dup, remove the element and continue iterating
- do this until we complete iterating through the LL
'''

# O(N) time, where N is the number of elements in the linked list


def remove_duplicates(head):
    prev = head
    curr = head
    dups = set()

    while curr is not None:
        if curr.value in dups:
            prev.next = curr.next
        dups.add(curr.value)

        prev = curr
        curr = curr.next

    return head
