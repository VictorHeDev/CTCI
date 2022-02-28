# Arrays and Strings
Arrays and string questions are often interchangeable

### Hash Tables
What is a Hash Table?
It is a data structure that maps keys to values for highly efficient lookup (O(1)). A simple implementation of a Hash Table is with an array of linked lists, and a hash code function.

In practice
1. Compute key's hash code (usually an int or long)
2. Map the hash code to an index in the array
3. At the index, there is a linked list that stores the key -> value


### ArrayList & Resizable Arrays
Also called Dynamic Arrays, will grow as you append items. 