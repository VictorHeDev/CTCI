# Stacks and Queues

### Implementing a Stack

A stack uses LIFO (last-in-first-out) ordering. It has the following operations:

- pop(): remove the top item from the stack
- push(item): add an item to the top of the stack
- peek(): return the top of the stack
- isEmpty(): return true if and only if the stack is empty

Does not offer constant-time access to ith item, but push and pop operations are constant time.

Often times stacks are useful in recursive algorithms where you might need to temporarily store data onto a stack as you recurse, but remove them as you backtrack.

### Implementing a Queue
A queue uses FIFO (first-in-first-out) ordering. Items are removed from the data structure int he same order that they are added. It uses the operations:

- add(item): add item to the end of the list
- remove(): remove the first item in the list
- peek(): return the top of the queue
- isEmpty(): return true if and only if the queue is empty

Queue are often used in breadth-first search or implementing a cache. 