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

