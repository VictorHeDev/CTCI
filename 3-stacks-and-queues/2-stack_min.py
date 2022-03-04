'''
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
'''


'''
APPROACH
- minimums only change when elements are added
- after an element is popped, the new minimum will be the last minimum before the current element was popped
- to ensure constant lookup time for minimum, what we can do is have the "nodes" keep track of the local minimum

- in a separate solution, what if we instead had 2 stacks?
- one stack to keep track of the original elements added
- second stack to keep track of new minimums that will be popped off when elements from og stack are popped off (if they match)
'''

