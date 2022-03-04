'''
Implement a function to check if a linked list is a palindrome
'''


def is_palindrome(head):
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
