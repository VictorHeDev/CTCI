# Linked Lists

### What is a Linked List?

Data structure that represents a sequence of nodes. In a singly linked list, each node points to the next node in the linked list. A doubly linked list gives each node pointers to both the next and previous nodes.

Unlike an array, a linked list does not provide constant time access to a particular "index" within the list. To find the Kth element in the linked list, you will need to iterate through K elements.

Adding and removing from the beginning of a linked list is constant time.

During an interview scenario, it is important to clarify with the interviewer whether the linked list is a singly linked list or a doubly linked list.

### Different Linked List techniques

Deleting a Node from a Singly Linked List
Given a node n, we find the previous node, prev, and set prev.next to n.next
**If the list is a doubly linked list, we must also update .next to set n.next.prev equal to n.prev.**
Remember to also check for:

1. the null pointer
2. update the head or tail pointer as necessary

```java
Node deleteNode(Node head, int d) {
  Node n = head;

  if (n.data == d) {
    return head.next; // moved head
  }

  while (n.next != null) {
    if (n.next.data == d) {
      n.next = n.next.next;
      return head; // head didn't change
    }
    n = n.next;
  }
  return head;
}
```

The "Runner" Technique
The "runner" (or second pointer) means that you iterate through the linked list with 2 pointers simultaneously. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through.

Recursive Problems
A number of linked list questions rely on recursion. Recursive algorithms take at least O(n) space, where n is the depth of the recursive call.

LESSONS/TECHNIQUES
- use a set to check if LL node.value has been seen
- 
