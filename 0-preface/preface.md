# VI Big O

### Time Complexity

What is Big O?
Big O is the language and metric we use to describe the efficiency of algorithms. In other words, it is a way in which we judge the speed or efficiency of an algorithm.

Differences between Big O, Big Theta, and Big Omega
Big O: describes an upper bound on time
Big Omega: describes the lower bound
Big Theta: describes both O and Omega.

In the industry, people seem to have merged Theta and O together. Most of the time when we reference Big O, what we usually mean is Theta.

### Space Complexity

Separate from Time in an algorithm is Space--the amount of memory. If we need to populate a data structure, that could take up additional memory. Another way to use memory is if we need to use a stack during recursion.

### Calculating Big O

Drop the Constants
Drop the Non-Dominant Terms

### Addition vs. Multiplication

How to tell the difference

- If your algorithm is in the form "do this, then when you're all done, do that" then you add the runtimes
- If your algorithm is in the form "do this for each time you do that" then multiply the runtimes

### Amortized Time

An ArrayList/dynamically resizing array will give you the benefits of an array while giving you flexibility in its size. It will grow in capacity as you insert elements. What it does under the hood is to create a new array with double the capacity and copy all the elements in the old array into the new (double sized) array.

Even though insertion times in an array is O(N), the majority of insertion time will actually be closer to O(1) because resizing (doubling the size of the array) does not happen very frequently.

### Recursive Runtime

Generally, when we have a recursive function that makes multiple calls, the runtime will often look like O(branches^depth), where branches in the number of times each recursive call branches. For example in this code snippet, it will give us O(2^N), because there are 2 branches.

```python
def recursiveAdd(n):
  if (n <= n): return 1
  return recursiveAdd(n - 1) + recursiveAdd(n - 1)
```

Most optimal way to calculate prime number

```python
import math
def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True
```

Normally, calculating the Fibonacci numbers will take O(2^n), but with a technique called memoization, it changes the runtime to only O(N)

```python
def allFib(n):
  memo = {}
  for i in range(len(n)):
    print(i + ": " + fib(i, memo))

def fib(n, memo):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  elif memo[n] > :
    return memo[n]

  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]
```

Summing all the digits in a number

```python
def sumDigits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n /= 10
  return sum
```

# VII Technical Questions

### Walking through a Problem

1. Listen
   1. Pay attention to any details that might help you optimize the algorithm later
   2. BUD: Bottlenecks, Unnecessary Work, Duplicated Work
2. Example
   1. Think about special cases/edge cases
3. Brute Force
   1. State a naive approach (do not code)
4. Optimize
   1. Talk through and see if BF approach works with an example
   2. Talk about Time/Space tradeoffs (do hashtables help?)
5. Walk Through
   1. Derive optimal approach and walk through it with examples
6. Implement
   1. Modularize code and clean/refactor afterwards
7. Test
   1. Conceptual test (walk through code with examples)
   2. Test for unusual test cases
      1. Arithmetic or null nodes
   3. Start small -- don't jump into using large test cases! Simple is better
   4. Fix bugs carefully

Best Conceivable Runtime (BCR)
After getting the time complexity to be the smallest possible, then optimize for space complexity if possible

What does "Good Code" look like?
- Correctness
  - Appropriate Code Reuse/
  - Error checking (through ASSERT statements or if-statements)
- Efficient
- Simple
- Readable
  - Modularity
- Maintainable
  - Use data structures generously
  - Flexible robust


# VIII The Offer and Beyond
### When evaluating an offer, some things to keep in mind
The financial package includes:
- Signing Bonus, Relocation, and other One Time Perks
- Cost of Living Difference
- Annual Bonus (usually in the 3%-30% range)
- Stock options and Grants

