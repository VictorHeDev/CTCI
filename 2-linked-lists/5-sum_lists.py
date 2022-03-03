'''
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit
is the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

EXAMPLE 1:
INPUT:  (7 -> 1 -> 6) + (5 -> 9 -> 2) => 617 + 295
OUTPUT: (2 -> 1 -> 9) => 912

EXAMPLE 2:
INPUT:  (6 -> 1 -> 7) + (2 -> 9 -> 5) => 617 + 295
OUTPUT: (9 -> 1 -> 2) => 912
'''


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll


def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next
