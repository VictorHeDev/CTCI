'''
Implement a function to check if a linked list is a palindrome
'''


def is_palindrome_brute(head):
    linked_list_values = []
    curr = head

    while curr is not None:
        linked_list_values.append(curr.value)
        curr = curr.next

    left = 0
    right = len(linked_list_values) - 1
    while left < right:
        if linked_list_values[left] != linked_list_values[right]:
            return False
        left += 1
        right -= 1

    return True

def is_palindrome_runner(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow is not None:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next
    return True


def is_palindrome_constant_space(ll):
    slow = ll.head
    if not slow or not slow.next:
        return True
    fast = slow.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # unlink left and right halves of list
    right_head = slow.next
    slow.next = None

    # reverse right half of list
    tail = reverse(right_head)

    # iterate through both lists
    left, right = ll.head, tail
    result = True

    while left and right:
        if left.value != right.value:
            result = False
            break
        left = left.next
        right = right.next

    # undo the reverse
    reverse(tail)
    slow.next = right_head
    return result


def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev


def is_palindrome_recursive(ll):
    def get_len(node):
        if not node:
            return 0
        else:
            return 1 + get_len(node.next)

    def recursive_transverse(node, length):
        if not node or length == 0:   # even list
            return True, node
        elif length == 1:   # odd list
            return True, node.next

        _is_palindrome, fwd_node = recursive_transverse(node.next, length - 2)

        if not _is_palindrome or not fwd_node:
            return False, None

        if node.value == fwd_node.value:
            return True, fwd_node.next
        else:
            return False, None

    return recursive_transverse(ll.head, get_len(ll.head))[0]